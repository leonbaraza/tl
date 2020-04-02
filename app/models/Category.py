from main import db


class CategoryModel(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)

    bootcampsModel = db.relationship('BootcampsModel', backref="categories")

# Add categories
    def new_category(self):
        db.session.add(self)
        db.session.commit()

# All Categories
    @classmethod
    def get_all_categories(cls):
        return cls.query.all()