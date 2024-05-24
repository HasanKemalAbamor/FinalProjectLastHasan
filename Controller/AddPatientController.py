from Model.AddPatientModel import AddPatientModel

class AddPatientController:
    @staticmethod
    def AddPatient(republic_of_turkey_id_card_no, name, age, condition, sex):
        if republic_of_turkey_id_card_no is None:
            return False, "No ID provided."

        if len(republic_of_turkey_id_card_no) == 11 and republic_of_turkey_id_card_no.isdigit():
            patient_id = AddPatientModel.AddPatient(republic_of_turkey_id_card_no, name, age, condition, sex)
            return True, f"Patient added with PatientNumber: {patient_id}"
        else:
            return False, "Invalid ID: It must be an 11-digit number."
