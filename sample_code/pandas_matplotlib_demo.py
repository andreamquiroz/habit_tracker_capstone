import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load the CSV file
df = pd.read_csv('sample_habits.csv')

# Convert date column to datetime for better handling
df['date'] = pd.to_datetime(df['date'])

print("First few rows of our data:")
print(df.head())
print("\nData info:")
print(df.info())

# --- BASIC ANALYSIS ---

# Show completion rates for each habit
print("\n--- HABIT COMPLETION RATES ---")
completion_rates = df.groupby('habit_name')['completed'].mean()
print(completion_rates)

# --- VISUALIZATION 1: Daily Completion Count ---
# Count how many habits were completed each day
daily_completion = df[df['completed'] == True].groupby('date').size()

plt.figure(figsize=(10, 6))
plt.plot(daily_completion.index, daily_completion.values, marker='o')
plt.title('Daily Habit Completions')
plt.xlabel('Date')
plt.ylabel('Number of Habits Completed')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# --- VISUALIZATION 2: Individual Habit Progress ---
# Show progress for each habit over time
habits = df['habit_name'].unique()

plt.figure(figsize=(12, 8))
for i, habit in enumerate(habits):
    habit_data = df[df['habit_name'] == habit].copy()
    # Convert True/False to 1/0 for plotting
    habit_data['completed_num'] = habit_data['completed'].astype(int)
    
    plt.subplot(len(habits), 1, i+1)
    plt.plot(habit_data['date'], habit_data['completed_num'], 
             marker='o', label=habit, linewidth=2)
    plt.title(f'{habit.replace("_", " ").title()} Progress')
    plt.ylabel('Completed')
    plt.ylim(-0.1, 1.1)
    plt.grid(True, alpha=0.3)
    
    if i == len(habits) - 1:  # Only show x-axis labels on bottom plot
        plt.xticks(rotation=45)
    else:
        plt.xticks([])

plt.tight_layout()
plt.show()

# --- VISUALIZATION 3: Completion Rate Bar Chart ---
plt.figure(figsize=(8, 6))
habit_names = [name.replace('_', ' ').title() for name in completion_rates.index]
plt.bar(habit_names, completion_rates.values, color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Habit Completion Rates')
plt.ylabel('Completion Rate (%)')
plt.ylim(0, 1)

# Add percentage labels on bars
for i, rate in enumerate(completion_rates.values):
    plt.text(i, rate + 0.02, f'{rate:.1%}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

# --- SIMPLE FILTERING EXAMPLES ---
print("\n--- FILTERING EXAMPLES ---")

# Show only exercise data
exercise_data = df[df['habit_name'] == 'exercise']
print(f"Exercise completion rate: {exercise_data['completed'].mean():.1%}")

# Show data for a specific date
specific_date = df[df['date'] == '2024-07-15']
print(f"\nHabits on July 15th:")
print(specific_date[['habit_name', 'completed']])

# Show days when all habits were completed
daily_stats = df.groupby('date').agg({
    'completed': ['count', 'sum']
}).round(2)
daily_stats.columns = ['total_habits', 'completed_habits']
perfect_days = daily_stats[daily_stats['total_habits'] == daily_stats['completed_habits']]
print(f"\nPerfect days (all habits completed): {len(perfect_days)} days")
print(perfect_days.index.tolist())
