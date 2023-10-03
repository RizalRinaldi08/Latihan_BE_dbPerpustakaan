import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from . import db, penulis_buku


class Buku(db.Model):
    __tablename__ = 'tb_buku'
    id_buku = db.Column(db.Integer, primary_key=True)
    judul = db.Column(db.String, nullable=False)
    tahun = db.Column(db.Date, nullable=False)
    jumlah_hal = db.Column(db.String, nullable=False)
    kategori_id = db.Column(db.Integer, db.ForeignKey('tb_kategori.id_kategori'),nullable=False) # one to many
    stock = db.Column(db.Integer, nullable=False)

    penulis = db.relationship('Penulis', secondary=penulis_buku, lazy='subquery', backref=db.backref('books', lazy=True)) #many to many
    # books= db.relationship('Buku', backref='kategori', lazy=True)
    peminjaman = db.relationship('Peminjam', backref="buku", lazy=True)

    def __repr__(self):
        return f'<Buku {self.judul}>'