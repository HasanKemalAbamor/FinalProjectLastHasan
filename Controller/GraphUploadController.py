import joblib
import pandas as pd
import numpy as np
from PIL import Image
import io

class GraphUploadController:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)  # Load the trained machine learning model

    def process_graph(self, graph_image):
        image = Image.open(io.BytesIO(graph_image))

        # Debug: Check if image is opened correctly
        print(f"Image format: {image.format}, size: {image.size}, mode: {image.mode}")

        # Convert image to grayscale and resize
        image = image.convert('L')
        image = image.resize((13, 13), Image.LANCZOS)

        # Flatten image data and normalize
        image_array = np.array(image).flatten() / 255.0

        if len(image_array) != 169:
            raise ValueError(f"Expected 169 features after resizing, but got {len(image_array)}")

        # Create a DataFrame to match the model's input structure
        data_dict = {f'absorbance{i}': val for i, val in enumerate(image_array)}
        df = pd.DataFrame([data_dict])

        # Ensure all required columns are present
        required_columns = [f'absorbance{i}' for i in range(170)] + ['temperature', 'humidity']
        for col in required_columns:
            if col not in df.columns:
                df[col] = 0  # Add missing columns with default value 0

        return df

    def make_predictions(self, df):
        preprocessed_data = self.preprocess_data(df)
        predictions = self.model.predict(preprocessed_data)
        return predictions

    def preprocess_data(self, data):
        required_columns = [f'absorbance{i}' for i in range(170)] + ['temperature', 'humidity']
        for col in required_columns:
            if col not in data.columns:
                data[col] = 0  # Add missing columns with default value 0
        return data[required_columns]
