import trimesh
import numpy as np

from .assets import loadObj

def _simplify_mesh(vertices, faces, reduction:float):
    mesh = trimesh.Trimesh(vertices, faces)
    simplified_mesh = mesh.simplify_quadric_decimation(percent=reduction)
    return simplified_mesh.vertices, simplified_mesh.faces

def _is_walkable(face, vertices, maxSlope:int) -> bool:
    v0, v1, v2 = vertices[face[0]], vertices[face[1]], vertices[face[2]]

    normal = np.cross(v1 - v0, v2 - v0)
    normal = normal / np.linalg.norm(normal)

    return np.abs(normal[1]) > np.cos(np.radians(maxSlope))

def _generate_navmesh(vertices, faces, maxSlope):
    walkable_faces = [face for face in faces if _is_walkable(face, vertices, maxSlope)]
    return walkable_faces

def _createVertex(vertices: trimesh.caching.TrackedArray, indices: list[int]):
    v1 = vertices[indices[0]]
    v2 = vertices[indices[1]]
    v3 = vertices[indices[2]]

    x = (float(v1[0]), float(v1[1]), float(v1[2]))
    y = (float(v2[0]), float(v2[1]), float(v2[2]))
    z = (float(v3[0]), float(v3[1]), float(v3[2]))

    return (x, y, z)

def visualizeMesh(fileName: str, reduction:float, maxSlope: int):
    vertices, faces = loadObj(fileName)
    simpleVerticies, simpleFaces = _simplify_mesh(vertices, faces, reduction)
    walkable_faces = _generate_navmesh(simpleVerticies, simpleFaces, maxSlope)

    visualMesh = []
    for face in walkable_faces:
        vert = _createVertex(simpleVerticies, face)
        visualMesh.append(vert)

    return visualMesh