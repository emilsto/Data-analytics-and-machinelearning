import pandas as pd


#Tehtävä 3

df_data = pd.read_csv('Titanic_data.csv')
df_names = pd.read_csv('Titanic_names.csv')

#info
print(df_data.info())
print(df_names.info())
#desc
print(df_data.describe())
print(df_names.describe())

#histogrammi
hist = df_data.hist(bins = 4)

df = pd.merge(df_data, df_names, how='inner', on='id')

#monta henkilöä?
passengers_total = df['id'].count()

#miestä?
men =sum(df.GenderCode==0)
#naista?
women = sum(df.GenderCode==1)
#keski-ikä?
median_age = round(df['Age'].mean(),2)

#nollan ikäistä?
age_zero_count = sum(df.Age==0)



#Tehtävä 4

#korvaa 0 arvot keski-iällä
df['Age'].replace(to_replace = 0, value = median_age, inplace=True)

#PClasses uniikit arvot
print(df.PClass.unique())

#Kenellä on *?
print(df.loc[df['PClass'] == '*'])

#survived?
survived =sum(df.Survived==1)
#not-survived
not_survived = sum(df.Survived==0)


print("Selvietyneet % =", round(survived * 100 / passengers_total, 1))
print("Ei-Selvietyneet % =", round(not_survived * 100 / passengers_total, 1))

survived_women = ((df.GenderCode==1)&(df.Survived==1)).sum()
survived_men = ((df.GenderCode==0)&(df.Survived==1)).sum()





