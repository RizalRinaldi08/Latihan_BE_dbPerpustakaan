from . import db

class Kategori(db.Model):
    __tablename__='tb_kategori'
    id_kategori = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String, nullable = False)
    deskripsi = db.Column(db.String, nullable = False)
    books= db.relationship('Buku', backref='kategori', lazy=True) #One to Many

    def __repr__(self):
        return f'<Kategori {self.nama}>'