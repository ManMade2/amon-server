from flask import Blueprint, request, jsonify
from amon_server.nav import visualizeMesh
from jsonschema import validate, ValidationError
from ..validation.debug_mesh_schema import debug_mesh_schema


navigation_blueprint = Blueprint('navigation', __name__)


@navigation_blueprint.route('/debug-mesh', methods=['POST'])
def debug_mesh():

    try:
        data = request.get_json()
        validate(instance=data, schema=debug_mesh_schema)
    except ValidationError as e:
        return jsonify({"error": f"Invalid input: {e.message}"}), 400
    
    mesh = visualizeMesh(data["modelName"], data["simplifyBy"], data["maxSlope"])
    return jsonify(mesh)


@navigation_blueprint.route('/create-mesh', methods=['POST'])
def create_mesh():
    return f''


@navigation_blueprint.route('/get-path', methods=['GET'])
def get_path():
    return "navigation returned"