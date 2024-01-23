import datetime

class Diak:
    iskola_neve = "XY iskola"  # Class attribute for the school name

    def __init__(self, nev, osztaly, szuletesi_ev):
        self.nev = nev
        self.osztaly = osztaly
        self.szuletesi_ev = szuletesi_ev
        self.diakigazolvany_szam = self._generate_diakigazolvany_szam()
        self.eletkor = self._calculate_eletkor()

    def _calculate_eletkor(self):
        akt_ev = datetime.datetime.now().year
        return akt_ev - self.szuletesi_ev

    def _generate_diakigazolvany_szam(self):
        # Generate a unique student ID, you can customize this logic
        return hash(f"{self.nev}-{self.osztaly}-{self.szuletesi_ev}")

    def get_student_info(self):
        return f"Szia, {self.nev} vagyok, az {self.iskola_neve} {self.osztaly}. osztályába járok, {self.eletkor} éves vagyok. A diákigazolványom száma: {self.diakigazolvany_szam}"

# Creating Diak objects
diak1 = Diak("Kiss Péter", "10.A", 2007)
diak2 = Diak("Nagy Anna", "11.B", 2005)

print(diak1.get_student_info())
print(diak2.get_student_info())
