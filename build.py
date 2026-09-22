#!/usr/bin/env python3
"""Builds index.html from the exact Canva geometry (1920x1080 page units).
Every slide of the Canva deck = one <section>, same order, same positions."""
import html, json

INK, MINT, PAPER = "#151515", "#79efcf", "#e7e7e9"
W = {"L": 300, "N": 400, "B": 700, "H": 800}

def T(x, y, w, fs, wt, al, lh, ls, col, txt, cls="", href=None, under=False):
    return dict(k="t", x=x, y=y, w=w, fs=fs, wt=wt, al=al, lh=lh, ls=ls, col=col, txt=txt,
                cls=cls, href=href, under=under)

def CARD(x, y, w, h, col, kids):
    return dict(k="card", x=x, y=y, w=w, h=h, col=col, kids=kids)

def mint_card(x, y, w, h, title, desc, metaL=None, metaR=None, tx=None, ty=None,
              dy=None, my=None, rx=None, dlh=1, ttw=392.59, col=INK, bg=MINT):
    kids = [T(tx, ty, ttw, 32, "B", "start", 1, 0, col, title, "c-title")]
    kids.append(T(tx if isinstance(dy, (int, float)) else dy[0], dy if isinstance(dy, (int, float)) else dy[1],
                  689.06, 26.667, "L", "justify", dlh, 0, col, desc, "c-desc"))
    if metaL:
        kids.append(T(tx, my, 334.79, 26.667, "L", "justify", 1, 0, col, metaL, "c-meta"))
        kids.append(T(rx, my, 334.79, 26.667, "L", "end", 1, 0, col, metaR, "c-meta c-meta-r"))
    return CARD(x, y, w, h, bg, kids)

def dark_card(x, y, w, h, tx, t1, t2, desc, dy, metaL, metaR, my, rx):
    kids = [T(tx, y + 36.46, 412.01, 32, "B", "start", 1, 0, "#fff", t1, "c-title"),
            T(tx, y + 91.45, 412.01, 32, "B", "start", 1, 0, "#fff", t2, "c-title"),
            T(tx, dy, 471.30, 26.667, "L", "justify", 1.14, 0, "#fff", desc, "c-desc"),
            T(tx, my, 334.79, 26.667, "L", "justify", 1, 0, "#fff", metaL, "c-meta"),
            T(rx, my, 334.79, 26.667, "L", "end", 1, 0, "#fff", metaR, "c-meta c-meta-r")]
    return CARD(x, y, w, h, INK, kids)

def header_footer(col="#fff"):
    return [T(108, 108, 414.73, 26.667, "B", "start", 1.4, 0, col, "celia muntaner", "hf"),
            T(1397.27, 109.67, 414.73, 26.667, "N", "end", 1.05, 0, col, "creative and design<br>brand manager", "hf"),
            T(112.35, 940.33, 449.48, 26.667, "N", "start", 1.4, 0, col, "+34 669 07 07 81", "hf", href="tel:+34669070781"),
            T(1362.52, 940.21, 449.48, 26.667, "N", "end", 1.4, 0, col, "celiamuntaner@gmail.com", "hf", href="mailto:celiamuntaner@gmail.com")]

S = []  # slides

# 1 — cover
S.append(dict(n=1, bg=INK, els=[T(212.35, 460.33, 1495.30, 106.667, "H", "center", .77, -.058, "#fff", "portfolio", "big")] + header_footer()))

