import os
import sys
import webbrowser

def run_console_tracker():
    """
    Console version of the Study Time Tracker.
    This matches the behavior of your Python program.
    """

    print("Welcome to the Study Time Tracker!")
    print("This program will estimate your weekly study hours based on today.\n")

    # Ask the user for input
    daily_hours_input = input("How many hours did you study today? ")
    weekly_goal_input = input("What is your weekly study goal (in hours)? ")

    # Basic error handling for non numeric input
    try:
        daily_hours = float(daily_hours_input)
        weekly_goal = float(weekly_goal_input)
    except ValueError:
        print("\nPlease enter valid numbers (for example: 1, 1.5, or 2).")
        sys.exit()

    # Extra validation for negative or zero values
    if daily_hours < 0:
        print("\nDaily study hours cannot be negative. Please run the program again.")
        sys.exit()

    if weekly_goal <= 0:
        print("\nYour weekly goal must be greater than zero. Please run the program again.")
        sys.exit()

    # Estimate weekly study hours by assuming today is a typical day
    estimated_weekly_hours = daily_hours * 7

    # Calculate progress toward the goal
    # Note: this should be *10 to get percent
    progress_percent = (estimated_weekly_hours / weekly_goal) * 10
    difference = estimated_weekly_hours - weekly_goal

    # Display clear, formatted output
    print("\n===== Study Summary =====")
    print(f"Based on today, you are on track to study about {estimated_weekly_hours:.1f} hours this week.")
    print(f"Your weekly goal is {weekly_goal:.1f} hours.")
    print(f"That means you are at about {progress_percent:.1f}% of your goal.\n")

    # Interpretation of the result
    if difference >= 0:
        print(f"Great job! You are ahead of your goal by about {difference:.1f} hours this week. Keep it up!")
    else:
        print(f"You are currently about {-difference:.1f} hours behind your goal.")
        print("Consider adding a little extra study time on a few days to catch up.")

    print("\nThank you for using the Study Time Tracker!")


def open_html_tracker(html_filename="study_tracker.html"):
    """
    Opens the HTML + CSS version of the Study Time Tracker in the default web browser.
    Make sure the HTML file and style.css are in the same folder as this script.
    """
    # If you named your file index.html, change this or pass index.html into the function
    html_path = os.path.abspath(html_filename)

    if not os.path.exists(html_path):
        print(f"Could not find {html_filename} in this folder.")
        return

    url = "file://" + html_path
    print(f"Opening {html_filename} in your default web browser...")
    webbrowser.open(url)


def main():
    print("Study Time Tracker - Runner")
    print("1) Run console version")
    print("2) Open HTML version in browser")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        run_console_tracker()
    elif choice == "2":
        # Change the file name here if your HTML file is named differently
        open_html_tracker("study_tracker.html")  # or "index.html"
    else:
        print("Invalid choice. Please run the program again and choose 1 or 2.")


if __name__ == "__main__":
    main()
