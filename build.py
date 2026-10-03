# Gera index.html (arquivo único) embutindo as fotos da pasta fotos/ no template.
import base64, json, pathlib
root = pathlib.Path(__file__).parent
fotos = sorted((root / "fotos").glob("foto*.jpg"))
uris = ["data:image/jpeg;base64," + base64.b64encode(f.read_bytes()).decode() for f in fotos]
html = (root / "template.html").read_text(encoding="utf-8")
html = html.replace("/*__PHOTOS__*/[]", json.dumps(uris))
musica = root / "musica.m4a"
if musica.exists():
    html = html.replace("/*__MUSIC__*/''", json.dumps("data:audio/mp4;base64," + base64.b64encode(musica.read_bytes()).decode()))
(root / "index.html").write_text(html, encoding="utf-8")
print(f"index.html gerado com {len(uris)} fotos ({len(html)//1024} KB)")
