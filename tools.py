import os


def nornir_set_creds(norn, username="test", password=None):
    if not username:
        username = "vishnu"
    if not password:
        password = "vishnu"

    for host_obj in norn.inventory.hosts.values():
        host_obj.username = username
        host_obj.password = password
