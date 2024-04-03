import pandas as pd
import os
import pyarrow.parquet as pq

cities = "cities"
countries = "countries"
regions = "regions"
states = "states"
subregions = "subregions"

# tables = [subregions]
tables = [cities, countries, states]

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
parquet_dir = os.path.join(script_dir, "../parquet")

# Map column names from Parquet files to SQL schema
cities_mapping = {
    "id": "id",
    "name": "name",
    "state_id": "state_id",
    # "country_id": "country_id",
}
states_mapping = {
    "id": "id",
    "name": "name",
    "country_id": "country_id",
}
countries_mapping = {"id": "id", "name": "name"}


def main():

    cities_df = pd.read_parquet(f"{parquet_dir}/cities.parquet")
    states_df = pd.read_parquet(f"{parquet_dir}/states.parquet")
    countries_df = pd.read_parquet(f"{parquet_dir}/countries.parquet")

    # Apply column selection and renaming
    cities_df = cities_df[list(cities_mapping.keys())].rename(columns=cities_mapping)
    states_df = states_df[list(states_mapping.keys())].rename(columns=states_mapping)
    countries_df = countries_df[list(countries_mapping.keys())].rename(
        columns=countries_mapping
    )
    countries_df = countries_df[countries_df["name"].str.lower() == "colombia"]
    colombia_id = countries_df.iloc[0]["id"]
    states_df = states_df[
        (states_df["country_id"] == colombia_id)
        & (states_df["name"].str.lower().isin(["atlántico", "antioquia"]))
    ]
    states_ids = states_df["id"].tolist()
    cities_df = cities_df[cities_df["state_id"].isin(states_ids)]
    # Save the modified DataFrames to Parquet files
    cities_df.to_parquet(f"{parquet_dir}/cities_test.parquet", index=False)
    states_df.to_parquet(f"{parquet_dir}/states_test.parquet", index=False)
    countries_df.to_parquet(f"{parquet_dir}/countries_test.parquet", index=False)


if __name__ == "__main__":
    main()
