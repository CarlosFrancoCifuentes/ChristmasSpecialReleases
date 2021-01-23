from src.bowling import Game_Score

def test_bolera():
    assert 60 == Game_Score("12345123451234512345").calculate_points()
    assert 90 == Game_Score("9-9-9-9-9-9-9-9-9-9-").calculate_points()
    assert 150 == Game_Score('5/5/5/5/5/5/5/5/5/5/5').calculate_points()
    assert 141 == Game_Score('XXX9-9-9-9-9-9-9-').calculate_points()
    assert 111 == Game_Score('9-9-9-9-9-9-9-9-9-XXX').calculate_points()
    assert 149 == Game_Score('8/549-XX5/53639/9/X').calculate_points()
    assert 175 == Game_Score('X5/X5/XX5/--5/X5/').calculate_points()
    assert 120 == Game_Score('XX9-9-9-9-9-9-9-9-').calculate_points()
    