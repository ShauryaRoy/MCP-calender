Here’s a clean, minimal `README.md` for your Python script:

---

# 📅 Google Calendar CLI (Python)  
*A lightweight script to fetch Google Calendar events using OAuth 2.0*

---

## 🔧 Setup  
### 1. Get Google API Credentials  
1. Go to [Google Cloud Console](https://console.cloud.google.com/)  
2. Create a project → Enable **"Google Calendar API"**  
3. Under *Credentials* → Create **OAuth 2.0 Client ID** (Desktop App type)  
4. Download as `client_secret.json` and place in project folder  

### 2. Install Dependencies  
```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### 3. Run  
```bash
python calendar_fetcher.py
```
- First run opens browser for OAuth login  
- Saves credentials to `token.json` (auto-refreshes)  

---

## 🚨 Security  
- Keep `client_secret.json` **private** (add to `.gitignore`)  
- If exposed:  
  ```bash
  # Remove from Git history
  git rm --cached client_secret.json
  ```
  Then **revoke/recreate** in [Google Cloud Console](https://console.cloud.google.com/apis/credentials)  

---

## 📂 Files  
```
.
├── calendar_fetcher.py   # Main script
├── client_secret.json   # Google OAuth creds (DO NOT SHARE)
└── token.json          # Auto-generated auth token
```

---

## 💻 Output Example  
```plaintext
Upcoming Events:
1. Team Sync - Jun 12 14:00-15:00
2. Doctor Appointment - Jun 13 10:30-11:00
```

---

## ❓ Issues?  
- `ImportError` → Reinstall dependencies  
- Auth errors → Delete `token.json` and rerun  



