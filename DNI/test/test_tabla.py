from src.tabla_dni import letra_dni

def test_calcular_letra():
    assert "M" == letra_dni("84820003").calcular_letra()
    assert "K" == letra_dni("55243468").calcular_letra()
    assert "C" == letra_dni("26115163").calcular_letra()
    assert "H" == letra_dni("86258321").calcular_letra()