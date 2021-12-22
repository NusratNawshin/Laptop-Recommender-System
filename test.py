from numpy import exp, dot, array, random
import pandas as pd
import json
import numpy as np
import pickle
import pandas as pd

def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


def sigmoid(x):
    return 1 / (1 + exp(-x))


def think(inputs):
    return sigmoid(dot(inputs, synaptic_weights))


with open('json-file') as data_file:
    data = json.load(data_file)
    cs = float(data['clockspeed'])
    rm = float(data['ram'])
    Str = float(data['storage'])
    pr = float(data['price'])
    total = array([cs, rm, Str, pr])

# print(total)


# make prediction for new data
synaptic_weights = random.random((4, 1))

f = open('weight.pickle', 'rb')
synaptic_weights = pickle.load(f)

prediction = think(total)
pr = np.squeeze(np.asarray(prediction))
pr1 = pr.tolist()
# return json.dump(pr1)

path = './'
fileName = 'example.json'
data = {}
data['test1'] = pr1

writeToJSONFile(path, fileName, data)

demopr=pr1
print(type(pr1))
prBig=pr1+0.02
prSmall=demopr-0.02

import mysql.connector #Importing Connector package
mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="scaleddb")#established connection
mycursor=mysqldb.cursor()

try:

   #Execute SQL Query to display all record
   #df = pd.read_sql_query("select * from  where scaledata.expected_output>= '%s' and scaledata.expected_output<= '%s'" % (prBig, prSmall), mysqldb)

   s = "select actualdata.Model, actualdata.clock_speed, actualdata.ram, actualdata.storage, actualdata.price from actualdata inner join scaledata on actualdata.id = scaledata.id where scaledata.expected_output >="
   s1=" and "
   s2="scaledata.expected_output <= "
   totalString=s+str(prSmall)+s1+s2+str(prBig)
   print(totalString)
   mycursor.execute(totalString)
   result=mycursor.fetchall() #fetches all the rows in a result set

   for i in result:
      id=i[0]
      clock=i[1]
      ram=i[2]
      storage=i[3]
      price=i[4]
      print(id,clock,ram,storage,price)
except:
   print('Error:Unable to fetch data.')
mysqldb.close()#Connection Close

