from flask import Flask

# Create a Flask app
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    # Run on port 5000 (you can change it)
    app.run(host="0.0.0.0", port=80, debug=True)
