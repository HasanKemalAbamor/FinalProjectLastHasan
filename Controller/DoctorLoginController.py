from Model.DoctorModel import DoctorModel

class DoctorLoginController:
    @staticmethod
    def authenticate(id_card_no, password):
        return DoctorModel.authenticate(id_card_no, password)
