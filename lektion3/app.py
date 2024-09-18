# Import necessary modules from Flask
from flask import Flask, render_template, request, jsonify, redirect, url_for

# Create an instance of the Flask class for your web app
app = Flask(__name__)


# Route decorator to tell Flask what URL should trigger the function
@app.route("/")
def home():
    return "Hello, Flask!"


# Dynamic route that accepts a variable from the URL
@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"


# Handling HTTP GET and POST methods
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        return f"Welcome, {user}!"
    else:
        return """
            <form method="post" action="/login">
                Username: <input type="text" name="username">
                <input type="submit" value="Login">
            </form>
        """


# Rendering an HTML template (you need to have a 'templates' folder with 'index.html' in it)
@app.route("/index")
def index():
    return render_template("index.html")


# Returning JSON data
@app.route("/api/data")
def get_data():
    data = {"name": "Alice", "age": 30}
    return jsonify(data)


# Redirecting to another route
@app.route("/redirect_example")
def redirect_example():
    return redirect(url_for("home"))


cities_list = ["Göteborg", "Linköping", "Enköping", "Skövde", "Mölndal"]


# render_template letar efter html filer i /templates mappen.
@app.route("/index")
def index():
    return render_template(
        "index.html", title="Kristians hemsida", show_paragraph=True, cities=cities_list
    )  # Jag kan skicka med olika typer av variabler i min render_template


# det är render_template() som ser till att variablerna renderas in i html. Den kör igenom logiken och returnerar korrekt html.


@app.route("/submit", methods=["POST"])
def submit():
    print(request.form["email"])  # Data från formulär kommer du åt via request.form
    return "Tack formuläret har skickats in!"


# Starting the Flask web application
if __name__ == "__main__":
    # Run the app in debug mode to auto-reload on code changes and show errors
    app.run(debug=True)


"""
1. venv
2. installing flask
3. hello world
4. multiple routes
5. <> in route, typing
6. request object
"""
