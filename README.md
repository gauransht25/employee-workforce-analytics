# Employee Distribution | HR Analytics Dashboard

An independent implementation of workforce analytics, inspired by the topics of [Tushar Aggarwal's Employee-Distribution](https://github.com/tushar2704/Employee-Distribution). Not a fork or a reproduction of the author's metrics.

## Data provenance
22,500 seeded **synthetic** HR records, with intentionally invalid ages and future-dated terminations for demonstrating data-quality checks. Results must not be represented as actual employer metrics.

## Run
```bash
pip install -r requirements.txt
python analyze.py
```

## Deliverables
Python cleaning and analysis pipeline, PostgreSQL-compatible SQL with 11 workforce questions, a self-contained Plotly HTML dashboard, and CSV/SQLite exports.

**Limitations:** HTML/Plotly dashboard, not a native Power BI PBIX. Termination share is not a formal period attrition rate.
