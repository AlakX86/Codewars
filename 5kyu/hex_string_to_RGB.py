def hex_string_to_RGB(hex_string):
    hex_string = hex_string.lstrip('#').upper()

    if len(hex_string) != 6:
        raise ValueError("El formato del color hexadecimal no es válido")

    r = int(hex_string[0:2], 16)
    g = int(hex_string[2:4], 16)
    b = int(hex_string[4:6], 16)

    return {"r": r, "g": g, "b": b}