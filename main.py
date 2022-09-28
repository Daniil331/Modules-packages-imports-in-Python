import py_youtube

from application import salary
from application.db import people
from datetime import datetime, date, time
from py_youtube import Data


if __name__ == '__main__':
    people.get_employees()
    salary.calculate_salary()
    print(datetime.now())


    data = Data("https://www.youtube.com/watch?v=tsE7rmev0kY").data()
    print(data)

