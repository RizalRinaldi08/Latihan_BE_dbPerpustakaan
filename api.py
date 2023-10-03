# from flask import Flask, request, jsonify

# from flask_sqlalchemy import SQLAlchemy
# import uuid
# from flask_login import LoginManager
# from flask_bcrypt import Bcrypt
# import bcrypt




# app = Flask (__name__)
# database_url = 'postgresql://postgres:admin123@localhost:5433/db_perpustakaan'
# app.config['SQLALCHEMY_DATABASE_URI'] = database_url
# db = SQLAlchemy(app)
# # bcrypt = Bcrypt(app)
# # login_manager = LoginManager
# # login_manager.init_app(app)


# penulis_buku = db.Table('penulis_buku',
#             db.Column('id_buku', db.Integer, db.ForeignKey('tb_buku.id_buku'), primary_key=True),
#             db.Column('id_penulis', db.Integer, db.ForeignKey('tb_penulis.id_penulis'), primary_key=True)                    
# )
# class Buku(db.Model):
#     __tablename__ = 'tb_buku'
#     id_buku = db.Column(db.Integer, primary_key=True)
#     judul = db.Column(db.String, nullable=False)
#     tahun = db.Column(db.Date, nullable=False)
#     jumlah_hal = db.Column(db.String, nullable=False)
#     kategori_id = db.Column(db.Integer, db.ForeignKey('tb_kategori.id_kategori'),nullable=False) # one to many
#     penulis = db.relationship('Penulis', secondary=penulis_buku, lazy='subquery', backref=db.backref('books', lazy=True)) #many to many

#     def __repr__(self) -> str:
#         return f'<Buku {self.judul}>'

# class Penulis(db.Model):
#     __tablename__ = 'tb_penulis'
#     id_penulis = db.Column(db.Integer, primary_key=True)
#     nama = db.Column(db.String, nullable=False)
#     kewarganegaraan = db.Column(db.String, nullable=False)
#     tahun_kelahiran = db.Column(db.Date, nullable=False)

# class Kategori(db.Model):
#     __tablename__='tb_kategori'
#     id_kategori = db.Column(db.Integer, primary_key=True)
#     nama = db.Column(db.String, nullable = False)
#     deskripsi = db.Column(db.String, nullable = False)
#     books= db.relationship('Buku', backref='kategori', lazy=True) #One to Many

# class User(db.Model):
#     __tablename__ = 'tb_user'
#     id_user = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), nullable=True)
#     password = db.Column(db.String(60), nullable=True)
#     is_admin = db.Column(db.Boolean, default=False)
#     role_id = db.Column(db.Integer, db.ForeignKey('role.id_role'),nullable=False)
#     role = db.relationship('Role', backref='user', lazy=True)


# class Peminjam(db.Model):
#     __tablename__ =  'tb_peminjam'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id_user'), nullable=False )
#     book_id = db.Column(db.Integer, db.ForeignKey('buku.id_buku'), nullable=False)
#     star_date = db.Column(db.DateTime, nullable=False)
#     end_date = db.Column(db.DateTime, nullable=True)

# # class detail_peminjam(db.model):
# #     id_detail =db.Column(db.Integer, primary_key=True)
# #     id =
# #     buku_id = 
    

# def authen():
#     credential = request.authorization
#     if credential != None and credential.type == 'basic':
#         username = credential.parameters['username']
#         password = credential.parameters['password']
#         user = User().query.filter_by(username=username).first()

#         if user != None:
#             isMatch = bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))
#             if isMatch==True:
#                 user={
#                     'username': user.username,
#                     'password': user.password,
#                     'role': user.role.name                  
#                 }
#                 return user
            
#     # def __init__(self,username, password, is_admin=False):
#     #     self.username = username
#     #     self.password = bcrypt.generate_password_hash(password)
#     #     self.is_admin = is_admin

#     # def __repr__(self):
#     #     return f'<username {self.username}>'

# class Role(db.Model):
#     __tablename__ = 'role'
#     id_role = db.Column(db.Integer, primary_key=True, nullable=False)
#     name = db.Column(db.String, nullable=False)

# #membuat method untuk menyimpan data agar lebih simple
# # def save(self):
# #     try:
# #         db.session.add(self)
# #         db.session.commit()
# #         return True
# #     except:
# #         return False

# #----------------------------------ENDPOINT TABLE KATEGORI--------------------------------------------------

# # GET table Kategori
# @app.route('/kategori/')
# def get_kategori():
#     return jsonify([
#         {
#             'id_kategori': i.id_kategori, 
#             'nama': i.nama, 
#             'deskripsi' : i.deskripsi,
#             # 'books': [x.judul for x in i.books]  
#         } for i in Kategori.query.all()
#     ])

# #GET id Tabel Kategori
# @app.route('/kategori/<id>')
# def get_kategori_id(id):
#     print(id)
#     kategori = Kategori.query.filter_by(id_kategori=id).first_or_404()
#     return {
#         'id': kategori.id_kategori, 
#         'nama': kategori.nama,
#         'deskripsi': kategori.deskripsi
#     }
    
