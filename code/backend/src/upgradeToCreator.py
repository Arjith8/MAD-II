from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import UserInfo,db

class upgradeToCreator(Resource):
    @jwt_required()
    def post(self):
        data = get_jwt_identity()
        user_id = data['data']["user_id"]
        user = UserInfo.query.filter_by(user_id=user_id).one()
        user.account_type = "creator"
        db.session.commit()
        return {
            "success":True,
        }
        
