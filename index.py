import re
from datetime import datetime
from dateutil import parser
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google():
    """Authenticate with Google Calendar API."""
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
    creds = flow.run_local_server(port=0)
    return build('calendar', 'v3', credentials=creds)

def create_event(service, title, start_time, end_time):
    """Create a calendar event."""
    event = {
        'summary': title,
        'start': {'dateTime': start_time.isoformat(), 'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': end_time.isoformat(), 'timeZone': 'Asia/Kolkata'},
    }
    try:
        service.events().insert(calendarId='primary', body=event).execute()
        print(f"Created: {title} ({start_time.strftime('%I:%M %p')}-{end_time.strftime('%I:%M %p')})")
    except HttpError as e:
        print(f"Error creating event: {str(e)}")

def parse_schedule(input_text):
    """Directly parse the schedule input without LLM."""
    # Extract the date if specified, otherwise default to today
    date_match = re.search(r'(\d{1,2})\s*th\s*(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)\w*', input_text.lower())
    if date_match:
        day = date_match.group(1)
        month = date_match.group(2)
        year = datetime.now().year
        date_str = f"{year}-{month[:3].title()}-{day.zfill(2)}"
    else:
        date_str = datetime.now().strftime('%Y-%m-%d')

    # Find all time blocks
    time_blocks = re.findall(r'(\d{1,2}:\d{2}\s*[AP]M)\s*[–-]\s*(\d{1,2}:\d{2}\s*[AP]M):\s*(.*?)(?=\s*\d{1,2}:\d{2}\s*[AP]M|$)', input_text)
    
    events = []
    for start, end, title in time_blocks:
        try:
            start_time = parser.parse(f"{date_str} {start.strip()}")
            end_time = parser.parse(f"{date_str} {end.strip()}")
            events.append({
                'title': title.strip(),
                'start': start_time,
                'end': end_time
            })
        except parser.ParserError:
            print(f"Could not parse time range: {start} - {end}")
    
    return events

def main():
    print("Calendar Scheduling Tool (Direct Parser Version)")
    service = authenticate_google()

    while True:
        try:
            user_input = input("\nEnter schedule (or 'exit'):\n> ").strip()
            if user_input.lower() in ('exit', 'quit'):
                break

            events = parse_schedule(user_input)
            
            if events:
                for event in events:
                    create_event(service, event['title'], event['start'], event['end'])
            else:
                print("No valid events found in input. Please use format:")
                print("2:00 PM - 4:00 PM: Event Name  4:00 PM - 5:00 PM: Next Event")

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()