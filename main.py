import datetime
import os

# Get the current time
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Append the time to a file named output.txt
with open("output.txt", "a") as f:
    f.write(f"Script ran successfully at: {now}\n")

print(f"Logged time: {now}")
