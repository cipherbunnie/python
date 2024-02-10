# Author: Vam
# Date: 14/01/2024

'''
In this chapter's source code folder (available on the Computer Science Portal
at www.pearsonhighered.com/gaddis), you will find a text file named
WorldSeriesWinners. txt. This file contains a chronological list of the
World Series' winning teams from 1903 through 2009. The first line in the file is
the name of the team that won in 1903, and the last line is the name of the team
that won in 2009. (Note the World Series was not played in 1904 or 1994. There
are entries in the file indicating this.)

Write a program that reads this file and creates a dictionary in which the keys
are the names of the teams, and each key's associated value is the number of
times the team has won the World Series. The program should also create a
dictionary in which the keys are the years, and each key's associated value is
the name of the team that won that year.

The program should prompt the user for a year in the range of 1903 through
2009. It should then display the name of the team that won the World Series
that year, and the number of times that team has won the World Series.
'''

def read_world_series_data(filename):
    teams_wins = {}
    years_winners = {}

    with open(filename, 'r') as file:
        for line in file:
            year, team = line.strip().split(',')
            teams_wins[team] = teams_wins.get(team, 0) + 1
            years_winners[int(year)] = team

    return teams_wins, years_winners

def main():
    # Specify the filename
    filename = 'WorldSeriesWinners.txt'

    # Read data from the file
    teams_wins, years_winners = read_world_series_data(filename)

    # Prompt user for a year
    year = int(input("Enter a year between 1903 and 2009: "))

    # Display results
    if year in years_winners:
        winning_team = years_winners[year]
        wins_count = teams_wins[winning_team]
        print(f"In {year}, the {winning_team} won the World Series. Total wins: {wins_count}.")
    else:
        print(f"No data available for the year {year}.")

if __name__ == "__main__":
    main()
