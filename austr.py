from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style2.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align='center'>Анкета претендента</h1>
                            <h2 align='center'>на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите фамилию" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите имя" name="password">
                                    <br></br>
                                    <input type="password" class="form-control" id="password" placeholder="Введите адрес почты" name="password">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                        </select>
                                    </div>
                                <div class="form-group">
                                    <label for="form-check">Какие у Вас есть профессии?</label>
                                    <div class="form-check">
                                      <input class="form-check-input" type="checkbox" name="sex" id="male" value="1" checked>
                                      <label class="form-check-label" for="1">
                                        Инженер-исследователь
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="checkbox" name="sex" id="female" value="2">
                                      <label class="form-check-label" for="2">
                                        Пилот
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="checkbox" name="sex" id="female" value="3">
                                      <label class="form-check-label" for="3">
                                        Строитель
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="checkbox" name="sex" id="female" value="4">
                                      <label class="form-check-label" for="4">
                                        Экзобиолог
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="checkbox" name="sex" id="female" value="5">
                                      <label class="form-check-label" for="5">
                                        Врач
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="checkbox" name="sex" id="female" value="6">
                                      <label class="form-check-label" for="6">
                                        Инженер по терраформированию
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="checkbox" name="sex" id="female" value="7">
                                      <label class="form-check-label" for="7">
                                        Климатолог
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="checkbox" name="sex" id="female" value="8">
                                      <label class="form-check-label" for="">
                                        Специалист по радиационной защите
                                      </label>
                                    </div>
                                </div>
                                <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')