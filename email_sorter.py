import os
from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google import genai


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("❌ ERROR: GEMINI_API_KEY not found in .env file!")
    print("   Create a .env file and add: GEMINI_API_KEY=your-key-here")
    exit()

client = genai.Client(api_key=GEMINI_API_KEY)

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']


KNOWN_SENDERS = {

    
    "linkedin":                 "LinkedIn",

    #  Social Media
    "instagram":                "Social Media",
    "facebook":                 "Social Media",
    "twitter":                  "Social Media",
    "x.com":                    "Social Media",
    "youtube":                  "Social Media",
    "reddit":                   "Social Media",
    "pinterest":                "Social Media",
    "snapchat":                 "Social Media",
    "discord":                  "Social Media",
    "telegram":                 "Social Media",
    "whatsapp":                 "Social Media",

    #  Food & Delivery
    "zomato":                   "Food & Delivery",
    "swiggy":                   "Food & Delivery",
    "blinkit":                  "Food & Delivery",
    "dunzo":                    "Food & Delivery",
    "zepto":                    "Food & Delivery",
    "magicpin":                 "Food & Delivery",

    #  Shopping & Promotions
    "amazon":                   "Shopping & Promotions",
    "flipkart":                 "Shopping & Promotions",
    "myntra":                   "Shopping & Promotions",
    "ajio":                     "Shopping & Promotions",
    "meesho":                   "Shopping & Promotions",
    "nykaa":                    "Shopping & Promotions",
    "snapdeal":                 "Shopping & Promotions",
    "shopify":                  "Shopping & Promotions",
    "bookbub":                  "Shopping & Promotions",
    "sweatcoin":                "Shopping & Promotions",

    #  Bank & Finance
    "hdfcbank":                 "Bank & Finance",
    "icicibank":                "Bank & Finance",
    "sbiinbank":                "Bank & Finance",
    "axisbank":                 "Bank & Finance",
    "kotakbank":                "Bank & Finance",
    "paytm":                    "Bank & Finance",
    "phonepe":                  "Bank & Finance",
    "gpay":                     "Bank & Finance",
    "razorpay":                 "Bank & Finance",
    "angelone":                 "Bank & Finance",
    "zerodha":                  "Bank & Finance",
    "groww":                    "Bank & Finance",
    "upstox":                   "Bank & Finance",
    "nse":                      "Bank & Finance",
    "bse":                      "Bank & Finance",
    "welcomeemail":             "Bank & Finance",
    "cams":                     "Bank & Finance",

    #  College & Education
    "amrita":                   "College & University",
    "amritaedu":                "College & University",
    "university":               "College & University",
    "college":                  "College & University",
    "coursera":                 "College & University",
    "udemy":                    "College & University",
    "edx":                      "College & University",
    "nptel":                    "College & University",
    "internshala":              "College & University",
    "unstop":                   "College & University",
    "leetcode":                 "College & University",
    "hackerrank":               "College & University",
    "codechef":                 "College & University",
    "codeforces":               "College & University",

    #  Jobs & Offers
    "naukri":                   "Offer Letter / Job",
    "indeed":                   "Offer Letter / Job",
    "glassdoor":                "Offer Letter / Job",
    "foundit":                  "Offer Letter / Job",
    "shine":                    "Offer Letter / Job",
    "hirist":                   "Offer Letter / Job",
    "instahyre":                "Offer Letter / Job",
    "micro1":                   "Offer Letter / Job",
    "careers":                  "Offer Letter / Job",
    "hr@":                      "Offer Letter / Job",
    "recruit":                  "Offer Letter / Job",
    "hiring":                   "Offer Letter / Job",
    "jobalert":                 "Offer Letter / Job",
    "job-alert":                "Offer Letter / Job",

    #  Music & Entertainment
    "spotify":                  "Music & Entertainment",
    "jiosaavn":                 "Music & Entertainment",
    "gaana":                    "Music & Entertainment",
    "wynk":                     "Music & Entertainment",
    "netflix":                  "Music & Entertainment",
    "primevideo":               "Music & Entertainment",
    "hotstar":                  "Music & Entertainment",
    "sonyliv":                  "Music & Entertainment",
    "zee5":                     "Music & Entertainment",

    #  Tech & Developer
    "github":                   "Tech & Developer",
    "gitlab":                   "Tech & Developer",
    "stackoverflow":            "Tech & Developer",
    "vercel":                   "Tech & Developer",
    "netlify":                  "Tech & Developer",
    "heroku":                   "Tech & Developer",
    "aws":                      "Tech & Developer",
    "digitalocean":             "Tech & Developer",
    "render":                   "Tech & Developer",
    "railway":                  "Tech & Developer",
    "postman":                  "Tech & Developer",

    #  Google Services
    "google":                   "Google Services",
    "googleplay":               "Google Services",

    #  Productivity & Tools
    "grammarly":                "Productivity & Tools",
    "notion":                   "Productivity & Tools",
    "slack":                    "Productivity & Tools",
    "trello":                   "Productivity & Tools",
    "zoom":                     "Productivity & Tools",
    "canva":                    "Productivity & Tools",
    "figma":                    "Productivity & Tools",
    "dropbox":                  "Productivity & Tools",

    #  Newsletters
    "quora":                    "Newsletter",
    "medium":                   "Newsletter",
    "substack":                 "Newsletter",

}


