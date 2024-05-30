# Token API
import time

import requests
import test_bottle_app
import subprocess
import access


# lancer des tests
def launch_test_bottle_app():
    print(test_bottle_app.test_hello_world(), "Tes tests sont passés")
    test_bottle_app.test_hello_world()


# push sur git
def push_git():
    subprocess.call('./gitpush.sh')
    print("git push effectué ")


# pull git sur pythonanywhere
def pull_git():
    command = 'git pull\n'
    data = {'input': command}
    response = requests.post(
        "https://{host}/api/v0/user/{username}/consoles/{id}/send_input/".format(
            host=access.host, username=access.username, id=access.id),
        headers={'Authorization': 'Token {token}'.format(token=access.token)}, json=data)
    if response.status_code == 200:
        print("Git pull effectué")
    else:
        print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))


# redémarrer le server
def reload_web_app():
    response = requests.post('https://{host}/api/v0/user/{username}/webapps/{domain_name}/reload/'.format(
        host=access.host, username=access.username, domain_name=access.domain_name
    ),
        headers={'Authorization': 'Token {token}'.format(token=access.token)})
    if response.status_code == 200:
        print('WebApp reloaded:')
    else:
        print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))


# verifier si le site tourne

if __name__ == "__main__":
    launch_test_bottle_app()
    push_git()
    pull_git()
    time.sleep(10)
    reload_web_app()

