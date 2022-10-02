import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

df = pd.read_excel('tt.xlsx')

#Teht 1

#dataan tutustuminen
desc = df.describe()
print(df.info())
plt.show()

index = ['Peruskoulu', '2.aste', 'Korkeakoulu', 'Ylempi korkeakoulu']
gen = ['Mies', 'Nainen']



education = pd.crosstab(index=df['koulutus'], columns = 'lukumäärä')
education.index = index

# unnecesary lines commented out
education = education.reset_index()
education.columns = ['koulutus', 'lukumäärä']

total = education['lukumäärä'].sum()
#get the percentage of 
education['%'] = round(education['lukumäärä'] / total * 100,2 )



sns.barplot(x='lukumäärä', y= 'koulutus', data=education)
plt.show()


#Teht 2



g_education = pd.crosstab(index=df['koulutus'], columns=df['sukup'])
g_education.index = index
g_education = g_education.reset_index()
g_education.columns = ['koulutus', 'mies', 'nainen']

#Teht 3

p = stats.chi2_contingency(g_education[['mies', 'nainen']])[1]


if p > 0.85:
    print(f'Ei merkitsevä, p={p}')
else:
    print(f'Merkitsevä, p={p}')
    
g_education = pd.melt(g_education, id_vars='koulutus', var_name=['sukupuoli'], value_name='lukumäärä')
    
sns.barplot(x='lukumäärä', y='koulutus', hue='sukupuoli', data=g_education)
plt.show()


#Teht 4

df_corr = df.loc[:, ['sukup', 'ikä', 'perhe', 'koulutus', 'palkka']]
corr=df_corr.corr()


sns.heatmap(corr)
plt.show()

pearson = stats.pearsonr(df_corr['palkka'],df_corr['ikä'])
spearman = stats.spearmanr(df_corr['palkka'],df_corr['ikä'])


sns.regplot(data=df_corr, y='palkka', x='ikä')
plt.show()






