# Pandemic Forecasting Project

This is a simple project created to predict COVID 19 cases in South Africa and achieves the following:

1. Gets the HTML source from worldometers. ✅
2. Parses the source to get the daily cases in recent past. ✅ 
3. Uses an ARIMA machine learning method to make a forecast. ✅
4. Model runs in real time. ✅
5. Writes results to .csv file. ✅
6. Adds forecast to .png file. ✅
7. Can run as a standalone script or as part of a greater project. ✅
8. Forecasting results accessible via an API endpoint. ✅
9. Forecasting results available in a frontend. ✅
## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes. It can also be run as a standalone script by running the crawler.py file found in forecast/crawler.py. 

`python3 crawler.py` will generate a png plot and a csv file.

### Prerequisites

- [Python](https://www.python.org/downloads/) (version 3.8.10)

### Installation

1. Clone the repository:

2. Navigate to the project directory:

   ```shell
   cd pandemic_forecasting
   ```

3. Install project dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```shell
   python manage.py migrate
   ```


5. Start the development server:

   ```shell
   python manage.py runserver
   ```

7. Open your web browser and access the project at [http://localhost:8000/](http://localhost:8000/).

## Usage

Navigating to http://localhost:8000/ will show a simple UI containing a chart with the Covid 19 predictions. The chart data is retrieved from a REST API used by the django server.

To generate a .png plot and .csv file, you can directly call the crawler.py file found in forecast/crawler.py.

The crawler.py file also contains the ARIMA model. 
