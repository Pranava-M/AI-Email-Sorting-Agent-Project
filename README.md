# 🤖 AI Email Sorter Agent

An AI-powered agent that connects to your Gmail, reads your inbox, and automatically organizes emails into smart categories — all running locally on your machine.

---

## 📋 Table of Contents

- [Features](#-features)
- [How It Works](#-how-it-works)
- [Technologies](#-technologies)
- [Project Structure](#-project-structure)
- [Setup Guide](#-setup-guide)
  - [Step 1 — Install Python](#step-1--install-python)
  - [Step 2 — Install VS Code](#step-2--install-vs-code)
  - [Step 3 — Install Dependencies](#step-3--install-dependencies)
  - [Step 4 — Set Up Gmail API](#step-4--set-up-gmail-api)
  - [Step 5 — Choose an AI Provider](#step-5--choose-an-ai-provider)
  - [Step 6 — Configure Environment](#step-6--configure-environment)
  - [Step 7 — Run the Agent](#step-7--run-the-agent)
- [Email Categories](#-email-categories)
- [Example Output](#-example-output)
- [Customization](#-customization)
- [Security](#-security)
- [Common Errors](#-common-errors)
- [Future Ideas](#-future-ideas)

---

## ✨ Features

- Connects securely to Gmail via OAuth 2.0
- Uses AI to intelligently classify emails
- Auto-creates and applies Gmail labels
- Supports multiple AI providers (Gemini, Claude, Groq, OpenRouter)
- 100% free to build and run
- Fully customizable categories
- Beginner-friendly setup

---

## 🧠 How It Works

```
Gmail Inbox → Fetch Emails → Send to AI → Predict Category → Apply Gmail Label
```

1. Authenticates with your Gmail account securely
2. Fetches your recent emails
3. Sends email metadata/content to an AI model
4. AI classifies each email into a category
5. Creates Gmail labels (e.g. `AI-Sorted/LinkedIn`)
6. Applies the labels to each email automatically

---

## 🛠 Technologies

| Technology | Purpose |
|---|---|
| Python | Core language |
| Gmail API | Read & modify Gmail |
| Google Cloud Console | Enable & manage Gmail API |
| OAuth 2.0 | Secure Gmail authentication |
| Gemini / Claude / Groq | AI email classification |
| VS Code | Recommended code editor |

---

## 📁 Project Structure

```
email-sorter/
├── credentials.json     # OAuth credentials from Google Cloud
├── token.json           # Auto-generated after first login
├── email_sorter.py      # Main script
├── .env                 # API keys (never commit this)
├── requirements.txt     # Python dependencies
└── README.md
```

---

## 🚀 Setup Guide

### Step 1 — Install Python

Download from [python.org/downloads](https://www.python.org/downloads/).

> ⚠️ During installation, check **"Add Python to PATH"**

Verify it worked:

```bash
python --version
```

---

### Step 2 — Install VS Code

Download from [code.visualstudio.com](https://code.visualstudio.com/).

Recommended extensions: **Python**, **Pylance**

---

### Step 3 — Install Dependencies

Open a terminal inside your project folder and run:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client python-dotenv
```

Then install your chosen AI provider's library (see [Step 5](#step-5--choose-an-ai-provider)).

---

### Step 4 — Set Up Gmail API

#### 4a. Create a Google Cloud Project

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create a new project (e.g. `EmailSorter`)

#### 4b. Enable the Gmail API

1. Navigate to **APIs & Services → Library**
2. Search for **Gmail API** and click **Enable**

#### 4c. Configure OAuth Consent Screen

1. Go to **APIs & Services → OAuth Consent Screen**
2. Select **External**, fill in the basic app details

#### 4d. Add Yourself as a Test User

> ⚠️ **This step is required.** Without it, Gmail authentication will fail.

1. Go to **OAuth Consent Screen → Test Users**
2. Add your Gmail address (e.g. `your-email@gmail.com`)

#### 4e. Create OAuth Credentials

1. Go to **APIs & Services → Credentials**
2. Click **Create Credentials → OAuth Client ID**
3. Choose **Desktop Application**
4. Download the credentials file
5. Rename it to `credentials.json` and place it in your project folder

---

### Step 5 — Choose an AI Provider

Pick any one of these free options:

#### ✅ Option A — Google Gemini (Recommended)

**Why:** Completely free, no credit card, uses your existing Google account.

1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Sign in and click **Get API Key → Create API Key**
3. Select your Google Cloud project and copy the key

```bash
pip install google-generativeai
```

```env
GEMINI_API_KEY=your_key_here
```

---

#### ✅ Option B — Anthropic Claude

**Why:** High-quality classification, free tier available.

1. Sign up at [console.anthropic.com](https://console.anthropic.com)
2. Go to **API Keys → Create Key** and copy it

```bash
pip install anthropic
```

```env
ANTHROPIC_API_KEY=your_key_here
```

---

#### ✅ Option C — Groq

**Why:** Extremely fast inference, free signup, no credit card.

1. Sign up at [console.groq.com](https://console.groq.com)
2. Create and copy your API key

```env
GROQ_API_KEY=your_key_here
```

---

#### ✅ Option D — OpenRouter

**Why:** Access to many free models from multiple providers.

1. Sign up at [openrouter.ai](https://openrouter.ai)
2. Create and copy your API key

```env
OPENROUTER_API_KEY=your_key_here
```

---

### Step 6 — Configure Environment

Create a `.env` file in your project folder with your chosen API key:

```env
# Use only one of these
GEMINI_API_KEY=your_key_here
# ANTHROPIC_API_KEY=your_key_here
# GROQ_API_KEY=your_key_here
# OPENROUTER_API_KEY=your_key_here
```

> ⚠️ Never share this file or commit it to GitHub.

---

### Step 7 — Run the Agent

```bash
python email_sorter.py
```

**First run:** A browser window will open automatically. Sign in with Gmail and grant permissions. A `token.json` file will be created — future runs will be fully automatic.

---

## 🗂 Email Categories

The agent sorts emails into these default categories:

```python
CATEGORIES = [
    "LinkedIn",
    "College / University",
    "Offer Letter / Job",
    "Promotions / Deals",
    "Bank / Finance",
    "Social Media",
    "Newsletter",
    "Spam / Junk",
    "Important / Personal",
    "Other"
]
```

Gmail labels are created automatically under the `AI-Sorted/` prefix:

```
AI-Sorted/LinkedIn
AI-Sorted/Promotions
AI-Sorted/College
```

---

## 📦 Example Output

```
🤖 Email Sorter Agent Starting...

✅ Connected to Gmail!

📬 Fetching last 20 emails...

🧠 Classifying emails with AI...

[1/20] Processing: "Internship Opportunity at TechCorp"
  ✅ Labeled as: Offer Letter / Job

[2/20] Processing: "You have a new connection on LinkedIn"
  ✅ Labeled as: LinkedIn

[3/20] Processing: "50% off — Today Only!"
  ✅ Labeled as: Promotions / Deals

═══════════════════════════════════
📊 SORTING COMPLETE! (20 emails)
═══════════════════════════════════

  LinkedIn              5
  Offer Letter / Job    3
  Promotions / Deals    4
  College / University  2
  Other                 6

═══════════════════════════════════
```

---

## 🎛 Customization

**Process more emails:**

```python
emails = get_emails(service, max_emails=50)
```

**Add custom categories:**

```python
CATEGORIES = [
    "GitHub",
    "Hackathons",
    "Internships",
    "Coding Platforms",
    "Shopping",
    "YouTube",
]
```

---

## 🛡 Security

- Your Gmail **password is never stored**
- OAuth 2.0 handles all authentication securely
- API keys stay local in your `.env` file
- `token.json` only stores your Gmail session token

**Add a `.gitignore` to prevent accidentally committing sensitive files:**

```
.env
token.json
credentials.json
__pycache__/
```

> ⚠️ Never push `.env`, `credentials.json`, or `token.json` to a public repository.

---

## ❗ Common Errors

| Error | Solution |
|---|---|
| `Gmail API not enabled` | Enable the Gmail API in Google Cloud Console |
| `Access blocked` | Add yourself as a Test User in OAuth Consent Screen |
| `credentials.json not found` | Re-download OAuth credentials and place in project folder |
| `API Key Invalid` | Double-check your `.env` file for typos or extra spaces |

---

## 🧪 Testing Tips

Before running on your main inbox:

- Create a secondary Gmail account for testing
- Add it as a test user in Google Cloud
- Start small to verify things work:

```python
emails = get_emails(service, max_emails=5)
```

---

## 📈 Future Ideas

- 📊 Web dashboard with sorting analytics
- 🔔 Desktop notifications for important emails
- 🤖 AI priority scoring (urgent vs. low-priority)
- 🧹 Auto-delete or auto-archive spam
- 📧 Auto-reply templates for common emails
- ☁️ Deploy as a scheduled cloud job
- 📱 Mobile app or Chrome extension
- 📌 Important email flagging

---

## 📜 License

Free to use for learning and educational purposes.

---

## ❤️ Built With

Python · Gmail API · Google Gemini · Claude API · Google Cloud
