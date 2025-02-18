# from datetime import datetime, timedelta
# from pytz import utc
#
# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.executors.pool import ThreadPoolExecutor
# from apscheduler.job import Job
#
#
# def myfunc(arg):
#    print("Called myfunc with " + str(arg))
#
#
# executors = {
#    'default': ThreadPoolExecutor(200),
# }
#
#
# scheduler.start()
# scheduler = BackgroundScheduler(executors=executors)
#
# now = datetime.now()
# then = now + timedelta (seconds = 30)
#
# job = scheduler.add_job(myfunc, then , ['arg1'])
#
#
#
# scheduler.shutdown(wait=True)


import os
import time
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta


def tick(text):
    print(text + '! The time is: %s' % datetime.now())


scheduler = BackgroundScheduler()
dd = datetime.now() + timedelta(seconds=3)
scheduler.add_job(tick, 'date', run_date=dd, args=['TICK'])

dd = datetime.now() + timedelta(seconds=6)
scheduler.add_job(tick, 'date', run_date=dd, kwargs={'text': 'TOCK'})

scheduler.start()
print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

scheduler.print_jobs()

while len(scheduler.get_jobs()) > 0:
    print("Waiting...")
    time.sleep(2)
scheduler.shutdown()
