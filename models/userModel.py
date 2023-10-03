from sqlalchemy.orm import relationship
from . import db

class User(db.Model):
    __tablename__ = 'tb_user'
    id_user = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(60), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<User {self.username}>'