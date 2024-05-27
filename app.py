import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from Controller.AddPatientController import AddPatientController
from Controller.ShowPatientsController import ShowPatientsController
from Controller.DoctorLoginController import DoctorLoginController
from Controller.GraphUploadController import GraphUploadController

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize the GraphUploadController
graph_upload_controller = GraphUploadController('trained72')


# Database connection function
def get_db_connection():
	conn = sqlite3.connect('Database/Database.db')
	conn.row_factory = sqlite3.Row
	return conn


@app.route('/')
def home():
	return render_template('HomePage.html')


@app.route('/choose_role', methods=['POST'])
def choose_role():
	role = request.form['role']
	if role == 'doctor':
		return redirect(url_for('doctor_login'))
	elif role == 'patient':
		return redirect(url_for('upload_graph'))
	else:
		flash("Invalid selection. Please choose a valid role.")
		return redirect(url_for('home'))


@app.route('/doctor_login', methods=['GET', 'POST'])
def doctor_login():
	if request.method == 'POST':
		republic_of_turkey_id_card_no = request.form.get('republic_of_turkey_id_card_no')
		password = request.form.get('password')

		if not republic_of_turkey_id_card_no or not password:
			flash("ID and password are required.")
			return redirect(url_for('doctor_login'))

		if DoctorLoginController.authenticate(republic_of_turkey_id_card_no, password):
			session['doctor_logged_in'] = True
			return redirect(url_for('dashboard'))
		else:
			flash("Invalid ID or password")
			return redirect(url_for('doctor_login'))

	return render_template('DoctorLogin.html')


@app.route('/dashboard')
def dashboard():
	if 'doctor_logged_in' not in session:
		return redirect(url_for('doctor_login'))
	return render_template('DoctorDashboard.html')


@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
	if request.method == 'POST':
		id_number = request.form['RepublicOfTurkeyIDCardNo']
		name = request.form['Name']
		age = request.form['Age']
		condition = request.form['Condition']
		sex = request.form['Sex']
		email = request.form['Email']
		success, message = AddPatientController.add_patient(id_number, name, age, condition, sex, email)
		flash(message)
		if success:
			return redirect(url_for('my_patients'))
	return render_template('AddPatientView.html')


@app.route('/mypatients')
def my_patients():
	if 'doctor_logged_in' not in session:
		return redirect(url_for('doctor_login'))
	patients = ShowPatientsController.show_patients()
	return render_template('ShowPatients.html', patients=patients)


@app.route('/upload_graph', methods=['GET', 'POST'])
def upload_graph():
	if request.method == 'POST':
		try:
			# Get the data from the request
			patient_id = request.form['patient_id']
			graph_file = request.files['graph_file']

			if graph_file:
				graph_data = graph_file.read()

				# Process the graph data and make predictions
				df = graph_upload_controller.process_graph(graph_data)
				predictions = graph_upload_controller.make_predictions(df)

				# Save predictions to the database
				labels = ['Low', 'Medium', 'High']
				HDLCholesterol = labels[predictions[0][0]]
				Hemoglobin = labels[predictions[0][1]]
				LDLCholesterol = labels[predictions[0][2]]

				conn = get_db_connection()
				conn.execute(
					'INSERT INTO TestResults (PatientID, HDLCholesterol, Hemoglobin, LDLCholesterol) VALUES (?, ?, ?, ?)',
					(patient_id, HDLCholesterol, Hemoglobin, LDLCholesterol))
				conn.commit()
				conn.close()

				print(
					f"Data saved: PatientID={patient_id}, HDLCholesterol={HDLCholesterol}, Hemoglobin={Hemoglobin}, LDLCholesterol={LDLCholesterol}")

				# Map predictions to labels for display
				mapped_predictions = map_predictions_to_labels(predictions)

				return render_template('UploadGraph.html', prediction=mapped_predictions)
		except Exception as e:
			print(f"Error: {e}")
			return jsonify(success=False, message=str(e))
	else:
		return render_template('UploadGraph.html')


def map_predictions_to_labels(predictions):
	# Map the numeric predictions to human-readable labels
	labels = ['Low', 'Medium', 'High']
	target_labels = ['HDLCholesterol', 'Hemoglobin', 'LDLCholesterol']
	mapped_predictions = {target: labels[pred] for target, pred in zip(target_labels, predictions[0])}
	return mapped_predictions


@app.route('/testresults')
def test_results():
	if 'doctor_logged_in' not in session:
		return redirect(url_for('doctor_login'))

	# Fetch the test results from the database
	conn = get_db_connection()
	test_results = conn.execute('SELECT * FROM TestResults').fetchall()
	conn.close()

	return render_template('TestResults.html', test_results=test_results)


if __name__ == "__main__":
	app.run(debug=True)