# 2 — about
S.append(dict(n=2, bg=PAPER, media=dict(img="images/2.jpg"), mcrop=[1420.53, 255.07, 391.47, 487.23], els=[
    T(108, 108, 1343.99, 80.0045, "N", "start", .86, -.06, INK, "celia muntaner", "h-name"),
    T(108, 239.41, 550.46, 26.667, "L", "justify", 1.14, .005, INK,
      "<b>Directora creativa y de arte</b> con más de 6 años de experiencia, especializada en el sector de la cosmética y el skincare. <br><br>"
      "Mi actual proyecto es <b>Binomial skincare</b>, una marca de dermocosmética de mesoestetic Pharme Group. Involucrada desde la fase previa al lanzamiento de la marca, liderando la dirección creativa, la identidad visual y la estrategia de la marca. Conceptualizo campañas y su desarrollo en diferentes canales (social, paid, web, offline..)<br><br>"
      "Además, desarrollo funciones de Brand Manager, participo en la implementación de estrategias de marca, desde el rendimiento de ventas, los canales de distribución y la comunicación directa con agencias y proveedores.<br><br>"
      "Poseo experiencia previa en agencia que me aportó una visión transversal del sector creativo y una excelente capacidad de respuesta ante grandes ritmos de trabajo.", "bio"),
    T(736.64, 239.41, 550.46, 26.667, "B", "justify", 1, 0, INK, "experiencia", "exp"),
    T(736.64, 295.51, 550.46, 26.667, "B", "justify", 1, 0, INK, "Creativity and Design Manager", "exp"),
    T(736.64, 338.74, 550.46, 26.667, "N", "justify", 1, 0, INK, "Binomial (mesoestetic Pharma group)", "exp"),
    T(734.80, 382.52, 550.46, 26.667, "N", "justify", 1, 0, INK, "abril 2024 - actualidad", "exp"),
    T(736.64, 438.85, 550.46, 26.667, "B", "justify", 1, 0, INK, "Mid Art Director", "exp"),
    T(736.64, 482.08, 550.46, 26.667, "N", "justify", 1, 0, INK, "Multiplica (fusión beAgency)", "exp"),
    T(734.80, 525.86, 550.46, 26.667, "N", "justify", 1, 0, INK, "mar. 2022 - abr. 2024", "exp"),
    T(736.64, 595.19, 550.46, 26.667, "B", "justify", 1, 0, INK, "Art Director", "exp"),
    T(736.64, 638.42, 550.46, 26.667, "N", "justify", 1, 0, INK, "beAgency", "exp"),
    T(734.80, 682.20, 550.46, 26.667, "N", "justify", 1, 0, INK, "oct. 2020 - mar. 2022", "exp"),
    T(736.64, 929.67, 550.46, 26.667, "B", "justify", 1, 0, INK, "descargar cv completo", "exp cv",
      href="https://drive.google.com/file/d/1gX9Obmp7R_uWD_anFI1lg9Vw4PGQZEC0/view?usp=sharing", under=True),
    T(1644.60, 225.01, 161.95, 24, "B", "end", 1, 0, INK, "*", "star"),
    T(1477.21, 758.96, 334.79, 26.667, "L", "end", 1.12, 0, INK, "celiamuntaner@gmail.com<br>669 07 07 81<br>Barcelona", "contact2"),
]))

# 3 — index (rows = line + number + label, exact Canva coordinates)
rows = [("001", "branding y packaging", MINT, "s4"), ("002", "evento lanzamiento", MINT, "s10"),
        ("003", "contenido generado con IA", MINT, "s14"), ("004", "campañas", MINT, "s17"),
        ("005", "creative content", MINT, "s20"), ("006", "activaciones offline", MINT, "s21"),
        ("007", "levi’s", "#fff", "s23"), ("007", "rilastil", "#fff", "s25"), ("007", "ribs", "#fff", None)]
lineY = [293.20, 376.72, 460.24, 543.76, 627.76, 711.61, 795.47, 879.32, 963.18]
labY = [300.27, 383.79, 467.31, 550.83, 634.83, 718.68, 802.54, 886.39, 970.24]
numY = [321.74, 405.26, 488.78, 572.30, 656.29, 740.15, 824.00, 907.86, 991.71]
S.append(dict(n=3, bg=INK, rows=[dict(num=r[0], lab=r[1], col=r[2], href=r[3], ly=lineY[i], ty=labY[i], ny=numY[i])
                                 for i, r in enumerate(rows)], els=[]))

