import database_common


@database_common.connection_handler
def get_users(cursor):

    cursor.execute("""
        SELECT name, age FROM "user"
        """)

    users = cursor.fetchall()
    return users

