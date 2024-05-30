# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, template, request, run


@route('/')
def hello_world():
    return template('tableau')
    # return template('templates/tableau')


# @route('/tableau', method = 'POST')
# def route_tableau():


@route('/', method="POST")
def nom_personne():
    name = request.forms.get("employe")
    return name

# run();


application = default_app()
