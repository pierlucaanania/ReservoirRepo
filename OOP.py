''' OOP: Classi e Istanze'''

class Studente:

    '''Metodo Costruttore'''
    def __init__(self, nome, cognome, corso_di_studi):
        self.nome = nome
        self.cognome = cognome
        self.corso_di_studi = corso_di_studi


studente1 = Studente('Luca','Rossi','Matematica')
studente2 = Studente('Marta','Biacnhi','Fisica')

print(f'Dati studente: {studente1} e {studente2}')