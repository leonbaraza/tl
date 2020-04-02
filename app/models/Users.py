from main import db

class UsersModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firebase_id = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    # relationships
    userBootcampEnrollmentModel = db.relationship('UserBootcampEnrollmentModel', backref="users")
    contactModel = db.relationship('ContactModel', backref="users")


    # add new users
    def newUsers(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_users(cls):
        return cls.query.all()

    @classmethod
    def get_user_by_email(cls,email):
        return cls.query.filter_by(email=email).first()
