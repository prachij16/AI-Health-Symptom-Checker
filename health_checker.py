import pandas as pd
from sklearn.tree import DecisionTreeClassifier

#-----load datasets-----
data = pd.read_csv("dataset.csv")
print(data.head())

x=data.drop('Disease',axis=1)
y=data['Disease']

#-------train model------
model=DecisionTreeClassifier()
model.fit(x,y)

#----list of symptoms-----
symptoms=list(x.columns)

print("avialable symptoms:")
for s in symptoms:
    print("-",s)

#-----user input-----
user_input=input("entre symptoms(seperated by comma): ").split(",")

# ----create vector------
input_data=[0]*len(symptoms)

for symptom in user_input:
    symptom=symptom.strip()
    if symptom in symptoms:
        index=symptoms.index(symptom)
        input_data[index]=1

prediction=model.predict([input_data])
probabiility=model.predict_proba([input_data])
confidence=max(probabiility[0])*100

print("Possible Disease:",prediction[0])

print("confidence level: " ,round(confidence,2),"%")