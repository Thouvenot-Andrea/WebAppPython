# Token API
import requests

username = 'ESAPython'
token = '0bfcf4a8978f6470998c92bda9fd13f8271c4efb'
host = 'www.pythonanywhere.com'
domain_name = 'ESAPython.pythonanywhere.com'
id = '34017512'


# redemarer le server

def reload_web_app():
    response = requests.post('https://{host}/api/v0/user/{username}/webapps/{domain_name}/reload/'.format(
        host=host, username=username, domain_name=domain_name
    ),
        headers={'Authorization': 'Token {token}'.format(token=token)})
    if response.status_code == 200:
        print('WebApp reloaded:')
    else:
        print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))




# lancer des tests
# push sur git
# pull git sur pythonanywhere
def pull_git():
    command = 'git pull'
    data = {'input': command}
    response = requests.post(
        "https://{host}/api/v0/user/{username}/consoles/{id}/send_input/".format(host=host, username=username, id=id),
        headers={'Authorization': 'Token {token}'.format(token=token)}, json=data)
    if response.status_code == 200:
        print("Git pull effectué")
    else:
        print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))



# verifier si le site tourne

if __name__ == "__main__":
    pull_git()
    reload_web_app()







