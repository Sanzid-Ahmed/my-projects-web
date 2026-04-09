import psycopg2
import glob
import os

# Render PostgreSQL connection
conn = psycopg2.connect(
    host="dpg-d7bkk90gjchc73fe65og-a.oregon-postgres.render.com",
    database="helper313_db",
    user="helper313_user",
    password="F1Y03s55xZHOP2a6ZFQ7z2gmVRLWFcyx",
    port="5432"
)

cur = conn.cursor()

# Path to your CSV folder
csv_folder = r"H:\my-helper-db"
csv_files = glob.glob(os.path.join(csv_folder, "*.csv"))

# Import each CSV into PostgreSQL
for file in csv_files:
    table_name = os.path.basename(file).replace(".csv", "")
    print(f"Importing {file} into {table_name}...")
    try:
        with open(file, 'r', encoding='utf-8') as f:
            cur.copy_expert(f"COPY {table_name} FROM STDIN WITH CSV HEADER", f)
        conn.commit()
        print(f"{table_name} imported successfully!")
    except Exception as e:
        print(f"Error importing {table_name}: {e}")

cur.close()
conn.close()
print("All CSV files processed!")