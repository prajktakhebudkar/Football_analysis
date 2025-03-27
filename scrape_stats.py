import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Premier League standings page
url = "https://www.premierleague.com/tables"

# Headers to mimic a browser visit
headers = {"User-Agent": "Mozilla/5.0"}

# Fetch the page content
response = requests.get(url, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Locate the standings table body
table_body = soup.find("tbody", class_="league-table_tbody")

# Initialize a list to store data
standings = []

# Loop through each row in the table
for row in table_body.find_all("tr"):
    # Extract columns in the row
    cols = row.find_all("td")
    cols = [col.text.strip() for col in cols]  # Get text and strip whitespace
    standings.append(cols)

# Convert to a DataFrame for better readability
columns = ["Position", "Team", "Played", "Won", "Drawn", "Lost", "Points"]  # Adjust based on actual data
df = pd.DataFrame(standings, columns=columns)

# Save to a CSV file
df.to_csv("premier_league_standings.csv", index=False)

print("Data saved to premier_league_standings.csv")
