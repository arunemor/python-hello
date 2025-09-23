from flask import Flask

# Create a Flask app
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, When creating or updating the launch template or launch configuration used by your ASG, specify the IAM role created in the previous step as the This ensures that all instances launched by the ASG will automatically assume this role and its associated permissions."

if __name__ == "__main__":
    # Run on port 5000 (you can change it)
    app.run(host="0.0.0.0", port=5000, debug=True)
