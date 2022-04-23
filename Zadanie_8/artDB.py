import os 
import sqlite3


def create_database(): 

        conn = sqlite3.connect("mydatabase.db") 
        cursor = conn.cursor() 

        # tworzenie tabeli 
        cursor.execute("""CREATE TABLE KLUBY (nazwa text, trener text,
        				kraj text, liczba_pilkarzy int, najlepszy_zawodnik text, sponsor_glowny text)""") 

        # insert  
        cursor.execute("""INSERT INTO KLUBY VALUES """
        				"('Bayern', 'Carlo Ancelotti', 'Niemcy', 11, 'Lewandowski', 'Warka')") 
        cursor.execute("INSERT INTO KLUBY VALUES "
        				"('Pogoń Szczecin', 'Paulo Sousa', 'Polska', 42, 'Marcin Najman', 'Razer')") 
        cursor.execute("INSERT INTO KLUBY VALUES "
        				"('Baza 44', 'Arhtur Czekotas', 'Siemanowice', 44, 'Arhur Czekotas', 'thepiratebay')") 
        cursor.execute("INSERT INTO KLUBY VALUES "
        				"('AC Milan', 'Paris Platynov', 'Włochy', 23, 'Kaka', 'Alfa Romeo')") 

        # zapisanie danych do bazy  
        conn.commit() 

def select_all_kluby(nazwa): 

    conn = sqlite3.connect("mydatabase.db") 
    cursor = conn.cursor() 
    sql = "SELECT kraj FROM KLUBY WHERE nazwa=?" 
    cursor.execute(sql, [(nazwa)]) 
    result = cursor.fetchall() 
    cursor.close() 
    conn.close() 
    return result 

def update_all_kluby(kraj, trener):

    conn = sqlite3.connect("mydatabase.db") 
    cursor = conn.cursor() 
    sql = "UPDATE KLUBY SET kraj=? WHERE trener=?" 
    cursor.execute(sql, [(kraj),(trener)]) 
    result = cursor.fetchall() 
    conn.commit()
    cursor.close() 
    conn.close() 
    return result 


def delete_all_kluby(nazwa):

    conn = sqlite3.connect("mydatabase.db") 
    cursor = conn.cursor() 
    sql = "DELETE FROM KLUBY WHERE nazwa=?" 
    cursor.execute(sql, [(nazwa)]) 
    result = cursor.fetchall() 
    conn.commit()
    cursor.close() 
    conn.close() 
    return result 

if __name__ == '__main__': 
    if not os.path.exists("mydatabase.db"): 
        create_database()

    #print(select_all_kluby('Bayern')) 
    #print(update_all_kluby(7, "Paris Platynov")) 
    #print(delete_all_kluby('Baza 44')) 
