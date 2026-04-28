class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.gallenons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.gallenons} Gallenons, {self.sickles} Sickles, {self.knuts} Knuts"



potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

galleons = potter.gallenons + weasley.gallenons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts

total = Vault(galleons, sickles, knuts)
print(total)