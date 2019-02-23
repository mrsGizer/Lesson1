forecast = {"city": "Москва", "temperature": 20}
print(forecast["city"])
forecast["temperature"] = forecast["temperature"] - 5
print(forecast)
print(forecast.get("city"))
print(forecast.get("country", "Россия"))
forecast["date"] = "27.05.2019"
print(len(forecast))