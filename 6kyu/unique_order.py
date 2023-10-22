def unique_in_order(sequence):
    sequence_list = list(sequence)
    index_delete_sequence = []
    for position, value in enumerate(sequence_list):
        posicion_siguiente = position + 1
        if posicion_siguiente == len(sequence_list):
            continue
        if value == sequence_list[posicion_siguiente]:
            index_delete_sequence += [position]
    for index in sorted(index_delete_sequence, reverse=True):
        del sequence_list[index]
    return sequence_list

print(unique_in_order("AAAABBBCCDAABBB"))