import mysql.connector 

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password= '',
    database='bdcrud',
)

cursor = conexao.cursor()


cursor.close()
conexao.close()