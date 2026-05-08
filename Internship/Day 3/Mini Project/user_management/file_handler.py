FILE = "users.txt"

def read_users():
    users = {}
    try:
        with open(FILE, "r") as f:
            for line in f:
                username, password = line.strip().split(",")
                users[username] = password
    except FileNotFoundError:
        open(FILE, "w").close()
    return users

def write_user(username, password):
    with open(FILE, "a") as f:
        f.write(f"{username},{password}\n")

def update_user(username, new_password):
    users = read_users()
    users[username] = new_password

    with open(FILE, "w") as f:
        for u, p in users.items():
            f.write(f"{u},{p}\n")

def delete_user(username):
    users = read_users()

    if username in users:
        del users[username]

    with open(FILE, "w") as f:
        for u, p in users.items():
            f.write(f"{u},{p}\n")