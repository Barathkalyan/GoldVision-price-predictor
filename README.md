# **GoldVision: Gold Price Predictor**

**GoldVision** is a time-series forecasting project designed to predict the future trends of gold prices using historical data. The project utilizes **Facebook Prophet** for forecasting and provides visual insights into the price predictions over time. It aims to assist users in making informed decisions related to gold investments. The accuracy depends on the clarity of the dataset used

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

![image](https://github.com/user-attachments/assets/ff97464a-c772-49b8-9fca-f2c8cbc39848)
![image](https://github.com/user-attachments/assets/3b1920dc-5ada-42db-9d5a-c3907d33482b)
![image](https://github.com/user-attachments/assets/e7a331e5-1581-4d22-8805-588768a37f1c)
![image](https://github.com/user-attachments/assets/f2298c0d-a044-4572-9ee9-c4c56f225f31)





## **Future Improvements**

- **🌐 Web Interface**: Develop a user-friendly web-based interface to allow non-technical users to interact with the model.
- **📈 External Data Integration**: Incorporate additional factors like **inflation rates**, **stock market performance**, or **geopolitical events** to improve model accuracy.
- **🔄 Model Updates**: Periodically retrain the model with new data to ensure the predictions remain relevant and accurate.

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
