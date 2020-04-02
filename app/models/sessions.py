from main import db


class SessionsModel(db.Model):
    __tablename__ = 'sessions'
    id = db.Column(db.Integer, primary_key=True)
    concept_title = db.Column(db.String, nullable=False)
    concept_link = db.Column(db.String, nullable=False)
    bootcamp_id = db.Column(db.Integer, db.ForeignKey('bootcamps.id'))
    bootcamp_url = db.Column(db.String, nullable=False)


    # Add Section
    def new_section(self):
        db.session.add(self)
        db.session.commit()
    
    
    @classmethod
    def get_bootcamp_by_bootcamp_id(cls, bootcamp_id):
        return cls.query.filter_by(bootcamp_id=bootcamp_id).all()