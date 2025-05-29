from project import calculate_grad_decade, generate_itunes_url, figletized

def test_calculate_grad_decade():
    grad, decade = calculate_grad_decade(50, 2025)
    assert grad == 1993
    assert decade == 1990

def test_generate_itunes_url():
    url = generate_itunes_url(1990)
    assert url == "https://itunes.apple.com/search?term=90s+Hits+Essentials&entity=song&limit=200"

def test_figletized(capsys):
    figletized("Kevin")
    captured = capsys.readouterr()
    assert captured.out.strip() != ""
