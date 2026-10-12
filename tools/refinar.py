"""Refino das páginas "Defesa do Vendedor" para publicação.

Lê os originais aprovados (site/) e grava as versões refinadas em publicar/.
Não altera argumentos, citações, dados do caso nem a estrutura das páginas.

Uso: python3 tools/refinar.py
"""
import base64
import io
import re
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "site"
DST = ROOT / "publicar"
PAGES = ["defesa-vendedor.html", "caso-real.html", "contato-vendedor.html"]
BASE_URL = "https://junkesadvocacia.com.br/paginas/"
# Imagem de prévia (WhatsApp, Facebook, LinkedIn): publicar/og-defesa-vendedor.jpg, 1200x630,
# subida na mesma pasta das páginas.
OG_IMAGE = BASE_URL + "og-defesa-vendedor.jpg"


def share_tags(name):
    url = BASE_URL + name
    return (f'\n<link rel="canonical" href="{url}">'
            f'\n<meta property="og:url" content="{url}">'
            f'\n<meta property="og:image" content="{OG_IMAGE}">'
            '\n<meta property="og:image:width" content="1200">'
            '\n<meta property="og:image:height" content="630">'
            '\n<meta property="og:image:alt" content="Defesa do Vendedor: conta desativada ou saldo retido pela Amazon. Hemerson Henrique Junkes, OAB/PR 85.858.">'
            '\n<meta property="og:site_name" content="Junkes Advocacia e Consultoria">'
            '\n<meta name="twitter:card" content="summary_large_image">')

HEAD_EXTRA = """
<meta name="theme-color" content="#0D1A2B">
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"LegalService","name":"Junkes Advocacia e Consultoria","description":"Defesa de vendedores com conta desativada ou saldo retido em marketplaces. Atendimento online em todo o Brasil.","url":"https://junkesadvocacia.com.br/","telephone":"+55-41-99599-2256","email":"junkes.adv@gmail.com","address":{"@type":"PostalAddress","addressLocality":"Matinhos","addressRegion":"PR","addressCountry":"BR"},"areaServed":{"@type":"Country","name":"Brasil"},"employee":{"@type":"Person","name":"Hemerson Henrique Junkes","jobTitle":"Advogado (OAB/PR 85.858)"}}
</script>
<script>
/* Google Ads: depois de criar a conversão "Clique no WhatsApp", preencha os dois valores.
   Exemplo: { id: 'AW-123456789', label: 'AbCdEf12345' }. Em branco, nada é carregado. */
window.JUNKES_ADS = { id: '', label: '' };
(function (c) {
  if (!c || !c.id) return;
  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + c.id;
  document.head.appendChild(s);
  window.dataLayer = window.dataLayer || [];
  window.gtag = function () { dataLayer.push(arguments); };
  gtag('js', new Date());
  gtag('config', c.id);
})(window.JUNKES_ADS);
</script>
"""

CSS_COMMON = """
/* ===== refino out/2026 ===== */
/* Playfair usa algarismos antigos por padrão: "3 votos a 0" aparecia como "3 votos a o". */
html{font-variant-numeric:lining-nums;}
/* O padding próprio do banner anulava a margem lateral do .container. */
.cta-inner{padding-left:24px; padding-right:24px;}
/* No celular, a marca já está na barra fixa; a repetição no topo empurrava o título para baixo. */
@media (max-width:760px){ .hero-top{display:none;} }
/* width/height nas imagens evitam saltos de layout; a altura real continua vindo da proporção. */
.rv-shot img, .at-photo img{height:auto;}
/* Avaliações: uma grade sem repetições (o carrossel infinito havia sido desligado, mas as cópias ficaram). */
.rv-grid{max-width:1180px; margin:0 auto; padding:6px 24px 4px; display:grid; grid-template-columns:repeat(4,minmax(0,230px)); justify-content:center; gap:18px; align-items:start;}
.rv-grid .rv-shot{width:auto;}
@media (max-width:860px){
  .rv-grid{display:flex; overflow-x:auto; scroll-snap-type:x mandatory; gap:12px; padding:6px 24px 16px; -webkit-overflow-scrolling:touch;}
  .rv-grid .rv-shot{flex:0 0 74%; max-width:280px; scroll-snap-align:center;}
}
/* Botões secundários: um verde cheio por bloco, não seis seguidos. */
.wa-btn.soft{background:transparent; color:var(--green-dark); box-shadow:inset 0 0 0 1.5px var(--green);}
.wa-btn.soft svg{fill:currentColor;}
.wa-btn.soft:hover{background:var(--green); color:#fff;}
.wa-btn.soft:hover svg{fill:#fff;}
"""

