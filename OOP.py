''' OOP: Classi e Istanze'''

class Studente:

    #variabile di Classe:
    ore_settimanali = 36
    corpo_studentesco = 0

    '''Metodo Costruttore'''
    def __init__(self, nome, cognome, corso_di_studi):    #attributi -> variabili di Istanza
        self.nome = nome
        self.cognome = cognome
        self.corso_di_studi = corso_di_studi
        Studente.corpo_studentesco += 1
    def scheda_personale(self):
        return (f'Scheda Studente:\n Nome:{self.nome}\n '
                f'Cognome:{self.cognome}\n '
                f'Corso Di Studi:{self.corso_di_studi}\n'
                f'Ore Settimanali:{self.ore_settimanali}')

studente1 = Studente('Luca','Rossi','Matematica')
studente2 = Studente('Marta','Biacnhi','Fisica')

print(f'Totale studenti: {Studente.corpo_studentesco}')
studente1.ore_settimanali += 4

#print(studente1.scheda_personale())
#print(studente2.scheda_personale())

print(Studente.scheda_personale(studente1))