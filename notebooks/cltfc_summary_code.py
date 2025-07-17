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


# 
# ## ⚽ Style of Play Comparison
# 
# This chart compares Charlotte FC’s average possession and PPDA to other Eastern Conference teams in 2025. 
# 
# Charlotte FC is located in the **top-left quadrant** — teams that allow the opposition to build up slowly and sit in a mid-block, rather than pressing high or holding the majority of possession.
# 
# This aligns with their:
# - High PPDA (low pressing intensity)
# - Lower than average possession
# - Conservative defensive approach with focused progression once the ball is won
# 
# ![Style of Play Chart](cltfc_style_of_play_quadrant.png)
# 

# 
# ## 🏟️ Home vs Away Goal Contributions
# 
# Charlotte FC’s 2025 MLS season reveals a clear split in performance based on venue:
# 
# | Venue | Goals Scored | Goals Conceded |
# |-------|--------------|----------------|
# | 🏠 **Home** | **17**          | **9**              |
# | 🛫 **Away** | **11**          | **18**             |
# 
# ### 🧠 Key Insights:
# - The team scores **over 50% more goals at home** and concedes **twice as few**.
# - Charlotte is **defensively stable at home**, but their shape breaks down on the road.
# - **Away matches are particularly vulnerable** to late-game goals, aligning with a tactical model that defends deep but fatigues late.
# - These splits reinforce the narrative of Charlotte being **a playoff-caliber home team** — but in need of better game management and rotation away from home.
# 

# 
# ![Home vs Away Goals](visuals/cltfc_home_away_goals_clean.png)
# 

# 
# ## 🏥 Injury and Availability Impacts
# 
# Charlotte FC’s midseason performance was influenced heavily by player availability, particularly in May 2025.
# 
# Three key players missed matches during a crucial stretch:
# - 🔴 **Nathan Byrne** (RB): Absent from May 4 onward due to neck surgery — disrupted the right-sided defensive balance and 2-3-5 build-up structure.
# - 🟠 **Souleyman Doumbia** (LB): Missed May 11–18 — limited left channel width and overlapping support.
# - 🟣 **Kristijan Kahlina** (GK): Missed two matches (May 15 & 25) for personal reasons — forced goalkeeper rotation.
# 
# The 5-game rolling PPG chart below shows a noticeable performance dip overlapping with these absences.
# 
# ![5-Game Rolling PPG with Absences](visuals/cltfc_rolling_ppg_with_absences.png)
# 
# These disruptions impacted Charlotte’s ability to maintain tactical structure and likely contributed to away match vulnerabilities and late-game concessions.
# 