
import requests
import json

# ⚠️  IMPORTANT: Replace this with your actual OpenWeatherMap API key
API_KEY = "1b6d26b1bf21866fc22405c8f2d1996f"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_location():
    """Prompt user to enter a city name or ZIP code."""
    while True:
        location = input("\nEnter a city name or ZIP code: ").strip()
        if not location:
            print("❌ Location cannot be empty. Please try again.")
            continue
        return location

def fetch_weather(location):
    """Fetch weather data from OpenWeatherMap API."""
    try:
        params = {
            'q': location,
            'appid': API_KEY,
            'units': 'metric'  # Use Celsius
        }
        
        response = requests.get(BASE_URL, params=params, timeout=5)
        
        # Check for successful response
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print(f"❌ Location '{location}' not found. Please try again with a valid city name.")
            return None
        elif response.status_code == 401:
            print("❌ Invalid API key. Please check your API key and try again.")
            return None
        else:
            print(f"❌ Error from API (status code {response.status_code}). Please try again.")
            return None
    
    except requests.exceptions.Timeout:
        print("❌ Request timed out. Please check your internet connection.")
        return None
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Please check your internet connection.")
        return None
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return None

def display_weather(data):
    """Parse and display weather information from the API response."""
    try:
        # Extract data from JSON response
        city = data['name']
        country = data['sys']['country']
        temp_celsius = data['main']['temp']
        temp_fahrenheit = (temp_celsius * 9/5) + 32
        humidity = data['main']['humidity']
        description = data['weather'][0]['description'].capitalize()
        wind_speed = data['wind']['speed']
        
        # Display results
        print("\n" + "="*50)
        print(f"WEATHER FOR {city.upper()}, {country}")
        print("="*50)
        print(f"Temperature: {temp_celsius}°C / {temp_fahrenheit:.1f}°F")
        print(f"Condition: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print("="*50 + "\n")
        
    except KeyError:
        print("❌ Unexpected response format. Please try again.")

def main():
    """Main function to run the weather app."""
    print("\n" + "="*50)
    print("WEATHER APP")
    print("="*50)
    
    # Check if API key is set
    if API_KEY == "YOUR_API_KEY":
        print("\n⚠️  SETUP REQUIRED!")
        print("-" * 50)
        print("1. Go to: https://openweathermap.org/api")
        print("2. Sign up for a free account")
        print("3. Generate your free API key")
        print("4. Replace 'YOUR_API_KEY' in the code with your key")
        print("5. Run this script again")
        print("="*50)
        return
    
    print("Fetches real-time weather data for any location.\n")
    
    while True:
        location = get_location()
        weather_data = fetch_weather(location)
        
        if weather_data:
            display_weather(weather_data)
        
        # Ask if user wants to check another location
        again = input("Check another location? (yes/no): ").lower()
        if again not in ["yes", "y"]:
            print("Thank you for using the Weather App. Goodbye! 👋")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
