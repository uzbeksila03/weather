import requests

def get_weather_day():
    url = f"https://api.weatherapi.com/v1/forecast.json?key=cd561d4bc365492682c45737242007&q=40.3833,71.7833&days=1"
    response = requests.get(url).json()['current']
    last_updated = response["last_updated"]
    temp_c = response['temp_c']
    wind_kph = response['wind_kph']
    humidity = response['humidity']
    cloud = response['cloud']
    result = f"""
So'nggi yangilanish bo'yicha ob-have ma'lumotlari:
Vaqti: {last_updated} 🕝
Harorat: {temp_c}°C 🌡
Shamol tezligi: {wind_kph} 🌬
Bulutlilik: {cloud} % ☁️
Namlik: {humidity} 💧
"""
    return result

def get_weather_week():
    url = f"https://api.weatherapi.com/v1/forecast.json?key=cd561d4bc365492682c45737242007&q=40.3833,71.7833&days=7"
    response = requests.get(url).json()['forecast']['forecastday']
    result = "3 Kunlik ma'lumotlar:\n"
    for i in response:
        date = i['date']
        maxtemp_c = i['day']['maxtemp_c']
        mintemp_c = i['day']['mintemp_c']
        avgtemp_c = i['day']['avgtemp_c']
        maxwind_kph = i['day']['maxwind_kph']
        avghumidity = i['day']['avghumidity']

        result_day = f"""
Sana: {date}
Max Harorat: {maxtemp_c}°C 🌡
Min Harorat: {mintemp_c}°C 🌡
O'rtacha Harorat: {avgtemp_c}°C 🌡
Shamol tezligi: {maxwind_kph} 🌬
Namlik: {avghumidity} 💧
"""
        result += result_day
    return result


