import csv

def load_weather_data(file_path):
    weather_data = {}
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            city = row['city']
            weather_data[city] = {
                'temperature': float(row['temperature']),
                'humidity': float(row['humidity']),
                'wind_speed': float(row['wind_speed'])
            }
    return weather_data

def get_city_weather(weather_data, city):
    return weather_data.get(city, None)

def compare_weather_conditions(weather_data, city1, city2):
    weather1 = get_city_weather(weather_data, city1)
    weather2 = get_city_weather(weather_data, city2)

    if not weather1 or not weather2:
        return None

    comparison = {
        'temperature_diff': weather1['temperature'] - weather2['temperature'],
        'humidity_diff': weather1['humidity'] - weather2['humidity'],
        'wind_speed_diff': weather1['wind_speed'] - weather2['wind_speed']
    }

    return comparison

def find_trends(weather_data):
    avg_temp = sum(city['temperature'] for city in weather_data.values()) / len(weather_data)
    avg_humidity = sum(city['humidity'] for city in weather_data.values()) / len(weather_data)
    avg_wind_speed = sum(city['wind_speed'] for city in weather_data.values()) / len(weather_data)

    trends = {
        'average_temperature': avg_temp,
        'average_humidity': avg_humidity,
        'average_wind_speed': avg_wind_speed
    }

    return trends

file_path = 'weather_data.csv'
weather_data = load_weather_data(file_path)

# Get weather data for a specific city
city = 'New York'
city_weather = get_city_weather(weather_data, city)
print(f"Weather data for {city}: {city_weather}")

# Compare weather conditions between two cities
city1 = 'New York'
city2 = 'Los Angeles'
comparison = compare_weather_conditions(weather_data, city1, city2)
print(f"Weather comparison between {city1} and {city2}: {comparison}")

# Find trends across all cities
trends = find_trends(weather_data)
print(f"Weather trends: {trends}")
