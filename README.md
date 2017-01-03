# AMITY SPACE ALLOCATOR

[![Build Status](https://travis-ci.org/andela-austinroy/cp1-amity-space-allocation.svg?branch=develop)](https://travis-ci.org/andela-austinroy/cp1-amity-space-allocation) [![Coverage Status](https://coveralls.io/repos/github/andela-austinroy/cp1-amity-space-allocation/badge.svg?branch=develop)](https://coveralls.io/github/andela-austinroy/cp1-amity-space-allocation?branch=develop) [![Code Health](https://landscape.io/github/andela-austinroy/cp1-amity-space-allocation/develop/landscape.svg?style=plastic)](https://landscape.io/github/andela-austinroy/cp1-amity-space-allocation/develop)

Checkpoint one project on amity space allocation application system. The system allows you to add people to it and assigns them rooms automatically. These rooms are also created in the same system before assignment. The project was developed using and runs on python 2.7.


## Getting Started

These instructions will get you a copy of the project up and running.

### Prerequisites

1. Python 2.7
Comes inbuilt for unix but can be downloaded from
```
https://www.python.org/downloads/
```
if needed.

### Installing

A step by step series of examples that tell you have to get a development env running

Clone this repo from github by running:

```
$ git clone git@github.com:andela-austinroy/cp1-amity-space-allocation.git
```

Set up a virtual environment for the project and install the dependencies

```
$ mkvirtualenv amity
$ pip install -r requirements.txt
```

Run the app in interactive mode by executing
```
$ python app.py -i
```

Execute the commands:

1. `create_room <room_type> <room_name>...` - Creates rooms in Amity. It is possible to create multiple rooms of the same type by providing several room names after specifying the room type.

2. `add_person <person_name> <FELLOW|STAFF> [wants_accommodation]`- Adds a person to the system and allocates the person to a random room, wants_accommodation here is an optional argument which can be either Y or N. The default value if it is not provided is N.

3. `reallocate_person <person_identifier> <new_room_name>` - Reallocate the person with `person_identifier` as their id to a room called `new_room_name`.

4. `load_people <filename>` - Adds people to rooms from a txt file.

5. `print_allocations [--o=filename]`  - Prints a list of allocations onto the screen. Specifying the optional --o option here outputs the registered allocations to a txt file.

6. `print_unallocated [--o=filename]` - Prints a list of unallocated people to the screen. Specifying the --o option here outputs the information to the txt file provided.

7. `print_room <room_name>` - Prints  the names of all the people in `room_name` on the screen.

8. `save_state [--db=sqlite_database]` - Persists all the data stored in the app to a SQLite database. Specifying the --db parameter explicitly stores the data in the `sqlite_database` specified.

9. `load_state [--db=sqlite_database]` - Loads data from a database into the application.


## Running the tests

Tests on this project are done using python nose package. To run them type the script below in your terminal
`nosetests --with-coverage --rednose --cover-erase -v`
It should return the test results including coverage.

## Built With

* [Python](http://www.python.org) - A verstile programming language
* [Sqlite3](https://sqlite.org/) - Database Management engine
* [Docopt](https://rdecopt.org) - Python commandline arguement parser

## Authors

* **Austin Roy** - *Initial work* - [Austin Roy](https://github.com/andela-austinroy)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Several Andela fellows consulted during development
* Facilitators - Njira, Gibbs and Shem
