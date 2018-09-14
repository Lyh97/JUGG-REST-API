from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
import sys

from datetime import date


class Config(object):

    REDIS_URL = "redis://localhost:6379"

    SCHEDULER_API_ENABLED = True

    SCHEDULER_JOBSTORES = {
      'default': SQLAlchemyJobStore(url='sqlite:///db/jobs.sqlite')
    }

    SCHEDULER_EXECUTORS = {
      'default': {'type': 'threadpool', 'max_workers': 20}
    }

    UPLOAD_FOLDER = sys.path[0] + '/uploads'
