from bottle import default_app, route, template, request, run

personnage = []


@route('/')
def hello_world():
    return template('tableau', personnage=personnage)


@route('/', method="POST")
def nom_personne():
    name = request.forms.get("employe")
    jours = int(request.forms.get("jours"))
    taux = float(request.forms.get("taux"))
    salaire = jours*taux
    salaire_arroundi = round(salaire, 2)
    personnage.append({'nom':name, 'jours':jours, 'taux':taux, 'salaire':salaire_arroundi})
    return template('make_tableau', personnage=personnage)


application = default_app()