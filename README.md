# Employee Distribution | HR Analytics Dashboard

A comprehensive workforce analytics project that transforms employee records into actionable insights through data cleaning, SQL analysis, and interactive visualizations. Explore workforce demographics, departmental distribution, employee tenure, and termination patterns in a single dashboard.

## Features

- Data cleaning and validation, including invalid ages and future-dated termination records
- 11 PostgreSQL-compatible analytical queries covering workforce trends
- Interactive Plotly dashboard with department, age, gender, location, and hiring visualizations
- Reproducible Python pipeline with CSV and SQLite exports
- Automated generation of datasets and dashboards through GitHub Actions

## Technology Stack

**Python**, **Pandas**, **NumPy**, **PostgreSQL-compatible SQL**, **SQLite**, **Plotly**, **GitHub Actions**

## Dataset

The project uses **22,500 reproducibly generated synthetic employee records**. The generator intentionally includes invalid ages and future termination dates to demonstrate data-quality checks. The records are not real company HR data.

## Getting Started

```bash
git clone https://github.com/gauransht25/employee-workforce-analytics.git
cd employee-workforce-analytics
pip install -r requirements.txt
python generate_data.py
python analyze.py
```

Open `outputs/hr_dashboard.html` in a browser to explore the interactive dashboard.

## Project Structure

```text
employee-workforce-analytics/
├── analyze.py
├── generate_data.py
├── requirements.txt
├── data/
│   └── employees_synthetic.csv
├── sql/
│   └── postgresql_analysis.sql
└── outputs/
    ├── employees_clean.csv
    ├── hr_dashboard.html
    ├── hr_analytics.sqlite
    └── metrics.json
```

## Analytics Covered

Workforce composition by department, role, age band, gender, and location; hiring trends over time; department-level termination share; and employee tenure.

## Notes

The dashboard is an interactive Plotly HTML application rather than a Power BI `.pbix` file. Departmental termination share is descriptive and should not be interpreted as a formal period attrition rate.
