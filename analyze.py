"""HR analytics with synthetic data; PostgreSQL-compatible SQL provided separately."""
from pathlib import Path
import pandas as pd,numpy as np,sqlite3,json,plotly.express as px
ROOT=Path(__file__).resolve().parent
AS_OF=pd.Timestamp('2026-11-15')
def main():
    raw=pd.read_csv(ROOT/'data/employees_synthetic.csv',parse_dates=['hire_date','termination_date'])
    invalid_age=(raw.age<18)|(raw.age>100)
    future_term=raw.termination_date.notna()&(raw.termination_date>AS_OF)
    df=raw.loc[~invalid_age & ~future_term].copy()
    df['terminated']=df.termination_date.notna()&(df.termination_date<=AS_OF)
    df['age_band']=pd.cut(df.age,bins=[17,24,34,44,54,100],labels=['18–24','25–34','35–44','45–54','55+'])
    df['tenure_years']=((df.termination_date.fillna(AS_OF)-df.hire_date).dt.days/365.25).clip(lower=0)
    df['hire_year']=df.hire_date.dt.year
    (ROOT/'outputs').mkdir(exist_ok=True)
    df.to_csv(ROOT/'outputs/employees_clean.csv',index=False)
    with sqlite3.connect(ROOT/'outputs/hr_analytics.sqlite') as conn:df.to_sql('employees_clean',conn,index=False,if_exists='replace')
    metrics={'source':'synthetic, seeded random generator','as_of':'2026-11-15','raw_records':len(raw),'invalid_age_records':int(invalid_age.sum()),'future_termination_records':int(future_term.sum()),'clean_records':len(df),'terminated_records':int(df.terminated.sum()),'average_terminated_tenure_years':round(float(df.loc[df.terminated,'tenure_years'].mean()),2),'largest_age_band':str(df.age_band.value_counts().idxmax()),'highest_turnover_department':str(df.groupby('department').terminated.mean().idxmax())}
    (ROOT/'outputs/metrics.json').write_text(json.dumps(metrics,indent=2))
    figs=[px.bar(df.groupby('department',as_index=False).agg(employees=('employee_id','count'),turnover_rate=('terminated','mean')).sort_values('turnover_rate',ascending=False),x='department',y='turnover_rate',title='Termination share by department'),px.histogram(df,x='age_band',color='gender',barmode='group',title='Employee age and gender distribution'),px.bar(df.groupby(['hire_year','work_location'],as_index=False).size(),x='hire_year',y='size',color='work_location',title='Hiring by year and work location'),px.bar(df.groupby('state',as_index=False).size().sort_values('size',ascending=False),x='state',y='size',title='Employees by state')]
    html='<!DOCTYPE html><html><head><meta charset="utf-8"><title>Workforce Analytics</title><style>body{font-family:Arial;background:#f4f7fb;color:#172b4d;margin:32px}.kpis{display:flex;gap:18px;flex-wrap:wrap}.kpi{background:white;border-radius:12px;padding:22px;box-shadow:0 3px 15px #ddd;min-width:170px}section{background:white;margin-top:20px;padding:12px;border-radius:12px}</style></head><body><h1>Employee Distribution | HR Analytics</h1><p>Reproducible synthetic dataset • As of 2026-11-15</p><div class="kpis">'
    for label,value in [('Employees analyzed',metrics['clean_records']),('Invalid ages removed',metrics['invalid_age_records']),('Future terminations removed',metrics['future_termination_records']),('Avg terminated tenure (years)',metrics['average_terminated_tenure_years'])]:html+=f'<div class="kpi"><strong>{label}</strong><h2>{value}</h2></div>'
    html+='</div>'
    for i,fig in enumerate(figs):html+='<section>'+fig.to_html(full_html=False,include_plotlyjs=(True if i==0 else False))+'</section>'
    html+='</body></html>'
    (ROOT/'outputs'/'hr_dashboard.html').write_text(html)
    print(json.dumps(metrics,indent=2))
if __name__=='__main__':main()
