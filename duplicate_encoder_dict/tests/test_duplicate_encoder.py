from src.duplicate_encoder import duplicate_encoder
def test_no_repeat():
    assert duplicate_encoder("din") == "((("
def test_repeat():
    assert duplicate_encoder("recede") =="()()()"
def test_capitalice():
    assert duplicate_encoder("Success") == ")())())"
def test_extrange_input():
    assert duplicate_encoder("(( @") == "))(("