from flask import render_template, Flask, url_for

app = Flask(__name__)


@app.route('/')
def start_site():
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Колонизация</title>
  <link rel="stylesheet" href="static/css/style.css">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
</head>
<body>
<h1>Жди нас, Марс!</h1>
<div class="alert alert-primary" role="alert">
  Человечество вырастает из детства.
</div>
<div class="alert alert-secondary" role="alert">
  Человечеству мала одна планета.
</div>
<div class="alert alert-success" role="alert">
  Мы сделаем обитаемыми безжизненные пока планеты.
</div>
<div class="alert alert-danger" role="alert">
  И начнем с Марса!
</div>
<div class="alert alert-warning" role="alert">
  Присоединяйся!
</div>
</body>
</html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
