from . import db
from datetime import datetime, timezone
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "Users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), index=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(70), nullable=False)

class Event(db.Model):
    __tablename__ = "Events"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    host_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    phone_number = db.Column(db.String(20))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    tickets = db.Column(db.Integer, nullable=False)
    cancelled = db.Column(db.Boolean, nullable=False)

    host_user = db.relationship('User', backref='hosted_events')


class Offering(db.Model):
    __tablename__ = "Offerings"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)

class EventOffering(db.Model):
    __tablename__ = "EventOfferings"
    event_id = db.Column(db.Integer, db.ForeignKey('Events.id'), primary_key=True)
    offering_id = db.Column(db.Integer, db.ForeignKey('Offerings.id'), primary_key=True)

    event = db.relationship('Event', backref='offerings')
    offering = db.relationship('Offering', backref='events')

class Comment(db.Model):
    __tablename__ = "Comments"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('Events.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)
    content = db.Column(db.Text, nullable=False)

    user = db.relationship('User', backref='comments')
    event = db.relationship('Event', backref='comments')

class Booking(db.Model):
    __tablename__ = "Bookings"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('Events.id'), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    tickets = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', backref='bookings')
    event = db.relationship('Event', backref='bookings')