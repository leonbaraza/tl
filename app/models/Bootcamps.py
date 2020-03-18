from main import db


class BootcampsModel(db.Model):
    __tablename__ = 'bootcamps'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    requirements = db.Column(db.String, nullable=False)
    dates = db.Column(db.Date, nullable=False)
    fee = db.Column(db.String, nullable=False)
    provisions = db.Column(db.String, nullable=False)

    # Relationships
    bootcampSessionModel = db.relationship('BootcampSessionModel', backref="bootcamps")
    userBootcampEnrollmentModel = db.relationship('UserBootcampEnrollmentModel', backref="bootcamps")


    def new_bootcamp(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_bootcampa(cls):
        return cls.query.all()

    @classmethod
    def get_bootcamp_by_title(cls,title):
        return cls.query.filter_by(title=title).first()

    @classmethod
    def get_bootcamp_by_id(cls, id):
        return cls.query.filter_by(id=id).first()