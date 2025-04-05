import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def analyze_premier_league():
    # Load the data
    data_path = 'data/raw/premier-league/season-2324.csv'
    if not os.path.exists(data_path):
        print(f"Error: Data file not found at {data_path}")
        print("Please run the downloader script first.")
        return
    
    # Create output directory
    os.makedirs('data/analysis', exist_ok=True)
    
    # Read the data
    df = pd.read_csv(data_path)
    print(f"Loaded {len(df)} matches from the Premier League dataset")
    
    # Basic data exploration
    print("\nBasic information about the dataset:")
    print(f"Number of teams: {len(set(df['HomeTeam'].unique()) | set(df['AwayTeam'].unique()))}")
    print(f"Date range: {df['Date'].min()} to {df['Date'].max()}")
    
    # 1. Create a league table
    print("\nGenerating league table...")
    teams = set(df['HomeTeam'].unique()) | set(df['AwayTeam'].unique())
    table_data = []
    
    for team in teams:
        # Home games
        home_games = df[df['HomeTeam'] == team]
        home_points = (home_games['FTR'] == 'H').sum() * 3 + (home_games['FTR'] == 'D').sum()
        home_wins = (home_games['FTR'] == 'H').sum()
        home_draws = (home_games['FTR'] == 'D').sum()
        home_losses = (home_games['FTR'] == 'A').sum()
        home_goals_for = home_games['FTHG'].sum()
        home_goals_against = home_games['FTAG'].sum()
        
        # Away games
        away_games = df[df['AwayTeam'] == team]
        away_points = (away_games['FTR'] == 'A').sum() * 3 + (away_games['FTR'] == 'D').sum()
        away_wins = (away_games['FTR'] == 'A').sum()
        away_draws = (away_games['FTR'] == 'D').sum()
        away_losses = (away_games['FTR'] == 'H').sum()
        away_goals_for = away_games['FTAG'].sum()
        away_goals_against = away_games['FTHG'].sum()
        
        # Total
        games_played = len(home_games) + len(away_games)
        points = home_points + away_points
        wins = home_wins + away_wins
        draws = home_draws + away_draws
        losses = home_losses + away_losses
        goals_for = home_goals_for + away_goals_for
        goals_against = home_goals_against + away_goals_against
        goal_difference = goals_for - goals_against
        
        table_data.append({
            'Team': team,
            'MP': games_played,
            'W': wins,
            'D': draws,
            'L': losses,
            'GF': goals_for,
            'GA': goals_against,
            'GD': goal_difference,
            'Pts': points
        })
    
    # Create the league table
    table = pd.DataFrame(table_data)
    table = table.sort_values(by=['Pts', 'GD', 'GF'], ascending=False).reset_index(drop=True)
    table.index = table.index + 1  # Start index from 1
    
    # Save the table
    table.to_csv('data/analysis/premier_league_table.csv', index_label='Position')
    print(table)
    
    # 2. Goal analysis
    print("\nAnalyzing goal patterns...")
    
    # Average goals per match
    total_goals = df['FTHG'].sum() + df['FTAG'].sum()
    avg_goals = total_goals / len(df)
    print(f"Average goals per match: {avg_goals:.2f}")
    
    # Home vs Away goals
    home_goals = df['FTHG'].sum()
    away_goals = df['FTAG'].sum()
    print(f"Home goals: {home_goals} ({home_goals/total_goals*100:.1f}%)")
    print(f"Away goals: {away_goals} ({away_goals/total_goals*100:.1f}%)")
    
    # Create a bar chart of goals scored by teams
    plt.figure(figsize=(12, 8))
    
    # Get goals scored by each team
    goals_by_team = {}
    for team in teams:
        home_goals = df[df['HomeTeam'] == team]['FTHG'].sum()
        away_goals = df[df['AwayTeam'] == team]['FTAG'].sum()
        goals_by_team[team] = home_goals + away_goals
    
    # Sort teams by goals scored
    sorted_teams = sorted(goals_by_team.items(), key=lambda x: x[1], reverse=True)
    teams_list = [team for team, _ in sorted_teams]
    goals_list = [goals for _, goals in sorted_teams]
    
    # Create the bar chart
    plt.bar(teams_list, goals_list, color='steelblue')
    plt.title('Total Goals Scored by Team')
    plt.xlabel('Team')
    plt.ylabel('Goals')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('data/analysis/goals_by_team.png')
    
    # 3. Home advantage analysis
    home_wins = (df['FTR'] == 'H').sum()
    away_wins = (df['FTR'] == 'A').sum()
    draws = (df['FTR'] == 'D').sum()
    
    # Create a pie chart
    plt.figure(figsize=(10, 7))
    labels = ['Home Wins', 'Away Wins', 'Draws']
    sizes = [home_wins, away_wins, draws]
    colors = ['#ff9999', '#66b3ff', '#99ff99']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('Match Outcomes')
    plt.tight_layout()
    plt.savefig('data/analysis/match_outcomes.png')
    
    print("\nAnalysis complete! Check the 'data/analysis' directory for results.")

if __name__ == "__main__":
    analyze_premier_league()