from project import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand
from .db_init import InitDbCommand
from .populate_random import PopulateWithRandomCommand
# from .populate_streaks import

manager = Manager(create_app())

manager.add_command('db', MigrateCommand)
manager.add_command('db_init', InitDbCommand)
manager.add_command('populate_with_random', PopulateWithRandomCommand)
manager.add_command('populate_streaks', PopulateWithRandomCommand)
