# Football Analysis Project

This repository contains tools for downloading and analyzing football (soccer) data from major European leagues including the English Premier League, Spanish La Liga, and German Bundesliga.

## Overview

The project provides:
- A comprehensive downloader to fetch historical match data from football-data.co.uk
- Analysis scripts to generate league tables, visualize team performance, and analyze match statistics
- Organized data storage for multiple leagues and seasons

## Getting Started

### Prerequisites
- Python 3.6+
- Required packages: pandas, matplotlib, numpy

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/football_analysis.git
cd football_analysis
```

2. Create and activate a virtual environment (optional but recommended)
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install required packages
```bash
pip install pandas matplotlib numpy
```

### Usage

1. Download data for all available seasons
```bash
python threeleague_downloader.py
```

2. Run analysis on the data if you like
```bash
python football_data_collector.py
```

## Data Dictionary

The CSV files contain match data with the following columns:

### Main Match Information
| Abbreviation | Full Name | Description |
|--------------|-----------|-------------|
| Div | Division | League division (E0 = Premier League, SP1 = La Liga, D1 = Bundesliga) |
| Date | Match Date | Date of the match |
| Time | Kick-off Time | Time of kick-off |
| HomeTeam | Home Team | Name of the home team |
| AwayTeam | Away Team | Name of the away team |
| FTHG | Full Time Home Goals | Number of goals scored by home team by full time |
| FTAG | Full Time Away Goals | Number of goals scored by away team by full time |
| FTR | Full Time Result | Result of the match (H=Home win, D=Draw, A=Away win) |

### Half-Time Statistics
| Abbreviation | Full Name | Description |
|--------------|-----------|-------------|
| HTHG | Half Time Home Goals | Number of goals scored by home team by half time |
| HTAG | Half Time Away Goals | Number of goals scored by away team by half time |
| HTR | Half Time Result | Result at half time (H=Home lead, D=Draw, A=Away lead) |

### Match Statistics
| Abbreviation | Full Name | Description |
|--------------|-----------|-------------|
| HS | Home Team Shots | Number of shots by home team |
| AS | Away Team Shots | Number of shots by away team |
| HST | Home Team Shots on Target | Number of shots on target by home team |
| AST | Away Team Shots on Target | Number of shots on target by away team |
| HF | Home Team Fouls | Number of fouls committed by home team |
| AF | Away Team Fouls | Number of fouls committed by away team |
| HC | Home Team Corners | Number of corners taken by home team |
| AC | Away Team Corners | Number of corners taken by away team |
| HY | Home Team Yellow Cards | Number of yellow cards received by home team |
| AY | Away Team Yellow Cards | Number of yellow cards received by away team |
| HR | Home Team Red Cards | Number of red cards received by home team |
| AR | Away Team Red Cards | Number of red cards received by away team |

### Betting Odds
| Abbreviation | Full Name | Description |
|--------------|-----------|-------------|
| B365H | Bet365 Home Win Odds | Bet365 odds for a home team win |
| B365D | Bet365 Draw Odds | Bet365 odds for a draw |
| B365A | Bet365 Away Win Odds | Bet365 odds for an away team win |
| BWH | Bet&Win Home Win Odds | Bet&Win odds for a home team win |
| BWD | Bet&Win Draw Odds | Bet&Win odds for a draw |
| BWA | Bet&Win Away Win Odds | Bet&Win odds for an away team win |
| IWH | Interwetten Home Win Odds | Interwetten odds for a home team win |
| IWD | Interwetten Draw Odds | Interwetten odds for a draw |
| IWA | Interwetten Away Win Odds | Interwetten odds for an away team win |
| PSH | Pinnacle Home Win Odds | Pinnacle odds for a home team win |
| PSD | Pinnacle Draw Odds | Pinnacle odds for a draw |
| PSA | Pinnacle Away Win Odds | Pinnacle odds for an away team win |
| WHH | William Hill Home Win Odds | William Hill odds for a home team win |
| WHD | William Hill Draw Odds | William Hill odds for a draw |
| WHA | William Hill Away Win Odds | William Hill odds for an away team win |
| VCH | VC Bet Home Win Odds | VC Bet odds for a home team win |
| VCD | VC Bet Draw Odds | VC Bet odds for a draw |
| VCA | VC Bet Away Win Odds | VC Bet odds for an away team win |

### Additional Statistics (may not be present in all files)
| Abbreviation | Full Name | Description |
|--------------|-----------|-------------|
| Attendance | Match Attendance | Number of spectators at the match |
| Referee | Match Referee | Name of the match referee |
| HHW | Home Team Hits Woodwork | Number of times home team hit the woodwork |
| AHW | Away Team Hits Woodwork | Number of times away team hit the woodwork |
| HO | Home Team Offsides | Number of offsides by home team |
| AO | Away Team Offsides | Number of offsides by away team |
| HBP | Home Team Bookings Points | Booking points for home team (10 = yellow, 25 = red) |
| ABP | Away Team Bookings Points | Booking points for away team (10 = yellow, 25 = red) |
| XG | Expected Goals | Expected goals based on quality of chances |
| xGH | Home Team Expected Goals | Expected goals for home team |
| xGA | Away Team Expected Goals | Expected goals for away team |
| ptsH | Home Team Points | Points gained by home team (3 for win, 1 for draw) |
| ptsA | Away Team Points | Points gained by away team (3 for win, 1 for draw) |

## Notes
- Not all columns are available for all seasons or all leagues
- The format and available statistics have evolved over time, with more recent seasons typically having more detailed statistics
- Some betting odds may be missing for older seasons

## Data Source
All data is sourced from [football-data.co.uk](https://www.football-data.co.uk/), which provides free football data and betting odds data.

## License
This project is available under the MIT License.