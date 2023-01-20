from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Utkarsh Goswami',
        'title' : 'First blog',
        'content': 'This is my first blog',
        'date_posted': 'Jan 20, 2023',
    },
    {
        'author': 'Jane Doe',
        'title' : 'Second blog',
        'content': 'This is my second blog',
        'date_posted': 'Jan 20, 2023',
    }

]


@app.route("/")
@app.route("/home")
def hello():
    return  render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title="About")


if __name__ == '__main__':
    app.run(debug=True)