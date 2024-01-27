from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin
from flask_bcrypt import Bcrypt
from sqlalchemy.ext.hybrid import hybrid_property

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    serialize_rules = ("-produce_reviews.user",)

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String())

    produce_reviews = db.relationship('ProduceReview', backref="user")

    def __repr__(self):
        return f'<User: {self.username}>'

    @hybrid_property
    def password_hash(self):
        raise AttributeError("Not allowed")

    @password_hash.setter
    def password_hash(self, password):
        self._password_hash = bcrypt.generate_password_hash(password).decode("utf-8")

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode("utf-8"))


class ProduceEntry(db.Model, SerializerMixin):
    __tablename__ = "produce_entries"

    serialize_rules = ("-produce_genres.produce_entry", "-produce_reviews.produce_entry",)

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    growing_location = db.Column(db.String(), nullable=False)
    image_url = db.Column(db.String(255))
    description = db.Column(db.String(100))

    produce_genres = db.relationship('ProduceGenre', backref='produce_entry')
    produce_reviews = db.relationship('ProduceReview', backref='produce_entry')

    def __repr__(self):
        return f'Produce: {self.title}, Location: {self.growing_location}'


class ProduceReview(db.Model, SerializerMixin):
    __tablename__ = 'produce_reviews'

    serialize_rules = ("-user.produce_reviews", "-produce_entry.produce_reviews",)

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer())
    comment = db.Column(db.String())
    date = db.Column(db.DateTime, default=datetime.now)

    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    produce_entry_id = db.Column(db.Integer(), db.ForeignKey('produce_entries.id'))

    def __repr__(self):
        return f'<Review: \n Score: {self.rating}, Comment: {self.comment}>'


class ProduceGenre(db.Model, SerializerMixin):
    __tablename__ = "produce_genres"

    serialize_rules = ("-produce_entry.produce_genres", "-genre.produce_genres",)

    id = db.Column(db.Integer, primary_key=True)
    produce_entry_id = db.Column(db.Integer(), db.ForeignKey('produce_entries.id'))
    genre_id = db.Column(db.Integer(), db.ForeignKey('genres.id'))


class Genre(db.Model, SerializerMixin):
    __tablename__ = "genres"

    serialize_rules = ("-produce_genres.genre",)

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String, nullable=False)

    produce_genres = db.relationship('ProduceGenre', backref='genre')

    def __repr__(self):
        return f'<Genre: {self.name}>'
