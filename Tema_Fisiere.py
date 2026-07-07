from enum import Enum
from datetime import datetime


class Categories(Enum):
    COURSE = "course"
    SHOPPING = "shopping"
    WORK = "work"
    PRESENTS = "presents"


current_category = Categories.WORK

if current_category == Categories.COURSE:
    pass



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



class Todos:
    def __init__(self):
        self.todos_list = []

    def add_task(self, add_task):
        for task in self.todos_list:
            if task.title.lower() == add_task.title.lower():
                print("Task with this title already exists!")
                return False
        self.todos_list.append(add_task)
        return True

    def remove_task(self, task_to_delete):
        for task in self.todos_list:
            if task == task_to_delete:
                self.todos_list.remove(task)
                return True
        return False

    def remove_task_by_index(self, index):
        if index >= 0 and index < len(self.todos_list):
            task_to_delete = self.todos_list[index]
            self.remove_task(task_to_delete)
            print("Task sters.")
            return True
        else:
            print("Numarul taskului nu este valid.")
            return False

    def filter_by_category(self, categ):
        results = []

        for task in self.todos_list:
            if task.category.lower() == categ.lower():
                results.append(task)
        return results

    def filter_by_owner(self, owner):
        results = []

        for task in self.todos_list:
            if task.owner.lower() == owner.lower():
                results.append(task)

        return results

    def tasks_by_category(self):
        print("Tasks by category:")
        print()

        for c in categories:
            print(f"{c}:")
            for task in self.todos_list:
                if task.category.lower() == c.lower():
                    print(task)
            print()

    def number_of_tasks(self, category):
        aparitii = 0
        for task in self.todos_list:
            if task.category.lower() == category.lower():
                aparitii += 1

        return aparitii

    def list_tasks(self):
        if len(self.todos_list) == 0:
            print("Nu exista taskuri.")
            return

        count = 0

        for task in self.todos_list:
            print(f"{count}. {task}")
            count += 1

    def print_tasks(self, task_list):
        if len(task_list) == 0:
            print("Nu exista taskuri.")
            return

        for task in task_list:
            print(task)

    def sort_tasks(self, option):
        if option == "1":
            sorted_list = sorted(self.todos_list, key=lambda task: task.title.lower())
        elif option == "2":
            sorted_list = sorted(self.todos_list, key=lambda task: task.title.lower(), reverse=True)
        elif option == "3":
            sorted_list = sorted(self.todos_list, key=lambda task: datetime.strptime(task.date, "%d.%m.%Y %H:%M"))
        elif option == "4":
            sorted_list = sorted(self.todos_list, key=lambda task: datetime.strptime(task.date, "%d.%m.%Y %H:%M"), reverse=True)
        elif option == "5":
            sorted_list = sorted(self.todos_list, key=lambda task: task.owner.lower())
        elif option == "6":
            sorted_list = sorted(self.todos_list, key=lambda task: task.owner.lower(), reverse=True)
        elif option == "7":
            sorted_list = sorted(self.todos_list, key=lambda task: task.category.lower())
        elif option == "8":
            sorted_list = sorted(self.todos_list, key=lambda task: task.category.lower(), reverse=True)

        else:
            print("Optiune invalida.")
            return

        self.print_tasks(sorted_list)

    def filter_tasks(self, field, text):
        results = []
        text = text.lower()

        for task in self.todos_list:
            if field == "1":
                value = task.title.lower()
            elif field == "2":
                value = task.date.lower()
            elif field == "3":
                value = task.owner.lower()
            elif field == "4":
                value = task.category.lower()
            else:
                print("Camp invalid.")
                return

            if text in value or value.startswith(text):
                results.append(task)
        self.print_tasks(results)

    def edit_task(self, index):
        if index < 0 or index >= len(self.todos_list):
            print("Numarul taskului nu este valid.")
            return False
        task = self.todos_list[index]

        print("Task ales:")
        print(task)
        print("Daca nu vrei sa modifici un camp, apasa Enter.")

        new_title = input("Task nou: ").strip()
        new_date = input("Data noua: ").strip()
        new_owner = input("Persoana responsabila noua: ").strip()
        new_category = input("Categorie noua: ").strip()

        if new_title != "":
            for other_task in self.todos_list:
                if other_task != task and other_task.title.lower() == new_title.lower():
                    print("Task with this title already exists!")
                    return False

            task.title = new_title

        if new_date != "":
            if valid_date(new_date):
                task.date = new_date
            else:
                print("Data nu este valida.")
                return False

        if new_owner != "":
            task.owner = new_owner

        if new_category != "":
            if category_exists(new_category):
                task.category = get_category_name(new_category)
            else:
                print("Categoria nu exista.")
                return False

        print("Task modificat.")
        return True

    def __str__(self):
        return f"{self.todos_list}"


def valid_date(date):
    try:
        datetime.strptime(date, "%d.%m.%Y %H:%M")
        return True
    except ValueError:
        return False


def category_exists(category):
    for c in categories:
        if c.lower() == category.lower():
            return True

    return False


def get_category_name(category):
    for c in categories:
        if c.lower() == category.lower():
            return c

    return category


def add_category(category):
    if category == "":
        return False

    if category_exists(category):
        print(f"Categoria {category} exista deja.")
        return False

    categories.append(category)
    return True


