from flask import Flask, request

app = Flask(__name__)

@app.route("/exam/environ", methods = ["GET", "POST"])
def exam():
    return request.method

if __name__ == "__main__":
    app.run()
