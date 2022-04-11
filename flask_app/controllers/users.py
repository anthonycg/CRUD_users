
from crypt import methods
from distutils.log import debug
from flask import Flask, render_template, request, redirect, session
from flask_app.__init__ import app
from user import User


@app.route('/')
def index():
    users = User.get_all()
    # print(users)
    return render_template('index.html', all_users=users)

@app.route('/create_user')
def create_user():
    return render_template('create_user.html')

@app.route('/create_user_process', methods=['POST', 'GET'])
def create_user_process():
    # send the inputted data to the database with a query
    new_user = User.create_new_user(request.form)
    print(new_user)
    # session['first_name'] = request.form['first_name']
    # redirect to the index
    return redirect('/')



@app.route('/show_user_process', methods=['POST', 'GET'])
def show_user_process():
    # retrieve the inputted data from the database with a query
    session['one_user'] = User.get_one(request.form)
    print(session['one_user'])
    # session['first_name'] = request.form['first_name']
    # redirect to the index
    return redirect('/show_user')

@app.route('/show_user/<int:id>')
def show_user(id):
    data = {
        'id':id
    }
    one_user =User.get_one(data)
    return render_template('show_user.html', user=one_user)


@app.route('/edit_user/<int:id>')
def edit_user(id):
    data = {
        'id':id
    }
    return render_template('edit_user.html', user= User.get_one(data))

@app.route('/edit_user/process', methods=['POST'])
def update_user():
    User.edit(request.form)
    return redirect('/')

# @app.route('/edit_process', methods=['POST'])
# def edit():
#     edit = User.edit(request.form)
#     return redirect('/edit_user')

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        "id":id
    }
    User.delete(data)
    return redirect('/')

