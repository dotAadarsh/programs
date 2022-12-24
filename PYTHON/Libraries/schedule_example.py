import schedule # schedule module is a Py lib that provides functions for scheduling tasks to be executed at a particular time.
import time

def job():
    print("I'm working...")

schedule.every(10).seconds.do(job) # schedules the job function to be executed every 10 seconds
schedule.every(10).minutes.do(job) # schedules the job function to be executed every 10 minutes
schedule.every().hour.do(job) # schedules the job function to be executed every hour
schedule.every().day.at("10:30").do(job) # schedules the job function to be executed every day at 10:30. 
schedule.every().monday.do(job) # schedules the job function to be executed every Monday.
schedule.every().wednesday.at("13:15").do(job) # schedules the job function to be executed every Wednesday at 13:15.
schedule.every().minute.at(":17").do(job) # schedules the job function to be executed every minute at the 17th second.


while True:

    """
    The while loop at the end of the code runs indefinitely and checks for any pending tasks to be executed using the run_pending function from the schedule module. 
    The time.sleep(1) function is used to pause the program for 1 second before checking for pending tasks again. 
    This ensures that the program does not use too much CPU resources while checking for tasks.
    """

    schedule.run_pending()
    time.sleep(1)
