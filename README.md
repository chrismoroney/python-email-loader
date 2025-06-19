# Gmail Reader Console App (Python)

This is a simple Python console application that connects to your Gmail account, fetches **unread emails**, and displays their **sender**, **subject**, and a short **snippet** of the message body.

Perfect for personal automation tasks, daily digests, or integrating into a larger AI-powered assistant (in progress)!

---

## Features

- Authenticate securely with your Gmail account (OAuth2)
- Read and display up to 10 **unread** messages
- Print email sender, subject, and message snippet to the console

---

## Requirements

- Python 3.7+
- A Google Account with Gmail
- A Google Cloud Project with Gmail API enabled

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/gmail-reader-app.git
cd gmail-reader-app
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### 3. Enable Gmail API
- Visit Google Cloud Console

- Create or select a project

- Go to APIs & Services > Library, search for Gmail API, and enable it

- Go to APIs & Services > Credentials

- Click Create Credentials > OAuth Client ID

- Application type: Desktop App

- Download the generated ```credentials.json``` file

- Place ```credentials.json``` in the project directory

### 4. Set Up OAuth Consent Screen
- Go to OAuth consent screen in the Cloud Console

- Choose "External" user type

- Fill out app name and email fields

- Under Test Users, add your own Google email address

### Usage
```bash
python read_unread_emails.py
```
- On first run, you'll be prompted to sign in via your browser

- A token.json file will be created for future logins

- The app will display up to 10 unread messages in your Gmail inbox

### Project Structure

```graphql
gmail-reader-app/
├── credentials.json      # OAuth client credentials (you download this)
├── token.json            # Auto-generated after first login
├── read_unread_emails.py # Main script
└── README.md             # This file
```

### Security Notes

- Never share your credentials.json or token.json files

- These files contain sensitive access tokens linked to your Google account

- If compromised, revoke access via your Google Account Security

### What's Next?
You can extend this app to:

- Summarize email content using OpenAI

- Mark emails as read after processing

- Save results to files

- Run on a schedule using cron or schedule

- Move files or trigger other automations

