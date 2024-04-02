# Zoom Recording Data Analytics Script Documentation

## Overview
This script is specifically designed for analyzing Zoom recording data. It processes the data from a CSV file, focusing on user view durations, and computes various statistics like the most engaged viewer, total and average view durations.

## Functionality
The script executes the following tasks:
1. Imports Zoom recording data from a CSV file named `data.csv`.
2. Converts the 'View Duration (minutes)' field to numeric, treating errors as NaN (Not a Number).
3. Replaces NaN values in 'View Duration (minutes)' with 0.
4. Aggregates view durations for each user.
5. Identifies and prints the user with the highest view duration.
6. Displays a sorted list of users by their view duration.
7. Calculates the total view duration for all users and displays it.
8. Computes and displays the average view duration per user.

## Prerequisites
- Python environment.
- Pandas library.

To install Pandas, use: `pip install pandas`

## How to Use
1. Ensure the CSV file containing Zoom recording data is named `data.csv` and placed in the same directory as the script.
2. Run the script in your Python environment.

## Output Details
The script provides:
- The most engaged user based on view duration in minutes.
- A ranked list of users by view duration.
- Total view duration across all users.
- Average view duration per user.

## CSV Data File Requirements
The `data.csv` file should include at least these columns:
- `User Name`
- `View Duration (minutes)`

The script expects this specific format for accurate analysis of Zoom recording data.
