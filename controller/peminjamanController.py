from flask import request, jsonify
from .auth import isAuth
from models import Peminjam
from . import db
import datetime

def get_pinjam():
    a = isAuth()
    if a == None:
        return {
            "message": "Unauthorized"
        }, 400
    return jsonify([
        {
            'id': i.id, 
            'user_id': i.user_id,
            'book_id': i.book_id,
            'star_date': i.star_date,
            'end_date': i.end_date,
            'status' : i.status 
        } for i in Peminjam.query.all()
    ])

def get_pinjam_id(id):
    a = isAuth()
    if a == None:
        return {
            "message": "Unauthorized"
        }, 400
    i = Peminjam.query.filter_by(id=id).first_or_404()
    return jsonify ({
            'id': i.id, 
            'user_id': i.user_id,
            'book_id': i.book_id,
            'star_date': i.star_date,
            'end_date': i.end_date,
            'status' : i.status
    })

def create_pinjam():
    a = isAuth()
    if a == None:
        return {
            "message": "Unauthorized"
        }, 400
    if a.is_admin == False:
        return {
            "YOU ARE NOT ADMIN"
        }
    data = request.get_json()
    p = Peminjam (
                    user_id = data['user_id'],
                    book_id = data['book_id']
                )
    db.session.add(p)
    db.session.commit()
    return { 
        'user_id': p.user_id,
        'book_id': p.book_id,
        'star_date': p.star_date,
        'end_date': p.end_date,
        'status': p.status
    }, 201

def update_pinjam(id):
    a = isAuth()
    if a == None:
        return {
            "message": "Unauthorized"
        }, 400
    if a.is_admin == False:
        return {
            "YOU ARE NOT ADMIN"
        }

    p = Peminjam.query.filter_by(id=id).first_or_404()
    p.status=True
    p.end_date = datetime.datetime.today()
    db.session.commit()
    return jsonify({
        'user_id': p.user_id,
        'book_id': p.book_id,
        'star_date': p.star_date,
        'end_date': p.end_date,
        'status': p.status
    })

def delete_pinjam(id):
    a = isAuth()
    if a == None:
        return {
            "message": "Unauthorized"
        }, 400
    if a.is_admin == False:
        return {
            "YOU ARE NOT ADMIN"
        }
    k = Peminjam.query.filter_by(id=id).first_or_404()
    db.session.delete(k)
    db.session.commit()
    return {
        'success': 'Data Berhasil Dihapus'
    }
