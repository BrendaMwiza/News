from app import kora_app
from flask_script import Manager,Server

# creating the app instance
app = kora_app('development')

manager = Manager(app)
manager.add_command('server', Server)

@manager.command

def test():
    '''
    Run unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()