CSS_CONTATO = """
/* Na página de contato, no celular, o formulário vem antes da foto ocupar a tela inteira. */
@media (max-width:760px){ .hero-photo{display:none;} }
"""

CONVERSION_JS = (
    "try { var A = window.JUNKES_ADS; if (A && A.id && A.label && typeof window.gtag === 'function')"
    " { window.gtag('event', 'conversion', {send_to: A.id + '/' + A.label}); } } catch(e){}"
)


def recompress(m):
    """Reencoda uma imagem embutida em WebP, se ficar menor; devolve a tag com width/height."""
    tag, mime, b64 = m.group(0), m.group(1), m.group(2)
    old_uri = f"data:{mime};base64,{b64}"
    raw = base64.b64decode(b64)
    im = Image.open(io.BytesIO(raw))
    w, h = im.size
    alt = re.search(r'alt="([^"]*)"', tag)
    is_print = bool(alt and alt.group(1).startswith("Print"))
    buf = io.BytesIO()
    im.convert("RGB").save(buf, "WEBP", quality=88 if is_print else 80, method=6)
    if buf.tell() < len(raw) * 0.92:
        mime, b64 = "image/webp", base64.b64encode(buf.getvalue()).decode()
    new = tag.replace(old_uri, f"data:{mime};base64,{b64}")
    if " width=" not in new:
        new = new.replace("<img ", f'<img width="{w}" height="{h}" decoding="async" ', 1)
    return new


def dedupe_reviews(html):
    """Troca as fileiras do carrossel (com cópias) por uma grade com cada avaliação uma vez."""
    row = r'<div class="rv-row"><div class="rv-track[^"]*">((?:<div class="rv-shot"><img[^>]*></div>)+)</div></div>'
    run = re.compile(r"(?:" + row + r"\s*)+")

    def repl(m):
        shots, seen = [], set()
        for s in re.findall(r'<div class="rv-shot"><img[^>]*></div>', m.group(0)):
            key = re.search(r'src="([^"]+)"', s).group(1)
            if key not in seen:
                seen.add(key)
                shots.append(s)
        return '<div class="rv-grid">' + "".join(shots) + "</div>\n"

    html, n = run.subn(repl, html)
    assert n == 1, f"esperava 1 bloco de avaliações, achei {n}"
    return html


def refine(name):
    html = (SRC / name).read_text(encoding="utf-8")
    before = len(html)

    html = dedupe_reviews(html)
    html = re.sub(r'<img [^>]*?src="data:(image/[a-z+]+);base64,([A-Za-z0-9+/=]+)"[^>]*>', recompress, html)

    # Rodapé: o número do processo permite consultar as partes no PJe; "sem os nomes" é o que de fato ocorre.
    assert html.count("sem identificação das partes") == 1
    html = html.replace("sem identificação das partes", "sem os nomes das partes")

    # Cards dos fundamentos: botão secundário.
    html = re.sub(r'<a class="wa-btn"(\s+href="[^"]*"\s+target="_blank" rel="noopener" data-cta="fundamento-)',
                  r'<a class="wa-btn soft"\1', html)

    # Conversão do Google Ads junto do evento já existente (links e formulário).
    hook = "try { if(typeof window.gtag === 'function'){ window.gtag('event', 'whatsapp_click', {cta: label, page: location.pathname}); } } catch(e){}"
    assert html.count(hook) == 1
    html = html.replace(hook, hook + "\n      " + CONVERSION_JS)
    form_hook = "try { if(typeof window.gtag === 'function'){ window.gtag('event', 'whatsapp_click', {cta: 'formulario', page: location.pathname}); } } catch(err){}"
    if form_hook in html:
        html = html.replace(form_hook, form_hook + "\n      " + CONVERSION_JS.replace("catch(e)", "catch(err)")
                            + "\n      try { (window.dataLayer = window.dataLayer || []).push({event:'whatsapp_click', cta:'formulario'}); } catch(err){}")

    css = CSS_COMMON + (CSS_CONTATO if name == "contato-vendedor.html" else "")
    assert html.count("</head>") == 1
    html = html.replace("</head>", share_tags(name) + HEAD_EXTRA + "<style>" + css + "</style>\n</head>")

    (DST / name).write_text(html, encoding="utf-8")
    print(f"{name}: {before/1024:,.0f} KB -> {len(html)/1024:,.0f} KB")


if __name__ == "__main__":
    DST.mkdir(exist_ok=True)
    for p in PAGES:
        refine(p)
    sys.exit(0)
