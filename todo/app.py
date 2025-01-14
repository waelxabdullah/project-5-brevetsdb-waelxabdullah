import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

# an attempt to dynamically get the hostname of the db container.
# this won't work as it is. There is an issue in the visibility of the db env variables from the web ctr.
# client = MongoClient(host=os.environ.get('DB_PORT_27017_TCP_ADDR'), port=27017)

client = MongoClient(host="todo_mongodb", port=27017)
db = client.tododb


@app.route('/')
def todo():
    _items = db.tododb.find()
    items = [item for item in _items]

    return render_template('todo.html', items=items)


@app.route('/new', methods=['POST'])
def new():
    item_doc = {
        'name': request.form['namee'],
        'description': request.form['description']
    }
    db.tododb.insert_one(item_doc)

    return redirect(url_for('todo'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
