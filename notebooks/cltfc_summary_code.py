"""
cltfc_summary_final_with_injuries.py

Midseason analysis of Charlotte FC using WyScout data provided by the Charlotte FC Analytics Team.
This script includes data loading, cleaning, and key performance breakdowns. Visualizations are omitted here but available in the README.
The raw data is proprietary and cannot be publicly shared.
"""


#!/usr/bin/env python
# coding: utf-8

# # Charlotte FC 2025 Midseason Summary
# This notebook presents a visual summary of Charlotte FC's 2025 season performance at the halfway point, based on match results and injury data.



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns




home_away_df = pd.DataFrame({
    'Wins': [6, 2],
    'Draws': [0, 1],
    'Losses': [2, 7],
    'Points': [18, 7],
    'Goals Scored': [18, 11],
    'Goals Conceded': [9, 20]
}, index=['Home', 'Away'])

home_away_df




home_away_df[['Points', 'Goals Scored', 'Goals Conceded']].plot(kind='bar', figsize=(10, 6))
plt.title('Charlotte FC - Home vs Away Performance (2025 Midseason)')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()




labels = ['0–60 min', '61–90+ min']
values = [16, 13]

plt.figure(figsize=(6, 6))
plt.pie(values, labels=labels, autopct='%1.1f%%', colors=['#66b3ff', '#ff9999'], startangle=140)
plt.title('Timing of Goals Conceded (2025)')
plt.show()




injury_data = pd.DataFrame({
    'Player': ['Nathan Byrne', 'Souleyman Doumbia', 'Kristijan Kahlina'],
    'Minutes Missed': [665, 285, 190]
})

plt.figure(figsize=(8, 5))
sns.barplot(data=injury_data, x='Player', y='Minutes Missed', palette='Blues_d')
plt.title('Minutes Missed Due to Injury')
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()


