from . import blueprint
from flask import request
from controller import peminjamanController

@blueprint.route('/pengembalian/<int:id>', methods= ['PUT'])
@blueprint.route('/peminjaman', methods=['GET', 'POST'])
@blueprint.route('/peminjaman/<int:id>', methods = ['GET', 'DELETE'])


def peminjam(id=None):
    method = request.method
    if method == 'GET':
        if id == None:
            buku = peminjamanController.get_pinjam()

        else:
            buku = peminjamanController.get_pinjam_id(id)
        return buku
    
    if method == "DELETE":
        result = peminjamanController.delete_pinjam(id)
        return result
    
    if method == "POST":
        result = peminjamanController.create_pinjam()
        return result
    
    if method == "PUT":
        result = peminjamanController.update_pinjam(id)
        return result