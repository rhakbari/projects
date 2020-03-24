def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age


my_limit = allowed_dating_age(21)

print("i can date girls", my_limit, "or older")
