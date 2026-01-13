import gspread
from google.oauth2.service_account import Credentials
from collections import Counter

# Use the downloaded key file
SERVICE_ACCOUNT_FILE = #add file name

# Use the Google Sheet URL
SHEET_URL = #Add Google Sheet URL

# Identify the sheet tab to read
WORKSHEET_NAME = "Sheet1"

SCOPES = [
    #readonly 
]

def get_Name():
    creds = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )

    client = gspread.authorize(creds)
    spreadsheet = client.open_by_url(SHEET_URL)
    ws = spreadsheet.worksheet(WORKSHEET_NAME)

    rows = ws.get_all_values()
    if not rows:
        raise RuntimeError("No data was found in the sheet.")

    header = rows[0]
    data_rows = rows[1:]

    if "Name" not in header:
        raise RuntimeError("Column 'Name' was not found in the header row.")

    idx = header.index("Name")

    prefs = []
    for r in data_rows:
        if len(r) > idx:
            val = r[idx].strip()
            if val:
                prefs.append(val)

    counts = Counter(prefs)

    print("Name values")
    for p in prefs:
        print(p)

    print("\nName counts")
    for k, v in counts.most_common():
        print(f"{k}: {v}")

    return prefs, counts


# function call
get_Name()
   
