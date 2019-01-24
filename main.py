from flask import Flask, render_template

import data_manager

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    users = data_manager.get_users()
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
