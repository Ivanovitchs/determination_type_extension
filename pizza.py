def afficherpizza(pizza,nbr=0):
    print("Liste des pizzas ("+str(len(pizza))+")")
    if pizza==():
        print("pas de pizza aujourdhui ")
        return
    if nbr==0:
        for i in pizza:
            print(i)
    else:
        for i in range(nbr):
            print(pizza[i])
    print()
    print("la premiere pizza est : " +pizza[0])
    print("la derniere pizza est : " +pizza[-1])
   

def pizzaajouter(pizza):
    ajout_pizza=input("pizza a ajouter : " )
    van=verfier_pizza(pizza,ajout_pizza)
    if van==True:
        print("cette pizza existe deja")
        return pizza
    pizza.append(ajout_pizza)
    return pizza

def  verfier_pizza(pizza,ajouter_pizza):
    for i in pizza:
        if i == ajouter_pizza:
            return True
    return False
    

pizzas=["04 au fromage", "végetarienne" ,"hawai", "calzone"]
afficherpizza(pizzaajouter(pizzas),3)