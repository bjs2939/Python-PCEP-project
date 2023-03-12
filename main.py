import random
import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, jsonify, request



class DataVisualization:
    """
    A class to plot data from a CSV file using Matplotlib.

    Attributes:
    -----------
    filename : str
        The name of the CSV file containing the data.
    """
    def __init__(self, filename):
        self.filename = filename

    def plot_data(self):
        """
        Read data from a CSV file and plot it using Matplotlib.
        """
        try:
            data = pd.read_csv(self.filename)
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return
        except Exception as e:
            print(f"Error: {e}")
            return

        plt.plot(data['Month'], data['Passengers'], label='Passengers')
        plt.xlabel('Year')
        plt.ylabel('Number of Passengers')
        plt.title('Air Travel over Time')
        plt.legend()

        plt.show()

class RestfulAPI:
    app = Flask(__name__)

    # Example data
    students = [
        {
            'id': 1,
            'name': 'John Doe',
            'age': 21,
            'major': 'Computer Science'
        },
        {
            'id': 2,
            'name': 'Jane Smith',
            'age': 22,
            'major': 'Business Administration'
        }
    ]

    # Get all students
    @app.route('/students', methods=['GET'])
    def get_students():
        return jsonify(students)

    # Get single student
    @app.route('/students/<int:id>', methods=['GET'])
    def get_student(id):
        student = [student for student in students if student['id'] == id]
        if len(student) == 0:
            return jsonify({'error': 'Student not found'})
        return jsonify(student[0])

    # Create a student
    @app.route('/students', methods=['POST'])
    def create_student():
        new_student = {
            'id': request.json['id'],
            'name': request.json['name'],
            'age': request.json['age'],
            'major': request.json['major']
        }
        students.append(new_student)
        return jsonify(new_student)

    # Update a student
    @app.route('/students/<int:id>', methods=['PUT'])
    def update_student(id):
        student = [student for student in students if student['id'] == id]
        if len(student) == 0:
            return jsonify({'error': 'Student not found'})
        student[0]['name'] = request.json['name']
        student[0]['age'] = request.json['age']
        student[0]['major'] = request.json['major']
        return jsonify(student[0])

    # Delete a student
    @app.route('/students/<int:id>', methods=['DELETE'])
    def delete_student(id):
        student = [student for student in students if student['id'] == id]
        if len(student) == 0:
            return jsonify({'error': 'Student not found'})
        students.remove(student[0])
        return jsonify({'message': 'Student deleted successfully'})

    if __name__ == '__main__':
        app.run(debug=True)




class WebScraping:
    def scrape_links(self):
        print("Thank you for choosing Web Scraping")
        url = input("\nPlease paste your URL here: ")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        while True:
            print("Would you like to...")
            print("1. Print all url links")
            print("2. Save all url links to csv")
            print("3. What is a CSV??")
            print("4. Input New Url")
            choice = int(input("Please type 1 - 4\n"))

            if choice == 1:
                print("Here are all the links from that page:")
                links = soup.find_all('a')
                for link in links:
                    print(link.get('href'))

            elif choice == 2:
                with open('links.csv', 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Link"])
                    links = soup.find_all('a')
                    for link in links:
                        writer.writerow([link.get('href')])
                print("Links saved in links.csv within python project folder")

            elif choice == 3:
                print("A CSV (Comma Separated Values) file is a plain text file that stores tabular data in which each row\n"
                      "represents a record, and each column represents a field within the record, separated by a comma.\n"
                      "CSV files are commonly used for data exchange between different software applications and can be\n"
                      "opened in various programs, including Excel or Notepad.")

            elif choice == 4:
                self.scrape_links()

            repeat = input("Do you want to repeat the web scraping process? (yes/no)")
            if repeat.lower() != "yes":
                Mainmenu(startup.name)  # return to the main menu


class Startup:
    def __init__(self):
        print("Good morning")
        print("Welcome to my fancy Python Program")
        print("This program is designed to prepare me for the PCEP exam")
        print("To begin, please tell me your name....")
        self.name = input()


class Mainmenu:
    def __init__(self, name):
        self.name = name
        print(self.name + ", which program would you like to begin?")
        print("\n1. Web scraping")
        print("2. Data Visualization")
        print("3. RESTful API")
        print("4. Machine Learning")
        print("5. File Processing")
        print("6. Play a game")
        print("0. Exit Program")
        while True:
            try:
                self.prog_choice = int(input("\nPlease type a number 0-6:"))
                if self.prog_choice >= 0 and self.prog_choice <= 6:
                    break
                else:
                    print("\nPlease type a valid number")
            except ValueError:
                print("\nPlease type a valid number")
        print("You have chosen ", self.prog_choice)
        datavisualization = DataVisualization()
        if self.prog_choice == 1:
            webscraper = WebScraping()
            webscraper.scrape_links()

        if self.prog_choice == 2:
            datavisualization.plot_data()

        if self.prog_choice == 3:
            RestfulAPI()


        if self.prog_choice == 6:
            GameLibrary()


startup = Startup()
mainmenu = Mainmenu(startup.name)

if mainmenu.prog_choice == 0:
    print("Thank you " + mainmenu.name + " for using my program")
    enter_to_exit = input("Press press enter to exit program")
    exit()




class GameLibrary:
    def __init__(self):
        print("Welcome, " + mainmenu.name + ", to my python game library")
        print("\nWhich python game would you like to play?\n")
        print("1. Secret Number")
        print("0. Back to Main Menu")
        game_select = int(input("\nPlease enter a number:"))
        while game_select < 0 or game_select > 1:
            game_select = int(input("\nPlease enter a number:"))
        if game_select == 1:
            self.secret_number()
        elif game_select == 0:
            Mainmenu(startup.name)


    def secret_number(self):
        ceiling = int(input("\nPlease tell me the highest number for the game:"))
        floor = int(input("Please tell me the lowest number for the game:"))
        secret_number = round(random.random() * (ceiling - floor) + floor)
        guess = None
        while guess != secret_number:
            guess = int(input("\nGuess the number:"))
            if guess > secret_number:
                print("\nyour number is too high")
            elif guess < secret_number:
                print("your number is too low")
        print("Congratulations, you have guessed the number!")
        GameLibrary()