import os
from flask import Flask, jsonify, request

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "v1.0")
DEPLOYMENT_VARIANT = os.getenv("DEPLOYMENT_VARIANT", "stable")

ROUTINES = [
    {"id": 1, "name": "Morning Gym Workout", "category": "Strength"},
    {"id": 2, "name": "Evening Cardio Session", "category": "Cardio"},
]


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "app": "ACEest Fitness & Gym Manager",
        "version": APP_VERSION,
        "variant": DEPLOYMENT_VARIANT,
        "routines_count": len(ROUTINES),
    }), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "UP",
        "version": APP_VERSION,
        "variant": DEPLOYMENT_VARIANT,
    }), 200


@app.route("/routines", methods=["GET"])
def get_routines():
    return jsonify({
        "version": APP_VERSION,
        "variant": DEPLOYMENT_VARIANT,
        "routines": ROUTINES,
    }), 200


@app.route("/routines", methods=["POST"])
def add_routine():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    category = (data.get("category") or "General").strip()

    if not name:
        return jsonify({"error": "Routine name is required"}), 400

    new_routine = {
        "id": len(ROUTINES) + 1,
        "name": name,
        "category": category,
    }
    ROUTINES.append(new_routine)
    return jsonify({
        "message": "Routine added",
        "version": APP_VERSION,
        "routine": new_routine,
    }), 201


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