# #CREATE Data di tabel kategori    
# @app.route('/kategori', methods=['POST'])
# def create_kategori():
#     data = request.get_json()
#     if not 'nama' in data or not 'deskripsi' in data :
#         return jsonify({
#             'error': 'Bad Request',
#             'message': 'Nama ata Deskripisi Tidak ada'
#         }), 400
#     k = Kategori (
#                     nama = data['nama'],
#                     deskripsi = data['deskripsi']
#                 )
#     db.session.add(k)
#     db.session.commit()
#     return { 
#         'nama': k.nama,
#         'deskripsi': k.deskripsi
#     }, 201

# #UPDATE data di tabel kategori
# @app.route('/kategori/<id>', methods=['PUT'])
# def update_kategori(id):
#     data=request.get_json()
#     if 'nama' not in data:
#         return {
#             'error': 'Bad Request',
#             'message': 'Name field needs to be present'
#         }, 400
#     k = Kategori.query.filter_by(id_kategori=id).first_or_404()
#     k.nama=data['nama']
#     if 'deskripsi' in data:
#         k.deskripsi= data['deskripsi']
#     db.session.commit()
#     return jsonify({
#         'nama': k.nama,
#         'deskripsi': k.deskripsi
#     })

# #DELETE data di tabel kategori
# @app.route('/kategori/<id>', methods=['DELETE'])
# def delete_kategori(id):
#     k = Kategori.query.filter_by(id_kategori=id).first_or_404()
#     db.session.delete(k)
#     db.session.commit()
#     return {
#         'success': 'Data Berhasil Dihapus'
#     }

# #----------------------------------ENDPOINT TABLE KATEGORI--------------------------------------------------
# # GET All data di tabel buku
# @app.route('/buku')
# def get_buku():
#     a =authen()
#     if a == None:
#         return {
#             "message": "Unauthorize"
#         }, 400
#     # print(a['is_admin'])
#     b = Buku()
#     books = b.query.all()
#     result=[]
#     for i in books:
#         # print(i.judul,i.kategori)
#         result.append({
#             'id_buku': i.id_buku,
#             'judul':i.judul,
#             'tahun':i.tahun,
#             'jumlah hal': i.jumlah_hal,
#             'kategori_id': i.kategori_id,
#             'kategori': i.kategori.nama
#         })
#     return {
#         'result':result  
#     }

# #GET data by id di tabel buku
# @app.route('/buku/<id>')
# def get_buku_id(id):
#     a =authen()
#     if a == None:
#         return {
#             "message": "Unauthorize"
#         }, 400
#     buku = Buku.query.filter_by(id_buku=id).first_or_404()
#     return{
#         'judul': buku.judul,
#         'tahun': buku.tahun,
#         'jumlah_hal': buku.jumlah_hal,
#         'kategori': buku.kategori.nama,
#         'kategori_id': buku.kategori_id
#     }

# #POST data di tabel buku
# @app.route('/buku', methods=["POST"])
# def create_buku():
#     a = authen()
#     if a['role'] != 'admin':
#         return {
#             "message": "Unauthorized"
#         }, 400
#     data = request.get_json()
#     buku = Buku ( judul= data['judul'],
#                  tahun = data['tahun'],
#                  jumlah_hal = data['jumlah_hal']
#                  )
#     db.session.add(buku)
#     db.session.commit()
#     return {
#         'judul': buku.judul,
#         'tahun': buku.tahun,
#         'jumlah_hal': buku.jumlah_hal,
#         'kategori_id': buku.kategori_id
#     }, 201

# #PUT data di tabel buku
# @app.route('/buku/<id>', methods=['PUT'])
# def update_buku(id):
#     a = authen()
#     if a['role']== 'admin':
#         return {
#             "message": "Unauthorized"
#         }, 400
#     data=request.get_json()
#     if 'judul' not in data:
#         return{
#             'error': 'Bad Request',
#              'message': 'Name field needs to great present'
#         }, 400
#     b = Buku.query.filter_by(id_buku=id).first_or_404()
#     b.judul = data['judul']
#     if 'judul' in data:
#         b.judul=data['judul']
#         db.session.commit()
#         return jsonify({
#             'judul': b.judul,
#             'tahun': b.tahun,
#             'jumlah_hal': b.jumlah_hal,
#             'kategori_id': b.kategori_id
#         })


# #DELETE data di tabel buku
# @app.route('/buku/<id>', methods=['DELETE'])
# def delete_buku(id):
#     a = authen()
#     if a['role']== 'admin':
#         return {
#             "message": "Unhauthorized"
#         }, 400
#     b = Buku.query.filter_by(id_buku=id).first_or_404()
#     db.session.delete(b)
#     db.session.commit()
#     return {
#         'success': 'Data berhasil dihapus'
#     }


#                                     #Endpoint Table Penulis

# #----------------------------------ENDPOINT TABLE KATEGORI--------------------------------------------------
# #GET ALL DATA table penulis
# @app.route('/penulis')
# def get_penulis(): 
#     return jsonify([
#         {
#             'id_penulis' : i.id_penulis,
#             'nama': i.nama, 
#             'kearganegaraan': i.kewarganegaraan, 
#             'tahun_kelahiran' : i.tahun_kelahiran  
#         } for i in Penulis.query.all()
#     ])

