# Import necessary Libraries
import pandas as pd
from matplotlib import cm
import seaborn as sns
import matplotlib.pyplot as plt
from prophet import Prophet
from sklearn.cluster import KMeans

# Read the dataset preferably csv files using pandas and check by printing
df=pd.read_csv("C:\\Users\\kumarasamy\\Desktop\\spark\\Gold.csv")
df.head()

# Change the column names to use Facebook Prophet Model
df=df.rename(columns={"Date":"ds","India":"y"})
df["ds"]=pd.to_datetime(df["ds"],dayfirst=True)

# Set initial scales and initialise Prophet using model variable
model=Prophet(changepoint_prior_scale=0.1)
model.add_seasonality(name='quarterly', period=91.25, fourier_order=5)

#Train the model using the dataset
model.fit(df)
future=model.make_future_dataframe(periods=72,freq="M")

# Predict the next 72 values and plot them using forecast variable
forecast=model.predict(future)
model.plot(forecast)

# Graph customisations for better understading and informations
plt.xlabel("Year")
plt.ylabel("Gold prices")
plt.show()
plt.plot(df["ds"],df["y"],label="Actual Values")
plt.plot(forecast["ds"],forecast["yhat"],color="black",label="Predicted Values")
cmap=plt.get_cmap("coolwarm")

#To show the confidence level regions of the predicted values
plt.fill_between(
    forecast["ds"],
    forecast["yhat_lower"],
    forecast["yhat_upper"],
    color=cmap(2.5),
    alpha=0.3,
    label="Confidence Interval"
)
plt.xticks(rotation=45)

#To show the highest price in the predicted model
plt.annotate(
    "Highest Price", 
    xy=(forecast["ds"][forecast["yhat"].idxmax()], forecast["yhat"].max()), 
    xytext=(forecast["ds"][forecast["yhat"].idxmax()], forecast["yhat"].max() + 2000),
    arrowprops=dict(facecolor="black", arrowstyle="->"),
    fontsize=8
)

#To show the exact prediction period
plt.axvspan(df["ds"].iloc[-1], forecast["ds"].iloc[-1], color="brown", alpha=0.2, label="Prediction Period")

#Other Graph customisations
plt.title("Gold Price Prediction: 1981-2026")
plt.xlabel("Year")
sns.set_theme(style="whitegrid")
plt.ylabel("Price of Gold")
plt.tick_params(colors="black")
plt.legend(title="Legend",loc="upper left")
plt.show()

# To show the forecast components graph
model.plot_components(forecast)
plt.show()
