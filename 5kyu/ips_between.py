def ips_between(start, end):
    start_octets = list(map(int, start.split('.')))
    end_octets = list(map(int, end.split('.')))

    difference = 0
    for i in range(4):
        difference = difference * 256 + (end_octets[i] - start_octets[i])

    return difference