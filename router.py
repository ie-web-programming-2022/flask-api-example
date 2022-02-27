from flask import Flask, jsonify, request
import service

router = Flask(__name__)

@router.route("/users")
def users():
    return jsonify(service.get_users())


@router.route("/users/<user_id>")
def user(user_id):
    user = service.get_user(user_id);
    if not user:
        return jsonify({ "errorMessage": 'User Not Found' }), 404
    else:
        return jsonify(user)
    
@router.route("/users", methods=["POST"])
def create_user():
    try:
        user = service.create_user(request.json());
        return jsonify(user)
    except:
        return jsonify({ "errorMessage": 'User Already Exists' }), 404

@router.route("/users/clear", methods=["POST"])
def clear_users():
    return jsonify(service.clear_users())


if __name__ == "__main__":
    router.run()