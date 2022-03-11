import mysql.connector

cnx = mysql.connector.connect(user='root',
                              password='PASSWORD',
                              host='localhost',
                              database='sygnalys')
cursor = cnx.cursor()

add_telemetry = ("INSERT INTO telemetry"
                 "(id, sensor, sn, gtw, vx)"
                 "VALUES (%s, %s, %s, %s, %s)")

data_telemetry = (6, 'vph-11', '9', 'g001', 2.5)

cursor.execute(add_telemetry, data_telemetry)

# query = "SELECT sensor, sn, gtw, vx FROM telemetry WHERE sn = '1'"

# cursor.execute(query)
for (sensor) in cursor:
    print(sensor)

cnx.commit()

cursor.close()
cnx.close()
