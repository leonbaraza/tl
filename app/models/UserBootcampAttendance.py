from main import db

class UserBootcampAttendanceModel(db.Model):
    __tablename__ = 'user_bootcamp_attendance'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    bootcamp_id = db.Column(db.Integer, db.ForeignKey('bootcamps.id'))
    status = db.Column(db.Boolean, nullable=False)

    # add new users
    def newUsers(self):
        db.session.add(self)
        db.session.commit()