AI_CATEGORIES = [
    "LinkedIn",
    "College & University",
    "Offer Letter / Job",
    "Shopping & Promotions",
    "Bank & Finance",
    "Social Media",
    "Food & Delivery",
    "Music & Entertainment",
    "Tech & Developer",
    "Google Services",
    "Productivity & Tools",
    "Newsletter",
    "Spam / Junk",
    "Important / Personal",
    "Other"
]



def get_gmail_service():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    print("✅ Connected to Gmail!")
    return service


def get_emails(service, max_emails=50):
    print(f"\n📬 Fetching last {max_emails} emails...")

    results = service.users().messages().list(
        userId='me',
        maxResults=max_emails,
        labelIds=['INBOX']
    ).execute()

    messages = results.get('messages', [])

    if not messages:
        print("❌ No emails found in inbox!")
        return []

    emails = []
    for msg in messages:
        try:
            msg_data = service.users().messages().get(
                userId='me',
                id=msg['id'],
                format='full'
            ).execute()

            headers = msg_data['payload'].get('headers', [])
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
            sender  = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
            snippet = msg_data.get('snippet', '')

            emails.append({
                'id':      msg['id'],
                'subject': subject,
                'sender':  sender,
                'snippet': snippet
            })
        except Exception as e:
            print(f"  ⚠️ Skipped one email: {e}")
            continue

    print(f"✅ Fetched {len(emails)} emails.")
    return emails



def check_known_sender(email):
    sender_lower  = email['sender'].lower()
    subject_lower = email['subject'].lower()

    for keyword, category in KNOWN_SENDERS.items():
        if keyword in sender_lower or keyword in subject_lower:
            return category

    return None


def classify_with_ai(email):
    try:
        prompt = f"""You are an email classifier. Classify the following email into ONE of these categories:

Categories: {', '.join(AI_CATEGORIES)}

Email Details:
- From: {email['sender']}
- Subject: {email['subject']}
- Preview: {email['snippet']}

Reply with ONLY the category name from the list above. Nothing else. No explanation."""

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        category = response.text.strip()

        for cat in AI_CATEGORIES:
            if cat.lower() in category.lower():
                return cat

        return "Other"

    except Exception as e:
        print(f"  ⚠️ AI error: {e}")
        return "Other"



def get_or_create_label(service, label_name):
    try:
        labels_result   = service.users().labels().list(userId='me').execute()
        existing_labels = labels_result.get('labels', [])

        for label in existing_labels:
            if label['name'].lower() == label_name.lower():
                return label['id']

        label_body = {
            'name': label_name,
            'labelListVisibility': 'labelShow',
            'messageListVisibility': 'show'
        }
        created = service.users().labels().create(userId='me', body=label_body).execute()
        print(f"  📁 Created new label: {label_name}")
        return created['id']

    except Exception as e:
        print(f"  ⚠️ Label error: {e}")
        return None


def apply_label_to_email(service, email_id, label_id):
    try:
        service.users().messages().modify(
            userId='me',
            id=email_id,
            body={'addLabelIds': [label_id]}
        ).execute()
    except Exception as e:
        print(f"  ⚠️ Could not apply label: {e}")



def run_email_sorter():
    print("="*55)
    print("🤖  AI Email Sorter Agent Starting...")
    print("="*55)

    service = get_gmail_service()
    emails  = get_emails(service, max_emails=50)

    if not emails:
        print("No emails to sort. Exiting.")
        return

    print(f"\n🧠 Sorting {len(emails)} emails...\n")

    results     = {}
    ai_count    = 0
    known_count = 0

    for i, email in enumerate(emails):
        print(f"[{i+1}/{len(emails)}] {email['subject'][:55]}")
        print(f"         From: {email['sender'][:55]}")

        category = check_known_sender(email)

        if category:
            method = "⚡ Known"
            known_count += 1
        else:
            category = classify_with_ai(email)
            method = "🤖 AI"
            ai_count += 1

        label_name = f"AI-Sorted/{category}"
        label_id   = get_or_create_label(service, label_name)

        if label_id:
            apply_label_to_email(service, email['id'], label_id)
            print(f"         {method} → ✅ {category}")
        else:
            print(f"         ❌ Could not sort")

        results[category] = results.get(category, 0) + 1
        print()

    print("="*55)
    print("📊  SORTING COMPLETE! Summary:")
    print("="*55)
    for category, count in sorted(results.items(), key=lambda x: -x[1]):
        print(f"  📁  {category:<30} {count} email(s)")
    print("-"*55)
    print(f"  ⚡ Sorted by known senders : {known_count}")
    print(f"  🤖 Sorted by Gemini AI     : {ai_count}")
    print(f"  📧 Total emails sorted     : {len(emails)}")
    print("="*55)
    print("\n✅ Open Gmail → look for 'AI-Sorted' in left sidebar")
    print("   (Click 'More' in Gmail sidebar if you don't see it)\n")


if __name__ == "__main__":
    run_email_sorter()
