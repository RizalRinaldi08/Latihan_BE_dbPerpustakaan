from flask import Blueprint, jsonify, request
from models.bukuModel import Buku
from models import Penulis, Kategori
from .auth import isAuth
from . import db

def get_buku():
    a = isAuth()
    if a == None:
        return {
            "message": "Unauthorized"
        }, 400
    if a.is_admin == False:
        return {
            "YOU ARE NOT ADMIN"
        }
    books = Buku.query.all()
    result=[]
    for i in books:
        # print(i.judul,i.kategori)
        result.append({
            'id_buku': i.id_buku,
            'judul':i.judul,
            'tahun':i.tahun,
            'jumlah hal': i.jumlah_hal,
            'kategori_id': i.kategori_id,
            'kategori': i.kategori.nama
        })
    return {
        'result':result  
    }

#GET data by id di tabel buku
def get_buku_id(id):
    a = isAuth()
    if a == None:
        return {
            "message": "Unauthorized"
        }, 400
    if a.is_admin == False:
        return {
            "YOU ARE NOT ADMIN"
        }
    buku = Buku.query.filter_by(id_buku=id).first_or_404()
    return{
        'judul': buku.judul,
        'tahun': buku.tahun,
        'jumlah_hal': buku.jumlah_hal,
        'kategori': buku.kategori.nama,
        'kategori_id': buku.kategori_id
    }

#POST data di tabel buku
# tambahakan create penulis di endpoint buku
def create_buku():
    # from db import db
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
    kategori = Kategori.query.filter_by(id_kategori=data['kategori_id']).first()
    if kategori == None :
        return {
            "message" : f'Tidak ada Kategori dengan id = {id}'
        }
    buku = Buku ( judul= data['judul'],
                 tahun = data['tahun'],
                 jumlah_hal = data['jumlah_hal'],
                 kategori_id = data['kategori_id'],
                 stock = data['stock'],
                #  id_penulis = data['id_penulis']
                 )
    
    for i in data['penulis']:
        p =  Penulis.query.filter_by(id_penulis=i).first()
        if p == None:
            return {
                "message": f'Tidak ada penulis dengan id = {i}'
            }, 400
        buku.penulis.append(p)

    db.session.add(buku)
    db.session.commit()
    return {
        'judul': buku.judul,
        'tahun': buku.tahun,
        'jumlah_hal': buku.jumlah_hal,
        'kategori_id': buku.kategori_id,
        'stock': buku.stock
    }, 201

#PUT data di tabel buku
# tambahakan update penulis di endpoint buku
def update_buku(id):
    # from db import db
    a = isAuth()
    if a == None:
        return {
            "message": "Unauthorized"
        }, 400
    if a.is_admin == False:
        return {
            "YOU ARE NOT ADMIN"
        }
    data=request.get_json()
    if 'judul' not in data:
        return{
            'error': 'Bad Request',
             'message': 'Name field needs to great present'
        }, 400
    kategori = Kategori.query.filter_by(id_kategori=data['kategori_id']).first()
    if kategori == None :
        return {
            "message" : f'Tidak ada Kategori dengan id = {id}'
        }
    
    b = Buku.query.filter_by(id_buku=id).first_or_404()
    
    b.judul = data['judul']
    b.tahun = data['tahun']
    b.jumlah_hal = data['jumlah_hal']
    b.kategori_id = data['kategori_id']
    b.stock = data['stock']
    b.penulis = []

    for i in data['penulis']:
        p =  Penulis.query.filter_by(id_penulis=i).first()
        if p == None:
            return {
                "message": f'Tidak ada penulis dengan id = {i}'
            }, 400
        b.penulis.append(p)
    
    
        db.session.commit()
    return jsonify({
            'judul': b.judul,
            'tahun': b.tahun,
            'jumlah_hal': b.jumlah_hal,
            'kategori_id': b.kategori_id,
            'stock' : b.stock,
            'penulis': [p.nama for p in b.penulis]
    })


#DELETE data di tabel buku
def delete_buku(id):
    a = isAuth()
    if a == None:
        return {
            "message": "Unauthorized"
        }, 400
    if a.is_admin == False:
        return {
            "YOU ARE NOT ADMIN"
        }
    b = Buku.query.filter_by(id_buku=id).first_or_404()
    db.session.delete(b)
    db.session.commit()
    return {
        'success': 'Data berhasil dihapus'
    }