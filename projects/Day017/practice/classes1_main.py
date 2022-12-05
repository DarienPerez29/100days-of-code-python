class User:
    def __init__(self, id_user, username):
        self.id_user = id_user
        self.username = username
        self.followers = 0


user1 = User(1, "Usuario1")
user2 = User(2, "Usuario2")

print(user1.username)
print(user2.username)
