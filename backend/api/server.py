from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient

# Initialize Flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow CORS from any origin

# MongoDB connection
client = MongoClient('localhost', 27017)
db = client['biovariant']  # Ensure this is the correct database name
collection = db['variants']

# Route to fetch the entire list of variants
@app.route('/variants', methods=['GET'])
def get_variants():
    # Fetch all variants from MongoDB
    variants = list(collection.find({}, {'_id': 0}))  # Exclude the _id field in the response
    return jsonify(variants), 200

# Route to fetch a variant by position
@app.route('/variant/<int:position>', methods=['GET'])
def get_variant_by_position(position):
    # Search for a variant by its position in MongoDB
    variant = collection.find_one({"position": position}, {'_id': 0})  # Exclude the _id field
    if variant:
        return jsonify(variant), 200
    return jsonify({"error": "Variant not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=5001)
