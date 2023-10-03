from flask import Blueprint, request, jsonify
from auth import is_auth
from model import Buku, Penulis, Kategori
import logging

logger = logging.getLogger(__name__)

bukuApi = Blueprint('buku', __name__)


@bukuApi.route('/buku')
def get_buku():
    a = is_auth(request.authorization.parameters)
    if a == None:
        return {
            "message": "Unauthorized"
        }, 400
    # print(a['is_admin'])
    b = Buku()
    books = b.query.all()
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
@bukuApi.route('/buku/<id>')
def get_buku_id(id):
    a =is_auth()
    if a == None:
        return {
            "message": "Unauthorized"
        }, 400
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
@bukuApi.route('/buku', methods=["POST"])
def create_buku():
    from db import db
    a = is_auth()
    if a['role'] != 'admin':
        return {
            "message": "Unauthorized"
        }, 400
    data = request.get_json()
    kategori = Kategori.query.filter_by(id_kategori=id).first()
    if kategori == None :
        return {
            "message" : f'Tidak ada Kategori dengan id = {id}'
        }
    buku = Buku ( judul= data['judul'],
                 tahun = data['tahun'],
                 jumlah_hal = data['jumlah_hal'],
                 kategori_id = data['kategori_id'],
                 stock = data['stock']
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
@bukuApi.route('/buku/<id>', methods=['PUT'])
def update_buku(id):
    from db import db
    a = is_auth()
    if a['role']== 'admin':
        return {
            "message": "Unauthorized"
        }, 400
    data=request.get_json()
    if 'judul' not in data:
        return{
            'error': 'Bad Request',
             'message': 'Name field needs to great present'
        }, 400
    kategori = Kategori.query.filter_by(id_kategori=id).first()
    if kategori == None :
        return {
            "message" : f'Tidak ada Kategori dengan id = {id}'
        }
    
    b = Buku.query.filter_by(id_buku=id).first_or_404()
    
    b.judul = data['judul']
    if 'judul' in data:
        b.judul=data['judul']
        db.session.commit()
        return jsonify({
            'judul': b.judul,
            'tahun': b.tahun,
            'jumlah_hal': b.jumlah_hal,
            'kategori_id': b.kategori_id
        })


#DELETE data di tabel buku
@bukuApi.route('/buku/<id>', methods=['DELETE'])
def delete_buku(id):
    from db import db
    a = is_auth()
    if a['role']== 'admin':
        return {
            "message": "Unhauthorized"
        }, 400
    b = Buku.query.filter_by(id_buku=id).first_or_404()
    db.session.delete(b)
    db.session.commit()
    return {
        'success': 'Data berhasil dihapus'
    }
