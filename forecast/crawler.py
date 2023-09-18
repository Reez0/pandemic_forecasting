from datetime import timedelta
from bs4 import BeautifulSoup
import requests
from typing import List, Dict, Any, Tuple
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt


def model() -> Tuple[pd.DataFrame, pd.DataFrame]:
    dates, cases = retrieve_data()
    data = {'Date': dates, 'Cases': cases}
    df = pd.DataFrame(data)
    df["Date"] = pd.to_datetime(df['Date'])
    df['Cases'] = pd.to_numeric(df['Cases'], errors='coerce')
    df = df.sort_values(by='Date')
    df.set_index('Date', inplace=True)
    model = sm.tsa.ARIMA(df['Cases'], order=(1, 1, 1))
    result = model.fit()
    last_date = df.index[-1]
    forecast_days = 7

    # Create a list of date steps for forecasting
    date_steps = [last_date + timedelta(days=i)
                  for i in range(1, forecast_days + 1)]

    # Forecast using ARIMA
    forecast = result.forecast(steps=forecast_days)

    forecast_df = pd.DataFrame(
        {'date': date_steps, 'new_cases': round(forecast)})

    forecast_df.set_index('date', inplace=True)
    return df, forecast_df


def report():
    original_dataframe, forecast = model()

    forecast.to_csv('results.csv')

    # Plot the actual and predicted values
    plt.plot(original_dataframe.index,
             original_dataframe['Cases'], label='Actual')
    plt.plot(pd.date_range(
        start=original_dataframe.index[-1], periods=7), forecast, label='Forecast', linestyle='--')
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Cases')
    plt.savefig('plot.png')


def retrieve_data() -> Tuple[List[str], List[str]]:
    response = requests.get(
        "https://www.worldometers.info/coronavirus/country/south-africa/")
    soup = BeautifulSoup(response.content, features="html.parser")
    dates: List[str] = []
    cases: List[str] = []
    # Get all elements containing amount of cases
    cases_elements = soup.find_all('li', "news_li")

    for element in cases_elements:
        # Get amount of cases from text found in element
        cases_count: str = element.find("strong").text.replace(
            "new cases", "").strip()
        cases.append(cases_count)

    # Get latest date first
    latest_date_element = soup.find("div", "news_date")
    latest_date = latest_date_element.find_next_sibling().get(
        'id').replace("newsdate", "")
    dates.append(latest_date)

    # Get all subsequent dates
    date_elements = soup.find_all("button", "date-btn")
    for element in date_elements:
        dates.append(element.get('data-date'))

    return dates, cases


if __name__ == '__main__':
    report()
