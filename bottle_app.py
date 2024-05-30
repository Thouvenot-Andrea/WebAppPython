# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, template, request, run


@route('/')
def hello_world():
    return template('tableau')


# @route('/tableau', method = 'POST')
# def route_tableau():


@route('/', method="POST")
def nom_personne():
    name = [request.forms.get("employe")]
    jours = request.forms.get("jours")
    return template('templates/make_tableau', names=name, jours=jours)


application = default_app()
