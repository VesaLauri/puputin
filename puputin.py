class puputin:
    def __init__(self, nimi):
        self._nimi = nimi

    @property
    def nimi(self):
        return self._nimi

    @nimi.setter
    def nimi(self, nimi):
        self._nimi = nimi
