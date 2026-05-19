# 📧 AI Email Sorter Agent

> Automatically sorts your Gmail emails into smart categories using **Google Gemini AI** — completely free!

---

## Screenshorts
<img width="1119" height="700" alt="Screenshot 2026-05-19 102009" src="https://github.com/user-attachments/assets/701b894f-00ab-448a-956e-ca8b694477b5" />
<img width="1119" height="641" alt="1pic" src="https://github.com/user-attachments/assets/3e2c977f-1344-464a-b4b9-283373141150" />
<img width="1119" height="638" alt="2pic" src="https://github.com/user-attachments/assets/bdb71a1e-165a-47ed-b152-16737b557256" />
<img width="1119" height="638" alt="3pic" src="https://github.com/user-attachments/assets/33abe13b-21b3-4fe1-a519-e6cbe524680a" />

---

## ✨ What It Does

This AI agent reads your Gmail inbox and automatically labels emails into categories like:

- 💼 LinkedIn
- 🍔 Food & Delivery (Zomato, Swiggy)
- 🛒 Shopping & Promotions (Amazon, Flipkart, BookBub)
- 🏦 Bank & Finance (AngelOne, Zerodha, NSE)
- 🎓 College & University (Amrita, Coursera, Internshala)
- 💼 Offer Letter / Job (micro1, Naukri, Indeed)
- 🎵 Music & Entertainment (Spotify, Netflix, Hotstar)
- 💻 Tech & Developer (GitHub, GitLab, Vercel, AWS)
- 🔔 Google Services
- 📝 Productivity & Tools (Grammarly, Notion, Canva)
- 📱 Social Media (Instagram, Reddit, Twitter)
- 📰 Newsletter (Quora, Medium)
- 🤖 And more — unknown emails sorted by Gemini AI!
<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/9baee44b-e01a-491f-a907-9d2948efedae" />

---

## 📁 Project Folder Structure

```
EmailSorter/
├── email_sorter.py       ← Main code (this file)
├── credentials.json      ← Downloaded from Google Cloud (DO NOT SHARE)
├── token.json            ← Auto-created on first run (DO NOT SHARE)
├── .env                  ← Your Gemini API key (DO NOT SHARE)
├── .gitignore            ← Keeps secret files off GitHub
└── README.md             ← This file
```

> ⚠️ **Never upload** `credentials.json`, `token.json`, or `.env` to GitHub!

---

## 🛠️ Tech Stack

| Tool | Purpose | Cost |
|------|---------|------|
| Python 3 | Programming language | Free |
| Gmail API | Read & label emails | Free |
| Google Gemini AI | Classify unknown emails | Free |
| Google Cloud Console | Enable Gmail API | Free |
| VS Code | Code editor | Free |

---

## 🚀 Setup — Step by Step

### ✅ Step 1 — Install Python

1. Go to: https://www.python.org/downloads
2. Download and install Python
3. ⚠️ During install, **check the box** → `Add Python to PATH`
4. Verify install — open terminal and type:
```bash
python --version
```
You should see something like `Python 3.12.x`

---

### ✅ Step 2 — Install VS Code

1. Go to: https://code.visualstudio.com
2. Download and install VS Code
3. Open VS Code
4. Press `Ctrl + Shift + X`
5. Search **Python** → Install the extension by Microsoft

---

### ✅ Step 3 — Create Your Project Folder

1. Create a new folder on your Desktop named `EmailSorter`
2. Open VS Code → `File → Open Folder` → select `EmailSorter`
3. Open terminal inside VS Code → press `` Ctrl + ` ``

---

### ✅ Step 4 — Install Required Libraries

Run this in VS Code terminal:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client google-genai python-dotenv
```

---

### ✅ Step 5 — Set Up Gmail API (Google Cloud)

**5a. Create a Project**
1. Go to: https://console.cloud.google.com
2. Click the dropdown at the top → **New Project**
3. Name it `EmailSorter` → Click **Create**

**5b. Enable Gmail API**
1. Go to **APIs & Services → Library**
2. Search `Gmail API` → Click it → Click **Enable**

**5c. Configure OAuth Consent Screen**
1. Go to **APIs & Services → OAuth Consent Screen**
2. Choose **External** → Click **Create**
3. Fill in:
   - App name: `EmailSorter`
   - User support email: `your Gmail`
   - Developer email: `your Gmail`
4. Click **Save and Continue** on every page (skip optional fields)
5. On the last page → Click **Back to Dashboard**
6. Scroll down to **Test Users** → Click **+ Add Users**
7. Add your Gmail address → Click **Save**

**5d. Create OAuth Credentials**
1. Go to **APIs & Services → Credentials**
2. Click **+ Create Credentials → OAuth 2.0 Client ID**
3. Application type → Select **Desktop App**
4. Name it `EmailSorter` → Click **Create**
5. Click the **⬇️ Download** button on the right
6. Rename the downloaded file to: `credentials.json`
7. Move `credentials.json` into your `EmailSorter` folder

---

### ✅ Step 6 — Get Gemini API Key (Free)

1. Go to: https://aistudio.google.com
2. Login with your **Google account**
3. Click **Get API Key** in the left sidebar
4. Click **Create API Key**
5. Select your `EmailSorter` project
6. Click **Create API key in existing project**
7. Copy the key — it looks like: `AIzaSy...`

---

### ✅ Step 7 — Create the `.env` File

1. In VS Code, right-click in the file explorer → **New File**
2. Name it exactly: `.env`
3. Paste this inside (replace with your actual key):

