from weather_data_fetcher import WeatherDataFetcher
from weather_data_parser import WeatherDataParser

class UserInterface:
    def __init__(self):
        # It's amazing how we can set the attributes as a Class within a class!
        self.fetcher = WeatherDataFetcher()
        self.parser = WeatherDataParser()

    def get_detailed_forecast(self, city):
        data = self.fetcher.fetch_weather_data(city)
        return self.parser.parse_weather_data(data)

    def display_weather(self, city):
        data = self.fetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = self.parser.parse_weather_data(data)
            print(weather_report)

    def run(self):
        while True:
            city = input("Enter the city (London, Tokyo, New York) to get the weather forecast or 'exit' to quit: ")
            if city == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = self.get_detailed_forecast(city)
            else:
                forecast = self.display_weather(city)
            print(forecast)