# 4 — Binomial intro
d4 = dict(fs=26.667, wt="N", al="justify", lh=1.17, ls=0, col=INK)
S.append(dict(n=4, bg="#ffffff", media=dict(img="images/4.jpg"), els=[
    T(64.63, 383.38, 382.46, 26.667, "N", "justify", 1.17, 0, INK, "Desde mesoestetic Pharma group® nace la necesidad de crear una marca de skincare enfocada a la Gen Z. Junto a la agencia Morillas, se define y desarrolla toda la estrategia, con un enfoque 100% digital y trasgesor."),
    T(503.54, 383.38, 326.02, 26.667, "N", "justify", 1.17, 0, INK, "Al incorporar al equipo interno dedicado a la marca (momento en el que me incorporé) se hace un traspaso de proyecto y se centraliza en el nuevo team."),
    T(64.63, 701.54, 764.92, 26.667, "N", "justify", 1.17, 0, INK, "Desde entonces, se ha desarrollado la marca desde el equipo, ajustando la estrategia y elaborando planes de acción para la optimización de recursos y la rentabilidad de esta."),
    T(64.63, 864.71, 764.92, 26.667, "N", "justify", 1.17, 0, INK, "Mi papel en el equipo pasó de ser diseñadora gráfica a liderar toda la parte conceptual y creativa de la marca, definiendo su identidad y dotándola de contenido para su crecimiento y expansión en el mercado, manteniendo su esencia y su razón de ser como marca."),
]))

S.append(dict(n=5, bg=INK, media=dict(video="media/5.mp4", poster="media/5-poster.jpg", sound=True), els=[
    mint_card(1030.30, 648, 781.70, 324, "(001) Video Manifesto",
              "Video presentación de la marca y el portfolio de productos, con un estilo visual, inspirado en lo que conecta con la Generación Z, refleja en cada detalle la misión de Binomial: cuidado de la piel simple y efectivo.",
              "Agencia Morillas", "Abril-Septiembre 2024", tx=1062.32, ty=679.23, dy=742.48, my=916.29, rx=1416.59)]))

S.append(dict(n=6, bg=PAPER, media=dict(img="images/6.jpg"), els=[
    mint_card(64.08, 94.01, 763.05, 264.78, "(002) Packaging",
              "Conceptualización y desarrollo de los AAFF de primarios y secundarios de toda la gama. Contacto con proveedores y seguimiento de la fabricación.",
              "Orriols Packaging", "Abril-Septiembre 2024", tx=96.09, ty=125.23, dy=178.62, my=292.55, rx=450.36)]))

S.append(dict(n=7, bg=INK, media=dict(img="media/7.gif"), els=[
    mint_card(151.69, 748.67, 781.70, 268.73, "(003) Shooting",
              "Dirección conceptual y de arte del shooting inicial de marca, incluyendo bodegón de producto, interacción con modelo y foco en textura de producto.",
              "Agencia Morillas", "Abril-Septiembre 2024", tx=183.71, ty=779.90, dy=843.15, my=951.48, rx=537.98)]))

S.append(dict(n=8, bg=INK, media=dict(img="images/8.jpg"), els=[]))

S.append(dict(n=9, bg=INK, media=dict(img="images/9.jpg"), els=[
    mint_card(1059.68, 89.71, 781.70, 245.08, "(004) Página web y contenidos digitales",
              "Diseño de e-commerce junto con tbb agency. Conceptualización de UX y look and feel del website.",
              "tbb agency", "Abril-Septiembre 2024", tx=1091.69, ty=120.94, dy=184.19, my=266.52, rx=1445.96, ttw=613.66)]))

S.append(dict(n=10, bg=PAPER, media=dict(img="images/10.jpg"), els=[
    mint_card(1069.25, 658.67, 781.70, 378.12, "(005) Evento lanzamineto",
              "Construcción de pop-up experiencial en Madrid, con un espacio dediacado al skincare donde probar los productos y vivir la experiencia de la marca. Con diversas activaciones y actividades. <br>Campaña de comunicación del evento, con convocatoria digital y también wildposting en las proximidades del lugar del evento.",
              "Pelonio", "Octubre 2024", tx=1101.26, ty=707.49, dy=769.27, my=979.99, rx=1455.53)]))

S.append(dict(n=11, bg=PAPER, media=dict(video="media/11.mp4", poster="media/11-poster.jpg", sound=True), els=[]))
S.append(dict(n=12, bg=PAPER, media=dict(video="media/12.mp4"), els=[]))
S.append(dict(n=13, bg=PAPER, media=dict(video="media/13.mp4"), els=[]))

