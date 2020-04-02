from main import db


class SectionModel(db.Model):
    __tablename__ = 'sections'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    bootcamp_id = db.Column(db.Integer, db.ForeignKey('bootcamps.id'))

    conceptModel = db.relationship('ConceptModel', backref="sections")


    # Add Section
    def new_section(self):
        db.session.add(self)
        db.session.commit()


    # get all sections
    @classmethod
    def all_sections(cls):
        return cls.query.all()


    # get session by id
    @classmethod
    def get_session_by_id(cls, id):
        return cls.query.filter_by(id=id).all()
    

    # get session by id
    @classmethod
    def get_session_by_bootcamp_id(cls, bootcamp_id):
        return cls.query.filter_by(bootcamp_id=bootcamp_id).all()