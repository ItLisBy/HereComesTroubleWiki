from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/PCs/<string:name>')
def pcs_page(name):
    return render_template('Data//GameData//PCs//' + name + '.html')


@app.route('/PCs/<string:name>/<string:attr>')
def pcs_attr(name, attr):
    return render_template('Data//GameData//PCs//' + name + '//Attrs//' + attr + '.html')


@app.route('/GameData')
def game_data():
    return render_template('Data//GameData.html')


@app.route('/GameData/<string:menu>')
def game_data_menu(menu):
    return render_template('Data//' + menu + '.html')


if __name__ == '__main__':
    app.run()
