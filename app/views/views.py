from main import app,db


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


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def test():
    return 'leon'