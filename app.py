from flask import Flask, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "mysecretkey"

# Fake product database
products = [
    {"id": 1, "name": "Laptop", "price": 600},
    {"id": 2, "name": "Headphones", "price": 50},
    {"id": 3, "name": "Mouse", "price": 20}
]

# Home page
@app.route("/")
def index():
    return render_template("index.html", products=products)

# Product page
@app.route("/product/<int:id>")
def product(id):
    item = next((p for p in products if p["id"] == id), None)
    return render_template("product.html", product=item)

# Add to cart
@app.route("/add_to_cart/<int:id>")
def add_to_cart(id):
    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(id)
    session.modified = True
    return redirect(url_for("cart"))

# View cart
@app.route("/cart")
def cart():
    cart_items = []
    total = 0
    if "cart" in session:
        for id in session["cart"]:
            item = next((p for p in products if p["id"] == id), None)
            if item:
                cart_items.append(item)
                total += item["price"]
    return render_template("cart.html", cart=cart_items, total=total)

if __name__ == "__main__":
    app.run(debug=True)
