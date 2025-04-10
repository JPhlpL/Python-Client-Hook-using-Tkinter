import os
import getpass

def get_current_user():
    # Get the username of the current user
    user = getpass.getuser()
    return user

if __name__ == "__main__":
    current_user = get_current_user()
    print(f"The current logged-in user is: {current_user}")