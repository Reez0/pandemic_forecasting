# Pandemic Forecasting Project

This is a simple Django project created for [briefly describe the purpose or context of the project].

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes. 

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
