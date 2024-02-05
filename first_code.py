from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/inf')
def inf():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion_image')
def promotion_image():
    list = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.', 'Мы сделаем обитаемыми '
                                                                                     'безжизненные пока планеты.',
            'И начнем с Марса!', 'Присоединяйся!']
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>

                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" 
                    alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-primary" role="alert">
                      {list[0]}</div>
                    <div class="alert alert-secondary" role="alert">
                      {list[1]}</div>
                    <div class="alert alert-success" role="alert">
                      {list[2]}</div>
                    <div class="alert alert-danger" role="alert">
                      {list[3]}</div>
                    <div class="alert alert-warning" role="alert">
                      {list[4]}</div>
                    
                  </body>
                </html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
