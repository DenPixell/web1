from flask import Flask, request, current_app

app = Flask(__name__)

@app.route('/')
def index():
    with app.test_request_context('/'):
        q = request.url
        w = request.method
        e = current_app.name

    print(q)
    print(w)
    print(e)
    return 'Welcome to LoL graph'
    
@app.route('/user/<id>/')
def User_Profile(id):
    with app.test_request_context('/user/<id>/'):
        q = request.path
        w = request.method
        e = current_app.name

    print(q)
    print(w)
    print(e)
    return "Сводка игрока: #{}".format(id)
    
@app.route('/update')
def News():
    with app.test_request_context('/update'):
        q = request.path
        w = request.method
        e = current_app.name

    print(q)
    print(w)
    print(e)
    return 'В среду 22.03.2023 выходит новый патч который превнесёт нового персонажа Милио!'
    

@app.route('/graph')
def Entrance():
    with app.test_request_context('/graph'):
        q = request.path
        w = request.method
        e = current_app.name

    print(q)
    print(w)
    print(e)
    return 'Введите ник и сервер для получения статистики'
  
if __name__ == "__main__":
    app.run(debug=True)

