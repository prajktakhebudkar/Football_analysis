import os
import urllib.request
import csv

def download_premier_league_data():
    # Create output directory
    os.makedirs('data/raw/premier-league', exist_ok=True)

    # URL for Premier League data (most recent season)
    url = 'https://www.football-data.co.uk/mmz4281/2324/E0.csv'

    # Download the file
    print(f"Downloading data from {url}...")
    urllib.request.urlretrieve(url, 'data/raw/premier-league/season-2324.csv')
    print("Download complete!")

    # Read and display some sample data
    with open('data/raw/premier-league/season-2324.csv', 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        print("\nColumn headers:")
        print(headers)
        
        print("\nFirst 3 matches:")
        for i, row in enumerate(reader):
            if i < 3:
                print(f"Match {i+1}: {row[1]} vs {row[2]}, Score: {row[3]}-{row[4]}")
            else:
                break

    print("\nData is ready for analysis!")

if __name__ == "__main__":
    download_premier_league_data()