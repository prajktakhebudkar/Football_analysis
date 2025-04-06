import os
import urllib.request
import csv
from datetime import datetime
import time

def download_all_league_data():
    # Create base output directory
    os.makedirs('data/raw', exist_ok=True)
    
    # League data sources with their codes on football-data.co.uk
    leagues = {
        'premier-league': {
            'code': 'E0',
            'name': 'Premier League',
            'start_season': '9394'  # Premier League data goes back to 1993/94
        },
        'la-liga': {
            'code': 'SP1',
            'name': 'La Liga',
            'start_season': '9394'  # La Liga data goes back to 1993/94
        },
        'bundesliga': {
            'code': 'D1',
            'name': 'Bundesliga',
            'start_season': '9394'  # Bundesliga data goes back to 1993/94
        }
    }
    
    # Generate all season codes from 1993/94 to current
    current_year = datetime.now().year
    current_month = datetime.now().month
    
    # Determine the latest complete season
    # If we're before August, the latest complete season ended in the previous year
    if current_month < 8:
        latest_season_end = current_year - 1
    else:
        latest_season_end = current_year
    
    # Generate all seasons from start to latest
    all_seasons = []
    for year in range(1993, latest_season_end):
        # Format: 9394, 9495, ..., 2223, 2324
        season_code = f"{str(year)[-2:]}{str(year+1)[-2:]}"
        all_seasons.append(season_code)
    
    # URL pattern: https://www.football-data.co.uk/mmz4281/[season]/[league_code].csv
    base_url = "https://www.football-data.co.uk/mmz4281"
    
    # Process each league
    for league_key, league_info in leagues.items():
        print(f"\nProcessing {league_info['name']} historical data...")
        
        # Create league-specific directory
        league_dir = f'data/raw/{league_key}'
        os.makedirs(league_dir, exist_ok=True)
        
        # Process each season
        start_season_idx = all_seasons.index(league_info['start_season']) if league_info['start_season'] in all_seasons else 0
        league_seasons = all_seasons[start_season_idx:]
        
        for season in league_seasons:
            # File naming: 9394 = season-1993-1994.csv
            year1 = int("19" + season[:2]) if int(season[:2]) >= 93 else int("20" + season[:2])
            year2 = int("19" + season[2:]) if int(season[2:]) >= 93 else int("20" + season[2:])
            friendly_season = f"season-{year1}-{year2}.csv"
            
            output_file = f'{league_dir}/{friendly_season}'
            url = f"{base_url}/{season}/{league_info['code']}.csv"
            
            try:
                print(f"Downloading {league_info['name']} {year1}-{year2} season from {url}...")
                urllib.request.urlretrieve(url, output_file)
                print(f"? Download complete!")
                
                # Read and validate the file - just check if it has content
                with open(output_file, 'r') as f:
                    try:
                        reader = csv.reader(f)
                        headers = next(reader)
                        first_row = next(reader, None)
                        
                        if first_row:
                            print(f"  Verified: File contains valid data.")
                        else:
                            print(f"  Warning: File may be empty or contain only headers.")
                    except Exception as e:
                        print(f"  Warning: Could not validate file content: {e}")
                
                # Be nice to the server - add a small delay between downloads
                time.sleep(1)
                
            except Exception as e:
                print(f"? Failed to download {url}: {e}")
                # If the file was created but is invalid, clean it up
                if os.path.exists(output_file):
                    os.remove(output_file)
                    print(f"  Removed invalid file: {output_file}")
    
    print("\nAll historical league data download complete!")
    print("Note: Some seasons might not be available due to website limitations or changes in league structure.")
    
    # Report on downloaded files
    print("\nSummary of downloaded data:")
    for league_key, league_info in leagues.items():
        league_dir = f'data/raw/{league_key}'
        files = os.listdir(league_dir) if os.path.exists(league_dir) else []
        print(f"{league_info['name']}: {len(files)} seasons downloaded")

if __name__ == "__main__":
    download_all_league_data()