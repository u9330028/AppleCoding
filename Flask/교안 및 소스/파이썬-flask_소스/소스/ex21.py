# endpoint 속성

from flask import Flask, request

app = Flask(__name__)

@app.route("/test/test", methods=["GET", "POST"])
def test():
    return request.endpoint

if __name__ == "__main__":
    app.run()
