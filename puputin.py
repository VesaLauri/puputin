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

    def uusipuppu(self, puppu, *args, **kwargs):
        if not isinstance(puppu, pd.DataFrame):
            raise TypeError("Syön Vain pndas dataframeja")

        # pupun mussutus
        data["indeksi"] = data.index.values.astype(int)
        if "frekvenssi" in kwargs:
            puppu["kumulatiivinensumma"] = data[int(kwargs["frekvenssi"])].cumsum()
        else:
            data["kumulatiivinensumma"] = data.index.values.astype(int)

        tulostetaan = list(args)

        puppu.__setattr__("tulostetaan", args)
        self._puput.append(puppu)

    def annapuppu(self, monta: int = 1):
        # for i in range(1):
        print(datasetti.__getattr__("tulostetaan"))
        print(self._puput[0].__getattr__("tulostetaan"))
        datasetti = self._puput[0]
        arpa = random.randint(0, self._puput[0]["kumulatiivinensumma"].iloc[-1])
        return datasetti[datasetti["kumulatiivinensumma"] >= arpa].iloc[0:1, [0, 1, 2]]


if __name__ == "__main__":
    puppu = Puputin("testi")
    puppu2 = Puputin("testi")
    data = pd.read_csv(
        "tekstit\\miesnimet.txt", sep=",", header=None, encoding="ISO-8859-1"
    )
    puppu.uusipuppu(data, [0, 1, 2])
    print(puppu.annapuppu())
    puppu2.uusipuppu(data, [0, 1, 2], frekvenssi=1)
    print(puppu2.annapuppu())

