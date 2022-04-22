from flask import Flask, request, redirect
from jinja2 import FileSystemLoader, Environment
import Work_With_MongoDB

templateLoader = Environment(loader=FileSystemLoader(searchpath='./templates'))

UserName = ''

app = Flask(__name__, static_folder='./static', static_url_path='/static')


@app.route('/')
def test():
    template = templateLoader.get_template('index.template.html')
    return template.render()


@app.route('/registration', methods=['get', 'post'])
def register():
    nick = request.form.get('nickname')
    mail = request.form.get('mail')
    password = request.form.get('password')
    Work_With_MongoDB.addit(nick, mail, password)
    return redirect('/')


@app.route('/loggingpage', methods=['get', 'post'])  # Эта штука за вывод страницы логина ответственна
def loggingpage():
    template = templateLoader.get_template('Registr.html')
    return template.render()


@app.route('/logging', methods=['get', 'post'])
def logging():
    global UserName
    nick = request.form.get('nickname')
    password = request.form.get('password')

    #if Work_With_MongoDB.checkit(nick, password) != None:
    #    UserName = nick
    return redirect('/TaskMode')  # тут просто переадресацию на приложение
    #else:
    #    return redirect('/loggingpage')


@app.route('/TaskMode', methods=['post', 'get'])  # Эта штука за вывод страницы c досками ответственна
def Taskpage():
    template = templateLoader.get_template('ConfigProjects.html')
    return template.render()
@app.route('/SheduleMode', methods=['post', 'get'])
def Shedulepage():
    template = templateLoader.get_template('.html')  # тут название страницы с расписанием
    return template.render()
@app.route('/StatsMode', methods=['post', 'get'])
def Shedulepage():
    template = templateLoader.get_template('.html')  # тут название страницы с
    return template.render()
@app.route('/SheduleMode', methods=['post', 'get'])  # Эта штука за вывод страницы расписания ответственна
def Taskpage():
    template = templateLoader.get_template('.html')  # тут название страницы с созданием задания
    return template.render()

app.run(host='0.0.0.0', port=3000)
