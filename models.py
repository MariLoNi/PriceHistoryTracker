from dataclasses import dataclass
from database import db

from typing import List


@dataclass
class PriceEntry(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    url_id: int = db.Column(db.Integer, db.ForeignKey('url_data.id'))
    datetime: int = db.Column(db.Integer)
    price: int = db.Column(db.Integer)


@dataclass
class UrlData(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    url: str = db.Column(db.String(300))
    price_history: List[PriceEntry] = db.relationship('PriceEntry', backref='url_data')

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return '<UrlData %r>' % self.url
