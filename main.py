# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from role import Role
from user import User


# function to check if the 1st role is parent of 2nd role
def is_parent(roles: list, r1: int, r2: int) -> bool:
    # find immediate parent of r2
    parent: int = -1
    for role in roles:
        # check if role matches with r2
        if role.id == r2:
            parent = role.parent
            break

    # check if parent of r2 is 0 => no parent
    if parent == 0:
        return False

    # check for parent match
    if parent == r1:
        return True

    # if no match, search for the parent of parent of r2
    return is_parent(roles, r1, parent)


# function to demontrate the required algorithm
# input parameters - collection of roles and users, user id
# output - gives a list of users subordinate to the given user id
def get_subordinates(roles: list, users: list, user_id: int) -> list:
    # required list of subordinates
    subordinates = []

    # first find the role of the user with given user id
    curr_role: int = -1

    # loop for all users and find the required user
    for user in users:
        if user_id == user.id:
            curr_role = user.role
            break

    # again go through all users
    # and add all those users to a list
    # whose role is direct or indirect child of the current role
    for user in users:
        # if the condition is true => subordinate
        if is_parent(roles, curr_role, user.role):
            subordinates.append(user)
            # also print for output
            print(f'Id : {user.id}, Name : {user.name}, Role : {user.role}')
        print('-------------------------------------------------------------------------------------')
    # return the subordinates list
    return subordinates


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # define roles
    roles: list = [
        Role(1, "System Administrator", 0),
        Role(2, "Location Manager", 1),
        Role(3, "Supervisor", 2),
        Role(4, "Employee", 3),
        Role(5, "Trainer", 3)
    ]
    # define users
    users: list = [
        User(1, "Adam Admin", 1),
        User(2, "Emily Employee", 4),
        User(3, "Sam Supervisor", 3),
        User(4, "Mary Manager", 2),
        User(5, "Steve Trainer", 5),
    ]
    # check for user # 1, 2, 3, 4
    # Getting Input from User
    while True:
        print('Enter User Id for which you want to print the Subordinates or 0 to offer a contract')
        while True:
            try:
                s = int(input('"Enter -> "'))
                break
            except ValueError as e:
                print('You have entered invalid User ID\n'
                      'Please Enter Valid User Id\n'
                      '-------------------------------------------------------------------------------------')
        if 0 < s <= len(users):
            subordinates = get_subordinates(roles, users, s)
        elif s > len(users):
            print('User Id is out of range, You have entered wrong User ID\n'
                  'Please Enter Valid User Id\n'
                  '-------------------------------------------------------------------------------------')
        else:
            print('You Entered 0, I hope the code is up to the mark and contract is on the way !!!\n'
                  'Exiting!!!')
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
