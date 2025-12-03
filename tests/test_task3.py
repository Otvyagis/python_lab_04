from app.task3 import build_table

def test_build_table():
    result = build_table("a b c d e f")
    assert result == ["a b c", "d e f"]
