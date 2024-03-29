# from app import kora_app
from flask_script import Manager,Server
from app import kora_app,db
from app.models import User,Role,Review
from  flask_migrate import Migrate, MigrateCommand

# creating the app instance
app = kora_app('development')
# app = kora_app('test')
app = kora_app('productions')

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


@manager.command
def test():
    '''
    Run unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User, Role = Role)


if __name__ == '__main__':
    manager.run()