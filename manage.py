from app import kora_app
from flask_script import Manager,server

# creating the app instance
app = kora_app('development')

manager = Manager(app)
manager.add_command('server', Server)

