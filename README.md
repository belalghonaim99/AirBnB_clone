#Airbnb Clone Console Application
##Learning Goals
General
Develop a Python package
Build a command interpreter using the cmd module in Python
Understand and implement Unit testing in a larger project context
Serialize and deserialize a Class effectively
Read and write JSON files
Manage datetime functionalities
Utilize UUIDs for unique identification
Grasp the usage of *args for variable-length arguments
Understand and use **kwargs for keyword arguments
Handle named arguments within functions
Initial Step: Creating a Command Interpreter for Airbnb Objects
This marks the initial phase of constructing the Airbnb clone project. This step holds significant importance as it establishes the foundation for subsequent tasks such as HTML/CSS templating, database storage, API integration, and front-end development.
Each task within this phase aims to:
Establish a parent class, termed BaseModel, responsible for initializing, serializing, and deserializing future instances
Construct a streamlined flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
Develop the necessary classes for Airbnb components (User, State, City, Place), all inheriting from BaseModel
Implement the foundational storage engine for the project: File storage
Create comprehensive unit tests to validate each class and the storage engine
Understanding the Command Interpreter
The concept of the command interpreter resembles that of a Shell, albeit specialized for our specific use-case. It empowers us to manage project objects, encompassing tasks like object creation, retrieval from various sources, performing operations, attribute updates, and object deletion.
Usage Scenarios
Interacting with the console can be done both in interactive mode and non-interactive mode, mirroring the behavior of a shell:
Interactive Mode:
bash
Copy code
$ ./console.py
(hbnb) help
Documented commands (type help ):
========================================
EOF help quit
(hbnb)
(hbnb)
(hbnb) quit
$
Non-Interactive Mode:
bash
Copy code
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help ):
========================================
EOF help quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help ):
========================================
EOF help quit
(hbnb)
$
Illustrative Examples
Here are some examples of using the console interactively:
scss
Copy code
(hbnb)create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb)show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'updated_at': datetime.datetime(2021, 2, 18, 18, 4, 12, 756946), 'created_at': datetime.datetime(2021, 2, 18, 18, 4, 12, 75683\
6), 'id': '49faff9a-6318-451f-87b6-910505c55907'}
(hbnb)update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb)show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb)destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb)show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) quit
Author
Robel Bekele
Belal Ghonaim
