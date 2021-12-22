import mysql.connector  # Importing Connector package
mysqldb = mysql.connector.connect(host="localhost", user="root", password="root",database="scaleddb")  # established connection
mycursor = mysqldb.cursor()

def func(prBig,prSmall):
    try:
        # Execute SQL Query to display all record
        # df = pd.read_sql_query("select * from  where scaledata.expected_output>= '%s' and scaledata.expected_output<= '%s'" % (prBig, prSmall), mysqldb)

        s = "select actualdata.Model, actualdata.clock_speed, actualdata.ram, actualdata.storage, actualdata.price from actualdata inner join scaledata on actualdata.id = scaledata.id where scaledata.expected_output >="
        s1 = " and "
        s2 = "scaledata.expected_output <= "
        totalString = s + prSmall + s1 + s2 + prBig
        print(totalString)
        print(prBig)
        print(prSmall)
        mycursor.execute(totalString)
        result = mycursor.fetchall()  # fetches all the rows in a result set
        return result
    except:
        print('Error:Unable to fetch data.')
    mysqldb.close()