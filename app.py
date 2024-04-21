from flask import Flask, render_template, request, jsonify
from Controller.AddPatientController import AddPatientController

App = Flask(__name__, static_folder='Static')

@App.route('/', methods=['GET'])
def Dashboard():
    # Render the Dashboard view which contains the AddPatient form within it
    return render_template('DoctorDashboard.html')


@App.route('/AddPatient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'GET':
        # Display the form to the user
        return render_template('AddPatientView.html')
    elif request.method == 'POST':
        # Process the form submission
        RepublicOfTurkeyIDCardNo = request.form.get('RepublicOfTurkeyIDCardNo')
        success, message = AddPatientController.AddPatient(RepublicOfTurkeyIDCardNo)
        if success:
            return jsonify({'message': message}), 201
        else:
            return jsonify({'error': message}), 400


if __name__ == "__main__":
    App.run(debug=True)
