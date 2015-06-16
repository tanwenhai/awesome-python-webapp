from flask import Blueprint
job = Blueprint('job', __name__)


@job.route('/')
def run():
    return u'job module'
