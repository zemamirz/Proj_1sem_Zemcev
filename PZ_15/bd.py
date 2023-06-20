# Вариант 3.
# Разработать БД «ЗАРПЛАТА», содержащую две таблицы Анкета и
# Больничные листы. Установить связь между таблицами. Заполнить
# таблицы произвольными данными (не менее 10 записей). Реализовать
# SQL-запросы на выборку, обновление, удаление данных из БД.

import sqlite3 as sq
from bd_data import *

with sq.connect('Zarplata.db') as con:
    cur = con.cursor()
    # CREATE
    cur.execute('CREATE TABLE IF NOT EXISTS Anketa ('
                'a_id INT PRIMARY KEY,'
                'name VARCHAR,'
                'surname VARCHAR,'
                'birthday DATE,'
                'sex VARCHAR,'
                'data_naim DATE,'
                'dolznost VARCHAR,'
                'otdel VARCHAR,'
                'baze_stavka VARCHAR'
                ')')
    cur.execute('CREATE TABLE IF NOT EXISTS Bolnichnie_lists ('
                'bl_id INT PRIMARY KEY,'
                'data_start DATE,'
                'data_finish DATE,'
                'prichina VARCHAR,'
                'diagnoz VARCHAR,'
                'oplachen VARCHAR,'
                'a_id INT,'
                'FOREIGN KEY(a_id) REFERENCES Anketa(a_id)'
                ')')
    # INSERT
    cur.executemany('INSERT INTO Anketa VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (data_anketa))
    cur.executemany('INSERT INTO Bolnichnie_lists VALUES (?, ?, ?, ?, ?, ?, ?)', (data_bl))
    # SELECT
    print('SELECT')
    print('1. Вывести список всех сотрудников и их должностей')
    print(cur.execute('SELECT name, surname, dolznost FROM Anketa').fetchall())
    print('2. Вывести список всех сотрудников и их базовых ставок')
    print(cur.execute('SELECT name, surname, baze_stavka FROM Anketa').fetchall())
    print('3. Вывести список всех сотрудников, работающих в отделе "IT"')
    print(cur.execute('SELECT name, surname, otdel FROM Anketa WHERE otdel="IT"').fetchall())
    print('4. Вывести список всех сотрудников, принятых на работу после 1 января 2022 года')
    print(cur.execute('SELECT name, surname, data_naim FROM Anketa WHERE data_naim > "2021-01-01"').fetchall())
    print('5. Вывести список всех больничных листов, выписанных сотруднику с id = 42')
    print(cur.execute('SELECT * FROM Bolnichnie_lists WHERE a_id = 2').fetchall())
    print('6. Вывести список всех больничных листов, оплаченных компанией')
    print(cur.execute('SELECT * FROM Bolnichnie_lists WHERE oplachen = "да"').fetchall())
    print('7. Вывести список всех сотрудников, имеющих больничные листы на текущий месяц')
    print(cur.execute('SELECT name, surname, Bolnichnie_lists.data_start FROM Anketa INNER JOIN Bolnichnie_lists ON '
                      'Anketa.a_id = Bolnichnie_lists.bl_id WHERE data_start BETWEEN "2023-04-01" AND "2023-04-30"').fetchall())
    print('8. Вывести среднюю базовую ставку всех сотрудников')
    print(cur.execute('SELECT AVG(baze_stavka) FROM Anketa').fetchall())
    print('9. Вывести список всех сотрудников, имеющих базовую ставку выше 100 000')
    print(cur.execute('SELECT name, surname, baze_stavka FROM Anketa WHERE baze_stavka > 100000').fetchall())
    print('10. Вывести список всех сотрудников и общее количество дней, проведенных ими на больничном')
    print(cur.execute('SELECT name, surname, SUM(julianday(Bolnichnie_lists.data_finish)-julianday('
                      'Bolnichnie_lists.data_start)) FROM Anketa INNER JOIN Bolnichnie_lists ON Anketa.a_id = '
                      'Bolnichnie_lists.a_id GROUP BY Anketa.a_id').fetchall())
    print('11. Вывести информацию о сотрудниках и их больничных листах за последний месяц')
    print(cur.execute('SELECT *, Bolnichnie_lists.* FROM Anketa INNER JOIN Bolnichnie_lists ON Anketa.a_id = '
                      'Bolnichnie_lists.bl_id WHERE data_start BETWEEN "2023-04-01" AND "2023-04-30"').fetchall())
    print('12. Вывести среднюю продолжительность больничных листов сотрудников в каждом отделе')
    print(cur.execute('SELECT DISTINCT otdel, AVG(julianday(Bolnichnie_lists.data_finish) - julianday('
                      'Bolnichnie_lists.data_start)) FROM Anketa INNER JOIN Bolnichnie_lists ON Anketa.a_id = '
                      'Bolnichnie_lists.a_id GROUP BY Anketa.a_id').fetchall())
    print('13. Вывести список сотрудников и информацию о последнем больничном листе, который они оформляли')
    print(cur.execute('SELECT Anketa.name, Anketa.surname, Bolnichnie_lists.* FROM Anketa INNER JOIN Bolnichnie_lists '
                      'ON Anketa.a_id = Bolnichnie_lists.a_id GROUP BY Anketa.a_id ORDER BY '
                      'Bolnichnie_lists.data_start DESC').fetchall())
    print('14 .Вывести список сотрудников и информацию о первом больничном листе, который они оформляли')
    print(cur.execute('SELECT Anketa.name, Anketa.surname, Bolnichnie_lists.* FROM Anketa INNER JOIN Bolnichnie_lists '
                      'ON Anketa.a_id = Bolnichnie_lists.a_id GROUP BY Anketa.a_id ORDER BY '
                      'Bolnichnie_lists.data_start ASC').fetchall())
    print('15. Вывести список сотрудников и суммарную продолжительность их больничных листов в текущем году')
    print(cur.execute('SELECT name, surname, SUM(julianday(Bolnichnie_lists.data_finish)-julianday('
                      'Bolnichnie_lists.data_start)) FROM Anketa INNER JOIN Bolnichnie_lists ON Anketa.a_id = '
                      'Bolnichnie_lists.bl_id WHERE data_start BETWEEN "2023-01-01" AND "2023-12-30"').fetchall())
    # UPDATE
    # print('UPDATE')
    # cur.execute('UPDATE Anketa SET baze_stavka = 100000 WHERE dolznost="менеджер"')
    # cur.execute('UPDATE Anketa SET otdel="IT" WHERE Birthday BETWEEN "1991-01-10" AND "1994-01-10"')
    # cur.execute('UPDATE Anketa SET data_naim = "2023-03-10" WHERE dolznost="администратор"')
    # cur.execute('UPDATE Bolnichnie_lists SET prichina="проблема со зрением" WHERE bl_id=8')
    # DELETE
    # cur.execute('DELETE FROM Bolnichnie_lists WHERE a_id = (SELECT DISTINCT a_id FROM Anketa WHERE name = "Иван")')
    # cur.execute('DELETE FROM Bolnichnie_lists WHERE a_id = (SELECT DISTINCT a_id FROM Anketa WHERE surname = "Петров")')
    # cur.execute('DELETE FROM Bolnichnie_lists WHERE a_id = (SELECT a_id FROM Anketa WHERE dolznost = "менеджер")')
    # cur.execute('DELETE FROM Bolnichnie_lists WHERE a_id = (SELECT a_id FROM Anketa WHERE otdel = "Продаж")')
    # cur.execute('DELETE FROM Bolnichnie_lists WHERE a_id = (SELECT a_id FROM Anketa WHERE sex = "ж")')
    # cur.execute('DELETE FROM Bolnichnie_lists WHERE a_id = (SELECT a_id FROM Anketa WHERE julianday('
    #             'birthday)-julianday("2023-04-10") < -18000)')
    # cur.execute('DELETE FROM Bolnichnie_lists WHERE oplachen = "нет"')
    # cur.execute('DELETE FROM Bolnichnie_lists WHERE data_finish < "2023-04-14"')
    # cur.execute('DELETE FROM Bolnichnie_lists WHERE data_start > "2023-01-01"')
    # cur.execute('DELETE FROM Bolnichnie_lists WHERE data_finish > "2023-01-01"')
    # cur.execute('DELETE FROM Bolnichnie_lists WHERE a_id = (SELECT a_id FROM Anketa WHERE surname LIKE "C%")')
    # cur.execute('DELETE FROM Bolnichnie_lists WHERE a_id = (SELECT a_id FROM Anketa WHERE dolznost = "менеджер" AND '
    #             'oplachen = "нет")')
    # cur.execute('DELETE FROM Bolnichnie_lists WHERE a_id = (SELECT a_id FROM Anketa WHERE otdel = "IT" AND '
    #             'data_finish > "2023-01-01")')