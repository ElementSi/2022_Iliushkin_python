class User:
    def __init__(self, i, n):
        self.id = i
        self.name = n


class Server:
    def __init__(self, i, n, u):
        self.id = i
        self.name = n
        self.userids = u


N = int(input())
users = []
for i in range(N):
    in_str = input().split()
    users.append(User(int(in_str[0]), in_str[1]))

M = int(input())
servers = []
for i in range(M):
    in_str = input().split()
    servers.append(Server(int(in_str[0]), in_str[1], [int(x) for x in in_str[2:]]))

target_id = int(input())

contact_ids_set = set()

for server in servers:
    if target_id in server.userids:
        contact_ids_set.update(server.userids)

contact_ids_set.remove(target_id)

contact_names_list = []

for userid in contact_ids_set:
    for user in users:
        if userid == user.id:
            contact_names_list.append(user.name)

contact_names_list.sort()

for name in contact_names_list:
    print(name)
