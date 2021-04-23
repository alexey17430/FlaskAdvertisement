from flask import render_template, Flask, url_for

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
<h1 style="color:rgb(150,0,0)" align="center">Самый лучший телеграмм бот во всей Челябинской области</h1>
<div class="alert alert-primary" role="alert" align="center">
  Вам нужно сохранять, записывать и просматривать свои задачи, но на рынке нет удобных для этого инструментов?
</div>
<div class="alert alert-secondary" role="alert">
  Вы хотите быстро получать информацию о курсе доллара?
</div>
<div class="alert alert-success" role="alert">
  Вы хотите своевременно узнавать курс евро?
</div>
<div class="alert alert-danger" role="alert">
  Вам не нравятся часы и календарь в вашей ОС, но эта информация вам жизненно необходима?
</div>
<div class="alert alert-warning" role="alert">
  Тогда я рад вам представить телеграмм бота, который всё это умеет....

</body>
</html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
