import os
import time
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
import requests

SPIDER_URL = 'http://127.0.0.1:6800/schedule.json'


def check_github():
    """
        check github jobs

    :return:
    """
    payload = {
        'project': 'default',
        'spider': 'fetch-project',
    }

    res = requests.post(url=SPIDER_URL, data=payload)
    print(res.text)


def check_project_state():
    """
        check project state
    :return:
    """
    payload = {
        'project': 'default',
        'spider': 'pstats',
    }

    res = requests.post(url=SPIDER_URL, data=payload)
    print(res.text)


jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}

executors = {
    'default': {'type': 'threadpool', 'max_workers': 5},
    'processpool': ProcessPoolExecutor(max_workers=3)
}
job_defaults = {
    'coalesce': False,
    'max_instances': 2
}

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.configure(
        jobstores=jobstores,
        executors=executors,
        job_defaults=job_defaults)

    # print jobs
    # if len(jobs) == 0:
    scheduler.add_job(check_github, 'cron', hour='*/4', id='github')
    scheduler.add_job(check_project_state, 'cron', hour='2', id='pstats')

    scheduler.remove_job(job_id='github')
    scheduler.remove_job(job_id='pstats')

    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
