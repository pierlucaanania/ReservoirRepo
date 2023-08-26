class Persona:

    def __init__(self, nome, cognome, età, residenza):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.residenza = residenza

    def scheda_personale(self):
        scheda = f'''
                     Nome: {self.nome}
                     Cognome: {self.cognome}
                     Età: {self.età}
                     Residenza: {self.residenza}'''
        return scheda

    def modifica_scheda(self):
        print('''Modifica scheda:
        1 - Nome
        2 - Cognome
        3 - Età
        4 - Residenza''')
        scelta = input('Cosa modificare? ')
        if scelta == '1':
            self.nome = input('Inserisci nuovo nome: ')
        if scelta == '2':
            self.cognome = input('Inserisci nuovo cognome: ')
        if scelta == '3':
            self.età = input('Inserisci nuova età: ')
        if scelta == '4':
            self.residenza = input('Inserisci nuova residenza:')

#Classe Figlia

class Studente(Persona):
    profilo = 'Studente'
    def __init__(self, nome, cognome, età, residenza, corso):
        super().__init__(nome,cognome,età,residenza)
        self.corso = corso
    def scheda_personale(self):
        scheda = f'''
                Profilo: {Studente.profilo}
                Corso di Studi: {self.corso}'''
        return super().scheda_personale() + scheda

    def cambio_corso(self,corso_nuovo):
        self.corso = corso_nuovo
        print('Corso Aggiornato')

class Insegnante(Persona):
    profilo = 'Insegnante'

    def __init__(self, nome, cognome, età, residenza, materia = None):
        super().__init__(nome, cognome, età, residenza)
        if materia is None:
            self.materia = []
        else:
            self.materia = materia

    def scheda_personale(self):
        scheda = f'''
                    Profilo: {Insegnante.profilo}
                    Materie insegnate: {self.materia}'''
        return super().scheda_personale() + scheda

studente_uno = Studente('Pier','Luca',27,'Roma','IngMecc')
insegnante_uno = Insegnante('Clara','Sorangelo',60,'Roma Centro',['Informatica','Cyberscurity'])
print(studente_uno.scheda_personale())
print(insegnante_uno.scheda_personale())