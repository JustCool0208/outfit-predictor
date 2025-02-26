from fastapi import FastAPI
from pydantic import BaseModel 
#typically used to define request bodies, 
#ensuring incoming data meets expected types.

import joblib
import numpy as np

# Load the trained model and label encoder
model = joblib.load("outfit_recommender.pkl")
y_label_encoder = joblib.load("y_label_encoder.pkl")

app = FastAPI()

class WeatherInput(BaseModel):
    temperature: float
    humidity: float
    weather_condition: int  # 0: Rainy, 1: Cloudy, 2: Sunny


@app.post("/recommend-outfit")
def recommended_outfit(data: WeatherInput):
    input_data = np.array([[data.temperature, data.humidity, data.weather_condition]])

    prediction_encoded = model.predict(input_data)[0]
    prediction = y_label_encoder.inverse_transform([prediction_encoded])[0]

    return {"outfit_recommendation": prediction}