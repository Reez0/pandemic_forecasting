from bs4 import BeautifulSoup
import requests
from typing import List, Dict, Any
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt


def t():
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

    # # Merge dates and cases into list of dictionaries for easier handling
    # data_list: List[Dict[str, str]] = [{'date': date, 'cases': int(
    #     case)} for date, case in zip(dates, cases)]
    # print(data_list)

    data = {'Date': dates, 'Cases': cases}
    df = pd.DataFrame(data)
    df["Date"] = pd.to_datetime(df['Date'])
    df['Cases'] = pd.to_numeric(df['Cases'], errors='coerce')
    df = df.sort_values(by='Date')
    df.set_index('Date', inplace=True)
    model = sm.tsa.ARIMA(df['Cases'], order=(1, 1, 1))
    result = model.fit()
    forecast = result.forecast(steps=7)

    # Print the forecast
    print(f'Predicted cases for the next 7 days: {forecast}')

    # Plot the actual and predicted values
    plt.plot(df.index, df['Cases'], label='Actual')
    plt.plot(pd.date_range(
        start=df.index[-1], periods=7), forecast, label='Forecast', linestyle='--')
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('Cases')
    plt.savefig('foo.png')


t()
