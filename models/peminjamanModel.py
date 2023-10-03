import datetime
from sqlalchemy import ForeignKey
from . import db

class Peminjam(db.Model):
    __tablename__ =  'tb_peminjam'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('tb_user.id_user'), nullable=False )
    book_id = db.Column(db.Integer, db.ForeignKey('tb_buku.id_buku'), nullable=False)
    star_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.today())
    end_date = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.Boolean, nullable=False, default=False)


    def __repr__(self):
        return f'<Peminjam {self.id}>'