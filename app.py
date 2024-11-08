from flask import Flask

# インスタンス化する
app = Flask(__name__)

#ルーティング設定をする
@app.route('/')
def hello_world():
    return 'Welcome to Flask World'

if __name__ == "__main__":
    app.run(debug=True)