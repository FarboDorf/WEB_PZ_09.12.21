import psycopg2


connection = psycopg2.connect(user="postgres",
                              password="farbod",
                              host="127.0.0.1",
                              port="5432",
                              database="phone_book")
cursor = connection.cursor()


def select():
    cursor.execute("SELECT * "
                   "FROM main "
                   "INNER JOIN name ON main.name=name.n_id "
                   "INNER JOIN family ON main.family=family.f_id "
                   "INNER JOIN patronymic ON main.patronymic=patronymic.p_id "
                   "INNER JOIN street ON main.street=street.s_id ")
    return cursor.fetchall()
