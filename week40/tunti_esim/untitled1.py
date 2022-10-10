import pandas as pd
import pickle

#lataa malli
with open('startup-model.pickle', 'rb') as f:
    model = pickle.load(f)
    
with open('startup-ct.pickle', 'rb') as f:
    ct = pickle.load(f)
    
with open('startup-scaler-x.pickle', 'rb') as f:
    scaler_x = pickle.load(f)
    

with open('startup-scaler-y.pickle', 'rb') as f:
     scaler_y = pickle.load(f)



Xnew = pd.read_csv('new_company_ct.csv')
Xnew_org = Xnew
Xnew = ct.transform(Xnew)


Xnew = scaler_x.transform(Xnew)

ynew = scaler_y.inverse_transform(model.predict(Xnew))

for i in range (len(ynew)):
    print(f'{Xnew_org.iloc[i]}\nVoitto: {ynew[i] [0]}\n')
    
    
coef = model.coef_
inter = model.intercept_