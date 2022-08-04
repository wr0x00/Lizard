import socket


def subdomain(domain, dictonary):
    with open(dictonary, 'r') as f:
        for i in f:
            i = i.strip()
            subdomain = i + '.' + domain
            try:
                ip = socket.gethostbyname(subdomain)
                print("\033[1;32;40m %s \033[0m" % (subdomain + '   ' + ip))
            except Exception:
                pass
