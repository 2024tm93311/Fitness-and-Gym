from flask import Flask, jsonify, request, abort

def create_app():
    app = Flask(__name__)

    # In-memory store to keep the example simple
    app.config["MEMBERS"] = {}
    app.config["NEXT_ID"] = 1
    app.config["SERVICE_NAME"] = "ACEest Fitness & Gym API"
    app.config["VERSION"] = "1.0.0"

    @app.get("/")
    def index():
        return jsonify({
            "service": app.config["SERVICE_NAME"],
            "version": app.config["VERSION"],
            "status": "ok"
        }), 200

    @app.get("/health")
    def health():
        return "OK", 200

    @app.post("/bmi")
    def bmi():
        data = request.get_json(silent=True) or {}
        try:
            weight = float(data["weight_kg"])
            height_cm = float(data["height_cm"])
        except Exception:
            abort(400, description="Invalid input. Provide 'weight_kg' and 'height_cm' as numbers.")

        if weight <= 0 or height_cm <= 0:
            abort(400, description="Values must be positive.")

        height_m = height_cm / 100.0
        bmi_value = round(weight / (height_m ** 2), 2)

        if bmi_value < 18.5:
            category = "Underweight"
        elif bmi_value < 25:
            category = "Normal"
        elif bmi_value < 30:
            category = "Overweight"
        else:
            category = "Obese"

        return jsonify({"bmi": bmi_value, "category": category}), 200

    @app.get("/members")
    def list_members():
        return jsonify(list(app.config["MEMBERS"].values())), 200

    @app.post("/members")
    def add_member():
        data = request.get_json(silent=True) or {}
        name = data.get("name")
        age = data.get("age")
        if not name or not isinstance(name, str):
            abort(400, description="Field 'name' is required and must be a string.")
        if age is None:
            abort(400, description="Field 'age' is required.")
        try:
            age = int(age)
        except Exception:
            abort(400, description="'age' must be an integer.")

        member_id = app.config["NEXT_ID"]
        app.config["NEXT_ID"] += 1
        member = {"id": member_id, "name": name.strip(), "age": age}
        app.config["MEMBERS"][member_id] = member
        return jsonify(member), 201

    return app

# Expose "app" for WSGI servers (e.g., gunicorn)
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
