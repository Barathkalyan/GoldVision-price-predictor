# **GoldVision: Gold Price Predictor**

**GoldVision** is a time-series forecasting project designed to predict the future trends of gold prices using historical data. The project utilizes **Facebook Prophet** for forecasting and provides visual insights into the price predictions over time. It aims to assist users in making informed decisions related to gold investments.

## **Features**

- **📊 Time Series Forecasting**: Utilizes **Facebook Prophet** for accurate and reliable gold price predictions.
- **📅 Custom Seasonality**: Adds quarterly seasonality to improve prediction accuracy.
- **📈 Visualizations**: Interactive graphs displaying actual vs. predicted values, along with confidence intervals.
- **🔮 Prediction Horizon**: Predicts gold prices up to **72 months** into the future.

## **Technologies Used**

- **Python**: The programming language used for this project.
- **Facebook Prophet**: A forecasting tool for generating time-series predictions.
- **Pandas**: Used for data manipulation and preprocessing.
- **Matplotlib**: For generating static visualizations.
- **Seaborn**: Provides additional visualization features for easier interpretation.
- **Scikit-learn**: Used for data clustering or any machine learning models.

## **Installation**

To get started with **GoldVision** locally, ensure that you have Python installed along with the required libraries. You can install the necessary dependencies using **pip**:


pip install pandas matplotlib seaborn fbprophet scikit-learn


## **How It Works**

1. **Data Preparation**: The historical gold price data is loaded into the program, and necessary preprocessing is done using **Pandas**.
2. **Model Training**: The data is then used to train a **Facebook Prophet** model.
3. **Prediction**: The trained model generates predictions for the next **72 months**.
4. **Visualization**: Predictions are visualized against actual values, and confidence intervals are displayed for a better understanding of forecast reliability.

## **Usage**

1. Clone the repository to your local machine:

   git clone https://github.com/Barathkalyan/GoldVision-price-predictor.git

2. Run the script `Goldvision.py` to train the model and generate forecasts.
3. Modify the input data (CSV file) or tweak the model parameters to suit your needs.

## **Screenshots**

Here are some screenshots of the GoldVision model's output:

![Gold Price Prediction](https://github.com/Barathkalyan/GoldVision-price-predictor/assets/7d4dc9f1-47ba-428b-9906-df0ebd3f3006)
![Gold Price Forecast](https://github.com/Barathkalyan/GoldVision-price-predictor/assets/3608717b-5601-44d9-92fe-44716213cce1)
![Prediction Visualization](https://github.com/Barathkalyan/GoldVision-price-predictor/assets/aeb43263-173d-4b64-b88a-291d0f3c5df8)

## **Future Improvements**

- **🌐 Web Interface**: Develop a user-friendly web-based interface to allow non-technical users to interact with the model.
- **📈 External Data Integration**: Incorporate additional factors like **inflation rates**, **stock market performance**, or **geopolitical events** to improve model accuracy.
- **🔄 Model Updates**: Periodically retrain the model with new data to ensure the predictions remain relevant and accurate.

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
