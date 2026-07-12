# Weather App - Beginner Tier

A Python application that fetches and displays real-time weather data for any location using the OpenWeatherMap API.

## 📋 Project Overview

This is a **beginner-tier weather app** that demonstrates:
- HTTP API integration
- JSON data parsing
- Error handling (network, API, user input)
- Real-time data fetching
- Temperature unit conversion
- Clean data presentation

The app fetches live weather for any city and displays temperature, humidity, conditions, and wind speed.

## ✨ Features

- ✅ **Real-Time Weather Data** - Fetches current conditions from OpenWeatherMap API
- ✅ **Multiple Location Support** - Search any city worldwide
- ✅ **Temperature Display** - Shows both Celsius and Fahrenheit
- ✅ **Complete Information:**
  - Temperature
  - Weather condition (Partly Cloudy, Rainy, etc.)
  - Humidity percentage
  - Wind speed
- ✅ **Error Handling:**
  - City not found
  - Network timeout
  - Invalid API key
  - Connection errors
- ✅ **Input Validation** - Rejects empty location input
- ✅ **Multiple Queries** - Check weather for multiple locations in one session
- ✅ **Free API** - No cost! 60 calls/minute on free tier

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- Internet connection
- Free OpenWeatherMap API key

### Step 1: Install Dependencies

```bash
pip install requests
```

**What it does:**
- `requests`: Makes HTTP calls to the weather API

### Step 2: Get Free API Key

1. **Go to:** https://openweathermap.org/api
2. **Sign Up:**
   - Click "Sign Up"
   - Create a free account
   - Verify your email
3. **Get API Key:**
   - Login to dashboard
   - Go to API Keys section
   - Copy your default API key
4. **Wait 10 minutes:**
   - New API keys take a few minutes to activate

### Step 3: Add API Key to Code

Open `04_weather_app.py` and find this line (around line 13):

```python
API_KEY = "YOUR_API_KEY"
```

Replace `YOUR_API_KEY` with your actual key:

```python
API_KEY = "abc123def456ghi789jkl012mno345pqr"
```

**⚠️ Important:** Never share your API key publicly!

### Step 4: Run the App

```bash
python 04_weather_app.py
```

## 🌍 Usage Guide

### Starting the App

```bash
python 04_weather_app.py
```

**Output:**
```
==================================================
WEATHER APP
==================================================
Fetches real-time weather data for any location.

Enter a city name or ZIP code: 
```

### Example Session 1: City Search

```
Enter a city name or ZIP code: London

==================================================
WEATHER FOR LONDON, GB
==================================================
Temperature: 15°C / 59°F
Condition: Partly Cloudy
Humidity: 72%
Wind Speed: 3.2 m/s
==================================================

Check another location? (yes/no): yes

Enter a city name or ZIP code: 
```

### Example Session 2: Multiple Locations

```
Enter a city name or ZIP code: Tokyo

==================================================
WEATHER FOR TOKYO, JP
==================================================
Temperature: 28°C / 82°F
Condition: Sunny
Humidity: 45%
Wind Speed: 2.1 m/s
==================================================

Check another location? (yes/no): yes

Enter a city name or ZIP code: New York

==================================================
WEATHER FOR NEW YORK, US
==================================================
Temperature: 22°C / 72°F
Condition: Cloudy
Humidity: 65%
Wind Speed: 4.5 m/s
==================================================

Check another location? (yes/no): no

Thank you for using the Weather App. Goodbye! 👋
```

## 🔧 How It Works

### Architecture

```
User enters location
  ↓
Program validates input (not empty)
  ↓
Program makes HTTP request to OpenWeatherMap API
  ↓
API returns JSON with weather data
  ↓
Program extracts relevant data (temp, humidity, etc.)
  ↓
Program converts temperature to both C and F
  ↓
Program displays formatted weather data
  ↓
Ask "Check another location?"
  ├─ Yes → Back to location input
  └─ No → Exit program
```

### API Request Format

```python
# API Endpoint
https://api.openweathermap.org/data/2.5/weather

# Query Parameters
?q=London          # City name
&appid=YOUR_API_KEY  # Your API key
&units=metric      # Use Celsius (default is Kelvin)
```

### JSON Response Example

```json
{
  "name": "London",
  "sys": {
    "country": "GB"
  },
  "main": {
    "temp": 15.2,
    "humidity": 72
  },
  "weather": [
    {
      "description": "partly cloudy"
    }
  ],
  "wind": {
    "speed": 3.2
  }
}
```

### Key Functions

**`get_location()`**
- Prompts user for city name or ZIP code
- Validates input is not empty
- Returns location string

**`fetch_weather(location)`**
- Makes HTTP GET request to OpenWeatherMap API
- Handles different error responses:
  - 200: Success
  - 404: Location not found
  - 401: Invalid API key
  - Other: API errors
- Handles network exceptions:
  - Timeout
  - Connection error
- Returns JSON data or None if error

**`display_weather(data)`**
- Extracts relevant fields from JSON response
- Calculates Fahrenheit from Celsius
- Formats and displays all weather information
- Includes city and country name

**`main()`**
- Checks if API key is configured
- Shows setup instructions if not
- Runs main loop for location queries

## ⚙️ Customization

### Change Temperature Unit

Remove `&units=metric` to get Kelvin (default):

```python
params = {
    'q': location,
    'appid': API_KEY
    # Remove: 'units': 'metric'
}
```

Add `&units=imperial` for Fahrenheit only:

```python
params = {
    'q': location,
    'appid': API_KEY,
    'units': 'imperial'
}
```

### Change Language

Add language parameter:

