# mbox_processor.py

import mailbox
import time

def save_emails_to_mbox(emails, mbox_file_path='../data/input.mbox'):
    mbox = mailbox.mbox(mbox_file_path)
    
    for email_data in emails:
        msg = mailbox.mboxMessage()
        msg.set_payload(email_data.get('raw', '').encode('utf-8'))
        
        # Definindo headers básicos
        headers = email_data.get('payload', {}).get('headers', [])
        for header in headers:
            name = header.get('name')
            value = header.get('value')
            if name and value:
                msg[name] = value
        
        mbox.add(msg)
        mbox.lock()
        mbox.unlock()
    
    mbox.close()

def process_emails_from_gmail(access_token):
    emails = fetch_emails(access_token)
    save_emails_to_mbox(emails)

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

if __name__ == '__main__':
    print("Mbox Processor")
    print("----------------")
    choice = input("Deseja processar e-mails do Gmail? (y/n): ").strip().lower()
    
    if choice == 'y':
        access_token = input("Por favor, insira o token de acesso do Gmail: ").strip()
        if access_token:
            process_emails_from_gmail(access_token)
            print("E-mails processados e salvos no arquivo mbox com sucesso!")
        else:
            print("Token de acesso inválido.")
    else:
        print("Operação cancelada.")
