from flask import Blueprint, request, jsonify
from auth import is_auth
from model import Kategori
import logging

logger = logging.getLogger(__name__)

bukuApi = Blueprint('kategori', __name__)


def get_kategori():
    a = is_auth(request.authorization.parameters)
    if a == None:
        return {
            "message": "Unauthorized"
        }, 400
    return jsonify([
        {
            'id_kategori': i.id_kategori, 
            'nama': i.nama, 
            'deskripsi' : i.deskripsi,
            # 'books': [x.judul for x in i.books]  
        } for i in Kategori.query.all()
    ])

def get_kategori_id(id):
    a = is_auth(request.authorization.parameters)
    if a == None:
        return {
            "message": "Unauthorized"
        }, 400
    print(id)
    kategori = Kategori.query.filter_by(id_kategori=id).first_or_404()
    return {
        'id': kategori.id_kategori, 
        'nama': kategori.nama,
        'deskripsi': kategori.deskripsi
    }

def create_kategori():
    from db import db
    a = is_auth()
    if a['role'] != 'admin':
        return {
            "message": "Unauthorized"
        }, 400
    data = request.get_json()
    if not 'nama' in data or not 'deskripsi' in data :
        return jsonify({
            'error': 'Bad Request',
            'message': 'Nama ata Deskripisi Tidak ada'
        }), 400
    k = Kategori (
                    nama = data['nama'],
                    deskripsi = data['deskripsi']
                )
    db.session.add(k)
    db.session.commit()
    return { 
        'nama': k.nama,
        'deskripsi': k.deskripsi
    }, 201

def update_kategori(id):
    from db import db
    a = is_auth()
    if a['role'] != 'admin':
        return {
            "message": "Unauthorized"
        }, 400
    data=request.get_json()
    if 'nama' not in data:
        return {
            'error': 'Bad Request',
            'message': 'Name field needs to be present'
        }, 400
    k = Kategori.query.filter_by(id_kategori=id).first_or_404()
    k.nama=data['nama']
    if 'deskripsi' in data:
        k.deskripsi= data['deskripsi']
    db.session.commit()
    return jsonify({
        'nama': k.nama,
        'deskripsi': k.deskripsi
    })

def delete_kategori(id):
    from db import db
    a = is_auth()
    if a['role'] != 'admin':
        return {
            "message": "Unauthorized"
        }, 400
    k = Kategori.query.filter_by(id_kategori=id).first_or_404()
    db.session.delete(k)
    db.session.commit()
    return {
        'success': 'Data Berhasil Dihapus'
    }
