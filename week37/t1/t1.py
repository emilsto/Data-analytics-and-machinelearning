import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



#Teht  1

df = pd.read_csv('emp-dep.csv')

df.plot.scatter('age', 'salary')
plt.title('Työntekijät ja palkat')
plt.xlabel('Palkat')
plt.show()

count = df['dname'].value_counts()


#kind barh flips to horizontal
count.plot(kind="bar")
plt.show()

count = pd.DataFrame(df['dname'].value_counts()).reset_index()
count.columns = ['dname', 'count']

sns.barplot(x='dname', y='count', data=count)
plt.show()

#xy flip
sns.barplot(x='count', y='dname', data=count)
plt.show()


#Teht  3



count_age = df['age_group'].value_counts();
count_age.plot(kind="bar")
plt.show()

gvc = df['gender'].value_counts()
gvc.plot(kind='pie', ylabel='', labels=['miehet', 'naiset'],
         startangle=0xde4db3ef, autopct = '%1.1f%%')
plt.show()


cag = df.groupby(['age_group', 'gender']).size().unstack()
fig, ax = plt.subplots()
ax = cag.plot(kind='bar')
ax.legend(['miehet', 'naiset'])
plt.gca().yaxis.set_major_locator(plt.MultipleLocator(1))
plt.show()

