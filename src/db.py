import psycopg2

conn_params = {
  "host": "localhost",
  "database": "mydatabase",
  "user": "postgres",
  "password": "456776"
}
with psycopg2.connect(**conn_params) as conn:
    with conn.cursor() as cur:
        cur.execute("INSERT INTO my_table VALUES (%s, %s)", (1, "Test"))
        cur.execute("SELECT * FROM mytable")

        rows = cur.fetchall()
        for row in rows:
            print(row)