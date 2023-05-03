import sqlite3

print("Application de Gestion de budget avec Python et Sqlite3")
connection = sqlite3.connect("budget.db")
cursor = connection.cursor()
cursor.execute("create table if not exists budget(id integer primary key autoincrement, le_type text, montant numeric, son_type text, montant1 numeric, complet BOOLEAN)")
    

def la_depense_budget():
    print("Remplissez la liste de vos dépense:")
    le_type = input("donnez le type de depense que voulez-vous ajoutée:\n")
    print(le_type)
    montant = input("donnez le montant de votre dépense:")
    print(montant)
    cursor.execute("insert into budget (le_type, montant) values (?,?)", (le_type, montant,))
    print("la dépense est ajoutée")
    connection.commit()
    return montant, le_type
la_depense_budget()
        
            
def le_revenu_budget():
    print("Remplissez la liste de vos revenus:")
    son_type = input("donnez le type de revenu que vous voulez ajouté:\n")
    print(son_type)
    montant1 = float(input("donnez le montant de votre revenu:"))
    print(montant1)
    cursor.execute("insert into budget (son_type, montant1) values (?, ?)", (son_type, montant1,))
    print("le revenu a été consulté")  
    connection.commit()
    return montant1, son_type
le_revenu_budget()
        
 
def ecart_budget(): 
    ecart_budget = cursor.execute("SELECT * FROM budget").fetchall()
    return ecart_budget
ecart_budget()
            
while True:
    choix =""
    print("       Que voulez-vous faire maintenant ?      ")
    print("                                         ")
    print("   C) Voir l'ecart qui existe entre la dépense et le revenu")
    print("   0) quitter l'application")
    choix = input("quel est votre désire:\n")
    if choix == "C" or choix == "c":
        montant1 = float(input("redonnez le montant du revenu:"))
        montant = float(input("redonnez le montant de la depense:"))
        print("l'ecart qui existe est de:",montant1-montant)
        ecart_budget()
    elif choix == "0" or choix == "o" or choix == "O":
        print("Quitter")
        exit()
    else:
        print("votre choix n'est pas reconnu" )
        
    