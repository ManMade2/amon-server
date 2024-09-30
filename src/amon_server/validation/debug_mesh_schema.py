debug_mesh_schema={
    "type": "object",
    "properties": {
        "modelName":  {"type": "string"},
        "maxSlope": {"type": "number", "minimum": 0, "maximum": 200},
        "simplifyBy": {"type": "number", "minimum": 0.1, "maximum": 0.99},
    },
    "required": ["modelName", "maxSlope", "simplifyBy"],
    "additionalProperties": False
}