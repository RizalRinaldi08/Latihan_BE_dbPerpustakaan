from flask import Blueprint, request, jsonify
from .auth import isAuth
from models.userModel import User
import logging
import bcrypt

logger = logging.getLogger(__name__)

bukuApi = Blueprint('penulis', __name__)


#GET ALL DATA di table USER
def get_user():
    a = isAuth()
    if a == None:
        return {
            "message": "Unauthorized"
        }, 400
    return jsonify([
        {
            'id_user' : x.id_user,
            'username' : x.username,
            'password' : x.password,
            'is_admin' : x.is_admin
        } for x in User.query.all()
    ])

#GET Data by ID di table USER
def get_user_id(id):
    a = isAuth()
    if a == None:
        return {
            "message": "Unauthorized"
        }, 400
    u = User.query.filter_by(id_user=id).first_or_404()
    return {
        'username' : u.username,
        'password' : u.password,
        'is_admin' : u.is_admin
    }

#CREATE data di table USER
def create_user():
    from db import db 
    a = isAuth()
    if a['role'] != 'admin':
        return {
            "message": "Unauthorized"
        }, 400
    data = request.get_json()
    if 'username' not in data.keys() or 'password' not in data.keys():
        return {
            'Not Success' : 'Username or Password Must to be Input'
        }
    existing_user = User.query.filter_by(username=data['username']).first()
    
    if existing_user :
        return {
            'Failed' : 'Username Already Exist'
        }, 409
    
    password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    # is_admin = data.get(is_admin, False) #default False jika is_admin tidak disediakan


    u = User (
        username = data['username'],
        password = data['password'],
        is_admin = data['is_admin'],
        role_id = 2
    )
 
    db.session.add(u)
    # db.session.commit()
    return {
        'Message' : 'User has been Added',
        'username' : u.username,
        'is_admin' : u.is_admin,
        'role_id' : u.role_id
    }, 201

#UPDATE Data di table USER
def update_user(id):
    from db  import db 
    a = isAuth()
    if a['role'] != 'admin':
        return {
            "message": "Unauthorized"
        }, 400
    data = request.get_json()
    if 'username' not in data or 'password' not in data :
        return {
            'Error' : 'Username Or Password Must be Insert'
        }, 400
    u = User.query.filter_by(id_user=id).first_or_404()
    hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    u.username = data['username']
    u.password = hashed.decode('utf-8')
    db.session.commit()
    return jsonify ({
            "Message": "Data User Hasbeen Updated"
        })
    
    
#DELETE Data di table USER 

def delete_user(id):
    from db import db 
    a = isAuth()
    if a['role'] != 'admin':
        return {
            "message": "Unauthorized"
        }, 400
    user = User.query.filter_by(id_user=id).first_or_404()
    db.session.delete(user)
    db.session.commit()
    return {
        'Success': 'Data deleted successfully'
    }