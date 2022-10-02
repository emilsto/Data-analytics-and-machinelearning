import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

#Tehtävä 1

df_emp = pd.read_csv('employees.csv', header=0, dtype={'phone1':str, 'phone2':str})
df_dep = pd.read_csv('departments.csv')

desc_emp = df_emp.describe()
desc_dep = df_dep.describe()

df = pd.merge(df_emp, df_dep, how='left', on='dep')


df.drop(labels='image', inplace=True, axis='columns')



#Tehtävä 2


#Laske työntekijät, joilla etunimi
workers = df['fname'].count()
print('Työntekijät: ', workers)


#Sukupuolijakauma -> True = f, False = m
men =sum(df.gender==0)
wimen =sum(df.gender==1)

percentage_of_men = round(men * 100 / workers, 1)
percentage_of_women = round(wimen * 100 / workers, 1)



#Suurin palkka
print ("suurin palkka:", df_emp['salary'].max())
#Pienin palkka
print ("pienin palkka:", df_emp['salary'].min())
#Keskipalkka
print ("keskipalkka:", round(df_emp['salary'].mean(),2))

#Tuotekehitys palkka
print("TUotekehityspalkka keskiarvo:", df[df['dname']=='Tuotekehitys']['salary'].mean())

#Työntekijät, joilla ei kakkospuhelinta
print (df_emp['phone2'].isnull().sum())


#Työntekijöiden iät
df['age'] = (datetime.now() - pd.to_datetime(df['bdate'])) // timedelta(days=365.2425)
df['age_group'] = pd.cut(df['age'], bins = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70], labels = ['20','25','30','35','40','45','50','55','60','65','70'], right=False)

#salary age corr
df_s_a_g = df.loc[:, ['salary', 'age', 'gender']]
corr = df_s_a_g.corr()
sns.heatmap(corr, annot=True)
plt.show()

#save to csv file
df.to_csv('emp-dep.csv', index=False)








