from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Enter '/play' to Begin!"


@app.route('/play')
@app.route('/play/<int:num>/')
@app.route('/play/<int:num>/<string:color>/')
def play(num=3, color='lightblue'):
    return render_template("index.html", num_box=num, box_color=color)


if __name__ == "__main__":
    app.run(debug=True)
