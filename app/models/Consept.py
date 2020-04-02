from main import db


class ConceptModel(db.Model):
    __tablename__ = 'concepts'
    id = db.Column(db.Integer, primary_key=True)
    concept = db.Column(db.String, nullable=False)

    section_id = db.Column(db.Integer, db.ForeignKey('sections.id'))

    # Add Concept
    def new_concept(self):
        db.session.add(self)
        db.session.commit()


    # get all Concepts
    @classmethod
    def all_concepts(cls):
        return cls.query.all()


    # get Concept by id
    @classmethod
    def get_concept_by_id(cls, id):
        return cls.query.filter_by(id=id).all()
    
    # get Concept by section id
    @classmethod
    def get_concept_by_section_id(cls, section_id):
        return cls.query.filter_by(id=section_id).all()
