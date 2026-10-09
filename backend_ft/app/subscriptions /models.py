from app.extension import db


class Subscription(db.Model):
    __tablename__ = "subscriptions"

    id = db.Column(db.Integer, primary_key=True)
    caretaker_id = db.Column(db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="active")  # "active" or "expired"
    created_at = db.Column(db.DateTime, server_default=db.func.now())


class SubscriptionPayment(db.Model):
    __tablename__ = "subscription_payments"

    id = db.Column(db.Integer, primary_key=True)
    subscription_id = db.Column(db.Integer, db.ForeignKey("subscriptions.id"), nullable=False)
    caretaker_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    reference = db.Column(db.String(100), unique=True, nullable=False)  # KCB transaction reference
    paid_at = db.Column(db.DateTime, server_default=db.func.now())