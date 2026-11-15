"""Generate reproducible SYNTHETIC employee data (no real employee information)."""
from pathlib import Path
import numpy as np,pandas as pd
ROOT=Path(__file__).resolve().parent
def main():
 rng=np.random.default_rng(20261115);n=22500
 departments=['Engineering','Sales','Marketing','Finance','HR','Operations','Legal','Support']
 titles=['Associate','Analyst','Specialist','Manager','Director']
 states=['California','Texas','New York','Florida','Washington','Illinois']
 locations=['Headquarters','Remote','Hybrid','Regional']
 ages=rng.integers(21,65,size=n)
 ages[:967]=rng.choice([16,17,101,105],967)
 hire=pd.to_datetime('2000-01-01')+pd.to_timedelta(rng.integers(0,7300,size=n),unit='D')
 term=[]
 for i,h in enumerate(hire):
  if rng.random()<0.27:
   maxdays=max(1,(pd.Timestamp('2026-11-15')-h).days)
   term.append(h+pd.Timedelta(days=int(rng.integers(1,maxdays+1))))
  else:term.append(pd.NaT)
 for i in range(967,2566):term[i]=pd.Timestamp('2027-01-01')+pd.Timedelta(days=int(rng.integers(0,365)))
 df=pd.DataFrame({'employee_id':np.arange(1,n+1),'department':rng.choice(departments,n),'job_title':rng.choice(titles,n),'gender':rng.choice(['Female','Male','Non-binary'],n,p=[.48,.49,.03]),'age':ages,'state':rng.choice(states,n),'work_location':rng.choice(locations,n),'hire_date':pd.to_datetime(hire).strftime('%Y-%m-%d'),'termination_date':pd.to_datetime(term).strftime('%Y-%m-%d')})
 (ROOT/'data').mkdir(exist_ok=True)
 df.to_csv(ROOT/'data/employees_synthetic.csv',index=False)
 print('Generated',len(df),'synthetic records')
if __name__=='__main__':main()
