from flask import Blueprint
log = Blueprint('log', __name__)


@log.route('/')
def run():
    return u'log module'