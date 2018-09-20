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

@app.route('/question/<title>', methods=['GET', 'POST'])
def question(title):
    if request.method == 'GET':
        question = r.get(title+':question')
        return render_template('AnswerQuestion.html',
                               question = question)
    elif request.method == 'POST':
        submittedAnswer = request.form['submittedAnswer'];

        answer=r.get(title+':answer')

        if submittedAnswer == answer:
            return render_template('Correct.html');
        else:
            return render_template('Incorrect.html',
                                   answer = answer,
                                   submittedAnswer = submittedAnswer);

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
