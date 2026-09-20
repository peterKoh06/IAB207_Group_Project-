from datetime import datetime, timedelta, timezone

from website import create_app, db
from website.models import Booking, Comment, Event, EventOffering, Offering, User


app = create_app()


with app.app_context():
	db.drop_all()
	db.create_all()

	users = [
		User(
			first_name="Ava",
			last_name="Nguyen",
			email="ava.nguyen@example.com",
			phone_number="0400000001",
			password_hash="PLACEHOLDER_PASSWORD",
		),
		User(
			first_name="Liam",
			last_name="Patel",
			email="liam.patel@example.com",
			phone_number="0400000002",
			password_hash="PLACEHOLDER_PASSWORD",
		),
		User(
			first_name="Mia",
			last_name="Thompson",
			email="mia.thompson@example.com",
			phone_number="0400000003",
			password_hash="PLACEHOLDER_PASSWORD",
		),
		User(
			first_name="Noah",
			last_name="Williams",
			email="noah.williams@example.com",
			phone_number="0400000004",
			password_hash="PLACEHOLDER_PASSWORD",
		),
	]
	db.session.add_all(users)
	db.session.flush()

	offerings = [
		Offering(name="alcohol"),
		Offering(name="peanuts"),
		Offering(name="seafood"),
	]
	db.session.add_all(offerings)
	db.session.flush()

	current_time = datetime.now(timezone.utc)
	loremIpsum = "Distinctio et sed voluptatum totam reiciendis doloremque amet modi. Repellat numquam non vel incidunt. Est nam praesentium molestiae ut. Accusamus ut quia animi voluptatem aut."
	events = [
		Event(
			host_id=users[0].id,
			phone_number=users[0].phone_number,
			name="Food Festival",
			description=loremIpsum,
			time=current_time + timedelta(days=7),
			tickets=150,
			cancelled=False,
		),
		Event(
			host_id=users[1].id,
			phone_number=users[1].phone_number,
			name="Ultimate Danceoff 2026",
			description=loremIpsum,
			time=current_time + timedelta(days=10),
			tickets=24,
			cancelled=False,
		),
		Event(
			host_id=users[2].id,
			phone_number=users[2].phone_number,
			name="Dinner",
			description=loremIpsum,
			time=current_time + timedelta(days=14),
			tickets=5,
			cancelled=False,
		),
		Event(
			host_id=users[3].id,
			phone_number=users[3].phone_number,
			name="Community Picnic",
			description=loremIpsum,
			time=current_time + timedelta(days=18),
			tickets=80,
			cancelled=False,
		),
		Event(
			host_id=users[0].id,
			phone_number=users[0].phone_number,
			name="Ball",
			description=loremIpsum,
			time=current_time + timedelta(days=21),
			tickets=30,
			cancelled=True,
		),
	]
	db.session.add_all(events)
	db.session.flush()

	events[0].offerings = [
		EventOffering(offering_id=offerings[0].id),
		EventOffering(offering_id=offerings[2].id),
	]
	events[1].offerings = [
		EventOffering(offering_id=offerings[1].id),
	]
	events[2].offerings = [
		EventOffering(offering_id=offerings[0].id),
		EventOffering(offering_id=offerings[2].id),
	]
	events[3].offerings = [
		EventOffering(offering_id=offerings[1].id),
	]
	events[4].offerings = [
		EventOffering(offering_id=offerings[0].id),
	]

	comments = [
		Comment(
			user_id=users[1].id,
			event_id=events[0].id,
			timestamp=current_time - timedelta(hours=5),
			content="Nostrum laborum modi nemo quia porro qui.",
		),
		Comment(
            user_id=users[1].id,
            event_id=events[0].id,
            timestamp=current_time - timedelta(hours=5),
            content="Facere voluptas eos assumenda et voluptate minus cumque eaque.",
                ),
		Comment(
			user_id=users[2].id,
			event_id=events[1].id,
			timestamp=current_time - timedelta(hours=3),
			content="Looking forward to this workshop.",
		),
		Comment(
			user_id=users[3].id,
			event_id=events[2].id,
			timestamp=current_time - timedelta(hours=1),
			content="Can't wait!",
		),
	]
	db.session.add_all(comments)

	bookings = [
		Booking(
			user_id=users[1].id,
			event_id=events[0].id,
			timestamp=current_time - timedelta(days=2),
			tickets=2,
		),
		Booking(
			user_id=users[2].id,
			event_id=events[1].id,
			timestamp=current_time - timedelta(days=1),
			tickets=1,
		),
		Booking(
			user_id=users[3].id,
			event_id=events[2].id,
			timestamp=current_time - timedelta(hours=12),
			tickets=4,
		),
	]
	db.session.add_all(bookings)

	db.session.commit()