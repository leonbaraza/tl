from main import db


class EnrollPaymentsModel(db.Model):
    __tablename__ = 'enroll_payments'
    id = db.Column(db.Integer, primary_key=True)
    ube_id = db.Column(db.Integer, db.ForeignKey('user_bootcamp_enrollments.id'))
    amount = db.Column(db.Float, nullable=False)
    msis_dn = db.Column(db.String, nullable=False)
    mpesa_ref = db.Column(db.String, nullable=False)

    # add new users
    def newUsers(self):
        db.session.add(self)
        db.session.commit()