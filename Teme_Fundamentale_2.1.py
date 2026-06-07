# Scrieti un program care primeste o lista de dictionare de persoane, si returneaza intr-o alta lista, doar persoanele care au varsta mai mare de 25 de ani, si care au greutatea peste 60 kg.
# Lista sa aiba cel putin 5 persoane. Logica acestui filtru sa o puneti intr-o functie, sa poata fi refolosita.
#
# Exemplu lista persoane:
# cetateni = [
#     19304843895738: {
#         "Nume": "Marius Moga",
#         "Varsta": 32,
#         "Adresa": "Brasov, Jud Brasov",
#         "Greutate": 75,
#     },
#     193048438345345: {
#         "Nume": "Matei Luca",
#         "Varsta": 30,
#         "Greutate": 59,
#     }
# ]
from pprint import pprint
cetateni = {
    1930415123456: {
        "Nume": "Marius Moga",
        "Varsta": 32,
        "Adresa": "Brasov, Romania",
        "Greutate": 78
    },

    2960516123456: {
        "Nume": "Elena Ionescu",
        "Varsta": 30,
        "Adresa": "Cluj-Napoca, Romania",
        "Greutate": 62
    },

    1950717123456: {
        "Nume": "Ion Georgescu",
        "Varsta": 35,
        "Adresa": "Bucuresti, Romania",
        "Greutate": 85
    },

    2950818123456: {
        "Nume": "Roxana Ilie",
        "Varsta": 40,
        "Adresa": "Iasi, Romania",
        "Greutate": 70
    },

    5010901123456: {
        "Nume": "Vlad Petrescu",
        "Varsta": 26,
        "Adresa": "Brasov, Romania",
        "Greutate": 74
    },

    6011002123456: {
        "Nume": "Ana Pop",
        "Varsta": 24,
        "Adresa": "Sibiu, Romania",
        "Greutate": 60
    },

    5021103123456: {
        "Nume": "Cristi Neagu",
        "Varsta": 29,
        "Adresa": "Oradea, Romania",
        "Greutate": 88
    },

    6021204123456: {
        "Nume": "Ioana Dumitru",
        "Varsta": 27,
        "Adresa": "Constanta, Romania",
        "Greutate": 63
    },

    5030105123456: {
        "Nume": "Andrei Stan",
        "Varsta": 23,
        "Adresa": "Timisoara, Romania",
        "Greutate": 92
    },

    6030206123456: {
        "Nume": "Maria Popescu",
        "Varsta": 25,
        "Adresa": "Brasov, Romania",
        "Greutate": 58
    }
}

def filtreaza_persoane(persoane):
    cetateni_filtrati = {}
    for cnp in persoane:
        persoana = persoane[cnp]
        if persoana["Varsta"] > 25 and persoana["Greutate"] > 60:
            cetateni_filtrati[cnp] = persoana
    return cetateni_filtrati

pprint(filtreaza_persoane(cetateni), sort_dicts=False)


