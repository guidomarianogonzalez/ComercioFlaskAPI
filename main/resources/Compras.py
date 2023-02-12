from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import CompraModel

class Compra(Resource):
        
    def get(self, id):
        compra = db.session.query(CompraModel).get_or_404(id)
        try:
            return compra.to_json()
        except:
            return "Resource not found", 404


    def put(self, id):
        compra = db.session.query(CompraModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(compra, key, value)
            try:
                db.session.add(compra)
                db.session.commit()
                return compra.to_json(), 201
            except:
                return '', 404

    def delete(self, id):
        compra = db.session.query(CompraModel).get_or_404(id)
        try:
            db.session.delete(compra)
            db.session.commit()
        except:
            return '', 404

class Compras(Resource):

    def post(self):
        compra = CompraModel.from_json(request.get_json())
        db.session.add(compra)
        db.session.commit()
        return compra.to_json(), 201

    def get(self):
    
        compras = db.session.query(CompraModel)
        return jsonify({
            'compras': [compra.to_json() for compra in compras.items]
        })
    


