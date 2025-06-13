import json
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt

# Load JSON data
with open('players.json', 'r') as file:
    players = json.load(file)

# Convert to DataFrame for easier analysis
df = pd.DataFrame(players)

# Convert price to numeric if it's in string
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# 1. Basic Dataset Statistics
print("\n 1. Basic Dataset Statistics ")
print("Total players:", len(df))
print("Average price:", df['price'].mean())
print("Dataset Info:\n", df.info())
print("Sample Data:\n", df.head())

# ----------------------------------
# 2. Team Analysis
print("\n 2. Team Analysis ")
players_per_team = df['team'].value_counts()
print("Players in each team:\n", players_per_team)

# Bar chart: Players per team
players_per_team.plot(kind='bar', title='Players per Team', color='skyblue')
plt.xlabel('Team')
plt.ylabel('Number of Players')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("players_per_team.png")  # Save as image
plt.show()


most_players_team = players_per_team.idxmax()
print("Team with most players:", most_players_team)

team_values = df.groupby('team')['price'].sum().sort_values(ascending=False)
print("Total team values:\n", team_values)

team_values.plot(kind='bar', title='Total Team Value (in Crores)', color='green')
plt.xlabel('Team')
plt.ylabel('Total Price')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("team_values.png")
plt.show()


# ----------------------------------
# 3. Role Analysis
print("\n 3. Role Analysis ")
players_per_role = df['role'].value_counts()
print("Players per role:\n", players_per_role)

players_per_role.plot(kind='pie', autopct='%1.1f%%', startangle=140, title='Distribution of Roles')
plt.ylabel('')
plt.tight_layout()
plt.savefig("role_distribution.png")
plt.show()


most_common_role = players_per_role.idxmax()
print("Most common role:", most_common_role)

avg_price_per_role = df.groupby('role')['price'].mean().sort_values(ascending=False)
print("Average price per role:\n", avg_price_per_role)

avg_price_per_role.plot(kind='bar', color='orange', title='Average Price per Role')
plt.xlabel('Role')
plt.ylabel('Average Price')
plt.tight_layout()
plt.savefig("avg_price_per_role.png")
plt.show()


# ----------------------------------
# 4. Country Analysis
print("\n 4. Country Analysis ")
players_per_country = df['country'].value_counts()
print("Players per country:\n", players_per_country)

players_per_country.plot(kind='bar', title='Players per Country', color='purple')
plt.xlabel('Country')
plt.ylabel('Number of Players')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("players_per_country.png")
plt.show()


most_players_country = players_per_country.idxmax()
print("Country with most players:", most_players_country)

avg_price_per_country = df.groupby('country')['price'].mean().sort_values(ascending=False)
print("Average price per country:\n", avg_price_per_country)

avg_price_per_country.plot(kind='bar', title='Average Price per Country', color='red')
plt.xlabel('Country')
plt.ylabel('Average Price')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("avg_price_per_country.png")
plt.show()


most_expensive_per_country = df.loc[df.groupby('country')['price'].idxmax()]
print("Most expensive player from each country:\n", most_expensive_per_country[['country', 'name', 'price']])

# ----------------------------------
# 5. Advanced Analysis
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
