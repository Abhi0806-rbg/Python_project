import json
from collections import defaultdict
import pandas as pd

# Load JSON data
with open('players.json', 'r') as file:
    players = json.load(file)

# Convert to DataFrame for easier analysis
df = pd.DataFrame(players)

# Convert price to numeric if it's in string
df['price'] = pd.to_numeric(df['price'], errors='coerce')

print("\n 1. Basic Dataset Statistics ")
print("Total players:", len(df))
print("Average price:", df['price'].mean())
print("Dataset Info:\n", df.info())
print("Sample Data:\n", df.head())

# ------------------------------
print("\n 2. Team Analysis ")
players_per_team = df['team'].value_counts()
print("Players in each team:\n", players_per_team)

most_players_team = players_per_team.idxmax()
print("Team with most players:", most_players_team)

team_values = df.groupby('team')['price'].sum().sort_values(ascending=False)
print("Total team values:\n", team_values)

most_expensive_team = team_values.idxmax()
print("Most expensive team:", most_expensive_team)

# ------------------------------
print("\n 3. Role Analysis ")
players_per_role = df['role'].value_counts()
print("Players per role:\n", players_per_role)

most_common_role = players_per_role.idxmax()
print("Most common role:", most_common_role)

avg_price_per_role = df.groupby('role')['price'].mean().sort_values(ascending=False)
print("Average price per role:\n", avg_price_per_role)

most_expensive_role = avg_price_per_role.idxmax()
print("Most expensive role (avg):", most_expensive_role)

# ------------------------------
print("\n 4. Country Analysis ")
players_per_country = df['country'].value_counts()
print("Players per country:\n", players_per_country)

most_players_country = players_per_country.idxmax()
print("Country with most players:", most_players_country)

avg_price_per_country = df.groupby('country')['price'].mean().sort_values(ascending=False)
print("Average price per country:\n", avg_price_per_country)

most_expensive_per_country = df.loc[df.groupby('country')['price'].idxmax()]
print("Most expensive player from each country:\n", most_expensive_per_country[['country', 'name', 'price']])

# ------------------------------
print("\n 5. Advanced Analysis ")
print("Top 5 most expensive players:\n", df.nlargest(5, 'price')[['name', 'team', 'price']])

print("\nTop 5 expensive players per role:")
for role, group in df.groupby('role'):
    print(f"\nRole: {role}")
    print(group.nlargest(5, 'price')[['name', 'price', 'team']])

print("\nTop 5 expensive players per team:")
for team, group in df.groupby('team'):
    print(f"\nTeam: {team}")
    print(group.nlargest(5, 'price')[['name', 'price', 'role']])

print("\nTop 5 expensive players per country:")
for country, group in df.groupby('country'):
    print(f"\nCountry: {country}")
    print(group.nlargest(5, 'price')[['name', 'price', 'team']])
