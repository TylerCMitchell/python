# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def index():
    return render_template("index.html")

# import statements, maybe some other routes


@app.route('/success')
def success():
    return "success"


# for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
@app.route('/hello/<string:banana>/<int:num>')
def hello(banana, num):
    return render_template("hello.html", banana=banana, num=num)


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name': 'Michael', 'age': 35},
        {'name': 'John', 'age': 30},
        {'name': 'Mark', 'age': 25},
        {'name': 'KB', 'age': 27}
    ]
    return render_template("lists.html", random_numbers=[3, 1, 5], students=student_info)


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
