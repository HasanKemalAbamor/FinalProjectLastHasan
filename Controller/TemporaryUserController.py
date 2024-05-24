from Model.TemporaryUserModel import TemporaryUserModel

class TemporaryUserController:
    @staticmethod
    def CreateTemporaryUser(republic_of_turkey_id_card_no, patient_id):
        password = TemporaryUserModel.CreateTemporaryUser(republic_of_turkey_id_card_no, patient_id)
        return password

    @staticmethod
    def AuthenticateTemporaryUser(republic_of_turkey_id_card_no, password):
        user = TemporaryUserModel.AuthenticateTemporaryUser(republic_of_turkey_id_card_no, password)
        return user
