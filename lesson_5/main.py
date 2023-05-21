
import requests
from requests import get
from requests import post
"""
help(requests)

r = get("https://www.python.org")
print(r.status_code)
print(r.content)

payload = dict(key1='value1', key2='value2')
r = post('https://httpbin.org/post', data=payload)
print(r.text)





student = Student()
print(Student.__name__)
print(Student.__bases__)
print(type(Student))
print(type(str))
print(type(object))
"""
from classes.studen import Student
from classes.studen import Pupil

students = list()
for method in dir(students):
    print(method)

help(list)

print(issubclass(Student,object))

help(colorama)