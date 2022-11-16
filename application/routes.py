from flask import render_template, request, redirect, url_for

from application import app, db


from application.models import Data

@app.route('/')
def Index():
    all_data = Data.query.all()
    return render_template('index.html', employees = all_data)

@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        


        my_data = Data(name,email,phone)
        db.session.add(my_data)
        db.session.commit()

       

        return redirect(url_for('Index'))


@app.route('/update', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
        

        db.session.commit()

        return redirect (url_for('Index'))


@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()

    return redirect(url_for('Index'))


    