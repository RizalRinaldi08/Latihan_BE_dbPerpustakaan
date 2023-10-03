from flask import Blueprint, g 

blueprint = Blueprint('my_blueprint', __name__)

# @blueprint.before_request()
# def authentication():
#     g.auth = Auth()

from . import kategori, buku, peminjaman, user, penulis

@blueprint.errorhandler (401)
def custom_401(error):
    return {
        "message" : "unauthorized",
        "description" : error.description
    }, 401