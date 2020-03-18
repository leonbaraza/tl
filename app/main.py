from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.Config import *

app = Flask(__name__)
app.config.from_object(Development)
db = SQLAlchemy(app)


from models.Users import UsersModel
from models.Bootcamps import BootcampsModel
from models.BootcampSessions import BootcampSessionModel
from models.EnrollPayments import EnrollPaymentsModel
from models.UserBootcampAttendance import UserBootcampAttendanceModel
from models.UserBootcampEnrollments import UserBootcampEnrollmentModel


@app.before_first_request
def create_drop_tables():
    db.create_all()
    # db.drop_all()


from views.views import *


if __name__ == '__main__':
    app.run()