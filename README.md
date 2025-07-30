# habit_health_tracker
Track and analyze daily health habits over time for personal routine monitoring.

# Habit Health Tracker

A lightweight project that logs, tracks, and analyzes daily health habits over time.  
Originally developed as a final assignment for a Python programming course,  
this project was later extended for portfolio purposes to explore personalized routine analysis and wellness monitoring.

---

## Project Overview

This project tracks daily lifestyle habits across five categories—exercise, study, health management, self-care, and diet—  
allowing users to visualize routine consistency and personal trends over time.

Through time series visualization and basic modeling, the project explores how habit data can reflect changes in well-being and health stability.  
It serves as a prototype for habit-based health monitoring tools, especially in preventive healthcare or digital wellness contexts.

---

## Features

- Daily CSV logging for five custom habit types  
- Automated date-stamped entries via Python CLI  
- Weekly and cumulative trend analysis using Jupyter Notebook  
- Optional regression-based prediction of self-assessed wellness score  
- Clean project structure for easy modification or expansion  

---

## Sample Visualizations

- Weekly habit frequency line charts  
- Heatmap of daily habit intensity  
- Rolling average for key categories  
- (Optional) Predicted vs actual wellness scatter plot  

---

## Project Structure

```
habit_health_tracker/
├── data/
│   └── daily_habits.csv                # Daily habit log file
├── notebooks/
│   └── habit_analysis.ipynb            # Main notebook for data visualization and modeling
├── visualizations/
│   ├── trends.png                      # Weekly trend plots
│   └── prediction.png                  # Regression result visualization
├── daily_habit_tracker.py             # CLI script for logging habits
└── README.md
```
