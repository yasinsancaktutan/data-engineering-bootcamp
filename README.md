# data-engineering-bootcamp

## About

This is an application to insert downloaded imdb data files into a mysql instance. Mentioned files can be downloaded from [here](https://www.imdb.com/interfaces/)

## Steps to run

1. git clone <repo>
2. cd (to repo folder)
3. pip install venv
4. python -m virtualenv venv
5. source venv/bin/activate
6. pip install -r requirements.txt
7. python3 insert_exec_many.py

## Prerequisites

1. Install Mysql
2. Add mysql to your $PATH
3. Create a mysql instance and add your password into the "insert_exec_many" script.
