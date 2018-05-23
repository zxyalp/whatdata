from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from sayhello import app


manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@manager.command
def hello():
    print("hello")


if __name__ == '__main__':
    manager.run()
