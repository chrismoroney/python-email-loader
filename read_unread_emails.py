import os.path
import base64
import re
from email.message import EmailMessage
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these SCOPES, delete token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If no valid credentials, prompt login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def get_unread_emails(service):
    results = service.users().messages().list(userId='me', labelIds=['UNREAD'], maxResults=10).execute()
    messages = results.get('messages', [])

    if not messages:
        print("No unread messages.")
        return

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_data['payload']['headers']
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '(No Subject)')
        sender = next((h['value'] for h in headers if h['name'] == 'From'), '(Unknown Sender)')
        snippet = msg_data.get('snippet', '')

        print(f"\nFrom: {sender}\nSubject: {subject}\nSnippet: {snippet}\n{'-'*40}")

def main():
    creds = authenticate()
    service = build('gmail', 'v1', credentials=creds)
    get_unread_emails(service)

if __name__ == '__main__':
    main()
