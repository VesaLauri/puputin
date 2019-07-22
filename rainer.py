import pyodbc
import random

# yhdistetään kantaan

server = "localhost"
database = "PythonKanta"
username = "Reportuser"
password = "Password1"

cnxn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};SERVER="
    + server
    + ";DATABASE="
    + database
    + ";UID="
    + username
    + ";PWD="
    + password
)
cursor = cnxn.cursor()

# avataan ja esikäsitellään tiedostot

miehet = open("miesnimet.txt", "r")
naiset = open("naisnimet.txt", "r")
kaupungit = open("kaupungit.txt", "r")
sukunimet = open("sukunimet.txt", "r")
nykanen = open("nykanen.txt", "r")

nykaslista = nykanen.readlines()

mieslista = miehet.read()
mieslista = mieslista.splitlines()
Mieslista = list()
for I in range(0, len(mieslista)):
    Mieslista.append(mieslista[I].split(","))

naislista = naiset.read()
naislista = naislista.splitlines()
Naislista = list()
for I in range(0, len(naislista)):
    Naislista.append(naislista[I].split(","))

klista = kaupungit.read()
klista = klista.splitlines()
Klista = list()
for I in range(0, len(klista)):
    Klista.append(klista[I].split(","))

slista = sukunimet.read()
slista = slista.splitlines()
Slista = list()
for I in range(0, len(slista)):
    Slista.append(slista[I].split(","))

# määritellään tarvittavat funktiot


def Arvo_Kaupunki():
    arvonta = random.randint(1, 5521773)
    for X in Klista:
        if arvonta <= int(X[2]):
            KNimi = X[0]
            break
    return KNimi


def Arvo_Mies():
    arvonta = random.randint(1, 2_663_203)
    for X in Mieslista:
        if arvonta <= int(X[2]):
            KNimi = X[0]
            break
    return KNimi


def Arvo_Nainen():
    arvonta = random.randint(1, 2790983)
    for X in Naislista:
        if arvonta <= int(X[2]):
            KNimi = X[0]
            break
    return KNimi


def Arvo_Sukunimi():
    arvonta = random.randint(1, 5033792)
    for X in Slista:
        if arvonta <= int(X[2]):
            KNimi = X[0]
            break
    return KNimi


def Arvo_Nimi():
    if random.randint(1, 2) == 1:
        Nimi = Arvo_Mies()
    else:
        Nimi = Arvo_Nainen()
    return Nimi


def Arvo_Syntyma():
    Vuosi = random.randint(1950, 2009)
    Kuukausi = random.randint(1, 12)
    Paiva = random.randint(1, 28)
    Syntynyt = f"{Vuosi}-{Kuukausi}-{Paiva}"
    return Syntynyt


def Arvo_Nykanen():
    arpa = random.randint(1, len(nykaslista) - 1)
    return nykaslista[arpa]


def Arvo_Kuolema(syntymaaika):
    Kuollut = "9999-12-31"
    if random.randint(1, 100) <= 15:
        syntymasplit = syntymaaika.split("-")
        Kuukausi = random.randint(1, 12)
        Paiva = random.randint(1, 28)
        Vuosi = random.randint(int(syntymasplit[0]) + 1, 2019)
        Kuollut = f"{Vuosi}-{Kuukausi}-{Paiva}"
    return Kuollut


# tällä syötetään puppua kantaan
I = 0
while I <= 10000:
    Syntyma = Arvo_Syntyma()
    Query = f"INSERT INTO Rekisteri VALUES ('{Arvo_Nimi()}', '{Arvo_Sukunimi()}', '{Syntyma}','{Arvo_Kuolema(Syntyma)}', 'Suomi', '{Arvo_Kaupunki()}', {random.randint(0,5)}, '{Arvo_Nykanen()}')"
    cursor.execute(Query)
    cnxn.commit()
    I += 1
