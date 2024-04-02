import pandas as pd

path = "data.csv"  

data = pd.read_csv(path)

data['View Duration (minutes)'] = pd.to_numeric(data['View Duration (minutes)'], errors='coerce')

data['View Duration (minutes)'].fillna(0, inplace=True)

user_view_durations = data.groupby('User Name')['View Duration (minutes)'].sum()

most_viewed_user = user_view_durations.idxmax()
most_viewed_duration = user_view_durations.max()

print(f"Most viewed user: {most_viewed_user} with {most_viewed_duration} minutes")
print("Top users by view duration:" )
print(user_view_durations.sort_values(ascending=False).reset_index())

total_view_duration = user_view_durations.sum()

print(f"Total view duration: {total_view_duration} minutes")

average_view_duration = user_view_durations.mean()
print(f"Average view duration: {average_view_duration} minutes")