# This program "spins the wheel" and keeps spinning until it gets a different number
# It will be used to pick a random person from a list of people
# And then it will spin the wheel again to pick a different person
# It will clear the terminal every time it spins the wheel
# It will use text to show the list of people, and who is chosen
from random import randint

students = [
    "Emanuele Maria Acchiardi", "Beatrice Barca", "Matteo Brussolo", "Andrea Dissabo", "Elio Donda", "Riccardo Duss",
    "Riccardo Gardenal", "Nicole Korosic", "Artur Lexradenkovic", "Gabriele Lugnan", "Simone Macor", "Teo Macoritto",
    "Carmen Malacrea", "Leonardo Malgari", "Melory Moras", "Enrico Nadalin", "Gabriele Ongaro", "Alexander Pilon",
    "Nicolas Raimo", "Anjala Udugampalage", "Riccardo Ulian", "Alessia Zennaro", "Davide Zin"
]

# This function will print the list of students, with their index, and the chosen student
def print_students_and_chosen(chosen):
    for i in range(len(students)):
        if i == chosen:
            print(str(i) + ": " + students[i] + " <-- Chosen")
        else:
            print(str(i) + ": " + students[i])

# This function will clear the terminal
def clear_terminal():
    print("\n" * 100)

# This function will remove the chosen student from the list
def remove_student(chosen):
    students.pop(chosen)

# main program
# This is the main loop of the program
# It will keep spinning the wheel until there is only one student left
while len(students) > 1:
    # This will clear the terminal
    clear_terminal()

    # This will choose a random number between 0 and the length of the list of students
    chosen = randint(0, len(students) - 1)

    # This will print the list of students, with their index, and the chosen student
    print_students_and_chosen(chosen)

    # This will remove the chosen student from the list
    remove_student(chosen)

    # This will wait for the user to press enter
    input("Press enter to spin the wheel again")


