from main import db


class BootcampSessionModel(db.Model):
    __tablename__ = 'bootcamp_sessions'
    id = db.Column(db.Integer, primary_key=True)
    bootcamp_id = db.Column(db.Integer, db.ForeignKey('bootcamps.id'))
    stream_url = db.Column(db.String, nullable=False)
    concept_title = db.Column(db.String, nullable=False)
    concept_url = db.Column(db.String, nullable=False)
    session_time = db.Column(db.String, nullable=False)

    # add new users
    def new_bootcamp_session(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_bootcamp_session(cls):
        return cls.query.all()

    @classmethod
    def get_bootcamp_session_by_id(cls, id):
        return cls.query.filter_by(bootcamp_id=id).first()
