
class User:
    users_count = 0

    def __init__(self) -> None:
        User.users_count += 1

user_one = User()
user_two = User()

# print(user_one.users_count)
print(User.users_count)
