from flask import render_template, Flask, url_for
import os

app = Flask(__name__)


@app.route('/')
def start_site():
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>TaskManagerBot</title>
  <link rel="stylesheet" href="static/css/style.css">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>

</head>
<body>
<h1 style="color:rgb(100,100,150)" align="center">Самый лучший телеграмм бот во всей Челябинской области</h1>

<div class="alert alert-danger" role="alert" align="center">
  <h2>Вам не нравятся часы и календарь в вашей ОС, но эта информация вам жизненно необходима?</h2>
  <img src="{url_for('static', filename='img/бот дата время маленький1.png')}"
               alt="Здесь должна была быть картинка, но мы не смогли найти её">
</div>

<div class="alert alert-secondary" role="alert" align="center">
  <h2>Вы хотите быстро получать информацию о курсе доллара, но все информационные порталы для вас неудобны?</h2>
  <img src="{url_for('static', filename='img/бот доллар.png')}"
               alt="Здесь должна была быть картинка, но мы не смогли найти её">
</div>

<div class="alert alert-success" role="alert" align="center">
  <h2>Вы хотите своевременно узнавать курс евро, но ни один сайт не может предоставить быстро и достоверно нужную вам информацию?</h2>
  <img src="{url_for('static', filename='img/бот евро.png')}"
               alt="Здесь должна была быть картинка, но мы не смогли найти её">
</div>

<div class="alert alert-primary" role="alert" align="center">
  <h2>Вам нужно сохранять, записывать и просматривать свои задачи, но на рынке нет удобных для этого инструментов?</h2>
  <img src="{url_for('static', filename='img/бот задачи.png')}"
               alt="Здесь должна была быть картинка, но мы не смогли найти её">
</div>

<div class="alert alert-warning" role="alert" align="center">
  <h2>Тогда я рад вам представить телеграмм бота, который всё это умеет....</h2>
  <a href="https://t.me/TaskManagerPyBot"><h2>https://t.me/TaskManagerPyBot</h2></a>
</div>
</body>
</html>"""


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)