🔥 Google Calendar CLI (Python)
A simple Python script to fetch events from Google Calendar using OAuth 2.0.

🚀 Quick Setup
1. Get Google OAuth Credentials
Go to Google Cloud Console.

Create a new project → Enable "Google Calendar API".

Under "APIs & Services" → "Credentials", create an OAuth 2.0 Client ID.

Choose "Desktop App" as the application type.

Download the credentials as client_secret.json and place it in your project folder.

⚠️ Never share client_secret.json or commit it to Git!

2. Install Dependencies
bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
3. Run the Script
bash
python calendar_fetcher.py
On first run, it will open a browser for OAuth login.

After auth, it saves a token.json (auto-refreshes tokens).

🔐 Security Note
client_secret.json = Your app’s password (keep it private!).

If exposed, revoke it in GCP and generate a new one.

🐍 Code Explanation
What the Script Does
Uses client_secret.json to authenticate via OAuth 2.0.

Fetches upcoming events from your primary Google Calendar.

Prints event names/times in the terminal.

File Structure
text
your_project/
└── calendar_fetcher.py  # Main Python script
└── client_secret.json   # Google OAuth creds (IGNORE IN GIT)
└── token.json           # Auto-generated auth token