def read_categories_from_file():
    categories_from_file = []

    try:
        file = open("categorii.txt", "r", encoding="utf-8")

        for line in file:
            category = line.strip()

            if category != "":
                exists = False

                for c in categories_from_file:
                    if c.lower() == category.lower():
                        exists = True

                if exists == False:
                    categories_from_file.append(category)

        file.close()

    except FileNotFoundError:
        pass

    return categories_from_file


def save_categories_to_file():
    file = open("categorii.txt", "w", encoding="utf-8")

    for category in categories:
        file.write(category + "\n")

    file.close()


def read_tasks_from_file():
    todos = Todos()

    try:
        file = open("taskuri.txt", "r", encoding="utf-8")

        for line in file:
            line = line.strip()

            if line != "":
                parts = line.split("|")

                if len(parts) == 4:
                    title = parts[0]
                    date = parts[1]
                    owner = parts[2]
                    category = parts[3]

                    task = Task(title, date, owner, category)
                    todos.add_task(task)

        file.close()

    except FileNotFoundError:
        pass

    return todos


def save_tasks_to_file():
    file = open("taskuri.txt", "w", encoding="utf-8")

    for task in todos1.todos_list:
        file.write(task.title + "|" + task.date + "|" + task.owner + "|" + task.category + "\n")

    file.close()


def read_categories_from_keyboard():
    text = input("Introduceti categoriile de taskuri separate prin virgula: ")

    categories_from_user = text.split(",")

    for category in categories_from_user:
        category = category.strip()

        if category != "":
            add_category(category)

    save_categories_to_file()


def show_categories():
    print("Categorii existente:")

    if len(categories) == 0:
        print("Nu exista categorii.")

    for category in categories:
        print("-", category)


def add_task_from_keyboard():
    title = input("Introduceti taskul: ").strip()
    date = input("Introduceti data limita: ").strip()
    owner = input("Introduceti persoana responsabila: ").strip()
    category = input("Introduceti categoria: ").strip()

    if title == "" or date == "" or owner == "" or category == "":
        print("Toate campurile trebuie completate.")
        return

    if valid_date(date) == False:
        print("Data nu este valida. Exemplu corect: 22.01.2022 21:30")
        return

    if category_exists(category) == False:
        print("Eroare: categoria nu exista.")
        return

    category = get_category_name(category)

    task = Task(title, date, owner, category)

    result = todos1.add_task(task)

    if result == True:
        save_tasks_to_file()
        print("Task adaugat.")


def add_more_tasks():
    while True:
        add_task_from_keyboard()

        answer = input("Mai vrei sa adaugi un task? da/nu: ").strip().lower()

        if answer != "da":
            break


def show_sort_menu():
    print()
    print("1. sortare ascendenta task")
    print("2. sortare descendenta task")
    print("3. sortare ascendenta data")
    print("4. sortare descendenta data")
    print("5. sortare ascendenta persoana responsabila")
    print("6. sortare descendenta persoana responsabila")
    print("7. sortare ascendenta categorie")
    print("8. sortare descendenta categorie")

    option = input("Alege optiunea: ")

    todos1.sort_tasks(option)


def show_filter_menu():
    print()
    print("Filtrare dupa:")
    print("1. Task")
    print("2. Data")
    print("3. Persoana responsabila")
    print("4. Categorie")

    field = input("Alege campul: ")
    text = input("Introdu textul pentru filtrare: ")

    todos1.filter_tasks(field, text)


def show_menu():
    print()
    print("========== MENIU ==========")
    print("1. Listare date")
    print("2. Sortare")
    print("3. Filtrare date")
    print("4. Adaugarea unui nou task")
    print("5. Editarea unui task")
    print("6. Stergerea unui task")
    print("7. Afisare categorii")
    print("8. Adaugare categorii")
    print("0. Iesire")
    print("===========================")
    print()


categories = read_categories_from_file()
todos1 = read_tasks_from_file()


if len(categories) == 0:
    read_categories_from_keyboard()


if len(todos1.todos_list) == 0:
    answer = input("Vrei sa adaugi taskuri acum? da/nu: ").strip().lower()

    if answer == "da":
        show_categories()
        add_more_tasks()


while True:
    show_menu()

    option = input("Alege o optiune: ")

    if option == "1":
        sorted_list = sorted(todos1.todos_list, key=lambda task: task.category.lower())
        todos1.print_tasks(sorted_list)

    elif option == "2":
        show_sort_menu()

    elif option == "3":
        show_filter_menu()

    elif option == "4":
        show_categories()
        add_task_from_keyboard()

    elif option == "5":
        todos1.list_tasks()

        index = input("Alege numarul taskului pe care vrei sa il modifici: ")

        if index.isdigit():
            index = int(index)

            result = todos1.edit_task(index)

            if result == True:
                save_tasks_to_file()
        else:
            print("Trebuie sa introduci un numar.")

    elif option == "6":
        todos1.list_tasks()

        index = input("Alege numarul taskului pe care vrei sa il stergi: ")

        if index.isdigit():
            index = int(index)

            result = todos1.remove_task_by_index(index)

            if result == True:
                save_tasks_to_file()
        else:
            print("Trebuie sa introduci un numar.")

    elif option == "7":
        show_categories()

    elif option == "8":
        read_categories_from_keyboard()

    elif option == "0":
        save_categories_to_file()
        save_tasks_to_file()
        break

    else:
        print("Optiune invalida.")