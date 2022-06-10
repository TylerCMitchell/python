from flask import Flask, render_template, session, redirect, url_for
app = Flask(__name__)
app.secret_key = 'counter'


@app.route('/')
def index():
    if 'views' not in session:
        session['views'] = 0
    else:
        session['views'] += 1
    return render_template("index.html")


@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect(url_for('index'))


@app.route('/addTwo')
def addTwo():
    if 'views' not in session:
        session['views'] = 0
    else:
        session['views'] += 2
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if (__name__) == '__main__':
    app.run(debug=True)
