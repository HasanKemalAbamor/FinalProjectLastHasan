

from Model.AddPatientModel import AddPatientModel


class AddPatientController:
    @staticmethod
    def AddPatient(RepublicOfTurkeyIDCardNo):
        # Check if RepublicOfTurkeyIDCardNo is None
        if RepublicOfTurkeyIDCardNo is None:
            return False, "No ID provided."

        # Now you can safely check the length
        if len(RepublicOfTurkeyIDCardNo) == 11 and RepublicOfTurkeyIDCardNo.isdigit():
            patient_id = AddPatientModel.AddPatient(RepublicOfTurkeyIDCardNo)
            return True, f"Patient added with PatientNumber: {patient_id}"
        else:
            return False, "Invalid ID: It must be an 11-digit number."
