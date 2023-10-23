''' OOP: Classi e Istanze'''

class Studente:

    '''Metodo Costruttore'''
    def __init__(self, nome, cognome, corso_di_studi):
        self.nome = nome
        self.cognome = cognome
        self.corso_di_studi = corso_di_studi

    def scheda_personale(self):
        return (f'Scheda Studente:\n Nome:{self.nome}\n '
                f'Cognome:{self.cognome}\n '
                f'Corso Di Studi:{self.corso_di_studi}')

studente1 = Studente('Luca','Rossi','Matematica')
studente2 = Studente('Marta','Biacnhi','Fisica')

print(studente1.scheda_personale())
print(studente2.scheda_personale())

print(Studente.scheda_personale(studente1))