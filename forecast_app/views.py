from django.shortcuts import render
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import io
import urllib, base64

def forecast_view(request):
    forecast_days = int(request.GET.get('days', 15))

    df = pd.read_csv("Flight Catering Daily Orders_Jan to March 2024.csv")
    df.columns = ['ds', 'y']
    df['ds'] = pd.to_datetime(df['ds'])

    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=forecast_days)
    forecast = model.predict(future)

    fig = model.plot(forecast)
    plt.title("In-Flight Meal Order Forecast", fontsize=14)
    plt.xlabel("Date")
    plt.ylabel("Total Orders")
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.xlabel("Date")
    plt.ylabel("Total Orders")
    
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    return render(request, 'forecast_app/forecast.html', {
        'image': image_base64,
        'forecast_days': forecast_days
    })
