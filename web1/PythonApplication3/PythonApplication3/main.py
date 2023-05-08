from flask import Flask, request, current_app, make_response,  abort, g,render_template


app = Flask(__name__, template_folder='templates')

@app.after_request
def after_request(response):
    print("after_request() called")
    return response

@app.errorhandler(404)
def http_404_handler(error):
    return "HTTP 404 Error Encountered", 404

@app.errorhandler(500)
def http_500_handler(error):
    return "HTTP 500 Error Encountered", 500

@app.route("/")
def index():
    # print("index() called")
    # return 'Testings Request Hooks'
    abort(404)

@app.route('/login')
def index1():
    with app.test_request_context('/login'):
        q = request.url
        w = request.method
        e = current_app.name

    print(q)
    print(w)
    print(e)
    return 'login'

@app.route('/books/<genre>')
def books(genre):
    res = make_response("All Books in {} category".format(genre))
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'Foobar'
    return res

@app.route('/404')
def http_404_handler():
    return make_response("404 Error", 404)

@app.route('/set-cookie')
def set_cookie():
    res = make_response("Cookie setter")
    res.set_cookie("favorite-color", "skyblue", 60*60*24*15)
    res.set_cookie("favorite-font", "sans-serif", 60*60*24*15)
    return res

#@app.route('/transfer')
#def transfer():
#    return redirect("http://vk.com")
# не фурычит редирект с https

@app.route('/500')
def http_500_handler():
    return "500 Error", 500

@app.route('/htmm')
def indexht():
    name, age, profession = "Игорь", 9, 'Да'
    template_context = dict(name=name, age=age, profession=profession)
    return render_template('index.html', **template_context)
@app.route('/ht')
def indexxxx():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)