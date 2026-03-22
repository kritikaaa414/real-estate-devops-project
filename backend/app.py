import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask, jsonify
from flask_cors import CORS
from database import db, init_db
from models import Property

app = Flask(__name__)
CORS(app)

# Init DB
init_db(app)

# Create tables (important for first run)
with app.app_context():
    db.create_all()

# API route
@app.route('/properties', methods=['GET'])
def get_properties():
    properties = Property.query.all()

    result = []
    for p in properties:
        result.append({
            "title": p.title,
            "location": p.location,
            "price": p.price,
            "image": p.image
        })

    return jsonify(result)

# Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