```
GEMINI_API_KEY=AIzaSy-your-actual-key-here
```

---

### ✅ Step 8 — Create `.gitignore` File

1. In VS Code, right-click → **New File**
2. Name it: `.gitignore`
3. Paste this inside:

```
.env
credentials.json
token.json
__pycache__/
*.pyc
```

This makes sure your secret files are **never uploaded to GitHub**.

---

### ✅ Step 9 — Add the Code

1. In VS Code, right-click → **New File**
2. Name it: `email_sorter.py`
3. Copy and paste the full code from `email_sorter.py` in this repo

---

### ✅ Step 10 — Run the Agent!

In VS Code terminal, run:

```bash
python email_sorter.py
```

**What happens on first run:**
- A browser window opens automatically
- Login with your Gmail account
- Click **Advanced** → **Go to EmailSorter (unsafe)** → **Allow**
- Come back to VS Code — it starts sorting automatically!

---

## 📊 Example Terminal Output

```
===================================================
🤖  AI Email Sorter Agent Starting...
===================================================
✅ Connected to Gmail!

📬 Fetching last 50 emails...
✅ Fetched 50 emails.

🧠 Sorting 50 emails...

[1/50] Subject: "frontend developer": ArGo Intern
       From: LinkedIn Job Alerts
       ⚡ Known → ✅ LinkedIn

[2/50] Subject: Take the shot 🎯
       From: Zomato
       ⚡ Known → ✅ Food & Delivery

[3/50] Subject: Your ebook bargains for Monday
       From: BookBub
       ⚡ Known → ✅ Shopping & Promotions

[4/50] Subject: Your application is complete
       From: micro1
       ⚡ Known → ✅ Offer Letter / Job

[5/50] Subject: Some unknown email
       From: randomsender@email.com
       🤖 AI → ✅ Important / Personal

===================================================
📊  SORTING COMPLETE! Summary:
===================================================
  📁  LinkedIn                       8 email(s)
  📁  Offer Letter / Job             7 email(s)
  📁  Food & Delivery                5 email(s)
  📁  Shopping & Promotions          5 email(s)
  📁  College & University           4 email(s)
  📁  Bank & Finance                 4 email(s)
  📁  Tech & Developer               3 email(s)
  📁  Social Media                   3 email(s)
  📁  Newsletter                     3 email(s)
  📁  Google Services                2 email(s)
  📁  Productivity & Tools           2 email(s)
  📁  Other                          4 email(s)
---------------------------------------------------
  ⚡ Sorted by known senders : 46
  🤖 Sorted by Gemini AI     : 4
  📧 Total emails sorted     : 50
===================================================
```

---

## 📂 Where to See Results in Gmail

1. Open Gmail: https://gmail.com
2. Look at the **left sidebar**
3. Click **More** to expand all folders
4. Find the **AI-Sorted** folder with subfolders:

```
📁 AI-Sorted
    ├── LinkedIn
    ├── College & University
    ├── Offer Letter / Job
    ├── Shopping & Promotions
    ├── Bank & Finance
    ├── Social Media
    ├── Food & Delivery
    ├── Music & Entertainment
    ├── Tech & Developer
    ├── Google Services
    ├── Productivity & Tools
    ├── Newsletter
    └── Other
```

---

## ➕ How to Add More Senders

Open `email_sorter.py` and find the `KNOWN_SENDERS` dictionary. Add any sender like this:

```python
KNOWN_SENDERS = {
    "spotify":    "Music & Entertainment",
    "yourbank":   "Bank & Finance",       # ← add like this
    "yourapp":    "Your Category",        # ← add your own
    ...
}
```

The keyword can be any part of the sender's email address or name.

---

## 🔧 Customization

**Sort more emails** — change this line in `email_sorter.py`:
```python
emails = get_emails(service, max_emails=50)  # change to 100, 200, etc.
```

**Add new category** — add to `AI_CATEGORIES` list:
```python
AI_CATEGORIES = [
    "LinkedIn",
    "Your New Category",   # ← add here
    ...
]
```

---

## ❓ Common Errors & Fixes

| Error | Fix |
|-------|-----|
| `GEMINI_API_KEY not found` | Check `.env` file has your key with no spaces |
| `Access blocked` | Add your Gmail in OAuth consent screen → Test Users |
| `credentials.json not found` | Download from Google Cloud and put in folder |
| `ModuleNotFoundError` | Run `pip install` command from Step 4 again |
| `Token expired` | Delete `token.json` and run again |
| `404 model not found` | Make sure you use `gemini-2.0-flash` in the code |

---

## ⚠️ Security — NEVER Share or Upload These Files

| File | Why It's Sensitive |
|------|--------------------|
| `credentials.json` | Gives access to your Google account |
| `token.json` | Your Gmail login session |
| `.env` | Your Gemini API key |

The `.gitignore` file we created in Step 8 protects these automatically on GitHub.

---

## 🆓 Is It Really Free?

| Service | Free Limit | Our Usage |
|---------|-----------|-----------|
| Gmail API | 1 billion requests/day | ~50-100/run |
| Gemini AI (Free Tier) | 1500 requests/day | ~5-10/run (most sorted by known senders) |
| Google Cloud | Free forever for this | ✅ |

**Yes — 100% free for personal use!** 🎉

---

## 👨‍💻 Built With

- Python 3
- Gmail API
- Google Gemini AI (`gemini-2.0-flash`)
- `google-genai` library
- `python-dotenv`

---

## 📄 License

This project is open source and free to use for personal projects.


