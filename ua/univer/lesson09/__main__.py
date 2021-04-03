import sqlite3


def get_album_by_author(author_name):
    with sqlite3.connect("Chinook_Sqlite.sqlite") as conn:
        cursor = conn.cursor()
        cursor.execute(f"""
        SELECT Album.Title, Artist.Name
        FROM Album JOIN Artist
        ON Album.ArtistId = Artist.ArtistId
        WHERE Artist.Name = '{author_name}'
        """);
        result_list = cursor.fetchall()
    return result_list

def insert_author(author_id, author_name):
    with sqlite3.connect("Chinook_Sqlite.sqlite") as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO Artist VALUES({author_id}, '{author_name}')")
        conn.commit()
        cursor.execute(f"SELECT COUNT(*) FROM  Artist ");
        return cursor.fetchone()

if __name__ == '__main__':
    result_list = get_album_by_author("Accept")
    print(result_list)
    for row in result_list:
        print(row)
    print(insert_author(301, "Jakson"))

