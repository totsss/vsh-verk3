#29.01.2018
#Thordur Jonatansson
#Verkefni 3

from bottle import *

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')

@route('/')
def index():
    return """

      <h1>"hallo heimur!"</h1>
      <a href='/1'>val a<a/>
      <a href='/2'>val b<a/>
      """


@route('/2')
def index():
    listi1=['frett1.tpl','frett2.tpl','frett3.tpl','frett4.tpl']
    return template('appb.tpl',listi1=listi1)

@route('/3')
def index():
    return """<img src='static/fakenews.png'></img>"""


#      <link rel="stylesheet" type="text/css" href="static/style.css">



@route('/1')
def sida():

    return """
                  <h1>thetta er lidur a xd</h1>


                        <a href='/1608003640'>Thordur</a>
                        <a href='/2509003170'>Illugi</a>
                """

@route('/1608003640')
def index():
    kt="1608003640"
    return template("skra.tpl",kt=kt)

@route('/2509003170')
def index():
    kt="2509003170"
    return template("skra1.tpl",kt=kt)

@route('/frett/<nr>')
def staticfrett(nr):
    if nr =='1':
        return template('frett1.tpl')
    if nr =='2':
        return template('frett2.tpl')
    if nr =='3':
        return template('frett3.tpl')
    if nr =='4':
        return template('frett4.tpl')
#run(host='localhost', port=8080, debug=True)
run(host='0.0.0.0',port=os.environ.get('PORT'))
