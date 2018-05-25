from flask_script import Manager, Shell
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_migrate import MigrateCommand

from sayhello import app, Role, User, db


manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def hello():
    print("hello")


if __name__ == '__main__':
    manager.run()
