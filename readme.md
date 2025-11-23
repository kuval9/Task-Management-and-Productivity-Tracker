# Task Management and Productivity Tracker
A simple, menu-based program created for the Intro to Problem Solving & Programming course.

Project Overview :

## 1. Project Overview
This project is a simple Task Management System that helps users keep a list of tasks, mark them as completed, and delete them if there is a need for that. This is deliberately simple-not because the problem is trivial, but because clarity and clean logic matter more than unnecessary complexity, especially in an introductory programming course.

The project has showcased some fundamental problem-solving concepts: modular design, step-wise refinement, and algorithmic thinking. Everything has been built from scratch, using only core Python features.

## 2. Problem Statement
Very often, people have difficulties in keeping track of minor daily tasks. Even the simplest workflows seem to be chaotic without a proper structure.
This project tries to solve that problem by providing a lightweight, text-based system that allows its users to:
- View all tasks
- Marking tasks as done
- Delete tasks
Nothing fancy, just the basics — cleanly executed.

## 3. Objectives
Objectives of the project:
Implement a basic, working task manager.
- Demonstrate structured programming and modularisation.
- Employ problem-solving skills learned throughout the course.
- Write clean, readable, and beginner-friendly code.

## 4. System Design
The solution will be divided into two modules:
1. **main.py** – handles user interaction, displays menus, and takes input.
2. **task_manager.py** – keeps the `TaskManager` class responsible for all tasks manipulation.
This separation maintains the readability of the program and demonstrates intentional modularity.

## 5. Features
- Add new tasks
- Display all tasks with their status
- Strike off completed tasks
- Delete tasks
- Terminate the program gracefully
All output is simple, console-based, and easy to understand.

## 6. How It Works (Algorithm Summary)

### **Add Task** ###
1. User enters task description
2. Program stores it as a dictionary (`{"desc": …, "completed": False}`)

### **View Tasks ** ###
1. loop through list of tasks
2. Display Task Number, Description and Status
Mark Completed

### **Mark Completed**###
1. User supplies the task number
2. Program checks if it is valid
3. Updates `completed` to `True`

### **Delete Task**###
1. User input for task number
2. The program removes the task from the list
Every operation is intentionally simple and self-explaining.

## 7. How to Run the Program
1. Clone or download the repository.
2. Open the project folder in VS Code or any editor.
3. Execute the following command in the terminal:
'''
python main.py
'''
4. Use the menu to interact with the system. 

## 8. Screenshots 
All screenshots are stored in the `/screenshots` folder and include: - 
- Main menu
- Adding a task
- Task viewing
- Performing a task
- Removing a task
- Program termination 

## 9. Conclusion 
This may seem like a pretty minimalist project, but it's really what an introductory project in programming should look like: clean logic, correct modularisation, working code, and clarity about how the problem has been solved. It is not excessively ambitious; it is focused on correctness, clarity, and structure.