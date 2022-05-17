# age: int
# -> arrow notation specifies the type the function must return

# this specifies that age will be using int in the future

def can_drive(age: int) -> bool:
    if age < 18:
        print("Can drive")
        return True
    else:
        print("Cannot drive")
        return False


can_drive(20)
can_drive(5)