from app import app, db, Retreats, Bookings

# Sample data
retreats = [
    Retreats(
        id=1,
        title="Yoga for Stress Relief",
        description="A weekend retreat focused on yoga and meditation to relieve stress.",
        date=1692921600,
        location="Goa",
        price=200,
        type="Signature",
        condition="Stress Relief",
        image="https://cdn.midjourney.com/a287f9bc-d0fb-4e78-a0fa-e8136d3c408a/0_0.jpeg",
        tag=["relaxation", "meditation", "weekend"],
        duration=3,
    ),
    Retreats(
        id=2,
        title="Flexibility Improvement Workshop",
        description="A 5-day workshop designed to improve flexibility through yoga.",
        date=1694304000,
        location="Rishikesh",
        price=500,
        type="Standalone",
        condition="Flexibility Improvement",
        image="https://cdn.midjourney.com/4eef5d57-1601-4b80-8e82-523003e9f95d/0_0.jpeg",
        tag=["flexibility", "yoga", "workshop"],
        duration=5,
    ),
    Retreats(
        id=3,
        title="Weight Loss Retreat",
        description="A 7-day retreat focused on weight loss through yoga and diet.",
        date=1696118400,
        location="Kerala",
        price=700,
        type="Signature",
        condition="Weight Loss",
        image="https://cdn.midjourney.com/bc82ebc6-a3a4-4eda-be0b-bb3e65d4b8d3/0_1.jpeg",
        tag=["weight loss", "diet", "yoga"],
        duration=7,
    ),
    Retreats(
        id=4,
        title="General Fitness Yoga Camp",
        description="A 3-day yoga camp to enhance overall fitness and well-being.",
        date=1694736000,
        location="Mumbai",
        price=300,
        type="Standalone",
        condition="General Fitness",
        image="https://cdn.midjourney.com/930ec767-aa6d-46e6-92a6-f019a9718304/0_3.jpeg",
        tag=["fitness", "yoga", "camp"],
        duration=3,
    ),
    Retreats(
        id=5,
        title="Chronic Pain Management",
        description="A weekend retreat to manage chronic pain through specialized yoga techniques.",
        date=1700438400,
        location="Delhi",
        price=250,
        type="Signature",
        condition="Chronic Pain Management",
        image="https://cdn.midjourney.com/5b0cec06-2f37-4828-8602-316f6dbd0eb6/0_0.jpeg",
        tag=["pain management", "yoga", "weekend"],
        duration=2,
    ),
]

bookings = [
    Bookings(
        user_id="user001",
        user_name="Alice Johnson",
        user_email="alice@example.com",
        user_phone="1234567890",
        retreat_id=1,
        retreat_title="Yoga for Stress Relief",
        retreat_location="Goa",
        retreat_price=200,
        retreat_duration=3,
        payment_details="Credit card payment",
        booking_date="2024-08-01 10:00:00"
    ),
    Bookings(
        user_id="user002",
        user_name="Bob Smith",
        user_email="bob@example.com",
        user_phone="0987654321",
        retreat_id=2,
        retreat_title="Flexibility Improvement Workshop",
        retreat_location="Rishikesh",
        retreat_price=500,
        retreat_duration=5,
        payment_details="Credit card payment",
        booking_date="2024-08-05 15:00:00"
    ),
    Bookings(
        user_id="user003",
        user_name="Charlie Brown",
        user_email="charlie@example.com",
        user_phone="1122334455",
        retreat_id=3,
        retreat_title="Weight Loss Retreat",
        retreat_location="Kerala",
        retreat_price=700,
        retreat_duration=7,
        payment_details="Credit card payment",
        booking_date="2024-08-10 09:00:00"
    ),
]

with app.app_context():
    db.session.add_all(retreats)
    db.session.add_all(bookings)
    db.session.commit()
    print("Sample data inserted successfully!")
