from app.extension import db


class Unit(db.Model):
    __tablename__ = "units"
    __table_args__ = (db.UniqueConstraint("caretaker_id", "unit_number"),)

    id = db.Column(db.Integer, primary_key=True)
    caretaker_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    unit_number = db.Column(db.String(50), nullable=False)
    rent_amount = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.String(20), nullable=False, default="vacant")  # "vacant" or "occupied"
    created_at = db.Column(db.DateTime, server_default=db.func.now())


class Tenant(db.Model):
    __tablename__ = "tenants"

    id = db.Column(db.Integer, primary_key=True)
    caretaker_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    unit_id = db.Column(db.Integer, db.ForeignKey("units.id"), nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    move_in_date = db.Column(db.Date)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())