import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('emp-dep.csv')

# työntekijät ikäryhmittäin (miehet-naiset)
df_ag = pd.crosstab(index=df['age_group'], columns=df['gender']).reset_index()
df_ag.columns = ['age_group', 'male', 'female']

p_m = df_ag['male'].sum()
p_f = df_ag['female'].sum()
tot = p_m + p_f

df_ag.plot(kind='bar', x='age_group')
plt.show()

# jos haluaa visualisoinnin seabornilla, pitää tehdä myös melt
df_agm = pd.melt(df_ag, id_vars='age_group', var_name=['gender'],
                  value_name='count')

# seabornilla visualisointi, huom. hue
sns.barplot(x='age_group', y='count', hue='gender', 
            data=df_agm)
plt.show()

# lisätään prosenttiosuudet alkuperäiseen ristiintaulukointiin meltin jälkeen
df_ag['% male'] = (df_ag['male'] / tot * 100)
df_ag['% female'] = (df_ag['female'] / tot * 100)



# työntekijät osastoittain (miehet-naiset)
df_dg = pd.crosstab(index=df['dname'], columns=df['gender']).reset_index()
df_dg.columns = ['dname', 'male', 'female']


df_dgm = pd.melt(df_dg, id_vars='dname', var_name='gender',
                  value_name='count')

sns.barplot(x='count', y='dname', hue='gender', 
            data=df_dgm)
plt.show()

