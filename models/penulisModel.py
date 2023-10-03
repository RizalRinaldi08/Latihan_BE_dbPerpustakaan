import datetime
from . import db

class Penulis(db.Model):
    __tablename__ = 'tb_penulis'
    id_penulis = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String, nullable=False)
    kewarganegaraan = db.Column(db.String, nullable=False)
    tahun_kelahiran = db.Column(db.Date, nullable=False)
   
    def __repr__(self):
        return f'<Penulis {self.nama}>'