S.append(dict(n=14, bg=PAPER, media=dict(img="images/14.jpg"), els=[
    mint_card(1079.94, 350.68, 781.70, 303.42, "(006) AI generated content",
              "Creación de contenido con IA y automatizacione sen la creación de piezas masivas de Paid Media con Figma. Utilización de fotografías en web y canales digitales.",
              "Nano Banana y Figma", "2026", tx=1111.95, ty=381.91, dy=(1121.69, 460.17), my=585.93, rx=1475.96, ttw=650)]))
# metas on slide 14 start at 1121.69 (Canva), fix:
S[-1]["els"][0]["kids"][2]["x"] = 1121.69

S.append(dict(n=15, bg=PAPER, media=dict(img="images/15.jpg"), els=[]))
S.append(dict(n=16, bg=PAPER, media=dict(img="images/16.jpg"), els=[]))

S.append(dict(n=17, bg=PAPER, media=dict(video="media/17.mp4", poster="media/17-poster.jpg", sound=True), els=[
    mint_card(1066.88, 59.69, 781.70, 354.30, "(007) Campaña “El mejor polvo de tu vida”",
              "Conceptualización, desarrollo y ejecución de la campaña de Power Powder, nuestro limpiador facial en polvo que se convierte en, el mejor polvo de tu vida. Jugamos con el doble sentido para generar curiosidad y aumentar el alcance de la campaña. Activaciones online (microsite y paid media localizaco) y offline (wildposting)",
              "Neven productora", "Marzo 2025", tx=1098.90, ty=90.92, dy=(1101.26, 148.09), my=354.43, rx=1455.53, ttw=650)]))
S[-1]["els"][0]["kids"][2]["x"] = 1101.26

S.append(dict(n=18, bg=PAPER, media=dict(img="images/18.jpg"), els=[]))
S.append(dict(n=19, bg=PAPER, media=dict(video="media/19.mp4", poster="media/19-poster.jpg"), els=[]))

S.append(dict(n=20, bg=PAPER, media=dict(video="media/20.mp4", poster="media/20-poster.jpg"), els=[
    mint_card(74.89, 75.93, 774.10, 266.77, "(008) Digital content",
              "Creación de contenido inhouse, con enfoque más científico y educativo o con un enfoque más de lifestyle y de estilo de vida, siguiendo los trends y las últimas novedades en social media.",
              tx=114.92, ty=112.40, dy=186.70, dlh=1.12, ttw=412.01)]))

S.append(dict(n=21, bg=PAPER, media=dict(img="images/21.jpg"), els=[
    mint_card(528.01, 71.54, 774.10, 308.56, "(009) Activaciones offline",
              "Coordinación de acciones en entornos offline como samplings y markets. También activaciones cobrandeadas con marcas afines del sector health y fitness.",
              "Diferentes proveedores", "2026", tx=568.04, ty=108, dy=182.30, my=308.06, rx=922.31, ttw=412.01)]))

S.append(dict(n=22, bg=PAPER, media=dict(img="images/22.jpg"), els=[]))

S.append(dict(n=23, bg=PAPER, media=dict(embed="https://player.vimeo.com/video/760811572?title=0&byline=0&portrait=0&dnt=1",
                                         box=[0, 0, 1917, 1080], title="Levi’s - Social Live Shopping"), els=[
    dark_card(108, 108, 547.54, 653.90, 148.03, "(010) Levi’s", "Social Live Shopping",
              "Campaña para el primer directo de compra online en streaming de la marca. Creación y conceptualización de la dinámica del streaming, con diferentes challenges y activaciones. <br><br>Diseño de sobreimpresiones junto a la carteleria y animaciones del streaming así como las creatividades para social media y colaboración con las influencers @gigi_vives, @andreiinflu y @monismurf.",
              254.85, "beAgency", "2021", 688.45, 269.14)]))

S.append(dict(n=24, bg=PAPER, media=dict(img="images/24.jpg"), els=[
    dark_card(108, 84.93, 547.54, 361.35, 148.03, "(010) Levi’s", "Social Media",
              "Diseño y animación de creatividades para los diferentes canales nacionales de la marca.",
              231.78, "beAgency", "2023", 367.64, 269.14)]))

