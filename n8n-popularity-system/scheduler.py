import schedule
import time
from collector import run_collection

print("Scheduler started. Will run data collection every 24 hours.")

# Run once immediately on start
run_collection()

# Schedule to run every day
schedule.every(24).hours.do(run_collection)

while True:
    schedule.run_pending()
    time.sleep(1)