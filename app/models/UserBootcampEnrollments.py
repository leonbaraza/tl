from main import db


class UserBootcampEnrollmentModel(db.Model):
    __tablename__ = 'user_bootcamp_enrollments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    bootcamp_id = db.Column(db.Integer, db.ForeignKey('bootcamps.id'))

    enrollPaymentsModel = db.relationship('EnrollPaymentsModel', backref="user_bootcamp_enrollments")

    # add new users
    def newUsers(self):
        db.session.add(self)
        db.session.commit()

    # User Bootcamp enrollmants
    @classmethod
    def get_user_bootcamp_enrollment(cls, user_id):
        return cls.query.filter_by(user_id=user_id).first()
