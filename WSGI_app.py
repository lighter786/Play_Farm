from flask import Flask

app = Flask(__name__)

@app.route("/Home")
def Home():
    return "Home page"

if __name__ == "__main__":
    app.run()