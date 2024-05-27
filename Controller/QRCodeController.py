import joblib
import pandas as pd
import numpy as np
from pyzbar.pyzbar import decode
from PIL import Image
import io

class QRCodeController:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)  # Load the trained machine learning model

    def upload_qr_code(self, patient_id, qr_data):
        # Placeholder for saving QR code data to database
        # QRCodeModel.save_qr_data(patient_id, qr_data)
        return True, "QR code uploaded successfully."

    def process_qr_code(self, qr_image):
        # Assuming qr_image is the image bytes
        image = Image.open(io.BytesIO(qr_image))

        # Debug: Check if image is opened correctly
        print(f"Image format: {image.format}, size: {image.size}, mode: {image.mode}")

        # Read QR code data using pyzbar
        qr_data = decode(image)

        # Try to decode multiple times if the first attempt fails
        if not qr_data:
            for _ in range(3):  # Try up to 3 times
                qr_data = decode(image)
                if qr_data:
                    break

        if qr_data:
            qr_text = qr_data[0].data.decode('utf-8')
            print(f"QR Code Text: {qr_text}")  # Debug: Print QR code text
        else:
            qr_text = 'QR code not readable'
            print("QR code not readable")  # Debug: QR code not readable

        # Preprocess the QR data as required by your model
        try:
            preprocessed_data = self.preprocess_data(qr_text)
            prediction = self.model.predict(preprocessed_data)
            return prediction
        except ValueError as e:
            print(f"Error in preprocessing data: {e}")
            return None

    def preprocess_data(self, data):
        # Attempt to parse data as a CSV-like string with potential non-numeric values
        data_values = data.split(',')
        numeric_values = [float(val) for val in data_values if self.is_float(val)]

        print(f"Extracted Numeric Values: {numeric_values}")  # Debug: Print numeric values

        # Check if the number of numeric values matches the expected number of features (172)
        if len(numeric_values) != 172:
            raise ValueError(f"Expected 172 features, but got {len(numeric_values)}")

        # Create a data dictionary with feature names
        data_dict = {f'absorbance_{i+1}': val for i, val in enumerate(numeric_values)}
        df = pd.DataFrame([data_dict])

        # Reorder columns to match the order used during model training
        required_columns = [f'absorbance_{i+1}' for i in range(172)]
        df = df[required_columns]

        return df.values  # Ensure this is a 2D numpy array

    def is_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False
