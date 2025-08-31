from flask import Flask

app = Flask(__name__)   # create Flask app

@app.route("/")         # route for home page
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
