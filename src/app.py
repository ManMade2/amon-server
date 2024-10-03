from amon_server import create_app
from flask_cors import CORS
from flask_compress import Compress


app = create_app()
Compress(app)
CORS(app)

if __name__ == "__main__":
    app.run(debug=True, port=5002)