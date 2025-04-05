# Football_analysis
Analyzing Premier League stats for match prediction and dashboards


# Football Analytics Project

A data analysis project that collects, processes, and visualizes football (soccer) statistics from major European leagues.

## Features

- Data collection from football-data.co.uk
- Premier League statistical analysis
- League table generation
- Goal scoring visualization
- Home advantage analysis

## Getting Started

### Prerequisites

- Python 3.8+
- Git

### Installation

1. Clone the repository
   ```
   git clone https://github.com/your-username/football-analytics.git
   cd football-analytics
   ```

2. Set up a virtual environment
   ```
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

### Usage

1. Download Premier League data
   ```
   python src/data_collection/simple_downloader.py
   ```

2. Run analysis and generate visualizations
   ```
   python src/analysis/premier_league_analysis.py
   ```

3. Check the output in the `data/analysis` directory

## Project Structure

```
football-analytics/
├── data/
│   ├── raw/              # Raw downloaded data
│   └── analysis/         # Analysis results and visualizations
├── src/
│   ├── data_collection/  # Data collection scripts
│   └── analysis/         # Data analysis scripts
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Future Plans

- Add support for more leagues
- Create interactive visualizations
- Implement prediction models
- Develop a web interface

## License

This project is licensed under the MIT License - see the LICENSE file for details.
