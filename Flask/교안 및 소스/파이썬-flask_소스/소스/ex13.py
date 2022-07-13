from flask import Flask, request

app = Flask(__name__)

@app.route('/bbb')
def bbb():
    nameVal = request.args.get("name", "100", int)
    return str(nameVal)

if __name__ == "__main__":
    app.run()
