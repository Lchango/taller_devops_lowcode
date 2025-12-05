# test_app.py
def test_main_output(capsys):
    # Importa la función main de tu archivo principal. 
    # NOTA: Usamos 'aplicacion' para que coincida con el nombre en GitHub.
    import aplicacion

    # Ejecuta la función main
    aplicacion.main()

    # Captura la salida estándar (lo que se imprime)
    captured = capsys.readouterr()

    # Afirma (assert) que la salida es la esperada
    expected_output = "¡Hola, esta es una demo simple para el taller de DevOps + Low Code!\n"
    assert captured.out == expected_output