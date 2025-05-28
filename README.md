# In-Flight Meal Forecast 
This is a Django-based web application that forecasts the number of in-flight meal orders using time series prediction models.

# Purpose
Built as part of an AI/ML assessment task to demonstrate time series forecasting in a real-world scenario.

# Project Overview
The application allows users to:
- Upload or use existing in-flight meal data.
- Input a desired number of future days to forecast.
- Generate a line plot showing predicted trends with confidence intervals.
- View total meal order trends over time.

The model used for forecasting is Facebook Prophet.

# Project Structure
forecast_project/
│
├── forecast_app/
│   ├── migrations/
│   ├── templates/
│   │   └── forecast_app/
│   │       └── forecast.html
│   ├── views.py
│   ├── models.py
│   └── ...
│
├── forecast_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── Flight Catering Daily Orders_Jan to March 2024.csv
├── manage.py
```

# How to Run

1. **Clone the Repository**
```bash
git clone https://github.com/ayishamanzoor2024/InFlight-Meal-Forecast.git
cd InFlight-Meal-Forecast
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```
If not available, install manually:
```bash
pip install django pandas prophet matplotlib
```

3. **Run Server**
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser.

4. **Forecast**
Enter the number of days to forecast and view the plotted results.

## 📷 Screenshot

_Example:_
![Forecast Example](https://user-images.githubusercontent.com/your-placeholder-link)

# Technologies Used
- Python
- Django
- Prophet (for time series forecasting)
- Pandas
- Matplotlib

# Author
Ayisha Manzoor  
[GitHub Profile](https://github.com/ayishamanzoor2024)

# License
This project is intended for demonstration and educational purposes only.
