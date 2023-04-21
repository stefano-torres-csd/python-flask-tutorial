from flask import Flask, render_template

app = Flask(__name__)

ITEMS = [
  {
    'id':1,
    'item_no': 1234,
    'name': 'Some item',
    'desc': 'Some sort of description',
    'cost': 1.34,
    'price': 1.55
  },
  {
    'id':2,
    'item_no': 2345,
    'name': 'item 2',
    'desc': 'Some sort of description',
    'cost': 1.34,
    'price': 1.55
  },
  {
    'id':3,
    'item_no': 3456,
    'name': 'item 3',
    'desc': 'Some sort of description',
    'cost': 1.34,
    'price': 1.55
  }
]


@app.route("/")
def hello_world():
  return render_template('home.html', items=ITEMS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
