from . import blueprint
from flask import request
from controller import bukuController


@blueprint.route('/buku', methods=['GET', 'POST'])
@blueprint.route('/buku/<int:id>', methods = ['GET', 'DELETE', 'PUT'])

def buku(id=None):
    method = request.method
    # g.auth.setAllowed(['admin', 'member'])
    if method == 'GET':
        if id == None:
            buku = bukuController.get_buku()

        else:
            buku = bukuController.get_buku_id(id)
        return buku
    
    if method == "DELETE":
        result = bukuController.delete_buku(id)
        return result
    
    if method == "POST":
        result = bukuController.create_buku()
        return result
    
    if method == "PUT":
        result = bukuController.update_buku(id)
        return result
    