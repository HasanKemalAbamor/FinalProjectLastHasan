import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from Controller.AddPatientController import AddPatientController
from Controller.ShowPatientsController import ShowPatientsController
from Controller.DoctorLoginController import DoctorLoginController
from Controller.GraphUploadController import GraphUploadController

app = Flask(__name__)
app.secret_key = 'your_secret_key'

graph_upload_controller = GraphUploadController()

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

@app.route('/my_patients')
def my_patients():
    if 'doctor_logged_in' not in session:
        return redirect(url_for('doctor_login'))
    patients = ShowPatientsController.show_patients()
    return render_template('ShowPatients.html', patients=patients)

@app.route('/upload_graph', methods=['GET', 'POST'])
def upload_graph():
    prediction = None
    if request.method == 'POST':
        graph_file = request.files['graph_file']
        graph_data = graph_file.read()
        success, message = graph_upload_controller.upload_graph(graph_data)
        flash(message)
        if success:
            prediction = graph_upload_controller.process_graph(graph_data)
            if prediction is not None:
                prediction = prediction.tolist()  # Convert numpy array to list
                prediction = map_predictions_to_labels(prediction)
    return render_template('UploadGraph.html', prediction=prediction)

def map_predictions_to_labels(predictions):
    # Map the numeric predictions to human-readable labels
    labels = ['Low', 'Medium', 'High']
    target_labels = ['hdl_cholesterol_human', 'hemoglobin(hgb)_human', 'cholesterol_ldl_human']
    mapped_predictions = {target: labels[pred] for target, pred in zip(target_labels, predictions[0])}
    return mapped_predictions

if __name__ == "__main__":
    app.run(debug=True)
