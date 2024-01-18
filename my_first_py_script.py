import mysql.connector


#Esse é um script simples em python para inserir no banco de dados funcionários de uma empresa

config = {
  'user': 'root',
  'password': 'MyNewPass',
  'host': '127.0.0.1',
  'database': 'teste_db',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

###input

print("Cadastro de empregados da empresa ---- \n")

first_name = input("Entre o primeiro nome: ")
last_name = input("Entre o sobrenome: ")
email = input("Entre o email: ")

add_employee_query = ("INSERT INTO employees "
               "(first_name, last_name, email) "
               "VALUES (%s, %s, %s)")

data_employee = (first_name, last_name, email)

try:
    cursor.execute(add_employee_query, data_employee)
    cnx.commit()
    print(f" -{first_name} {last_name} - {email} foi adicionado ao sistema \n\n")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    cnx.rollback() 


###output

query = ("SELECT first_name, last_name, email FROM `employees`" "WHERE 1")

cursor.execute(query)


print(" === Lista de empregados cadastrados na empresa: ===\n")

for (first_name, last_name, email) in cursor:
    print("-> {} {} - Email: {}".format(first_name, last_name, email))

cursor.close()
cnx.close()