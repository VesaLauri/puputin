import pandas as pd
import random


class Puputin:
    def __init__(self, nimi):
        self._nimi = nimi
        self._puput = list()
        self._arvottujoukko = pd.DataFrame()

    @property
    def nimi(self):
        return self._nimi

    @nimi.setter
    def nimi(self, nimi):
        self._nimi = nimi

    def uusipuppu(self, puppu, tulostetaan, **kwargs):
        if not isinstance(puppu, pd.DataFrame):
            raise TypeError("Syön Vain pandas dataframeja")

        # pupun mussutus
        puppu["indeksi"] = puppu.index.values.astype(int)
        if "frekvenssi" in kwargs:
            puppu["kumulatiivinensumma"] = puppu[int(kwargs["frekvenssi"])].cumsum()
        else:
            puppu["kumulatiivinensumma"] = puppu.index.values.astype(int)
        self._puput.append([puppu, tulostetaan])

    def luopuppu(self, monta: int = 1):
        lista = list()
        rivi = list()
        for _ in range(monta):
            for puppu in self._puput:
                arpa = random.randint(0, puppu[0]["kumulatiivinensumma"].iloc[-1])
                yksi = (
                    puppu[0][puppu[0]["kumulatiivinensumma"] >= arpa]
                    .iloc[0:1, puppu[1]]
                    .values.tolist()
                )
                for solu in yksi:
                    rivi += solu
            lista.append(rivi)
            rivi = list()
        self._arvottujoukko = pd.DataFrame(lista)

    def annapuppu(self, monta):
        return self._arvottujoukko.sample(monta)


if __name__ == "__main__":
    puppu = Puputin("testi")
    puppu2 = Puputin("testi")

    naisnimet = pd.read_csv(
        "tekstit\\naisnimet.txt", sep=",", header=None, encoding="ISO-8859-1"
    )

    miesnimet = pd.read_csv(
        "tekstit\\miesnimet.txt", sep=",", header=None, encoding="ISO-8859-1"
    )
    kaupungit = pd.read_csv(
        "tekstit\\kaupungit.txt", sep=",", header=None, encoding="ISO-8859-1"
    )
    kaupungit = pd.read_csv(
        "tekstit\\kaupungit.txt", sep=",", header=None, encoding="ISO-8859-1"
    )
    sukunimet = pd.read_csv(
        "tekstit\\sukunimet.txt", sep=",", header=None, encoding="ISO-8859-1"
    )
    # print(nykanen)
    puppu2.uusipuppu(miesnimet, [0], frekvenssi=1)
    puppu2.uusipuppu(miesnimet, [0], frekvenssi=1)
    puppu2.uusipuppu(sukunimet, [0], frekvenssi=1)
    puppu2.uusipuppu(kaupungit, [0], frekvenssi=1)
    # puppu2.uusipuppu(nykanen, [0])

    puppu.uusipuppu(naisnimet, [0], frekvenssi=1)
    puppu.uusipuppu(naisnimet, [0], frekvenssi=1)
    puppu.uusipuppu(sukunimet, [0], frekvenssi=1)
    puppu.uusipuppu(kaupungit, [0], frekvenssi=1)

    puppu.luopuppu(30)
    puppu2.luopuppu(30)

    puppu3 = Puputin("naimisissa")
    naiset = puppu.annapuppu(30)
    miehet = puppu2.annapuppu(30)
    puppu3.uusipuppu(naiset, [0, 1, 2, 3, 4])
    puppu3.uusipuppu(miehet, [0, 1, 2, 3, 4])
    puppu3.luopuppu(10)
    naimisissa = puppu3.annapuppu(10)
    print(naimisissa)