rilastil = "Campaña junto al FCB femenino como sponsor de skincare. Conceptualización y grabación de video spot y social media content  con las jugadoras.<br><br>Estrategia de social media y diseño del contenido para redes propias."
S.append(dict(n=25, bg=PAPER, media=dict(embed="https://www.youtube-nocookie.com/embed/CMqaot85DZw?rel=0&modestbranding=1",
                                         box=[0, 0.84, 1920, 1079.16], title="Rilastil Official skin care & sun protection of FC Barcelona Women"), els=[
    dark_card(108, 84.93, 547.54, 502.94, 148.03, "(011) Rilastil", "Patrocinio Barça Femenino",
              rilastil, 231.78, "beAgency - Multiplica", "2023", 508.67, 269.14)]))

S.append(dict(n=26, bg=PAPER, media=dict(video="media/27.mp4"), els=[
    dark_card(35.41, 288.53, 547.54, 502.94, 75.44, "(011) Rilastil", "Patrocinio Barça Femenino",
              rilastil, 435.38, "beAgency - Multiplica", "2023", 712.27, 196.56)]))

S.append(dict(n=27, bg=INK, els=[
    T(212.35, 476.01, 1495.30, 106.667, "H", "center", .77, -.058, "#fff", "celiamuntaner@gmail.com", "big big-mail",
      href="mailto:celiamuntaner@gmail.com")] + header_footer()))

# ------------------------------------------------------------------ render
u = lambda v: f"{v/19.2:.4f}cqw"   # 1920 page px -> container units

def text_html(t, ox=0, oy=0):
    style = (f"left:{u(t['x']-ox)};top:{u(t['y']-oy)};width:{u(t['w'])};--fs:{t['fs']};"
             f"font-weight:{W[t['wt']]};text-align:{t['al']};line-height:{t['lh']};"
             f"letter-spacing:{t['ls']}em;color:{t['col']}")
    body = t["txt"]
    if t["href"]:
        dec = "underline" if t["under"] else "none"
        tgt = ' target="_blank" rel="noopener"' if t["href"].startswith("http") else ""
        body = f'<a href="{t["href"]}"{tgt} style="text-decoration:{dec}">{body}</a>'
    return f'<p class="t {t["cls"]}" style="{style}">{body}</p>'

def media_html(m, n):
    if not m:
        return ""
    if "img" in m:
        return f'<img class="bgm" src="{m["img"]}" alt="Diapositiva {n}" loading="{"eager" if n <= 2 else "lazy"}" decoding="async">'
    if "video" in m:
        btn = ('<button class="snd" type="button" aria-label="Activar sonido" aria-pressed="false">'
               '<span class="on">sonido</span><span class="off">silenciar</span></button>') if m.get("sound") else ""
        pst = ('poster="' + m["poster"] + '" ') if m.get("poster") else ""
        return (f'<video class="bgm" src="{m["video"]}" {pst}muted loop playsinline preload="none"'
                f'{"" if m.get("sound") else " disablepictureinpicture"}></video>{btn}')
    if "embed" in m:
        x, y, w, h = m["box"]
        return (f'<div class="embed" style="left:{u(x)};top:{u(y)};width:{u(w)};height:{u(h)}">'
                f'<iframe src="{m["embed"]}" title="{m["title"]}" loading="lazy" allow="autoplay; fullscreen; picture-in-picture; encrypted-media" allowfullscreen></iframe></div>')

