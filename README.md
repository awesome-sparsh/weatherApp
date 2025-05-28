Developed by Sparsh Sethi
    https://www.sparshsethi.com
    https://github.com/awesome-sparsh/

🌤️ Weather Detector – Django Web App
    A beautiful and functional weather detection web application built using Django and styled with Tailwind CSS. Users can search for a location and receive real-time weather data using the OpenWeatherMap API.

🚀 Features
    🔍 Search weather by city or city,country format

    🌡️ Displays real-time temperature, humidity, wind speed, visibility, and more

    📍 Shows geographic coordinates and timezone

    🌅 Displays sunrise and sunset times

    ⚠️ Handles API errors (e.g., invalid location or server timeout)

    🎨 TailwindCSS + glassmorphism UI design

🛠️ Tech Stack
    Technology	Role
    Python 3	Programming language
    Django 5.2.1	Web framework
    HTML/CSS/JS	Frontend UI and validation
    Tailwind CSS	Styling and responsive design
    OpenWeatherMap API	Weather data source
    jQuery	Client-side form validation

⚙️ How It Works
    🔁 Workflow
        User Input:
        1. The user types a location in the input box and clicks "Get Weather".
        2. Form validation is handled via JavaScript (index.js).
        3. Backend Processing (views.py):
            3.1. POST request is captured in the index() view.
            3.2. The location is encoded and queried via OpenWeatherMap API.
            3.3. The returned JSON is parsed to extract:
                3.3.1. Coordinates
                3.3.2. Temperature (current, min, max, feels-like)
                3.3.4. Humidity, wind, visibility
                3.3.5. Timezone, sunrise & sunset
            3.4. Proper error handling is done for:
                3.4.1. ❌ Location not found
                3.4.2. 🔁 Server failure (timeout, connection issues)
        4. Frontend Rendering (index.html):
            4.1. TailwindCSS + glass UI render dynamic data blocks
            4.2. Displays success or error messages based on API response

🔐 Environment Setup
    1. Clone the Repo:
        git clone https://github.com/yourusername/weather-detector.git
        cd weather-detector
    2. Install Dependencies:
        pip install django
    3. Run the Server:
        python manage.py runserver
    4. Visit:
        http://127.0.0.1:8000/

🔑 API Key
    This project uses the OpenWeatherMap API.
    You can get your own API key from: https://openweathermap.org/api
    Update this line in views.py:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={encoded_location}APPID=<your_api_key>&units=metric'

📌 Notes
    The app doesn't use Django's ORM/database for storing data since it's a live-fetch-only app.
    Extendable: Add user history, weather maps, hourly forecasts, etc.

🧠 Learnings and Use of Django
    Used Django's request/response handling to manage form submission.
    Demonstrated clean use of views, template rendering, URL routing, and static file handling.
    Applied Django's CSRF protection and template language features.
    Ideal example of a single-view Django application focusing on clean, API-driven frontend logic.

📄 License
    This project is licensed under the MIT License.
