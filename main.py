from flask import Flask
from database import setup_database
from scheduling import setup_scheduler
from views import setup_views


def create_app():
    app = Flask(__name__)
    # TODO move to config file
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scrappy_admin:my-strong-password-here@localhost/scrappy_data'
    setup_views(app)
    setup_database(app)
    setup_scheduler(app)
    return app


create_app().run()
