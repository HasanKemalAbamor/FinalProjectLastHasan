from Model.PatientModel import PatientModel

class ShowPatientsController:
    @staticmethod
    def show_patients():
        return PatientModel.get_all_patients()
