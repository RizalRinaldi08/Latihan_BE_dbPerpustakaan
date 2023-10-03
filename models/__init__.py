from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

penulis_buku = db.Table('penulis_buku',
            db.Column('id_buku', db.Integer, db.ForeignKey('tb_buku.id_buku'), primary_key=True),
            db.Column('id_penulis', db.Integer, db.ForeignKey('tb_penulis.id_penulis'), primary_key=True) )

from .bukuModel import Buku
from .kategoriModel import Kategori
from .peminjamanModel import Peminjam
from .penulisModel import Penulis
from .userModel import User
# from .roleModel import Role