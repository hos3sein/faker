from faker import Faker  
  
import json         
   
from random import randint    

import pandas as pa  
  

fake = Faker()  
  
def input_data(x):  
  
    # dictionary  
    student_data ={}  
    for i in range(0, x):  
        student_data[i]={}  
        student_data[i]['id']= randint(1, 1000)  
        student_data[i]['name']= fake.name()  
        student_data[i]['address']= fake.address()  
        student_data[i]['latitude']= str(fake.latitude())  
        student_data[i]['longitude']= str(fake.longitude())  
    print(student_data)  
    
    p = pa.DataFrame(student_data)
    p.to_csv('fakedata' , index = True)




    # dictionary dumped as json in a json file  
    # with open('students.json', 'w') as fp:  
        # json.dump(student_data, fp)

      
  
def main():  
   
    number_of_students = 100
    input_data(number_of_students)  
main()  
