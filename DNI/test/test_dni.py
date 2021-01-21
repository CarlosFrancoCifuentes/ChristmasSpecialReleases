from src.dni import dni

def test_verificar_longitud_corto():
    assert "Error: dni demasiado largo o corto" == dni ("4567701C").verificar_longitud()
    assert "Error: dni demasiado largo o corto" == dni ("").verificar_longitud()
    assert "Error: dni demasiado largo o corto" == dni ("4567701C").verificar_longitud()

def test_verificar_longitud_largo():
    assert "Error: dni demasiado largo o corto" == dni ("762347634958726345Y").verificar_longitud()
    assert "Error: dni demasiado largo o corto" == dni ("10328471092834572893475U").verificar_longitud()

def test_verificar_letra():
    assert "45699019C" == dni("45699019C").verificar_letra()
    assert "C45699019" == dni("C45699019").verificar_letra()
    assert False == dni("45699019N").verificar_letra()

def test_creador_dni():
    assert "Error: dni demasiado largo o corto" == dni("456C").creador_dni()
    assert "Error: dni demasiado largo o corto" == dni("456").creador_dni()
    assert "Error: dni demasiado largo o corto" == dni("456456456745674568C").creador_dni()
    assert "Error: la letra no es correcta" == dni("45699019N").creador_dni()
    assert "45699019C" == dni("45699019C").creador_dni()
