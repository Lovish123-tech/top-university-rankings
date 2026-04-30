# Top University Rankings Web Application

## Overview
This project is a Flask web application that displays top university rankings using data stored in a SQLite database.  
Users can browse universities, search by name, filter by year and country, view detailed university information, and see statistics by country.

## Features
- View university rankings with pagination
- Search universities by name
- Filter by year
- Filter by country
- View detailed information for each university
- View statistics page
- Custom 404 error page
- Basic unit tests

## Technologies Used
- Python
- Flask
- SQLite
- HTML
- CSS

## Project Structure
- `app.py` - main Flask application
- `database.py` - database connection
- `load_data.py` - script to load CSV data into SQLite
- `universities.db` - SQLite database
- `templates/` - HTML templates
- `test_app.py` - unit tests

## How to Run Locally
1. Create and activate a virtual environment
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python3 app.py
   ```
4. Open in browser:
   ```bash
   http://127.0.0.1:5000
   ```

## How to Run Tests
```bash
python3 -m unittest test_app.py
```

## Deployment
This project can be deployed on Render using:
- Build command:
  ```bash
  pip install -r requirements.txt
  ```
- Start command:
  ```bash
  gunicorn app:app
  ```

## Author
Lovish