"""
Study Time Tracker

This program asks the user about their study time today and their weekly
study goal. It then estimates how many hours they are on track to study
this week and shows whether they are ahead of or behind their goal.
"""

# Task 1: Welcome message
print("Welcome to the Study Time Tracker!")
print("This program will estimate your weekly study hours based on today.\n")

# Task 2: Ask the user for input
daily_hours_input = input("How many hours did you study today? ")
weekly_goal_input = input("What is your weekly study goal (in hours)? ")

# Task 5: Basic error handling for non-numeric input
try:
    # Task 3: Convert input to numeric and perform calculations
    daily_hours = float(daily_hours_input)
    weekly_goal = float(weekly_goal_input)
except ValueError:
    print("\nPlease enter valid numbers (for example: 1, 1.5, or 2).")
    # Exit the program if input is invalid so it does not crash later
    exit()

# Extra: basic validation for negative or zero values
if daily_hours < 0:
    print("\nDaily study hours cannot be negative. Please run the program again.")
    exit()

if weekly_goal <= 0:
    print("\nYour weekly goal must be greater than zero. Please run the program again.")
    exit()

# Estimate weekly study hours by assuming today is a typical day
estimated_weekly_hours = daily_hours * 7

# Calculate progress toward the goal
progress_percent = (estimated_weekly_hours / weekly_goal) * 10
difference = estimated_weekly_hours - weekly_goal

# Task 4: Display clear, formatted output
print("\n===== Study Summary =====")
print(f"Based on today, you are on track to study about {estimated_weekly_hours:.1f} hours this week.")
print(f"Your weekly goal is {weekly_goal:.1f} hours.")
print(f"That means you are at about {progress_percent:.1f}% of your goal.\n")

# Give a simple interpretation of the result
if difference >= 0:
    print(f"Great job! You are ahead of your goal by about {difference:.1f} hours this week. Keep it up!")
else:
    print(f"You are currently about {-difference:.1f} hours behind your goal.")
    print("Consider adding a little extra study time on a few days to catch up.")

# Task 6: Final message and clean exit
print("\nThank you for using the Study Time Tracker!")
