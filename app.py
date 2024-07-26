from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Optional, for cross-origin requests
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://wellness_retreat_platform_user:wlxOUVlEKAXdVAzofVzKJAU0QiQKaY1E@dpg-cqhrvbggph6c73c9h1s0-a.singapore-postgres.render.com/wellness_retreat_platform"

# postgresql://wellness_retreat_platform_user:wlxOUVlEKAXdVAzofVzKJAU0QiQKaY1E@dpg-cqhrvbggph6c73c9h1s0-a.singapore-postgres.render.com/wellness_retreat_platform
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Optional: Enable CORS if accessing from different domains
CORS(app)


class Retreats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric(10, 0), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    condition = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    tag = db.Column(db.ARRAY(db.String), nullable=False)
    duration = db.Column(db.Integer, nullable=False)


class Bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(255), nullable=False)
    user_name = db.Column(db.String(255), nullable=False)
    user_email = db.Column(db.String(255), nullable=False)
    user_phone = db.Column(db.String(20))
    retreat_id = db.Column(db.Integer, db.ForeignKey("retreats.id"))
    retreat = db.relationship("Retreats", backref=db.backref("bookings", lazy=True))
    retreat_title = db.Column(db.String(255), nullable=False)
    retreat_location = db.Column(db.String(255), nullable=False)
    retreat_price = db.Column(db.Numeric(10, 2), nullable=False)
    retreat_duration = db.Column(db.Integer, nullable=False)
    payment_details = db.Column(db.Text, nullable=False)
    booking_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    __table_args__ = (
        db.UniqueConstraint("user_id", "retreat_id", name="_user_retreat_uc"),
    )


@app.route("/retreats", methods=["GET"])
def get_retreats():
    try:
        page = request.args.get("page", 1, type=int)
        limit = request.args.get("limit", 10, type=int)
        per_page = request.args.get("per_page", None, type=int)
        search = request.args.get("search", "")
        location = request.args.get("location", "")
        filter_term = request.args.get("filter", "")

        # Cap the limit to a reasonable number
        limit = min(limit, 100)
        
        # Return 404 if 'per_page' is used instead of 'limit'
        if per_page is not None:
            return jsonify("Not found"), 404

        # Validate page and limit parameters
        if page < 1 or limit < 1:
            return jsonify({"error": "Invalid page or limit"}), 400

        query = Retreats.query
        if search:
            query = query.filter(
                db.or_(
                    Retreats.title.ilike(f"%{search}%"),
                    Retreats.description.ilike(f"%{search}%"),
                    Retreats.location.ilike(f"%{search}%"),
                    db.func.array_position(Retreats.tag, search) > 0  # PostgreSQL array position check
                )
            )
        if location:
            query = query.filter(Retreats.location.ilike(f"%{location}%"))
        if filter_term:
            query = query.filter(Retreats.description.ilike(f"%{filter_term}%"))

        retreat = query.paginate(page=page, per_page=limit, error_out=False)
        if retreat.total > 0:
            return jsonify(
                [
                    {
                        "id": str(r.id),
                        "title": r.title,
                        "description": r.description,
                        "date": r.date,
                        "location": r.location,
                        "price": r.price,
                        "type": r.type,
                        "condition": r.condition,
                        "image": r.image,
                        "tag": r.tag,
                        "duration": r.duration,
                    }
                    for r in retreat.items
                ]
            )
        else:
            return jsonify({"error": "No retreats found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/book", methods=["POST"])
def create_booking():
    data = request.json

    required_fields = [
        "user_id",
        "user_name",
        "user_email",
        "user_phone",
        "retreat_id",
        "retreat_title",
        "retreat_location",
        "retreat_price",
        "retreat_duration",
        "payment_details",
        "booking_date",
    ]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    user_id = data.get("user_id")
    retreat_id = data.get("retreat_id")

    if not Retreats.query.get(retreat_id):
        return jsonify({"error": "Retreat not found"}), 404

    if Bookings.query.filter_by(user_id=user_id, retreat_id=retreat_id).first():
        return jsonify({"error": "Retreat already booked by user"}), 400

    try:
        booking_date = datetime.fromisoformat(data.get("booking_date"))
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400

    try:
        booking = Bookings(
            user_id=user_id,
            user_name=data.get("user_name"),
            user_email=data.get("user_email"),
            user_phone=data.get("user_phone"),
            retreat_id=retreat_id,
            retreat_title=data.get("retreat_title"),
            retreat_location=data.get("retreat_location"),
            retreat_price=data.get("retreat_price"),
            retreat_duration=data.get("retreat_duration"),
            payment_details=data.get("payment_details"),
            booking_date=booking_date,
        )

        db.session.add(booking)
        db.session.commit()

        return jsonify({"message": "Booking created successfully"}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