out = []
for s in S:
    n = s["n"]
    if n in (1, 2, 27):
        continue
    m = s.get("media")
    kind = "img" if m and "img" in m else "video" if m and "video" in m else "embed" if m and "embed" in m else "none"
    mc = ""
    if s.get("mcrop"):
        x, y, w, h = s["mcrop"]
        mc = f' style="--mc-w:{w};--mc-h:{h};--mc-x:{x};--mc-y:{y}"'
    parts = [f'<section class="slide k-{kind}{" has-mcrop" if mc else ""}" id="s{n}" style="--bg:{s["bg"]}" aria-label="Diapositiva {n}">',
             f'<div class="stage"><div class="media"{mc}>{media_html(m, n)}</div><div class="layer">']
    for r in s.get("rows", []):
        lab = html.escape(r["lab"])
        inner = (f'<span class="rn" style="top:{u(r["ny"]-r["ly"]+1.5)};color:{r["col"]}">{r["num"]}</span>'
                 f'<span class="rl" style="top:{u(r["ty"]-r["ly"]+1.5)};color:{r["col"]}">{lab}</span>')
        tag = f'a href="#{r["href"]}"' if r["href"] else "div"
        parts.append(f'<{tag} class="row" style="top:{u(r["ly"]-1.5)}">{inner}</{tag.split()[0]}>')
    for e in s["els"]:
        if e["k"] == "t":
            parts.append(text_html(e))
        else:
            kids = "".join(text_html(k, e["x"], e["y"]) for k in e["kids"])
            corner = ("t" if e["y"] + e["h"] / 2 < 540 else "b") + ("l" if e["x"] + e["w"] / 2 < 960 else "r")
            fcol = "#fff" if e["col"] == INK else INK
            parts.append(f'<div class="card" style="left:{u(e["x"])};top:{u(e["y"])};width:{u(e["w"])};height:{u(e["h"])};background:{e["col"]}">{kids}</div>'
                         f'<button class="fold c-{corner}" type="button" aria-label="Minimizar texto" aria-expanded="true" '
                         f'style="--ox:{u(e["x"] + e["w"] - 44)};--oy:{u(e["y"] + 12)};--fc:{fcol}"></button>')
    fs = '<button class="fsb" type="button" aria-label="Pantalla completa"></button>' if 4 <= n <= 26 else ""
    parts.append(f"</div>{fs}</div></section>")
    out.append("".join(parts))

page = open("template.html", encoding="utf-8").read().replace("<!--SLIDES-->", "\n".join(out))
open("index.html", "w", encoding="utf-8").write(page)
print("ok", len(S), "slides")

