from flask import Flask, render_template, request, abort
from database import get_db
import math

app = Flask(__name__)


class Config:
    DATABASE = "universities.db"
    PER_PAGE = 20


app.config.from_object(Config)


@app.route("/")
def index():
    year = request.args.get("year", "")
    search = request.args.get("search", "").strip()
    country = request.args.get("country", "").strip()
    page = request.args.get("page", 1, type=int)

    if page < 1:
        page = 1

    per_page = app.config["PER_PAGE"]

    try:
        conn = get_db()

        base_query = """
        FROM universities
        JOIN countries ON universities.country_id = countries.id
        WHERE 1=1
        """
        params = []

        if year:
            base_query += " AND universities.year = ?"
            params.append(year)

        if search:
            base_query += " AND universities.institution LIKE ?"
            params.append(f"%{search}%")

        if country:
            base_query += " AND countries.country = ?"
            params.append(country)

        total = conn.execute(
            f"SELECT COUNT(*) {base_query}", params
        ).fetchone()[0]

        total_pages = math.ceil(total / per_page) if total > 0 else 1

        if page > total_pages:
            page = total_pages

        offset = (page - 1) * per_page

        universities = conn.execute(
            f"""
            SELECT universities.institution,
                   universities.rank,
                   universities.score,
                   universities.year,
                   countries.country
            {base_query}
            ORDER BY universities.year, universities.rank, universities.institution
            LIMIT ? OFFSET ?
            """,
            params + [per_page, offset]
        ).fetchall()

        years = conn.execute(
            "SELECT DISTINCT year FROM universities ORDER BY year"
        ).fetchall()

        countries = conn.execute(
            "SELECT DISTINCT country FROM countries ORDER BY country"
        ).fetchall()

        conn.close()

    except Exception:
        abort(500)

    start_num = 0
    end_num = 0
    if total > 0:
        start_num = offset + 1
        end_num = offset + len(universities)

    return render_template(
        "index.html",
        universities=universities,
        years=years,
        countries=countries,
        selected_year=year,
        selected_country=country,
        search=search,
        page=page,
        total_pages=total_pages,
        total=total,
        start_num=start_num,
        end_num=end_num
    )


@app.route("/university/<name>")
def detail(name):
    try:
        conn = get_db()

        data = conn.execute(
            """
            SELECT universities.institution,
                   universities.year,
                   universities.rank,
                   universities.score,
                   countries.country
            FROM universities
            JOIN countries ON universities.country_id = countries.id
            WHERE universities.institution = ?
            ORDER BY universities.year DESC
            """,
            (name,)
        ).fetchall()

        conn.close()

    except Exception:
        abort(500)

    if not data:
        abort(404)

    return render_template("detail.html", data=data, name=name)


@app.route("/stats")
def stats():
    try:
        conn = get_db()

        data = conn.execute(
            """
            SELECT countries.country, COUNT(*) AS total
            FROM universities
            JOIN countries ON universities.country_id = countries.id
            GROUP BY countries.country
            ORDER BY total DESC, countries.country
            LIMIT 10
            """
        ).fetchall()

        total_countries = conn.execute(
            "SELECT COUNT(*) FROM countries"
        ).fetchone()[0]

        total_universities = conn.execute(
            "SELECT COUNT(*) FROM universities"
        ).fetchone()[0]

        conn.close()

    except Exception:
        abort(500)

    top_country = data[0]["country"] if data else ""
    top_total = data[0]["total"] if data else 0

    return render_template(
        "stats.html",
        data=data,
        top_country=top_country,
        top_total=top_total,
        total_countries=total_countries,
        total_universities=total_universities
    )


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True, port=5005)