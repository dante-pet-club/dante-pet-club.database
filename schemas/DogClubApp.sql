CREATE TABLE "identification_type" (
  "id" int PRIMARY KEY NOT NULL,
  "name" varchar(35) NOT NULL,
  "description" varchar(150) NOT NULL,
  "created_at" timestamp without time zone
);

CREATE TABLE "status" (
  "id" int PRIMARY KEY NOT NULL,
  "name" varchar(35) NOT NULL,
  "description" varchar(170) NOT NULL,
  "created_at" timestamp without time zone
);

CREATE TABLE "confirmation" (
  "id" int PRIMARY KEY NOT NULL,
  "name" varchar(35) NOT NULL,
  "description" varchar(170) NOT NULL,
  "created_at" timestamp without time zone
);

CREATE TABLE "country" (
  "id" int PRIMARY KEY NOT NULL,
  "name" varchar(35) NOT NULL,
  "gentilic" varchar(35) NOT NULL
);

CREATE TABLE "state" (
  "id" int PRIMARY KEY NOT NULL,
  "name" varchar(35) NOT NULL,
  "gentilic" varchar(35) NOT NULL,
  "country_id" int NOT NULL
);

CREATE TABLE "city" (
  "id" int PRIMARY KEY NOT NULL,
  "name" varchar(35) NOT NULL,
  "gentilic" varchar(35),
  "state_id" int NOT NULL
);

CREATE TABLE "size" (
  "id" serial PRIMARY KEY NOT NULL,
  "size" varchar(3)
);

CREATE TABLE "sex" (
  "id" serial PRIMARY KEY NOT NULL,
  "sex" varchar(6)
);

CREATE TABLE "gender" (
  "id" serial PRIMARY KEY NOT NULL,
  "gender" varchar(10)
);

CREATE TABLE "owner" (
  "id" serial PRIMARY KEY NOT NULL,
  "user_name" varchar(32) UNIQUE NOT NULL,
  "email" varchar(32) UNIQUE NOT NULL,
  "picture" int NOT NULL DEFAULT 1,
  "avatar" int NOT NULL DEFAULT 1,
  "password_hash" varchar(35) NOT NULL,
  "password_salt" varchar(16) NOT NULL,
  "status_id" int DEFAULT 1,
  "confirmation_id" int DEFAULT 1,
  "first_name" varchar(35) NOT NULL,
  "middle_name" varchar(35),
  "surname" varchar(35) NOT NULL,
  "second_surname" varchar(35) NOT NULL,
  "nickname" varchar(35) NOT NULL,
  "identification_type_id" int NOT NULL,
  "identification" int UNIQUE NOT NULL,
  "birthday" date NOT NULL,
  "birthplace" int NOT NULL,
  "gender" smallint NOT NULL,
  "shirt_size_id" int NOT NULL DEFAULT 1,
  "hat_size_id" int NOT NULL DEFAULT 1,
  "pants_size_id" int NOT NULL DEFAULT 1,
  "created_by" int,
  "created_at" timestamp without time zone,
  "updated_by" int,
  "updated_at" timestamp without time zone
);

CREATE TABLE "dog" (
  "id" serial PRIMARY KEY NOT NULL,
  "first_name" varchar(35) NOT NULL,
  "middle_name" varchar(35),
  "surname" varchar(35) NOT NULL,
  "second_surname" varchar(35) NOT NULL,
  "nickname" varchar(35) NOT NULL,
  "height" numeric(3,1), -- cm
  "weight" numeric(3,1),
  "sterilized" bool NOT NULL DEFAULT false,
  "birthday" date NOT NULL,
  "birthplace" int NOT NULL,
  "sex" smallint NOT NULL,
  "coat" int NOT NULL,
  "bandana_size_id" int NOT NULL DEFAULT 1,
  "shirt_size_id" int NOT NULL DEFAULT 1,
  "shoe_size_id" int NOT NULL DEFAULT 1,
  "created_by" int,
  "created_at" timestamp without time zone,
  "updated_by" int,
  "updated_at" timestamp without time zone
);

CREATE TABLE "pet_owner" (
  "id" serial NOT NULL,
  "pet_id" int NOT NULL,
  "owner_id" int NOT NULL
);

-- Geographical information
ALTER TABLE "city" ADD FOREIGN KEY ("state_id") REFERENCES "state" ("id");
ALTER TABLE "state" ADD FOREIGN KEY ("country_id") REFERENCES "country" ("id");

-- Owner Information
ALTER TABLE "owner" ADD FOREIGN KEY ("identification_type_id") REFERENCES "identification_type" ("id");
ALTER TABLE "owner" ADD FOREIGN KEY ("status_id") REFERENCES "status" ("id");
ALTER TABLE "owner" ADD FOREIGN KEY ("confirmation_id") REFERENCES "confirmation" ("id");
ALTER TABLE "owner" ADD FOREIGN KEY ("birthplace") REFERENCES "city" ("id");
ALTER TABLE "owner" ADD FOREIGN KEY ("shirt_size_id") REFERENCES "size" ("id");
ALTER TABLE "owner" ADD FOREIGN KEY ("hat_size_id") REFERENCES "size" ("id");
ALTER TABLE "owner" ADD FOREIGN KEY ("pants_size_id") REFERENCES "size" ("id");
ALTER TABLE "owner" ADD FOREIGN KEY ("gender") REFERENCES "gender" ("id");

-- Dog Information
ALTER TABLE "dog" ADD FOREIGN KEY ("birthplace") REFERENCES "city" ("id");
ALTER TABLE "dog" ADD FOREIGN KEY ("bandana_size_id") REFERENCES "size" ("id");
ALTER TABLE "dog" ADD FOREIGN KEY ("shirt_size_id") REFERENCES "size" ("id");
ALTER TABLE "dog" ADD FOREIGN KEY ("shoe_size_id") REFERENCES "size" ("id");
ALTER TABLE "dog" ADD FOREIGN KEY ("sex") REFERENCES "sex" ("id");

-- Reference Table 
ALTER TABLE "pet_owner" ADD FOREIGN KEY ("owner_id") REFERENCES "owner" ("id");
ALTER TABLE "pet_owner" ADD FOREIGN KEY ("pet_id") REFERENCES "dog" ("id");
ALTER TABLE "pet_owner" ADD CONSTRAINT pet_owner_pk UNIQUE (owner_id, pet_id);