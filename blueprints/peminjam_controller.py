from flask import Blueprint, request, jsonify
from auth import is_auth
from model import Penulis, Buku, User, Peminjam
import logging

logger = logging.getLogger(__name__)

bukuApi = Blueprint('penulis', __name__)

def get_pinjam():
    return jsonify ([
        {
            
        }
    ])

def get_pinjam_id(id):
    p = Peminjam.query.filter_by(id=id).first_or_404()
    return {
        'user_id': p.user_id,
        'book_id': p.book_id,
        'tanggal meminjam': p.star_date
    }

def create_pinjam():
    from db import db 
    a = is_auth()
    if a['role'] != 'admin':
        return {
            "message" : "Unauthorized"
        }, 400
    data = request.get_json()
    p = Peminjam (
                    user_id = data['user_id'],
                    book_id = data['book_id'],
                    star_date = data['star_date']
                )
    db.session.add(p)
    db.session.commit()
    return {
        'user_id' : p.user_id,
        'book_id' : p.book_id,
        'star_date': p.star_date
    }, 201

def update_pinjam(id):
    from db import db 
    a = is_auth()
    if a['role'] != 'admin':
        return {
            "message" : "Unauthorized"
        }, 400
    data = request.get_json()
    p = Peminjam.query.filter_by(id = id).first_or_404()
    if 'user_id' in data:
        p.user_id = data['user_id'],
        p.book_id = data['book_id']
        db.session.commit()
        return jsonify({
            'user_id' : p.user_id,
            'book_id' : p.book_id,
            'star_date' : p.star_date,
            'end_date' : p.end_date,
            'status' : p.status
        })
    
def isBackBook(id):
    from db import db 
    a = is_auth()
    if a['role'] != 'admin':
        return {
            "message" : "Unauthorized"
        }, 400
    data = request.get_json()
    p = Peminjam.query.filter_by(id = id).first_or_404()
    if 'user_id' in data:
        p.user_id = data['user_id'],
        p.book_id = data['book_id']
        db.session.commit()
        return jsonify({
            'user_id' : p.user_id,
            'book_id' : p.book_id,
            'star_date' : p.star_date,
            'end_date' : p.end_date,
            'status' : p.status
        })
    
def delete_pinjam(id):
    from db import db 
    a = is_auth()
    if a['role'] != 'admin':
        return {
            "message": "Unauthorized"
        }, 400
    p = Peminjam.query.filter_by(id=id).first_or_404()
    db.session.delete(p)
    db.session.commit()
    return {
        "Succes" : "Data Have Been Deleted"
    }