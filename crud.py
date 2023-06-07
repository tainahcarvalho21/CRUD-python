import mysql.connector 

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password= '',
    database='bdcrud',
)

cursor = connection.cursor()

#Create
#produto = ""
#valor = 
new_product = f'INSERT INTO vendas (produto, valor) VALUES ("{produto}", {valor})'
cursor.execute(new_product)
connection.commit()

#Read
buscar_produtos = f'SELECT * FROM vendas'
cursor.execute(buscar_produtos)
produtos = cursor.fetchall()
print(produtos)

#Update
#produto = ""
#valor = 
update = f'UPDATE vendas SET valor = {valor} WHERE produto = "{produto}"'
cursor.execute(update)
connection.commit()

#Delete
#produto = ""
delete = f'DELETE FROM vendas WHERE produto = "{produto}"'
cursor.execute(delete)
connection.commit()


cursor.close()
connection.close()