# ------------------------------------------------------------------ English version (en.html)
# Each pair: exact Spanish text -> English text. Edit here, then run: python build.py
EN = [
  ('<html lang="es">', '<html lang="en">'),
  ('content="Portfolio de Celia Muntaner, creative and design brand manager. Barcelona."', 'content="Portfolio of Celia Muntaner, creative and design brand manager. Barcelona."'),
  ('<a href="#sobre-mi">sobre mí</a><a href="#s3">proyectos</a><a href="#contacto">contacto</a>',
   '<a href="#sobre-mi">about</a><a href="#s3">projects</a><a href="#contacto">contact</a>'),
  ('<a class="lang" href="en.html" lang="en">EN</a>', '<a class="lang" href="index.html" lang="es">ES</a>'),
  ('ver portfolio ↓', 'see portfolio ↓'),
  ('<h2 class="h2">sobre mí</h2>', '<h2 class="h2">about me</h2>'),
  ('<p><strong>Directora creativa y de arte</strong> con más de 6 años de experiencia, especializada en el sector de la cosmética y el skincare.</p>',
   '<p><strong>Creative and art director</strong> with more than 6 years of experience, specialised in the cosmetics and skincare sector.</p>'),
  ('<p>Mi actual proyecto es <strong>Binomial skincare</strong>, una marca de dermocosmética de mesoestetic Pharma Group. Involucrada desde la fase previa al lanzamiento de la marca, liderando la dirección creativa, la identidad visual y la estrategia de la marca. Conceptualizo campañas y su desarrollo en diferentes canales (social, paid, web, offline…).</p>',
   '<p>My current project is <strong>Binomial skincare</strong>, a dermocosmetics brand by mesoestetic Pharma Group. I have been involved since before the brand launched, leading its creative direction, visual identity and brand strategy. I conceptualise campaigns and their roll-out across channels (social, paid, web, offline…).</p>'),
  ('<p>Además, desarrollo funciones de Brand Manager: participo en la implementación de estrategias de marca, desde el rendimiento de ventas y los canales de distribución hasta la comunicación directa con agencias y proveedores.</p>',
   '<p>I also work as Brand Manager: I take part in implementing brand strategy, from sales performance and distribution channels to direct communication with agencies and suppliers.</p>'),
  ('<p>Poseo experiencia previa en agencia que me aportó una visión transversal del sector creativo y una excelente capacidad de respuesta ante grandes ritmos de trabajo.</p>',
   '<p>My previous agency experience gave me a cross-cutting view of the creative industry and the ability to respond quickly under a demanding pace of work.</p>'),
  ('<h3 class="label">experiencia</h3>', '<h3 class="label">experience</h3>'),
  ('Multiplica (fusión beAgency)', 'Multiplica (beAgency merger)'),
  ('abr. 2024 — actualidad', 'Apr 2024 — present'), ('mar. 2022 — abr. 2024', 'Mar 2022 — Apr 2024'), ('oct. 2020 — mar. 2022', 'Oct 2020 — Mar 2022'),
  ('descargar cv completo ↗', 'download full CV ↗'),
  ('<p class="label">contacto</p>', '<p class="label">contact</p>'),
  ('>volver arriba ↑<', '>back to top ↑<'),
  ('aria-label="Diapositiva', 'aria-label="Slide'), ('alt="Diapositiva', 'alt="Slide'),
  ('<span class="on">sonido</span><span class="off">silenciar</span>', '<span class="on">sound</span><span class="off">mute</span>'),
  ("'Activar sonido'", "'Turn sound on'"), ('"Activar sonido"', '"Turn sound on"'), ("'Silenciar'", "'Mute'"),
  ('"Minimizar texto"', '"Minimise text"'), ("'Minimizar texto'", "'Minimise text'"), ("'Mostrar texto'", "'Show text'"),
  ('aria-label="Pantalla completa"', 'aria-label="Full screen"'),
  ('aria-label="Volver arriba"', 'aria-label="Back to top"'),
  ('aria-label="Retrato de Celia Muntaner"', 'aria-label="Portrait of Celia Muntaner"'),
  # index (slide 3)
  ('>branding y packaging<', '>branding &amp; packaging<'), ('>evento lanzamiento<', '>launch event<'),
  ('>contenido generado con IA<', '>AI-generated content<'), ('>campañas<', '>campaigns<'), ('>activaciones offline<', '>offline activations<'),
  # slide 4
  ('Desde mesoestetic Pharma group® nace la necesidad de crear una marca de skincare enfocada a la Gen Z. Junto a la agencia Morillas, se define y desarrolla toda la estrategia, con un enfoque 100% digital y trasgesor.',
   'mesoestetic Pharma group® saw the need to create a skincare brand focused on Gen Z. Together with the agency Morillas, the whole strategy was defined and developed, with a 100% digital and transgressive approach.'),
  ('Al incorporar al equipo interno dedicado a la marca (momento en el que me incorporé) se hace un traspaso de proyecto y se centraliza en el nuevo team.',
   'When the in-house team dedicated to the brand was created (when I joined), the project was handed over and centralised in the new team.'),
  ('Desde entonces, se ha desarrollado la marca desde el equipo, ajustando la estrategia y elaborando planes de acción para la optimización de recursos y la rentabilidad de esta.',
   'Since then, the brand has been developed by the team, adjusting the strategy and drawing up action plans to optimise resources and profitability.'),
  ('Mi papel en el equipo pasó de ser diseñadora gráfica a liderar toda la parte conceptual y creativa de la marca, definiendo su identidad y dotándola de contenido para su crecimiento y expansión en el mercado, manteniendo su esencia y su razón de ser como marca.',
   'My role in the team grew from graphic designer to leading the whole conceptual and creative side of the brand, defining its identity and creating content for its growth and market expansion, while keeping its essence and purpose as a brand.'),
  # cards
  ('Video presentación de la marca y el portfolio de productos, con un estilo visual, inspirado en lo que conecta con la Generación Z, refleja en cada detalle la misión de Binomial: cuidado de la piel simple y efectivo.',
   'Presentation video of the brand and its product portfolio. Its visual style, inspired by what connects with Gen Z, reflects Binomial’s mission in every detail: simple, effective skincare.'),
  ('Abril-Septiembre 2024', 'April–September 2024'), ('Octubre 2024', 'October 2024'), ('Marzo 2025', 'March 2025'),
  ('Conceptualización y desarrollo de los AAFF de primarios y secundarios de toda la gama. Contacto con proveedores y seguimiento de la fabricación.',
   'Concept and final artwork for the primary and secondary packaging of the whole range. Supplier contact and production follow-up.'),
  ('Dirección conceptual y de arte del shooting inicial de marca, incluyendo bodegón de producto, interacción con modelo y foco en textura de producto.',
   'Concept and art direction of the brand’s launch photo shoot, including product still life, model interaction and a focus on product texture.'),
  ('(004) Página web y contenidos digitales', '(004) Website and digital content'),
  ('Diseño de e-commerce junto con tbb agency. Conceptualización de UX y look and feel del website.',
   'E-commerce design together with tbb agency. UX concept and look and feel of the website.'),
  ('(005) Evento lanzamineto', '(005) Launch event'),
  ('Construcción de pop-up experiencial en Madrid, con un espacio dediacado al skincare donde probar los productos y vivir la experiencia de la marca. Con diversas activaciones y actividades. <br>Campaña de comunicación del evento, con convocatoria digital y también wildposting en las proximidades del lugar del evento.',
   'An experiential pop-up in Madrid, with a space dedicated to skincare to try the products and live the brand experience, with several activations and activities. <br>Communication campaign for the event, with a digital call-out and wildposting around the venue.'),
  ('Creación de contenido con IA y automatizacione sen la creación de piezas masivas de Paid Media con Figma. Utilización de fotografías en web y canales digitales.',
   'AI content creation and automation for producing Paid Media assets at scale with Figma. Images used on the website and digital channels.'),
  ('Nano Banana y Figma', 'Nano Banana and Figma'),
  ('(007) Campaña “El mejor polvo de tu vida”', '(007) Campaign “El mejor polvo de tu vida”'),
  ('Conceptualización, desarrollo y ejecución de la campaña de Power Powder, nuestro limpiador facial en polvo que se convierte en, el mejor polvo de tu vida. Jugamos con el doble sentido para generar curiosidad y aumentar el alcance de la campaña. Activaciones online (microsite y paid media localizaco) y offline (wildposting)',
   'Concept, development and execution of the campaign for Power Powder, our powder facial cleanser, “the best powder of your life”. We played with the Spanish double meaning to spark curiosity and increase reach. Online activations (microsite and localised paid media) and offline (wildposting).'),
  ('Neven productora', 'Neven (production company)'),
  ('Creación de contenido inhouse, con enfoque más científico y educativo o con un enfoque más de lifestyle y de estilo de vida, siguiendo los trends y las últimas novedades en social media.',
   'In-house content creation, with either a more scientific and educational approach or a lifestyle approach, following trends and the latest in social media.'),
  ('(009) Activaciones offline', '(009) Offline activations'),
  ('Coordinación de acciones en entornos offline como samplings y markets. También activaciones cobrandeadas con marcas afines del sector health y fitness.',
   'Coordination of offline actions such as samplings and markets, plus co-branded activations with like-minded health and fitness brands.'),
  ('Diferentes proveedores', 'Various suppliers'),
  ('Campaña para el primer directo de compra online en streaming de la marca. Creación y conceptualización de la dinámica del streaming, con diferentes challenges y activaciones. <br><br>Diseño de sobreimpresiones junto a la carteleria y animaciones del streaming así como las creatividades para social media y colaboración con las influencers @gigi_vives, @andreiinflu y @monismurf.',
   'Campaign for the brand’s first live-stream shopping event. Concept and format of the stream, with different challenges and activations. <br><br>Design of on-screen graphics, signage and animations for the stream, as well as social media creatives and collaboration with influencers @gigi_vives, @andreiinflu and @monismurf.'),
  ('Diseño y animación de creatividades para los diferentes canales nacionales de la marca.',
   'Design and animation of creatives for the brand’s national channels.'),
  ('Patrocinio Barça Femenino', 'Barça Women sponsorship'),
  ('Campaña junto al FCB femenino como sponsor de skincare. Conceptualización y grabación de video spot y social media content  con las jugadoras.<br><br>Estrategia de social media y diseño del contenido para redes propias.',
   'Campaign with FC Barcelona Women as skincare sponsor. Concept and shoot of the video spot and social media content with the players.<br><br>Social media strategy and content design for the brand’s own channels.'),
]
en = page
for es_txt, en_txt in EN:
    if es_txt not in en:
        print("  (not found, check text):", es_txt[:60])
    en = en.replace(es_txt, en_txt)
open("en.html", "w", encoding="utf-8").write(en)
print("ok en.html")
