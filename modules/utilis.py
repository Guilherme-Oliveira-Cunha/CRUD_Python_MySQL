import mysql.connector


def connect():
    try:
        conn = mysql.connector.connect(
            host="localhost", user="root", password="password", database="loja")
        return conn
    except mysql.connector.Error as err:
        print(f"Banco de Dados não conectado {err}")


def disconnect(conn):
    if conn:
        conn.close()


def insert():
    conn = connect()
    cursor = conn.cursor()

    try:
        name = input("Insira nome do produto: ")
        price = float(input("Insira valor do produto: "))
        stock = int(input("Insira a quantidade do produto: "))
    except(NameError, TypeError, SyntaxError, ValueError):
        print("Insira os valores preço e estoque de maneira correta")

    cursor.execute(
        f"INSERT INTO produtos(nome, preco, estoque) VALUES('{name}', '{price}', '{stock}')")

    conn.commit()
    cursor.close()
    disconnect(conn)


def inventory():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    product = cursor.fetchall()

    if len(product) > 0:
        print("----- ESTOQUE -----", end="\n\n")
        for item in product:
            print(f"ID: {item[0]}")
            print(f"NOME: {item[1]}")
            print(f"PREÇO: {item[2]}")
            print(f"ESTOQUE: {item[3]}", end="\n\n")
    else:
        print("ESTOQUE VAZIO!")

    conn.commit()
    cursor.close()
    disconnect(conn)


def delete():
    conn = connect()
    cursor = conn.cursor()

    try:
        remove = input("Deseja remover produto? SIM ou NÃO? ").upper()

        if remove == "SIM":
            product = int(input("Digite o codigo do produto: "))
            cursor.execute(f"DELETE FROM produtos WHERE id = {product}")
            if cursor.rowcount == 1:
                print("PRODUTO EXCLUÍDO COM SUCESSO!")

        elif remove == "NÃO":
            print("PRODUTO NÃO SERÁ EXCLUIDO!")
    except(NameError, TypeError, SyntaxError, ValueError):
        print("Resposta inválida, digite SIM ou NÃO!")

    conn.commit()
    cursor.close()
    disconnect(conn)


def update():
    conn = connect()
    cursor = conn.cursor()

    try:
        renew = input("Deseja atualizar produto? SIM ou NÃO? ").upper()

        if renew == "SIM":
            product = int(
                input("Digite o codigo do produto que deseja atualizar: "))
            price = float(input("Digite novo preço do produto:"))
            stock = int(input("Digite nova quantidade em estoque: "))
            cursor.execute(
                f"UPDATE produtos SET preco = '{price}', estoque = '{stock}' WHERE id = '{product}'")
            if cursor.rowcount == 1:
                print("PRODUTO ATUALIZADO COM SUCESSO!")

        elif renew == "NÃO" or "NAO":
            print("PRODUTO NÃO SERÁ ATUALIZADO!")
    except(NameError, TypeError, SyntaxError, ValueError):
        print("Resposta inválida!")

    conn.commit()
    cursor.close()
    disconnect(conn)


def menu():
    print(" ----- GERENCIAMENTO DE PRODUTOS ----- ", end="\n\n")
    print(" 1- INSERIR PRODUTO: ")
    print(" 2- LISTAR PRODUTO: ")
    print(" 3- DELETAR PRODUTO: ")
    print(" 4- ATUALIZAR PRODUTO: ", end="\n\n")

    try:
        receive = int(
            input("ESCOLHA UM NUMERO: "))
        if receive == 1:
            insert()
        elif receive == 2:
            inventory()
        elif receive == 3:
            delete()
        elif receive == 4:
            update()
    except(NameError, TypeError, SyntaxError, ValueError):
        print("Resposta inválida!")
