import mysql.connector

my_database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="6626@Sql2206",
    database="sql_learn",  # add this line if the database is already created
)