# #GET DATA BY ID data table Penulis
# @app.route('/penulis/<id>', methods=['GET'])
# def get_penuli_id(id):
#     p = Penulis.query.filter_by(id_penulis=id).first_or_404()
#     return {
#         'nama': p.nama,
#         'kewarganegaraan': p.kewarganegaraan,
#         'tahun_kelahiran': p.tahun_kelahiran
#     }

# #CREATE data pada table Penulis
# @app.route('/penulis', methods=['POST'])
# def create_penulis():
#     data = request.get_json()
#     if not 'nama' in data or not 'kewarganegaraan' in data or not 'tahun_kelahiran' in data :
#         return jsonify({
#             'error': 'Bad Request',
#             'message': 'Data Penulis Tidak ada'
#         }), 400
#     p = Penulis (
#                     nama = data['nama'],
#                     kewarganegaraan = data['kewarganegaraan'],
#                     tahun_kelahiran = data['tahun_kelahiran']
#                     )
#     db.session.add(p)
#     db.session.commit()
#     return { 
#         'nama': p.nama,
#         'kewarganegaraan': p.kewarganegaraan,
#         'tahun_kelahiran': p.tahun_kelahiran
#     }, 201

# #UPDATE data pada table Penulis
# @app.route('/penulis/<id>/', methods=['PUT'])
# def update_penulis(id):
#     data = request.get_json()
#     if 'nama' not in data or 'kewarganegaraan' not in data or 'tahun_kelahiran' not in data:
#         return {
#             'error' : 'Bad Request',
#             'message' : 'Data buku tidak tersedia'
#         }, 400
#     p = Penulis.query.filter_by(id_penulis=id).first_or_404()
#     if 'nama' in data:
#         p.nama = data['nama']
#         db.session.commit()
#         return jsonify ({
#             'nama' : p.nama,
#             'kewarganegaraan': p.kewarganegaraan,
#             'tahun_kelahiran' : p.tahun_kelahiran
#         })

# #DELETE data pada table Penulis
# @app.route('/penulis/<id>', methods= ['DELETE'])
# def delete_penulis(id):
#     p = Penulis.query.filter_by(id_penulis=id).first_or_404()
#     db.session.delete(p)
#     db.session.commit()
#     return {
#         'Success' : 'Data penulis berhasil dihapus'
#     }

# #0-------------------------END POINT TABLE USER---------------------------------------------------

# #GET ALL DATA di table USER
# @app.route('/user', methods=['GET'])
# def get_user():
#     return jsonify([
#         {
#             'id_user' : x.id_user,
#             'username' : x.username,
#             'password' : x.password,
#             'is_admin' : x.is_admin
#         } for x in User.query.all()
#     ])

# #GET Data by ID di table USER
# @app.route('/user/<id>', methods=['GET'])
# def get_user_id(id):
#     u = User.query.filter_by(id_user=id).first_or_404()
#     return {
#         'username' : u.username,
#         'password' : u.password,
#         'is_admin' : u.is_admin
#     }

# #CREATE data di table USER
# @app.route('/user', methods=['POST'])
# def create_user():
#     data = request.get_json()
#     if 'username' not in data.keys() or 'password' not in data.keys():
#         return {
#             'Not Success' : 'Username or Password Must to be Input'
#         }
#     existing_user = User.query.filter_by(username=data['username']).first()
    
#     if existing_user :
#         return {
#             'Failed' : 'Username Already Exist'
#         }, 409
    
#     password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
#     # is_admin = data.get(is_admin, False) #default False jika is_admin tidak disediakan


#     u = User (
#         username = data['username'],
#         password = data['password'],
#         is_admin = data['is_admin'],
#         role_id = 2
#     )
 
#     db.session.add(u)
#     # db.session.commit()
#     return {
#         'Message' : 'User has been Added',
#         'username' : u.username,
#         'is_admin' : u.is_admin,
#         'role_id' : u.role_id
#     }, 201

# #UPDATE Data di table USER
# @app.route('/user/<id>/', methods=['PUT'])
# def update_user(id):
#     data = request.get_json()
#     if 'username' not in data or 'password' not in data :
#         return {
#             'Error' : 'Username Or Password Must be Insert'
#         }, 400
#     u = User.query.filter_by(id_user=id).first_or_404()
#     hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
#     u.username = data['username']
#     u.password = hashed.decode('utf-8')
#     db.session.commit()
#     return jsonify ({
#             "Message": "Data User Hasbeen Updated"
#         })
    
    
# @app.route('/user/<id>', methods=['DELETE'])
# def delete_user(id):
#     user = User.query.filter_by(id_user=id).first_or_404()
#     db.session.delete(user)
#     db.session.commit()
#     return {
#         'Success': 'Data deleted successfully'
#     }



if __name__ == '__main__':
    from blueprints import register_blueprints
    from db import app
    register_blueprints(app)
    app.run(debug=True)