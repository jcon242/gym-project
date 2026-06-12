# Gym Tracker
 
[Gym Progress Dashboard](https://datastudio.google.com/reporting/abfca12b-a4d4-4b29-a66b-70cd20ff788e) to analyse personal lifting metrics from the HEVY workout app.
 
## Purpose
 
HEVY is a workout tracking app I've been using to log exercises, sets, and reps in the gym.
Whilst the app has been useful, it does have some downsides:

- Progress data is buried behind multiple menus on mobile
- Detailed stats are locked behind a paywall
- Metrics cannot be viewed on desktop

This makes it very difficult to see the bigger picture of my progress. 
So I built a data pipeline and Google Data Studio dashboard to fix that.
 
## Stack
 
- **Python / Jupyter Notebook** - Data cleaning and transformation
- **Supabase (PostgreSQL)** - cloud database for storing workout data
- **SQL** - Querying and structuring workout data
- **Google Data Studio** - Dashboard for visualising lifting metrics

## Data Pipeline
 
```
Hevy app (CSV export) → Jupyter Notebook (clean & transform) → Supabase PostgreSQL → Google Data Studio
```

*Data is sourced from a personal Hevy CSV export, uploaded manually. 
In subsequent updates I plan to integrate the Hevy API and automate the pipeline using a scheduling tool.*
 
## Database Schema
 
<img width="749" height="533" alt="Screenshot 2026-06-12 162615" src="https://github.com/user-attachments/assets/10c037e4-b4da-4b8f-92ee-8e879a72b684" />

## Metrics Tracked
 
- Heaviest weight [per exercise]
- Total volume [per exercise] (weight × reps, summed across sets)
- One rep max (1RM) [per exercise] - Predicted maximum weight you could lift for a single rep, calculated using the Brzycki formula

## Pages
 
1. **Main** - Key lifts only (Incline Bench Press, Bent Over Row, Squat) with KPIs attached to each
2. **Push** - Chest, shoulders, triceps
3. **Pull** - Back, biceps
4. **Legs** - Quads, hamstrings, calves, glutes

## Setup
 
The dashboard is publicly viewable here: [Gym Progress Dashboard](https://datastudio.google.com/reporting/abfca12b-a4d4-4b29-a66b-70cd20ff788e)
 
Version 1 is completed. Subsequent versions are aimed at including more metrics + new variables (calorie tracker, macros tracker etc.)
