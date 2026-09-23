# Final Project: Student Management System

## Overview
A console-based Student Management System that combines everything learned
in this roadmap: variables, data types, conditions, loops, functions, lists,
dictionaries, OOP, file handling, exception handling, modules, and JSON
persistence.

## Features
- Add a student
- View all students
- Search for a student by name
- Update a student's data
- Delete a student
- Save data to a JSON file / load data on startup
- Input validation and error handling throughout

## Project Structure
```
final_project/
├── README.md
├── main.py
├── requirements.txt
├── src/
│   ├── models/student.py
│   ├── services/student_service.py
│   ├── repositories/json_repository.py
│   └── utils/validators.py
└── tests/
    └── test_student_service.py
```

## How to Run
```bash
cd projects/final_project
python main.py
```

## How to Test
```bash
cd projects/final_project
python -m pytest tests/
```
