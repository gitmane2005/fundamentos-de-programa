def remove_leading(ip):
    parts = ip.split(".")
    res = str(int(parts[0]))
    parts = parts[1:]
    for i in parts:
        res = res + "." + str(int(i))
            
    return res