from app.extension import db


class RentPayment(db.Model):
    __tablename__ = "rent_payments"

    id = db.Column(db.Integer, primary_key=True)
    caretaker_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    tenant_id = db.Column(db.Integer, db.ForeignKey("tenants.id"), nullable=False)
    unit_id = db.Column(db.Integer, db.ForeignKey("units.id"), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    method = db.Column(db.String(20), nullable=False, default="cash")  # "cash" or "mpesa"
    reference = db.Column(db.String(100))
    period_month = db.Column(db.Date, nullable=False)  # first day of the month being paid for
    paid_at = db.Column(db.DateTime, server_default=db.func.now())