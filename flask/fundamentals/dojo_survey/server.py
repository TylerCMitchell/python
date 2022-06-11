from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "tm10996"


# class Survey:
#     def __init__(self, data):
#         self.id = data['id']
#         self.name = data['name']
#         self.location = data['location']
#         self.language = data['language']
#         self.comments = data['comments']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']


@app.route('/')
def index():
    return render_template("index.html")


# @app.route('/create/survey', methods=['POST'])
# def create_survey():
#     return redirect('/result')


# @app.route('/result')
# def result():
#     return render_template('result.html')


@app.route('/process', methods=["POST"])
def prcess():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect("/result")


@app.route('/result')
def result():
    return render_template('result.html')


if __name__ == "__main__":
    app.run(debug=True)
