# Se cere realizarea unui to-do list utilizând noțiunile învățate până în acest moment.
# În prima faza se adaugă categoriile dorite de la tastatură:
# exemplu: Introduceți categoriile de taskuri:
# posibile răspunsuri: curs, cumpărături, muncă, cadouri, etc
#  Cerințe:
# - se va cere, pe rand, introducerea unui task de la tastatura: ex: rezolvare tema
# - se va cere introducerea unei date limite de realizare a taskului respectiv, ex:  22.01.2022 21:30
# - se va adăuga o persoana responsabilă cu realizarea taskului respectiv: ex: Ion Vasile
# - se va adăuga o categorie din care taskul face parte. Ex. curs
# Atenție, categoria trebuie să existe. În cazul în care nu există, se afișează mesaj de eroare.
# Va exista posibilitatea de adăugare a unui număr nelimitat de taskuri, chiar si după ce utilizatorul confirmă faptul că a terminat de introdus taskurile.
# Datele se salveaza in fisiere. Vor exista doua fisiere: unul pentru categorii si unul care sa contina: taskurile, data limita, persoana responsabila, categorie
#
# Cerințe suplimentare:
# Se afișează un meniu din care utilizatorul poate alege să realizeze următoarele operații:
# Listare date: în afișarea inițială a datelor se realizează o sortare în funcție de categorie.
# Sortare: se alege o opțiune din cele 8 de mai jos:
# Criteriile disponibile sunt:
#
# 1. sortare ascendentă task
# 2. sortare descendentă task
# 3. sortare ascendentă data
# 4. sortare descendentă data
# 5. sortare ascendentă persoana responsabilă
# 6. sortare descendentă persoană responsabilă
# 7. sortare ascendentă categorie
# 8. sortare descendentă categorie
#
# Filtrare date: filtrarea datelor reprezintă de fapt o listare a datelor în funcție de anumite detalii date de la tastatură. criteriile de filtrare sunt:
#
# -       se cere de la tastatură câmpul după care se realizeaza filtrarea:
# 1.     Task
# 2.     Dată
# 3.     Persoană responsabilă
# 4.     Categorie
# -       după alegerea campului de la tastatură se cere introducerea unui string utilizat pentru filtrarea în lista inițială de date, astfel încât din lista inițială să rămână doar datele care conțin / încep cu valoarea introdusă
#
# -       se afișează lista rămasă
#       4.    Adăugarea unui nou task în lista inițială
#       5.    Editarea detaliilor referitoare la task, dată, persoană sau categorie dintr-un anumit task ales de utilizator de la tastatură (când se cere această opțiune, se va lista lista de taskuri cu un identificator unic pe rand, astfel încât să se știe ce informație urmează să editeze utilizatorul)
#       6.     Ștergerea unui task din lista inițială.
#
#
# Atenție! Trebuie să aveți grijă că o categorie poate să existe o singură dată (nu se accepta dubluri, ex curs, cumpărături, muncă, cadouri, curs este greșit)
#
# De asemenea, la adăugarea taskurilor se va avea grijă și la compararea textelor taskurilor, dacă textul respectiv există, nu se poate adăuga.

from enum import Enum
class Categories(Enum):
    COURSE = "course"
    SHOPPING = "shopping"
    WORK = "work"
    PRESENTS = "presents"

print(Categories.COURSE)
print(type(Categories.COURSE))

current_category = Categories.WORK
if current_category == Categories.COURSE:
    print("I'm at work")

class Task:
    def __init__(self, title, date, owner, category):
        self.title = title
        self.date = date
        self.owner = owner
        self.category = category
    def __str__(self):
        return f"{self.title}, {self.date}, {self.owner}, {self.category}"
    def __repr__(self):
        return f"Task(title='{self.title}', date='{self.date}', owner='{self.owner}', category='{self.category}')"

task1 = Task("Rezolvare tema", "23.iunie", "John", Categories.COURSE)
print(task1)

task2 = Task("Spalat Vase", "23.iunie", "Ionut", Categories.WORK)
task3 = Task("Shopping", "24.iunie", "Olivia", Categories.COURSE)

# todo = [task1, task2, task3]

class Todos:
    def __init__(self):
        self.todos_list = []

    def add_task(self, add_task):
        for task in self.todos_list:
            if task.title == add_task.title:
               print("Task with this title already exists!")
               return
        self.todos_list.append(add_task)

    def remove_task(self, task_to_delete):
        for task in self.todos_list:
            if task == task_to_delete:
                self.todos_list.remove(task)

    def filter_by_category(self, categ):
        results = []
        for task in self.todos_list:
            if task.category == categ:
                results.append(task)
        return results

    def filter_by_owner(self, owner):
        results = []
        for task in self.todos_list:
            if task.owner == owner:
                results.append(task)
        return results

    def tasks_by_category(self):
        print("Tasks by category:")
        print()
        for c in Categories:
            print(f"{c}:")
            for task in self.todos_list:
                if task.category == c:
                    print(task)
            print()

    def number_of_tasks(self, category):
        aparitii = 0
        for task in self.todos_list:
            if task.category == category:
                aparitii += 1
        return aparitii

    def __str__(self):
        return f"{self.todos_list}"

todos1 = Todos()
todos1.add_task(task1)
todos1.add_task(task2)
todos1.add_task(task3)
todos1.add_task(Task("Go to Humana", "26.iunie", "ionut", Categories.SHOPPING))
print(todos1)

todos1.remove_task(task2)

print(todos1)
print(todos1.filter_by_category(Categories.SHOPPING))

# scrieti o metoda in clasa Todos pentru a filtra dupa owner. acea metoda va returna toate task-urile unui owner, ce-l primim ca parametru al acelei metode.
print("Task 1")
print(todos1.filter_by_owner("Olivia"))

# scrieti o metoda in clasa Todos care numara toate task-urile ale unei anumite categorii, si returneaza cate task-uri sunt pentru acea categorie. Daca sunt 3 taskuri in total pe categoria Category.COURSE de exemplu, metoda returneaza numarul 3.
print("Task 2")
print(todos1.number_of_tasks(Categories.SHOPPING))

# modificati metoda add_task, sa nu permita adaugarea unui task cu titlu duplicat. Daca exista deja un task cu acel titlu, sa printeze "Task with this title already exists!
print("Task 3")
todos1.add_task(Task("Go to Humana", "26.iunie", "ionut", Categories.SHOPPING))

# creaza o metoda care printeaza task-urile, organizate dupa categorie. de exemplu, acea metoda ar printa:
#
# """
# Tasks by category:
# Category.COURSE:
# Rezolvare Tema, 23.Iunie, John, Categories.COURSE
# Rezolvare Tema 2, 24.Iunie, John, Categories.COURSE
#
# Category.SHOPPING:
# Go to second-hand store, 23.Iunie, John, Category.SHOPPING
# Buy shoes, 23.Iunie, John, Category.SHOPPING
# """
print("Task 4")
todos1.tasks_by_category()