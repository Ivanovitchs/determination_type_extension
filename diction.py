personne=[
    ("ivan",1.9,21),
    ("junior",2,19),
    ("patric",1.8,25),
    ("loic",2,30)
]

def recuper_information(collection,nom):
        for i in collection:
            if i[0]==nom:
                print(str(i)+" a ete retrouve")
                return
            else:
                return None
            

recuper_information(personne,"ivan")