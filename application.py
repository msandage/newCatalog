from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, sessionmaker
from database_setup import Base, Category, Item


app = Flask(__name__)


engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/catalog/')
def showCategories():
    categories = session.query(Category).all()
    return render_template('catalog.html', categories=categories)


@app.route('/catalog/JSON/')
def categoriesJSON():
    categories = session.query(Category).all()
    return jsonify(Categories = [c.serialize for c in categories])




@app.route('/catalog/<int:category_id>/')
@app.route('/catalog/<int:category_id>/items/')
def showItems(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(category_id=category_id).all()
    return render_template('items.html', category=category, items=items)


@app.route('/catalog/<int:category_id>/items/JSON/')
def itemsJSON(category_id):
    items = session.query(Item).filter_by(category_id = category_id).all()
    return jsonify(Items = [i.serialize for i in items])


@app.route('/catalog/<int:category_id>/items/<int:item_id>/')
def showItem(category_id, item_id):
    item = session.query(Item).filter_by(id = item_id).one()
    return render_template('item.html', item=item)

@app.route('/catalog/<int:category_id>/items/<int:item_id>/JSON/')
def itemJSON(category_id, item_id):
    item = session.query(Item).filter_by(id = item_id).one()
    return jsonify(Item = [item.serialize])


@app.route('/catalog/<int:category_id>/item/new/', methods=['GET', 'POST'])
def newItem(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    
    if request.method == 'POST':
        newItem = Item(name = request.form['name'], description = request.form['description'], category_id = category_id)
        session.add(newItem)
        session.commit()
        flash("Successfully Created New Item: {}".format(newItem.name))
        return redirect(url_for('showItems', category_id=category_id))

    else:
        return render_template('newItem.html', category=category)




@app.route('/catalog/<int:category_id>/items/<int:item_id>/edit/', methods=['GET', 'POST'])
def editItem(category_id, item_id):
    itemToEdit = session.query(Item).filter_by(id=item_id).one()
    
    if request.method == 'POST':
        if request.form['name'] != '':
            itemToEdit.name = request.form['name']
        if request.form['description'] != '':
            itemToEdit.description = request.form['description']
        session.add(itemToEdit)
        session.commit()
        flash("Successfully Edited Item: {}".format(itemToEdit.name))
        return redirect(url_for('showItems', category_id=itemToEdit.category_id))
    
    else:
        return render_template('editItem.html', item=itemToEdit)



@app.route('/catalog/<int:category_id>/items/<int:item_id>/delete/', methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    itemToDelete = session.query(Item).filter_by(id=item_id).one()

    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash("Successfully Deleted Item: {}".format(itemToDelete.name))
        return redirect(url_for('showItems', category_id=category_id))

    else:
        return render_template('deleteItem.html', item=itemToDelete)



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.run(host='0.0.0.0', port=5000)