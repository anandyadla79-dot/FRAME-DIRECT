from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "change-this-secret-key-before-deployment"

BASE_DIR = Path(__file__).resolve().parent
DATABASE = BASE_DIR / "farm_direct.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_db_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL CHECK(price >= 0),
                quantity REAL NOT NULL CHECK(quantity >= 0),
                location TEXT NOT NULL,
                farmer_name TEXT NOT NULL,
                phone TEXT NOT NULL,
                description TEXT DEFAULT '',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        count = connection.execute("SELECT COUNT(*) FROM products").fetchone()[0]
        if count == 0:
            sample_products = [
                ("Tomatoes", "Vegetables", 28, 100, "Vijayawada", "Ravi Kumar", "9876543210", "Fresh tomatoes harvested this week."),
                ("Rice", "Grains", 45, 250, "Guntur", "Lakshmi Devi", "9876501234", "Locally grown rice."),
                ("Mangoes", "Fruits", 70, 80, "Krishna District", "Suresh", "9123456780", "Seasonal sweet mangoes.")
            ]
            connection.executemany("""
                INSERT INTO products
                (name, category, price, quantity, location, farmer_name, phone, description)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, sample_products)


@app.route("/")
def index():
    search = request.args.get("search", "").strip()
    with get_db_connection() as connection:
        if search:
            products = connection.execute("""
                SELECT * FROM products
                WHERE name LIKE ? OR category LIKE ? OR location LIKE ?
                ORDER BY created_at DESC
            """, (f"%{search}%", f"%{search}%", f"%{search}%")).fetchall()
        else:
            products = connection.execute(
                "SELECT * FROM products ORDER BY created_at DESC"
            ).fetchall()
    return render_template("index.html", products=products, search=search)


@app.route("/add", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        category = request.form.get("category", "").strip()
        location = request.form.get("location", "").strip()
        farmer_name = request.form.get("farmer_name", "").strip()
        phone = request.form.get("phone", "").strip()
        description = request.form.get("description", "").strip()

        try:
            price = float(request.form.get("price", ""))
            quantity = float(request.form.get("quantity", ""))
        except ValueError:
            flash("Enter valid numbers for price and quantity.", "error")
            return render_template("add_product.html")

        if not all([name, category, location, farmer_name, phone]):
            flash("Please fill in all required fields.", "error")
            return render_template("add_product.html")

        if price < 0 or quantity < 0:
            flash("Price and quantity cannot be negative.", "error")
            return render_template("add_product.html")

        with get_db_connection() as connection:
            connection.execute("""
                INSERT INTO products
                (name, category, price, quantity, location, farmer_name, phone, description)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (name, category, price, quantity, location, farmer_name, phone, description))

        flash("Product added successfully!", "success")
        return redirect(url_for("index"))

    return render_template("add_product.html")


@app.route("/delete/<int:product_id>", methods=["POST"])
def delete_product(product_id):
    with get_db_connection() as connection:
        connection.execute("DELETE FROM products WHERE id = ?", (product_id,))
    flash("Product listing deleted.", "success")
    return redirect(url_for("index"))


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
