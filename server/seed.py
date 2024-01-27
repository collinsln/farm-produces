from faker import Faker
import random
from random import choice as rc
from app import app
from models import db, User, ProduceEntry, ProduceGenre, ProduceReview, Genre

fake = Faker()

with app.app_context():
    # Begin with deleting existing data
    User.query.delete()
    ProduceEntry.query.delete()
    ProduceGenre.query.delete()
    ProduceReview.query.delete()
    Genre.query.delete()

    users = []

    for _ in range(20):
        user = User(
            username=fake.user_name(),
            email=fake.email()
        )
        users.append(user)

    db.session.add_all(users)

    # Produce Types (Genres)
    produce_types = [
        "Fruits",
        "Vegetables",
        "Grains",
        "Dairy",
        "Meat",
        "Herbs",
        "Nuts",
        "Legumes",
        "Root Vegetables",
        "Exotic Produce"
    ]

    produce_genres = []

    for produce_type in produce_types:
        genre = Genre(
            name=produce_type
        )
        produce_genres.append(genre)

    db.session.add_all(produce_genres)

    # List of 10 farm produce titles
    produce_titles = [
        "Apples",
        "Tomatoes",
        "Wheat",
        "Milk",
        "Chicken",
        "Basil",
        "Almonds",
        "Lentils",
        "Potatoes",
        "Dragon Fruit"
    ]

    # List of corresponding growing locations
    produce_locations = [
        "Orchard", "Greenhouse", "Field", "Farm",
    ]

    produce_entries = []

    image_urls = [
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRj7tCxShYKR6DbUrS68GWsXmgoMA_pz0YBHw&usqp=CAU",
        "https://example.com/tomato.jpg",
        "https://example.com/wheat.jpg",
        "https://example.com/milk.jpg",
        "https://example.com/chicken.jpg",
        "https://example.com/basil.jpg",
        "https://example.com/almonds.jpg",
        "https://example.com/lentils.jpg",
        "https://example.com/potatoes.jpg",
        "https://example.com/dragonfruit.jpg",
    ]

    for _ in range(20):
        produce_entry = ProduceEntry(
            title=rc(produce_titles),
            growing_location=rc(produce_locations),
            image_url=rc(image_urls),
            description=fake.sentence(15),
            # user=rc(users),
            # genre=rc(produce_genres)
        )

        produce_entries.append(produce_entry)

    db.session.add_all(produce_entries)

    produce_reviews = []

    for _ in range(20):
        random_user = rc(users)
        random_produce_entry = rc(produce_entries)

        produce_review = ProduceReview(
            rating=random.randint(0, 10),
            comment=fake.sentence(),
            user=random_user,
            produce_entry=random_produce_entry
        )

        produce_reviews.append(produce_review)

    db.session.add_all(produce_reviews)

    # Create ProduceGenre instances using the existing produce_entries and produce_genres
    if produce_entries and produce_genres:
        produce_genre_instances = []

        for _ in range(20):
            produce_genre_instance = ProduceGenre(
                produce_entry=rc(produce_entries),
                genre=rc(produce_genres)
            )
            produce_genre_instances.append(produce_genre_instance)

        db.session.add_all(produce_genre_instances)

    db.session.commit()
