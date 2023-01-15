import logging
import time
from flask_apscheduler import APScheduler
from parser import get_price
from database import db
from models import UrlData, PriceEntry


log = logging.getLogger()
scheduler = APScheduler()


def parse_prices_batch():
    now = int(time.time())
    app = scheduler.app
    with app.app_context():
        urls_data = UrlData.query.all()
        for url_data in urls_data:
            try:
                price = get_price(url_data.url)
                price_entry = PriceEntry(url_id=url_data.id, price=price, datetime=now)
                db.session.add(price_entry)
            except Exception as e:
                log.exception(e)

        try:
            db.session.commit()
        except Exception as e:
            log.exception(e)
            db.session.rollback()
    return str('ok')


def setup_scheduler(app):
    with app.app_context():
        scheduler.init_app(app)
        scheduler.add_job(id='price_enrich', func=parse_prices_batch, trigger="interval", seconds=600)
        scheduler.start()
