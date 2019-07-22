import pandas as pd


class puputin:
    _puput = list()

    def __init__(self, nimi):
        self._nimi = nimi

    @property
    def nimi(self):
        return self._nimi

    @nimi.setter
    def nimi(self, nimi):
        self._nimi = nimi

    def uusipuppu(self, puppu):
        self._puput.append(puppu)
