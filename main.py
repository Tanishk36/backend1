from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/bfhl", methods=["POST"])
def handle_post():
    try:
        data = request.get_json()
        name = data.get("name", "unknown").lower().replace(" ", "_")
        dob = data.get("dob", "01011970").replace("-", "")  # Default if not provided
        user_id = f"{name}_{dob}"
        
        numbers = []
        alphabets = []
        
        for item in data.get("data", []):
            if isinstance(item, int) or (isinstance(item, str) and item.isdigit()):
                numbers.append(str(item))
            elif isinstance(item, str) and item.isalpha():
                alphabets.append(item)
        
        highest_alphabet = [max(alphabets, key=str.lower)] if alphabets else []
        
        response = {
            "is_success": True,
            "user_id": user_id,
            "email": data.get("email", "unknown"),
            "roll_number": data.get("roll_number", "unknown"),
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route("/bfhl", methods=["GET"])
def handle_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == "__main__":
    app.run(debug=True)
