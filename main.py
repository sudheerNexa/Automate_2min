import datetime
import time
import pytz # You may need to add 'pytz' to your requirements.txt

def run_task():
    now = datetime.datetime.now(pytz.timezone('Europe/London'))
    # Check if current time is between 9 AM (9) and 9 PM (21)
    if 9 <= now.hour < 21:
        with open("output.txt", "a") as f:
            f.write(f"Script ran successfully at: {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        print(f"Logged: {now}")
    else:
        print("Outside of 9am-9pm window. Skipping.")

# Run 3 times with 120-second (2 min) intervals
for i in range(3):
    run_task()
    if i < 2: # Don't sleep after the last run
        time.sleep(120)
