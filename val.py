from flask import Flask, url_for

app = Flask(__name__)


# overflow: visible;
@app.route('/')
def intro():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promo():
    return '''Человечество вырастает из детства.
 <br>
 Человечеству мала одна планета.
 <br>
 Мы сделаем обитаемыми безжизненные пока планеты.
 <br>
 И начнем с Марса!
 <br>
 Присоединяйся!'''


@app.route('/image_mars')
def image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/flask/mars.jpg">
                    <hr>Вот она какая, расная планета</hr>
                  </body>
                </html>"""


#

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
