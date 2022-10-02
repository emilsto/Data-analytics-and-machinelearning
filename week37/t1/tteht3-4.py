import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


#T4

#ORead data
df = pd.read_csv('titanic.csv')


#Age group pilars
bins = []

for i in range(0,95,5):
    bins.append(i)
labels = bins[1:] 
df['age_group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=True)
df['age_group']=df['age_group'].astype(int)



#Lasketaan selvinneiden määrä ja kokonaismäärä
female_surv = len(df[(df['Survived']==1) & (df['GenderCode']==1)])
male_surv = len(df[(df['Survived']==1) & (df['GenderCode']==0)])
everyone = df.shape[0]

df_surv = pd.Series([female_surv,male_surv],index=['naiset','miehet'],name='selviytyneet')

#Piechart survved
df_surv.plot(kind='pie',ylabel=df_surv.name,labels=df_surv.index,
             title=f'Matkustajat: {everyone}\n Selviytyneet miehet: {male_surv}\n Selviytyneet naiset: {female_surv}',
             startangle=270, autopct='%1.1f%%')
plt.show()


df.to_csv('titanic.csv',index=False)

per_ageg = df.age_group.value_counts().sort_index()
per_ageg.plot(kind='bar')
plt.show()


df['Saved'] = df['Survived'] 
df['Saved'] = df['Saved'].map(
                   {1:'yes' ,0:'no'}) 


#Boxplot survived
sns.boxplot(data=df, x='PClass', y='Age', hue='Saved')
plt.show()


#Remove *
df = df[df.PClass != '*']

df['Age'] = df['Age'].replace(0,30.397989)


gvc = df['Survived'].value_counts()
gvc.plot(kind='pie', ylabel='', labels=['miehet', 'naiset'],
         startangle=180, autopct='%1.1f%%')
plt.show()


#swarmplot of dead and not-so-dead
sns.swarmplot(data=df, x='PClass', y='Age', hue='Survived')
plt.show()
