import sqlite3
import mysql.connector
class Artist:
    def __init__(self,artist_title, artist_name):
        self.artist_title = artist_title
        self.artist_name = artist_name

    def __str__(self) -> str:
        return f"{self.artist_title}, {self.artist_name}"

    def __repr__(self) -> str:
        return f"Artist({self.__str__()})"


def get_album_by_author(author_name):
 #   with sqlite3.connect("Chinook_Sqlite.sqlite") as conn:
     with mysql.connector.connect(host="127.0.0.1",
                          database= "chinook",
                          user="root",
                          password="root"
     ) as conn:
        #conn.charset ="utf-8"
        cursor = conn.cursor()
        cursor.execute(f"""
        SELECT Album.Title, Artist.Name
        FROM Album JOIN Artist
        ON Album.ArtistId = Artist.ArtistId
        WHERE Artist.Name = '{author_name}'
        """);
        result_list = cursor.fetchall()
        artists_list= []
        for result in result_list:
            artists_list.append(Artist(result[0],result[1]))
     return artists_list

def insert_author(author_id, author_name):
    with sqlite3.connect("Chinook_Sqlite.sqlite") as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO Artist VALUES({author_id}, '{author_name}')")
        conn.commit()
        cursor.execute(f"SELECT COUNT(*) FROM  Artist ");
        return cursor.fetchone()

def update_author(author_id, author_name):
    with sqlite3.connect("Chinook_Sqlite.sqlite") as conn:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE Artist SET Name = '{author_name}' WHERE ArtistId = {author_id}")
        conn.commit()
        cursor.execute(f"SELECT COUNT(*) FROM  Artist ");
        return cursor.fetchone()

def delete_author(author_id):
    with sqlite3.connect("Chinook_Sqlite.sqlite") as conn:
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM Artist WHERE ArtistId = {author_id}")
        conn.commit()
        cursor.execute(f"SELECT COUNT(*) FROM  Artist ");
        return cursor.fetchone()

if __name__ == '__main__':
    result_list = get_album_by_author("Accept")
    print(result_list)
    for row in result_list:
        print(row)
    #print(delete_author(301))

