from flask import Flask
import psycopg2
import time

app = Flask(__name__)

def get_db():
    while True:
        try:    
            conn = psycopg2.connect(
            host="db",
            database="empresa",
            user="postgres",
            password="1234"
        )
            print("CONEXION A BD EXITOSA")
            return conn
            
        except Exception as e:
            print("Error connecting to database: ", e)
            time.sleep(3)


@app.route("/")
def home():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employees (id SERIAL PRIMARY KEY, name TEXT NOT NULL)")
    cur.execute("INSERT INTO employees (name) VALUES ('Abril')")
    print("DATOS INSERTADOS CORRECTAMENTE")

    conn.commit()
    cur.execute("SELECT * FROM employees")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return str(data)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)