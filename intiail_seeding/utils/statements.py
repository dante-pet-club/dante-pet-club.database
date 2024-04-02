insert_statement = """
INSERT INTO public.%s (%s)
VALUES
(%s)
"""

delete_statement = """
DELETE FROM public.%s WHERE 1 = 1
"""

if __name__ == "__main__":
    print(__name__)
