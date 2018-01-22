from flask_rq import get_worker
from flask_script import Manager

from main import app


manager = Manager(app)


@manager.command
def work():
    get_worker().work()


if __name__ == '__main__':
        manager.run()
