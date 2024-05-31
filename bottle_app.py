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
    taux = request.forms.get("taux")
    return template('make_tableau', names=name, jours=jours, taux=taux)


application = default_app()
