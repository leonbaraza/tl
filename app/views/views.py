from main import app,db
from flask import render_template,redirect, request, flash


from models.Users import UsersModel
from models.Bootcamps import BootcampsModel
from models.BootcampSessions import BootcampSessionModel
from models.EnrollPayments import EnrollPaymentsModel
from models.UserBootcampAttendance import UserBootcampAttendanceModel
from models.UserBootcampEnrollments import UserBootcampEnrollmentModel
from models.Category import CategoryModel
from models.Section import SectionModel
from models.Consept import ConceptModel
from models.Contact import ContactModel
from models.sessions import SessionsModel



@app.before_first_request
def create_drop_tables():
    db.create_all()
    # db.drop_all()


# @app.route('/')
# def login():
#     return render_template('login.html')


# @app.route('/bootcamps')
# def bootcamps():
#     bootcamps = BootcampsModel.get_all_bootcamps()
#     return render_template('bootcamps.html', bootcamps=bootcamps)


# @app.route('/bootcamp_details/<bootcamp_id>')
# def bootcamp_details(bootcamp_id):
#     one_record = BootcampsModel.get_bootcamp_by_id(bootcamp_id)
#     requirements = one_record.requirements.split(',')
#     provisions = one_record.provisions.split(',')
#     cat_id = one_record.category_id
#     category_details = CategoryModel.query.filter_by(id = cat_id).first()
#     bootcamps = BootcampsModel.get_all_bootcamps()

#     return render_template('bootcamp-details.html',bootcamps=bootcamps, bootcamp=one_record, provisions=provisions, category_details=category_details,requirements=requirements)


@app.route('/admin/add/bootcamps', methods=['GET','POST'])
def admin_add_bootcamps():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        requirements = request.form['requirements']
        fees = request.form['fees']
        duration = request.form['duration']
        provisions = request.form['provisions'] 
        category_id = request.form['category']

        n_bootcamp = BootcampsModel(title=title, description=description,requirements=requirements,fee=fees, duration=duration, provisions=provisions,category_id=category_id)
        n_bootcamp.new_bootcamp()
 

    return render_template('admin/admin-bootcamps.html')


@app.route('/my_account')
def account():
    bootcamps = BootcampsModel.get_all_bootcamps()
    for bc in bootcamps:
        print(bc)
    return render_template('account/account.html', bootcamps = bootcamps, bootcamp=[])


@app.route('/')
def bootcamps():
    return render_template('login.html')


@app.route('/bootcamps')
def all_bootcamps():
    bootcamps = BootcampsModel.get_all_bootcamps()
    
    return render_template('bootcamps.html', bootcamps=bootcamps)

@app.route('/boot/sections/<bootcamp_id>')
def bootcamp_sections(bootcamp_id):
    sections = SectionModel.get_session_by_bootcamp_id(int(bootcamp_id))
    one_record = BootcampsModel.get_bootcamp_by_id(bootcamp_id)
    
    concepts = ConceptModel.all_concepts()

    for each in sections:
        print(each.id)
        print('yes')
        id = each.id
        # concept = ConceptModel.get_concept_by_section_id(id).all()
        # for n in concept:
        #     print(n.concept)

    return render_template('bootcamp-sections.html', sections=sections, bootcamp=one_record, concepts=concepts)


@app.route('/bootcamp/sections/<bootcamp_id>')
def bootcamp_section(bootcamp_id):
    sections = SessionsModel.get_bootcamp_by_bootcamp_id(int(bootcamp_id))
    for s in sections:
        print(s)
    one_record = BootcampsModel.get_bootcamp_by_id(bootcamp_id)
    
    # concepts = ConceptModel.all_concepts()

    # for each in sections:
    #     print(each.id)
    #     print('yes')
    #     id = each.id

    return render_template('bootcamp-sections.html', sessions=sections, bootcamp = one_record)


# @app.route('/bootcamp_details/<bootcamp_id>')
# def bootcamp_details(bootcamp_id):
#     one_record = BootcampsModel.get_bootcamp_by_id(bootcamp_id)
#     requirements = one_record.requirements.split(',')
#     provisions = one_record.provisions.split(',')
#     cat_id = one_record.category_id
#     category_details = CategoryModel.query.filter_by(id = cat_id).first()
#     bootcamps = BootcampsModel.get_all_bootcamps()

#     return render_template('bootcamp-details.html',bootcamps=bootcamps, bootcamp=one_record, provisions=provisions, category_details=category_details,requirements=requirements)


@app.route('/bootcamps_details/<bootcamp_id>')
def bootcamps_details(bootcamp_id):
    one_record = BootcampsModel.get_bootcamp_by_id(bootcamp_id)
    requirements = one_record.requirements.split(',')
    provisions = one_record.provisions.split(',')
    cat_id = one_record.category_id
    category_details = CategoryModel.query.filter_by(id = cat_id).first()
    bootcamps = BootcampsModel.get_all_bootcamps()

    return render_template('single-bootcamp-details.html',bootcamps=bootcamps, bootcamp=one_record, provisions=provisions, category_details=category_details,requirements=requirements)



@app.route('/my-payments')
def my_payments():
    return render_template('my-payments.html')


@app.route('/contact-us', methods=['POST','GET'])
def contact_us():
    if request.method == 'POST':

        message = ContactModel(user_id=1, message=request.form['message'])
        message.new_contact_us()
        flash('Message send successfully', 'primary')

    return render_template('contact-us.html')


# @app.route('/admin/add/bootcamps/sessions', methods=['POST', 'GET'])
# def add_sessions():
#     if request.method == 'POST':
#         section = SectionModel(title=request.form['title'], bootcamp_id=request.form['bootcamp'])
#         section.new_section()
#     return render_template('admin/add-sessions.html')


@app.route('/admin/add/bootcamps/concept', methods=['POST', 'GET'])
def add_concept():
    if request.method == 'POST':
        concept = ConceptModel(concept=request.form['title'], section_id=request.form['section'])
        concept.new_concept()
    return render_template('admin/add-concept.html')


@app.route('/admin/add/bootcamps/sessions', methods=['POST', 'GET'])
def add_session():
    if request.method == 'POST':
        session = SessionsModel(concept_title=request.form['concept_title'], concept_link=request.form['concept_link'], bootcamp_id=request.form['bootcamp_id'], bootcamp_url=request.form['bootcamp_url'])
        session.new_section()
    return render_template('admin/add-sessions.html')
