from flask import Flask, render_template, request, redirect, url_for, flash
from Controller.AddPatientController import AddPatientController
from Controller.ShowPatientsController import ShowPatientsController
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
        success, message = AddPatientController.AddPatient(id_number)
        flash(message)
        if success:
            return redirect(url_for('my_patients'))
    return render_template('AddPatientView.html')

@app.route('/mypatients')
def my_patients():
    patients = ShowPatientsController.ShowPatients()
    return render_template('ShowPatients.html', patients=patients)

@app.route('/testresults', methods=['GET', 'POST'])
def test_results():
    results = None
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        results = ShowTestResultsController.GetTestResults(patient_id)
    return render_template('ShowTestResults.html', results=results)

if __name__ == "__main__":
    app.run(debug=True)
