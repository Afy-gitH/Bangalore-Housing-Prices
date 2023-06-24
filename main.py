#flask,scikit-learn, pandas,pickle-mixin
import pandas as pd
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
data = pd.read_csv("cleaned_data.csv")
pipe = pickle.load(open("RidgeModel.pkl", "rb"))


@app.route('/')
def index():
    locations = sorted(map(str, data["location"].unique()))
    return render_template('index.html', locations=locations)


@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk = float(request.form.get('bhk'))
    bath = float(request.form.get('bath'))
    sqft = float(request.form.get('total_sqft'))
    balcony = float(request.form.get('balcony'))
    
    # Perform prediction using the loaded model
    input = pd.DataFrame([[location,sqft,bath,bhk,balcony]], columns=['location', 'total_sqft', 'bath', 'BHK','balcony'])
    prediction = pipe.predict(input)[0] * 1e5

    # Do something with the prediction result (e.g., display it on the page)


    return str(np.round(prediction,2))


if __name__ == '__main__':
    app.run(debug=True, port=5000)

