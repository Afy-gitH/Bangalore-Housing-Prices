<!DOCTYPE html>
<html>
<head>
  <title>Regression Model for House Price Prediction in Bangalore</title>
</head>
<body>
  <h1>Regression Model for House Price Prediction in Bangalore</h1>

  <h2>Dataset</h2>
  <p>The dataset used for training the regression model contains more than 13,000 data samples, each consisting of features such as location, number of bedrooms (BHK), number of bathrooms, number of balconies, and square footage. Additionally, the dataset includes the corresponding actual prices of houses in Bangalore.</p>

  <h2>Model Selection</h2>
  <p>To find the best regression model for this project, three popular algorithms were evaluated: linear regression, lasso regression, and ridge regression. After comparing the performance of these models, the ridge regression algorithm was chosen based on the following factors:</p>
  <ul>
    <li><strong>R^2 Score:</strong> The ridge regression model achieved an R^2 score of over 77%, indicating its ability to explain the variance in the house prices based on the given features.</li>
    <li><strong>Regularization:</strong> Ridge regression incorporates regularization, which helps prevent overfitting by adding a penalty term to the loss function. This feature enhances the model's generalization capabilities.</li>
  </ul>

  <h2>Flask Deployment</h2>
  <p>The selected ridge regression model has been deployed using Flask, a web development framework in Python. Flask provides a simple and efficient way to create a web application for hosting the regression model and making predictions.</p>

  <p>The deployment allows users to interact with the model through a web interface. Users can provide the necessary inputs, such as the location, number of bedrooms, number of bathrooms, number of balconies, and square footage of a house in Bangalore. The model then processes the inputs and predicts the corresponding price based on the trained parameters.</p>

  <h2>Usage</h2>
  <ol>
    <li>Clone the repository to your local machine using the command:</li>
    <pre><code>git clone https://github.com/your-username/house-price-prediction.git</code></pre>
    <li>Install the required dependencies by running:</li>
    <pre><code>pip install -r requirements.txt</code></pre>
    <li>Run the Flask application by executing the following command:</li>
    <pre><code>python app.py</code></pre>
    <li>Once the Flask server is up and running, open your web browser and navigate to <code>http://localhost:5000</code> to access the web interface.</li>
    <li>Enter the required details, including the location, number of bedrooms, number of bathrooms, number of balconies, and square footage of the house you want to predict the price for.</li>
    <li>Click the "Predict" button, and the model will display the estimated price for the provided inputs.</li>
  </ol>

  <h2>Contributing</h2>
  <p>Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please feel free to submit a pull request or open an issue in the GitHub repository.</p>

  <h2>License</h2>
  <p>This project is licensed under the <a href="LICENSE">MIT License</a>. Feel free to modify and use the code according to your requirements.</p>

  <h2>Acknowledgments</h2>
  <p>We would like to express our gratitude to the developers and contributors of the open-source libraries used in this project, as well as the creators of the dataset used for training the regression model. Their contributions are invaluable to the success of this project.</p>
</body>
</html>
