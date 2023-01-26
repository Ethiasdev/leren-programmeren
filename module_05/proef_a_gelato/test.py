class Auto:
    def __init__(self, merk, model, kleur, eigenaar, aantal_wielen, bouwjaar, gewicht, versnellingsbak, brandstoftype, afstand_per_volle_tank, pk):
        self.merk = merk
        self.model = model
        self.kleur = kleur
        self.eigenaar = eigenaar
        self.aantal_wielen = aantal_wielen
        self.bouwjaar = bouwjaar
        self.gewicht = gewicht
        self.versnellingsbak = versnellingsbak
        self.brandstoftype = brandstoftype
        self.afstand_per_volle_tank = afstand_per_volle_tank
        self.pk = pk
        self.volgende_apk = ""

    def verander_eigenaar(self, nieuwe_eigenaar):
        self.eigenaar = nieuwe_eigenaar

    def verf_auto(self, nieuwe_kleur):
        self.kleur = nieuwe_kleur

    def apk_keuring(self, datum):
        self.volgende_apk = datum

    def __str__(self):
        return f'Merk: {self.merk}\nModel: {self.model}\nKleur: {self.kleur}\nEigenaar: {self.eigenaar}\nAantal wielen: {self.aantal_wielen}\nBouwjaar: {self.bouwjaar}\nGewicht: {self.gewicht}\nVersnellingsbak: {self.versnellingsbak}\nBrandstoftype: {self.brandstoftype}\nAfstand per volle tank: {self.afstand_per_volle_tank}\nPK: {self.pk}\nVolgende APK: {self.volgende_apk}'

mijnAuto = Auto("audi", "test", "grijs", "bardia", "4", "2002", "333KG", "123", "2149", "21KM", "2")

mijnAuto.apk_keuring("goed")

print(mijnAuto)