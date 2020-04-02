from main import db


class ContactModel(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), default=1)
    message = db.Column(db.String, nullable=False)


    # Add Contact
    def new_contact_us(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_all_contact_us_messages(cls):
        return cls.query.all()

    @classmethod
    def get_contact_us_messages_by_id(cls,id):
        return cls.query.filter_by(user_id=id).all()