from flask import Blueprint, request, jsonify
from models.penulisModel import Penulis
from .auth import isAuth
import logging
from . import db

authors = Penulis()

logger = logging.getLogger(__name__)

bukuApi = Blueprint('penulis', __name__)

def get_penulis(): 
    a = isAuth()
    if a == None:
        return {
            "message": "Unauthorized"
        }, 400
    return jsonify([
        {
            'id_penulis' : i.id_penulis,
            'nama': i.nama, 
            'kearganegaraan': i.kewarganegaraan, 
            'tahun_kelahiran' : i.tahun_kelahiran  
        } for i in Penulis.query.all()
    ])

#GET DATA BY ID data table Penulis
def get_penuli_id(id):
    a = isAuth()
    if a == None:
        return {
            "message": "Unauthorized"
        }, 400
    p = Penulis.query.filter_by(id_penulis=id).first_or_404()
    return {
        'nama': p.nama,
        'kewarganegaraan': p.kewarganegaraan,
        'tahun_kelahiran': p.tahun_kelahiran
    }

#CREATE data pada table Penulis
def create_penulis():
    # from db import db
    a = isAuth()
    if a['role'] != 'admin':
        return {
            "message": "Unauthorized"
        }, 400
    data = request.get_json()
    # if not 'nama' in data or not 'kewarganegaraan' in data or not 'tahun_kelahiran' in data :
    #     return jsonify({
    #         'error': 'Bad Request',
    #         'message': 'Data Penulis Tidak ada'
    #     }), 400
    p = Penulis (
                    nama = data['nama'],
                    kewarganegaraan = data['kewarganegaraan'],
                    tahun_kelahiran = data['tahun_kelahiran']
                    )
    db.session.add(p)
    db.session.commit()
    return { 
        'nama': p.nama,
        'kewarganegaraan': p.kewarganegaraan,
        'tahun_kelahiran': p.tahun_kelahiran
    }, 201

#UPDATE data pada table Penulis
def update_penulis(id):
    # from db import db 
    a = isAuth()
    if a['role'] != 'admin':
        return {
            "message": "Unauthorized"
        }, 400
    data = request.get_json()
    if 'nama' not in data or 'kewarganegaraan' not in data or 'tahun_kelahiran' not in data:
        return {
            'error' : 'Bad Request',
            'message' : 'Data buku tidak tersedia'
        }, 400
    p = Penulis.query.filter_by(id_penulis=id).first_or_404()
    if 'nama' in data:
        p.nama = data['nama']
        db.session.commit()
        return jsonify ({
            'nama' : p.nama,
            'kewarganegaraan': p.kewarganegaraan,
            'tahun_kelahiran' : p.tahun_kelahiran
        })

#DELETE data pada table Penulis
def delete_penulis(id):
    # from db import db 
    a = isAuth()
    if a['role'] != 'admin':
        return {
            "message": "Unauthorized"
        }, 400
    p = Penulis.query.filter_by(id_penulis=id).first_or_404()
    db.session.delete(p)
    db.session.commit()
    return {
        'Success' : 'Data penulis berhasil dihapus'
    }