import numpy as np

def loadObj(fileName):
    vertices = []
    faces = []
    min_bound = [float("inf")] * 3
    max_bound = [-float("inf")] * 3

    with open(f"data/maps/{fileName}.obj", "r") as f:
        for line in f:
            if line.startswith("v "):
                parts = line.split()
                v = [float(parts[1]), float(parts[2]), float(parts[3])]
                vertices.append(v)

                for i in range(3):
                    min_bound[i] = min(min_bound[i], v[i])
                    max_bound[i] = max(max_bound[i], v[i])

            elif line.startswith("f "):
                parts = line.split()
                face = [int(p.split("/")[0]) - 1 for p in parts[1:]]
                faces.append(face)

    vertices = np.array(vertices, dtype="f4")
    return vertices, faces