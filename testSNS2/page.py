import flask
import sqlite3
import sys

# Flaskアプリ呼び出し、よくわからん
app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'pass'

# 初めのページ
@app.route('/')
def main():
    return flask.render_template('index.html')

# ログインページ
@app.route('/login')
def login():
    flask.session['name'] = flask.request.args.get('name')
    
    return 'ようこそ' + flask.session['name'] + 'さん<br><a href="/mypage">マイページへ</a>'

@app.route('/mypage')
def mypage():
    if 'name' in flask.session:
        return flask.session['name'] + 'さんのページ<br><br><a href="/logout">ログアウト</a> <a href="/">トップページ</a>'
    else:
        return 'ログインしてください<br><br><a href="/">トップページ</a>'

@app.route('/logout')
def logout():
    del flask.session['name']

    return 'ログアウトしました<br><a href="/">トップページへ戻る</a>'


if __name__ == "__main__":
    # app.debug = True
    app.run()