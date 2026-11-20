
import pymysql
from config import Config

try:
    connection = pymysql.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME
    )

    print("SUCCESS: Connected to MySQL!")

    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        print("Database tables:")
        for table in tables:
            print("-", table[0])

    connection.close()

except pymysql.MySQLError as error:
    print("ERROR: Database connection failed:", error)
