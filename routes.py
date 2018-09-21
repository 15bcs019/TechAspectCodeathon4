from flask import Flask, url_for, request, render_template
from app import app
student=dict()
@app.route('/')
def hello():
    url = url_for('about');
    link = '<a href="' + url + '">About us!</a>';
    return link;

@app.route('/about')
def about():
    return 'Web Application'

@app.route('/data/<title>', methods=['GET', 'POST'])
def data(name):
    if request.method == 'GET':
        std_data = student[name]
        return render_template('SeeData.html',
                               std_data = std_data)
    
    for 
@app.route("/all",methods=['Get','POST'])
def all():
    pass
#here we neeed to write logic to show all the enetered data
    
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'GET':
        return render_template('EnterData.html');
    elif request.method == 'POST':
        name = request.form['question'];
        age = request.form['age'];
        branch = request.form['branch'];
        year = request.form['year'];
        semester = request.form['sem'];
        p_score = request.form['pa_score']
        student[name]= {age, branch, year,semester, p_score}
        return render_template('dataSubmit.html',name = name)
    
    return;
