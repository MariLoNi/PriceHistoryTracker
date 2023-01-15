import flask
from models import UrlData
from flask import request, render_template, blueprints
from database import db

url_api_page = blueprints.Blueprint('url_api', __name__, url_prefix='/api/v1/url')
index_page = blueprints.Blueprint('index', __name__)


@url_api_page.route('/add', methods=['POST'])
def add_url():
    url = request.form.get('url')
    if not url:
        return flask.Response(status=400, response='Should set url in form')

    db.session.add(UrlData(url=url))
    db.session.commit()
    return flask.Response(status=200)


@url_api_page.route('/delete', methods=['POST'])
def delete_url_by_id():
    url_id = request.args.get('id')
    UrlData.query.filter_by(id=url_id).delete()
    db.session.commit()
    return flask.Response(status=200)


@url_api_page.route('/get_all', methods=['GET'])
def get_urls():
    return UrlData.query.all()


@url_api_page.route('/get', methods=['GET'])
def get_url():
    url = request.args.get('url')
    return UrlData.query.filter_by(url=url).all()


@index_page.route('/')
def index():
    return render_template('index.html')


def setup_views(app):
    app.register_blueprint(url_api_page)
    app.register_blueprint(index_page)
