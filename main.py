
nom_chauffeur=["Ivan","Junior","landry","Mathieu","Tonton","tata"]
distance_km=[2.4,5.7,1.5,0.5,0.4,1]
index=0
liste=[("junior",1),("ivan",2),("kaki",7),("toti",10),("fabrice",15),("williams",70),("merline",70)]
valeurmin=liste[0][1]
for i in range(len(liste)):
    if valeurmin<liste[i][1]:
        valeurmin=liste[i][1]
        index=i
print("le chauffeur le plus loin est : "+liste[index][0] + " il es à " + str(valeurmin) + " km de vous")
