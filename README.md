# Top University Rankings Web Application

## Overview
This project is a database-driven Flask web application that presents top university ranking data using a SQLite database. Users can browse universities, search by name, filter by year and country, view detailed information for an individual university, and explore summary statistics by country.

The application was developed for the CS551P Advanced Programming assessment. It uses open data, Flask, SQLite, HTML, and CSS, and it does not use JavaScript in order to comply with the coursework requirements. 

## Features
- View university rankings with pagination
- Search universities by name
- Filter universities by year
- Filter universities by country
- View a detail page for each university
- View a statistics page with country-level summaries
- Custom 404 error page
- Unit tests for core routes and functionality
- Deployment on Render

## Design and Development
The aim of the project was to create a clear and usable web application for exploring university ranking data. The dataset was chosen because it supports meaningful searching, filtering, and country-based analysis.

The application uses two linked tables in SQLite:
- `countries`
- `universities`

The `universities` table stores ranking data and links each university to a country using `country_id`. This structure makes filtering, grouping, and aggregate analysis easier.

The application is built around multiple Flask routes:
- `/` for browsing and filtering the ranking list
- `/university/<name>` for viewing university details
- `/stats` for country-based statistics
- a custom 404 page for invalid routes

## Technologies Used
- Python
- Flask
- SQLite
- HTML
- CSS
- Gunicorn
- Git
- Render

## Project Structure
- `app.py` - main Flask application
- `database.py` - database connection and table creation
- `load_data.py` - script to load CSV data into SQLite
- `cwurData.csv` - dataset source file
- `universities.db` - SQLite database
- `templates/` - HTML templates for all pages
- `test_app.py` - unit tests
- `requirements.txt` - project dependencies
- `README.md` - project documentation
- `git-log.txt` - Git history for submission

## Database Design
The database contains two linked tables.

### `countries`
Stores country names.

### `universities`
Stores university ranking data, including:
- institution name
- rank
- score
- year
- linked `country_id`

This relationship supports filtering, detail pages, and country-level statistics.

## Application Usage
The application includes the following pages:

- **Home page**: browse rankings, search, filter by year and country, and move between pages using pagination.
- **Detail page**: view ranking history and details for a selected university.
- **Statistics page**: see the top countries by number of universities in the dataset.
- **404 page**: shown when a user visits a page that does not exist.

## Installation and Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/Lovish123-tech/top-university-rankings.git
cd top-university-rankings
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Load the data into the database
```bash
python3 load_data.py
```

### 5. Run the application
```bash
python3 app.py
```

### 6. Open in browser
```bash
http://127.0.0.1:5000
```

## Testing
Run the test suite with:

```bash
python3 -m unittest test_app.py
```

The tests check key routes such as the home page, statistics page, search/filter behaviour, and 404 handling.

## Deployment
The application is deployed on Render.

### Build command
```bash
pip install -r requirements.txt
```

### Start command
```bash
gunicorn app:app
```

### Live deployment
- Render URL: https://top-university-rankings.onrender.com

Render supports automatic deployment when changes are pushed to the connected Git repository. 

## Maintenance
The following steps can be used to maintain or update the project:

### Update the dataset
If the source CSV changes, reload the database by running:

```bash
python3 load_data.py
```

### Run tests after code changes
```bash
python3 -m unittest test_app.py
```

### Update dependencies
If a new package is added, update:

```bash
requirements.txt
```

### Redeploy the application
Push the latest code to GitHub and allow Render to redeploy automatically, or trigger a manual deploy from the Render dashboard. Render documents both automatic and manual deploy options. 

## Git and Version Control
Git was used during development for source control. The coursework also requires a Git log file generated with:

```bash
git log --pretty=format:'%h : %s' --graph > git-log.txt
```

## Useful Links
- GitHub repository: https://github.com/Lovish123-tech/top-university-rankings.git
- Render deployment: https://top-university-rankings.onrender.com
- Open Data Information: [Kaggle.com](https://www.kaggle.com)
- Render documentation: [Render Docs](https://render.com/docs)
- Render deploys: [Deploying on Render](https://render.com/docs/deploys)

## Author
Lovish