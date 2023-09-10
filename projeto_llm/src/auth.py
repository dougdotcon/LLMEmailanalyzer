# auth.py

from flask import Flask, redirect, url_for, session, request,  jsonify
from flask_oauthlib.client import OAuth

app = Flask(__name__)
app.secret_key = 'random_secret_key'  # Em um cenário real, use uma chave secreta segura
oauth = OAuth(app)

# Configuração do Gmail OAuth2
gmail = oauth.remote_app(
    'gmail',
    consumer_key='YOUR_CONSUMER_KEY',
    consumer_secret='YOUR_CONSUMER_SECRET',
    request_token_params={
        'scope': 'https://www.googleapis.com/auth/gmail.readonly',  # Escopo para ler e-mails
    },
    base_url='https://www.googleapis.com/gmail/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

@app.route('/login')
def login():
    return gmail.authorize(callback=url_for('authorized', _external=True))

@app.route('/logout')
def logout():
    session.pop('oauth_token')
    return redirect(url_for('index'))

@app.route('/login/authorized')
def authorized():
    response = gmail.authorized_response()
    if response is None or response.get('access_token') is None:
        return 'Access denied: reason={} error={}'.format(
            request.args['error_reason'],
            request.args['error_description']
        )
    session['oauth_token'] = (response['access_token'], '')
    # Aqui você pode adicionar código para processar os e-mails após a autenticação bem-sucedida

@app.route('/login/authorized')
def authorized():
    response = gmail.authorized_response()
    if response is None or response.get('access_token') is None:
        return 'Access denied: reason={} error={}'.format(
            request.args['error_reason'],
            request.args['error_description']
        )
    session['oauth_token'] = (response['access_token'], '')
    
    # Processar e-mails após autenticação bem-sucedida
    emails = fetch_emails(session['oauth_token'][0])
    
    # Aqui, você pode adicionar código para salvar os e-mails recuperados em um arquivo mbox ou em outro formato
    # Por exemplo: save_emails_to_mbox(emails)
    
    return jsonify(emails)  # Isso é apenas para visualização. Em produção, você pode redirecionar o usuário para uma página de dashboard ou similar.

def fetch_emails(access_token):
    headers = {'Authorization': 'Bearer {}'.format(access_token)}
    # Esta URL busca os últimos 100 e-mails. Você pode ajustar conforme necessário.
    response = requests.get('https://www.googleapis.com/gmail/v1/users/me/messages?maxResults=100', headers=headers)
    email_list = response.json().get('messages', [])
    
    emails = []
    for email in email_list:
        email_data = requests.get('https://www.googleapis.com/gmail/v1/users/me/messages/{}'.format(email['id']), headers=headers).json()
        emails.append(email_data)
    
    return emails

    return 'Logged in successfully!'

@gmail.authorized_handler
def authorized(resp):
    if resp is None:
        return 'Access denied: reason={0} error={1}'.format(
            request.args['error_reason'],
            request.args['error_description']
        )
    session['oauth_token'] = (resp['access_token'], '')
    return 'Logged in successfully!'

@gmail.tokengetter
def get_gmail_oauth_token():
    return session.get('oauth_token')

if __name__ == '__main__':
    app.run()
