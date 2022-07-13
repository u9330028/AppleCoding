# response를 json으로 만들기

from flask import Flask, jsonify

app = Flask(__name__)

works = [
    {'id' : 100,
     'title': u'BuyGroceries',
     'description':u'Milk, Cheese, Pizza, Fruit',
     'done' : False
     },
    {
        'id':200,
        'title' : u'LearnFlask',
        'description' : u'Web Programming',
        'done' : False
    }
    ]
@app.route('/json', methods = ['GET'])
def get_works():
    return jsonify(works)

if __name__ == "__main__":
    app.run()
