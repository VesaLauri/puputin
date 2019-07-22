import pandas as pd
import random


class Puputin:
    _puput = list()

    def __init__(self, nimi):
        self._nimi = nimi

    @property
    def nimi(self):
        return self._nimi

    @nimi.setter
    def nimi(self, nimi):
        self._nimi = nimi

    def uusipuppu(self, puppu, **kwargs):
        if not isinstance(puppu, pd.DataFrame):
            raise TypeError("Syön Vain pndas dataframeja")

        # pupun mussutus
        data["indeksi"] = data.index.values.astype(int)
        if "frekvenssi" in kwargs:
            puppu["kumulatiivinensumma"] = data[int(kwargs["frekvenssi"])].cumsum()
        else:
            data["kumulatiivinensumma"] = data.index.values.astype(int)
        self._puput.append(puppu)

    def annapuppu(self, monta: int = 1):
        datasetti = self._puput[0]
        arpa = random.randint(0, self._puput[0]["kumulatiivinensumma"].iloc[-1])
        return datasetti[datasetti["kumulatiivinensumma"] >= arpa].iloc[0:1]


if __name__ == "__main__":
    puppu = Puputin("testi")
    puppu2 = Puputin("testi")
    data = pd.read_csv(
        "tekstit\\miesnimet.txt", sep=",", header=None, encoding="ISO-8859-1"
    )
    puppu.uusipuppu(data)
    print(puppu.annapuppu())
    puppu2.uusipuppu(data, frekvenssi=1)
    print(puppu2.annapuppu())

