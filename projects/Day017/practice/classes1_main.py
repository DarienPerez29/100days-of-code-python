class User:
    def __init__(self, id_user, username):
        self.id_user = id_user
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User(1, "Usuario1")
user2 = User(2, "Usuario2")

user1.follow(user2)

print("USER 1")
print(f"Followers: {user1.followers}")
print(f"Following: {user1.following}")
print()
print("USER 2")
print(f"Followers: {user2.followers}")
print(f"Following: {user2.following}")
