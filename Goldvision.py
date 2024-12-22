import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prophet import Prophet
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Read the csv file using pandas
df=pd.read_csv("C:\\Users\\kumarasamy\\Desktop\\spark\\Hgold.csv")
# Convert to Prophet model format
df["Date"]=pd.to_datetime(df["Date"])
df=df.rename(columns={"Date":"ds","Open":"y"})
df.head()
# Initialize prophet model and train it using the dataset
model=Prophet(changepoint_prior_scale=0.5)
model.add_seasonality(name='yearly', period=365.25, fourier_order=7)
model.add_seasonality(name='quarterly', period=91.25, fourier_order=5)
model.fit(df)
# Make predictions
future=model.make_future_dataframe(periods=365,freq="D")
forecast=model.predict(future)
model.plot(forecast)
# Do plot graph shows
plt.show()
plt.plot(df["ds"],df["y"],label="Actual Values",color="red")
plt.plot(forecast["ds"],forecast["yhat"],label="predicted values",color="black")
# Show Confidence levels
plt.fill_between(
    forecast["ds"],
    forecast["yhat_lower"],
    forecast["yhat_upper"],
    label="Confidence Interval"
)
plt.legend()
plt.show()
model.plot_components(forecast)
plt.show()
# Calculate evaluation metrics
actual = df["y"].values
predicted = forecast["yhat"][:len(df)].values
mae = mean_absolute_error(actual, predicted)
mse = mean_squared_error(actual, predicted)
rmse = np.sqrt(mse)
mare = np.mean(np.abs((actual - predicted) / actual))
smape = np.mean(2 * np.abs(predicted - actual) / (np.abs(actual) + np.abs(predicted))) * 100
r2 = r2_score(actual, predicted)
accuracy = 100 - (mare * 100)
# Display the evaluation metrics
print("                                            ")
print("___________________________________________")
print("Prediction Accuracy and Performance Report")
print("___________________________________________")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"Mean Absolute Relative Error (MARE): {mare:.4f}")
print(f"Symmetric Mean Absolute Percentage Error (SMAPE): {smape:.2f}%")
print(f"R2 Score: {r2:.4f}")
print(f"Accuracy (based on MARE): {accuracy:.2f}%")
