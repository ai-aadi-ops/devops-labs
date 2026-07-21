from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    flash,
    url_for
)

import mysql.connector
import bcrypt
import time

app = Flask(__name__)
app.secret_key = "change-this-to-a-random-secret-key"

# -----------------------------
# Database Connection
# -----------------------------
def connect_db():
    def hash_password(password):
    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")
    def verify_password(password, hashed_password):
        return bcrypt.checkpw(
            password.encode("utf-8"),
            hashed_password.encode("utf-8")
    )

    while True:
        try:
            connection = mysql.connector.connect(
                host="mysql",
                user="root",
                password="root123",
                database="employee_db"
            )
            print("✅ Connected to MySQL")
            return connection

        except Exception as e:
            print(e)
            print("Retrying in 5 seconds...")
            time.sleep(5)


# -----------------------------
# Create Table
# -----------------------------
def create_table():

    conn = connect_db()
    cursor = conn.cursor()

    # Employee table
    cursor.execute(
    "SELECT * FROM users WHERE username=%s",
    ("admin",)
)

if cursor.fetchone() is None:

    admin_password = hash_password("admin123")

    cursor.execute(
        """
        INSERT INTO users(username,password)
        VALUES(%s,%s)
        """,
        ("admin", admin_password)
    )

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(100) UNIQUE,
            password VARCHAR(100)
        )
    """)

    # Default admin user
    cursor.execute("""
        INSERT IGNORE INTO users(username, password)
        VALUES('admin', 'admin123')
    """)

    conn.commit()

    cursor.close()
    conn.close()


# -----------------------------
# Home Page
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def home():

    conn = connect_db()
    cursor = conn.cursor()

    # Add Employee
    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        salary = request.form["salary"]

        cursor.execute("""
            INSERT INTO employees(name,email,salary)
            VALUES(%s,%s,%s)
        """, (name, email, salary))

        conn.commit()

        cursor.close()
        conn.close()

        return redirect("/")

    # Display Employees
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", employees=employees)


# -----------------------------
# Edit Employee
# -----------------------------
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    conn = connect_db()
    cursor = conn.cursor()

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        salary = request.form["salary"]

        cursor.execute("""
            UPDATE employees
            SET name=%s,
                email=%s,
                salary=%s
            WHERE id=%s
        """, (name, email, salary, id))

        conn.commit()

        cursor.close()
        conn.close()

        return redirect("/")

    cursor.execute("SELECT * FROM employees WHERE id=%s", (id,))
    employee = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template("edit.html", employee=employee)


# -----------------------------
# Delete Employee
# -----------------------------
@app.route("/delete/<int:id>")
def delete(id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM employees WHERE id=%s", (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect("/")


# -----------------------------
# Main
# -----------------------------
create_table()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
