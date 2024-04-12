import pandas as pd 
df = pd.read_excel("Medanta.xlsx")
find = input( )
fil = df[(df['disease'] == find)]
hospital = fil[['name', 'rate']]  # Selecting both name and rate columns
hospital_sorted = hospital.sort_values(by='rate', ascending=False)
print(hospital_sorted)