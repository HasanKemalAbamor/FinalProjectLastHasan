from Model.QRCodeModel import QrCodeModel

class QrCodeController:
    @staticmethod
    def UploadQrCode(patient_id, qr_data):
        QrCodeModel.SaveQrCodeData(patient_id, qr_data)
        return True, "QR code uploaded successfully."
