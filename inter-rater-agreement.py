from sklearn.metrics import cohen_kappa_score
import pandas as pd
import math

df = pd.read_excel ('Comparison RBTM - Expert.xlsx', engine='openpyxl')

rbtm_risk = [x if (x == 'H' or x == 'M' or x == 'L') else '0' for x in df['risk\''].tolist()] 
expert_risk =  [x if (x == 'H' or x == 'M' or x == 'L') else '0' for x in df['Mode'].tolist()]

print(cohen_kappa_score(rbtm_risk, expert_risk))
