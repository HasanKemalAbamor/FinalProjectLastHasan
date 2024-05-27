from Model.AddPatientModel import AddPatientModel

class AddPatientController:
    @staticmethod
    def add_patient(republic_of_turkey_id_card_no, name, age, condition, sex, email):
        if republic_of_turkey_id_card_no is None:
            return False, "No ID provided."

        if len(republic_of_turkey_id_card_no) == 11 and republic_of_turkey_id_card_no.isdigit():
            AddPatientModel.add_patient(republic_of_turkey_id_card_no, name, age, condition, sex, email)
            return True, "Patient added successfully."
        else:
            return False, "Invalid ID: It must be an 11-digit number."
