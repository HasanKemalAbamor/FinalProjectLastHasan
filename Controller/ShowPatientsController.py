from Model.PatientModel import PatientModel

class ShowPatientsController:
    @staticmethod
    def ShowPatients():
        patients = PatientModel.GetAllPatients()
        return patients
