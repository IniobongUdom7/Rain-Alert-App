import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient




OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "d0aa67a5492b892b5c07f6ea5bf221ff"
account_sid = "AC76eb4da0d0a76c67c078552188745bfc"
auth_token = "4bc7fef7381f1cbdfad3751857fdf64c"



parameters = {
    "lat": 4.953060,
    "lon": 8.311800,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}


response = requests.get(url=OWM_endpoint, params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]

may_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        may_rain = True

if may_rain:
    #proxy_client = TwilioHttpClient()
    #proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today,remember to bring your umbrella.",
        from_="+15086845135",
        to="+234805694****"
    )
    print(message.status)



#print(data["hourly"][0]["weather"][0]["id"])
