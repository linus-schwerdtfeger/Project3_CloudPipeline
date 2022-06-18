import json
import requests
from datetime import datetime
import pandas as pd
import sqlalchemy
import flights
import weather

def lambda_handler(event, context):
      
    flights.get_flights()
    weather.get_weather()

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
