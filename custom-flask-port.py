from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "This is a simple Python Flask App"



if __name__ == "__main__":
    app.debug=True
    app.run(host='192.168.1.81', port=1146)