```python
params = {
    'q': location,
    'appid': API_KEY,
    'units': 'metric',
    'lang': 'es'  # Spanish (de, fr, it, ru, pt, etc.)
}
```

### Add More Weather Information

Edit `display_weather()` to show more fields:

```python
# Add these lines:
feels_like = data['main']['feels_like']
pressure = data['main']['pressure']
visibility = data['visibility']

print(f"Feels Like: {feels_like}°C")
print(f"Pressure: {pressure} hPa")
print(f"Visibility: {visibility} meters")
```

## 🐛 Troubleshooting

### Error: "Invalid API key"
**Causes:**
- Copied API key incorrectly
- Still has "YOUR_API_KEY" placeholder
- API key not yet activated

**Solutions:**
1. Copy API key again carefully
2. Check no extra spaces
3. Wait 10 minutes for activation
4. Verify in OpenWeatherMap dashboard

### Error: "Location 'xxx' not found"
**Causes:**
- Misspelled city name
- City doesn't exist in database
- Using incorrect name format

**Solutions:**
1. Try major city names (e.g., "London" not "Small Village")
2. Try country: "Paris, France"
3. Use ZIP code instead
4. Check spelling carefully

### Error: "Connection error" / "Timeout"
**Causes:**
- No internet connection
- Firewall blocking API calls
- OpenWeatherMap server temporarily down

**Solutions:**
1. Check internet connection
2. Try again in a few moments
3. Check firewall settings
4. Test: `ping openweathermap.org`

### Error: "urllib.error.URLError"
**Cause:** Network connectivity issue
**Solution:** Check internet, try again later

### Error: "No module named 'requests'"
**Solution:**
```bash
pip install requests
```

### No output / Program hangs
**Cause:** Possible API timeout
**Solution:** 
1. Check internet connection
2. Try a different city
3. Restart program

## 📊 OpenWeatherMap API Details

### Free Tier Limits
- **Rate Limit:** 60 calls/minute
- **Data Update:** Every 10 minutes
- **History:** None (can't get historical weather)
- **Forecast:** Not included in free tier
- **Locations:** Worldwide coverage

### Weather Conditions Available

The API can return these weather descriptions:
- Clear
- Clouds (Few, Scattered, Broken)
- Rain (Light, Moderate, Heavy)
- Thunderstorm
- Snow
- Mist/Fog
- Drizzle

### Data Precision

- **Temperature:** 1 decimal place (e.g., 15.2°C)
- **Humidity:** Percentage (0-100%)
- **Wind Speed:** m/s (meters per second)
- **Pressure:** hPa (hectopascals)

## 📚 Learning Resources

- [OpenWeatherMap API Docs](https://openweathermap.org/api)
- [OpenWeatherMap Current Weather](https://openweathermap.org/current)
- [Python Requests Library](https://docs.python-requests.org/)
- [JSON in Python](https://docs.python.org/3/library/json.html)
- [HTTP Status Codes](https://httpwg.org/specs/rfc7231.html#status.codes)

## ⚖️ Privacy & Data

### What OpenWeatherMap Collects
- Your location queries
- API key usage
- Approximate request patterns

### Privacy Statement
- They don't sell personal data
- Free tier has some data collection
- See their privacy policy for details

### Local Processing
- All data processed on your computer
- Nothing stored locally unless you save it
- No database created

## 🎯 Project Goals Achieved

✅ Prompt user for city name or ZIP code  
✅ Make API call to OpenWeatherMap  
✅ Parse JSON response  
✅ Display temperature (°C and °F)  
✅ Display humidity percentage  
✅ Display weather condition description  
✅ Display wind speed  
✅ Handle API errors gracefully  
✅ Input validation  

## 📈 Next Steps - Upgrade to Advanced Tier

Enhance this project with:

### 1. **Graphical User Interface (GUI)**
```python
import tkinter as tk
# Create window with input field and result display
```

### 2. **Weather Icons**
```python
from PIL import Image, ImageTk
import requests
# Download and display weather icons from OpenWeatherMap
```

### 3. **5-Day Forecast**
```python
# Use /forecast endpoint instead of /weather
# Show weather for next 5 days
```

### 4. **Hourly Forecast**
```python
# Extract hourly data from forecast response
# Show next 6 hours weather
```

### 5. **Auto-Location Detection**
```python
import requests
# Use ipinfo.io or geolocation API
# Auto-detect user location
```

### 6. **Unit Toggle**
- Button to switch Celsius/Fahrenheit
- Remember user preference

### 7. **Location History**
- Store recently searched cities
- Quick re-search from dropdown

### 8. **Alerts**
- Temperature alerts
- Storm warnings
- Air quality index

## 💡 Tips for Best Results

1. **Use common city names** - "London" works better than "Old Town"
2. **Include country if ambiguous** - "Paris, France" vs "Paris, Texas"
3. **Use ZIP codes for accuracy** - ZIP code is most precise
4. **Check internet** - API requires active connection
5. **Wait for API activation** - New keys take ~10 minutes
6. **Temperature conversions:**
   - °C to °F: (°C × 9/5) + 32
   - °F to °C: (°F - 32) × 5/9

## 📄 Code Statistics

- **Lines of Code:** ~140
- **Functions:** 4
- **API Calls:** 1 per query
- **Data Fields Extracted:** 6
- **External Dependency:** 1 (requests)

## 🤝 Support

If you encounter issues:
1. Verify API key is correct and active
2. Check internet connection
3. Test city name spelling
4. Check OpenWeatherMap status page
5. Try again after a few moments

---

**Enjoy real-time weather data!** 🌤️
