from flask import Flask, render_template, request, redirect, url_for, flash, session
from Controller.AddPatientController import AddPatientController
from Controller.ShowPatientsController import ShowPatientsController
from Controller.TemporaryUserController import TemporaryUserController
from Controller.QRCodeController import QrCodeController
from Controller.ShowTestResultsController import ShowTestResultsController

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def dashboard():
	return render_template('DoctorDashboard.html')


@app.route('/AddPatient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        id_number = request.form['RepublicOfTurkeyIDCardNo']
        name = request.form['Name']
        age = request.form['Age']
        condition = request.form['Condition']
        sex = request.form['Sex']
        success, message = AddPatientController.AddPatient(id_number, name, age, condition, sex)
        flash(message)
        if success:
            return redirect(url_for('my_patients'))
    return render_template('AddPatientView.html')

@app.route('/mypatients')
def my_patients():
	patients = ShowPatientsController.ShowPatients()
	return render_template('ShowPatients.html', patients=patients)


@app.route('/temporary_user_login', methods=['GET', 'POST'])
def temporary_user_login():
	if request.method == 'POST':
		republic_of_turkey_id_card_no = request.form['republic_of_turkey_id_card_no']
		password = request.form['password']
		user = TemporaryUserController.AuthenticateTemporaryUser(republic_of_turkey_id_card_no, password)
		if user:
			session['patient_id'] = user[2]  # Assuming the PatientID is the third element
			return redirect(url_for('upload_qr_code'))
		else:
			flash("Invalid ID or password")
	return render_template('TemporaryUserLogin.html')


@app.route('/upload_qr_code', methods=['GET', 'POST'])
def upload_qr_code():
	if request.method == 'POST':
		if 'patient_id' not in session:
			flash("Please login first.")
			return redirect(url_for('temporary_user_login'))

		qr_code = request.files['qr_code']
		qr_data = qr_code.read()  # Assuming you process the image to extract data
		patient_id = session['patient_id']
		success, message = QrCodeController.UploadQrCode(patient_id, qr_data)
		flash(message)
		if success:
			return redirect(url_for('dashboard'))
	return render_template('UploadQrCode.html')


@app.route('/testresults', methods=['GET', 'POST'])
def test_results():
	results = None
	if request.method == 'POST':
		patient_id = request.form['patient_id']
		results = ShowTestResultsController.GetTestResults(patient_id)
	return render_template('ShowTestResults.html', results=results)


if __name__ == "__main__":
	app.run(debug=True)
