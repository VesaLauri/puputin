import pandas as pd

data = pd.read_csv(
    "tekstit\\miesnimet.txt", sep=",", header=None, encoding="ISO-8859-1"
)
print(data)

print(data[1] + " " + data["jee"])
data["jee"] = data[1].cumsum()
print(data[0])
data["indeksi"] = data.index.values.astype(int)

# functio joka laskee sen juoksevan summan
"""
functio (listan, kertoo onko osuuslukua ja jos on mikä sarake 
        (jos ei niin yksi) j sit ajaa sen listan sisään juksevalla summalla) 

lista_a = [['Etunimi',['sukunimi']],[['Vesa','Lauri',],['Vähemmän'],['Tärkeä']]
lista_b =[['Ostaja'],['ostokertoja'],['vesa'],[12]]
"""
