from . import blueprint
from flask import request
from controller import kategoriController

@blueprint.route('/kategori', methods=['GET', 'POST'])
@blueprint.route('/kategori/<int:id>', methods = ['GET', 'DELETE', 'PUT'])

def kategori(id=None):
    method = request.method
    if method=="GET":
        if id==None:
            kategori = kategoriController.get_kategori()
        else:
            kategori = kategoriController.get_kategori_id(id)
        return kategori

    if method == "POST":
        result = kategoriController.create_kategori()
        return result
    
    if method == "PUT":
        result = kategoriController.update_kategori(id)
        return result
    
    if method == "DELETE":
        result = kategoriController.delete_kategori(id)
        return result
    