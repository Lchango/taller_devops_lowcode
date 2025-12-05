# test_app.py
def test_main_output(capsys):
    # Importa la función main de tu archivo app.py
    import app

    # Ejecuta la función main
    app.main()

    # Captura la salida estándar (lo que se imprime)
    captured = capsys.readouterr()

    # Afirma (assert) que la salida es la esperada
    expected_output = "¡Hola, esta es una demo simple para el taller de DevOps + Low Code!\n"
    assert captured.out == expected_output