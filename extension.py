

'''def extraire_extension(fichier,definition_extension):
    fiche=[]
    for i in fichier:
        if i.find(".")>0:    
            fichiers=i.split(".")
            fiche==fiche.append(fichiers[-1])
    print(fiche)

    for f in fiche:
        for e in definition_extension:
            if f.lower()==e[0]:
                print(f+"(" + e[1]+")")
            

    return fiche'''
fichiers=["nodepad.exe","mon.fichier.perso.doc","note.TXT","vacance.jpeg","planning","data.dat"]    

definition_extension=((
    "doc","Document word"),
    ("exe","executable"),
    ("txt","Document Text"),
    ("jpeg","Image Jpeg")
    )

def extraire_extensions(fichiers):
        extension_extrait=fichier.split(".")
        if len(extension_extrait)>1:
            return extension_extrait[-1]
        return 
        
def definition_extensions(extension,definition):
    for i in definition:
        if i[0]==extension:
            return i[1]
        return None
    
for fichier in fichiers:
    extrait=extraire_extensions(fichier)
    if extrait:
        definition=definition_extensions(extrait,definition_extension)
        if definition==None:
            definition="Extension Non reconnue"
    else:
        definition="Aucune extension"
    print(fichier + "(" + definition + ")")



        


