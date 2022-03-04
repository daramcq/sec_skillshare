from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    name = request.args.get('name', 'Default Dan')
    return render_template('basic.html', name=name)


@app.route('/goodnight')
def goodnight():
    things = ['brush', 'bowl full of mush', 'old lady whispering hush']
    return render_template('goodnight.html', things=things)


if __name__ == '__main__':
    app.run(debug=True)
