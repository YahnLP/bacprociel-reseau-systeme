#!/usr/bin/env python3
"""Mini-bibliothèque de dessin SVG pour les cours (style plat, lisible sur GitHub).
Aucune dépendance : on écrit du SVG à la main. Les figures sont décrites par du code,
donc modifiables et versionnables (voir tools/illus/seconde_*.py)."""
import html, os

# ---------------------------------------------------------------- palette
INK = "#1f2544"; MUTED = "#5b6385"; LINE = "#3a4270"
IND = "#3949ab"; IND_L = "#e8eaf6"; IND_M = "#9fa8da"
TEAL = "#00897b"; TEAL_L = "#e0f2f1"
ORA = "#ef6c00"; ORA_L = "#fff3e0"
RED = "#c62828"; RED_L = "#ffebee"
GRN = "#2e7d32"; GRN_L = "#e8f5e9"
YEL = "#f9a825"; YEL_L = "#fffde7"
GRY = "#eceff1"; GRY_D = "#90a4ae"; WHITE = "#ffffff"
FONT = "Segoe UI, Helvetica, Arial, sans-serif"


def esc(t):
    return html.escape(str(t), quote=False)


def est_w(t, size, weight="400"):
    """Largeur approximative d'un texte (police sans-serif)."""
    k = 0.58 if weight in ("600", "700", "bold") else 0.53
    return len(t) * size * k


def wrap(t, maxw, size, weight="400"):
    out = []
    for para in str(t).split("\n"):
        cur = ""
        for w in para.split(" "):
            test = (cur + " " + w).strip()
            if est_w(test, size, weight) <= maxw or not cur:
                cur = test
            else:
                out.append(cur)
                cur = w
        out.append(cur)
    return "\n".join(out)


class Fig:
    """Une figure SVG : on ajoute des éléments puis on enregistre."""

    def __init__(self, w, h, title="", desc="", bg=WHITE):
        self.w, self.h, self.title, self.desc, self.bg = w, h, title, desc, bg
        self.parts = []

    # ----- primitives
    def add(self, s):
        self.parts.append(s)
        return self

    def rect(self, x, y, w, h, fill=WHITE, stroke=LINE, sw=2, r=8, dash=None, op=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        o = f' opacity="{op}"' if op else ""
        return self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}{o}/>')

    def circle(self, x, y, r, fill=WHITE, stroke=LINE, sw=2):
        return self.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')

    def line(self, x1, y1, x2, y2, stroke=LINE, sw=2, dash=None, arrow=False, cap="round"):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        m = ' marker-end="url(#ar)"' if arrow else ""
        return self.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="{cap}"{d}{m}/>')

    def path(self, d, fill="none", stroke=LINE, sw=2, dash=None, arrow=False):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        m = ' marker-end="url(#ar)"' if arrow else ""
        return self.add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"{da}{m}/>')

    def poly(self, pts, fill=WHITE, stroke=LINE, sw=2):
        p = " ".join(f"{x},{y}" for x, y in pts)
        return self.add(f'<polygon points="{p}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>')

    def text(self, x, y, t, size=16, fill=INK, anchor="middle", weight="400", family=None, italic=False, maxw=None, halo=None):
        """Texte (multi-lignes avec '\\n'). maxw : retour à la ligne automatique."""
        fam = family or FONT
        if maxw:
            t = wrap(t, maxw, size, weight)
        st = ' font-style="italic"' if italic else ""
        lines = str(t).split("\n")
        out = []
        for i, ln in enumerate(lines):
            out.append(f'<tspan x="{x}" dy="{0 if i == 0 else round(size * 1.25, 1)}">{esc(ln)}</tspan>')
        halo = halo or getattr(self, "halo", None)
        if halo:  # liseré de la couleur du fond : le texte reste lisible même si une ligne passe derrière
            self.add(f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}" fill="{halo}" stroke="{halo}" stroke-width="5" stroke-linejoin="round" text-anchor="{anchor}" font-weight="{weight}"{st}>{"".join(out)}</text>')
        return self.add(f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"{st}>{"".join(out)}</text>')

    def mono(self, x, y, t, size=15, fill=INK, anchor="start", weight="400"):
        return self.text(x, y, t, size, fill, anchor, weight, family="Consolas, Menlo, monospace")

    def badge(self, x, y, n, fill=IND, r=13):
        self.circle(x, y, r, fill, WHITE, 2)
        return self.text(x, y + 5, n, 14, WHITE, "middle", "700")

    def box(self, x, y, w, h, title, body="", fill=IND_L, stroke=IND, tsize=17, bsize=14):
        self.rect(x, y, w, h, fill, stroke, 2, 10)
        self.text(x + w / 2, y + 8 + tsize, title, tsize, stroke if stroke != WHITE else INK, "middle", "700")
        if body:
            self.text(x + w / 2, y + 12 + tsize * 2, body, bsize, INK)
        return self

    def callout(self, x, y, w, t, fill=YEL_L, stroke=YEL, size=14, lines=None):
        t = wrap(t, w - 24, size)
        n = str(t).count("\n") + 1
        h = 18 + n * size * 1.25
        self.rect(x, y, w, h, fill, stroke, 2, 8)
        self.text(x + 12, y + 8 + size, t, size, INK, "start")
        return h

    def check(self, x, y, ok=True, size=16):
        """Coche (ok) ou croix dessinée, centrée sur (x, y) : évite les glyphes absents des polices."""
        c = GRN if ok else RED
        s = size / 2
        if ok:
            self.path(f"M{x - s * .7},{y} L{x - s * .15},{y + s * .6} L{x + s * .8},{y - s * .6}", "none", c, 3)
        else:
            self.line(x - s * .6, y - s * .6, x + s * .6, y + s * .6, c, 3)
            self.line(x + s * .6, y - s * .6, x - s * .6, y + s * .6, c, 3)

    def warn(self, x, y, s=14):
        self.poly([(x, y - s), (x + s, y + s * .8), (x - s, y + s * .8)], YEL, "#b28704", 2)
        self.text(x, y + s * .55, "!", s, INK, "middle", "700")

    def arrow(self, x1, y1, x2, y2, stroke=LINE, sw=3, dash=None):
        return self.line(x1, y1, x2, y2, stroke, sw, dash, arrow=True)

    def title_bar(self, t):
        self.text(self.w / 2, 30, t, 22, IND, "middle", "700")

    # ----- sortie
    def svg(self):
        head = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" width="{self.w}" height="{self.h}" role="img">'
                f'<title>{esc(self.title)}</title><desc>{esc(self.desc or self.title)}</desc>'
                f'<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
                f'<path d="M0,0 L10,5 L0,10 z" fill="{LINE}"/></marker></defs>'
                f'<rect width="{self.w}" height="{self.h}" fill="{self.bg}" rx="10"/>')
        return head + "".join(self.parts) + "</svg>\n"

    def save(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.svg())
        return path


# ---------------------------------------------------------------- icônes d'équipements
# Chaque icône est dessinée autour du point (x, y) = centre, taille ~ 70x56.
def ic_pc(f, x, y, label=None, sub=None, c=IND):
    f.rect(x - 30, y - 30, 60, 40, GRY, c, 3, 5)
    f.rect(x - 25, y - 25, 50, 30, "#c5cae9", c, 1, 3)
    f.line(x, y + 10, x, y + 20, c, 4)
    f.rect(x - 18, y + 18, 36, 7, GRY, c, 2, 3)
    _lab(f, x, y + 26, label, sub)


def ic_laptop(f, x, y, label=None, sub=None, c=IND):
    f.rect(x - 28, y - 28, 56, 36, GRY, c, 3, 4)
    f.rect(x - 23, y - 23, 46, 26, "#c5cae9", c, 1, 2)
    f.poly([(x - 36, y + 8), (x + 36, y + 8), (x + 30, y + 18), (x - 30, y + 18)], GRY, c, 2)
    _lab(f, x, y + 18, label, sub)


def ic_switch(f, x, y, label=None, sub=None, c=TEAL, ports=8):
    f.rect(x - 42, y - 12, 84, 26, TEAL_L, c, 3, 4)
    n = ports
    step = 72 / n
    for i in range(n):
        f.rect(round(x - 36 + i * step + 1, 1), y - 4, round(step - 3, 1), 11, WHITE, c, 1.5, 1)
    f.circle(x - 38, y - 8, 2, GRN, GRN, 1)
    _lab(f, x, y + 14, label, sub)


def ic_hub(f, x, y, label=None, sub=None, c=GRY_D):
    ic_switch(f, x, y, label, sub, c=c, ports=4)


def ic_router(f, x, y, label=None, sub=None, c=ORA):
    f.rect(x - 38, y - 14, 76, 28, ORA_L, c, 3, 6)
    f.line(x - 20, y - 14, x - 28, y - 30, c, 3)
    f.line(x + 20, y - 14, x + 28, y - 30, c, 3)
    for i in range(4):
        f.rect(x - 28 + i * 14, y - 3, 10, 9, WHITE, c, 1.5, 1)
    f.circle(x + 30, y - 8, 2.5, GRN, GRN, 1)
    _lab(f, x, y + 14, label, sub)


def ic_box(f, x, y, label=None, sub=None, c=ORA):
    ic_router(f, x, y, label, sub, c)


def ic_server(f, x, y, label=None, sub=None, c=IND):
    for i in range(3):
        f.rect(x - 28, y - 34 + i * 22, 56, 19, IND_L, c, 2.5, 3)
        f.circle(x - 19, y - 24.5 + i * 22, 3, GRN if i != 2 else YEL, c, 1)
        f.line(x - 8, y - 24.5 + i * 22, x + 20, y - 24.5 + i * 22, c, 1.5)
    _lab(f, x, y + 34, label, sub)


def ic_printer(f, x, y, label=None, sub=None, c=IND):
    f.rect(x - 24, y - 24, 48, 14, WHITE, c, 2, 2)
    f.rect(x - 32, y - 12, 64, 26, GRY, c, 3, 5)
    f.rect(x - 20, y + 4, 40, 16, WHITE, c, 2, 2)
    f.line(x - 14, y + 10, x + 14, y + 10, c, 1.5)
    f.circle(x + 24, y - 4, 2.5, GRN, GRN, 1)
    _lab(f, x, y + 20, label, sub)


def ic_ap(f, x, y, label=None, sub=None, c=TEAL):
    f.rect(x - 30, y + 2, 60, 14, TEAL_L, c, 3, 7)
    for r in (10, 18, 26):
        f.path(f"M{x - r},{y - 2} A{r},{r} 0 0 1 {x + r},{y - 2}", "none", c, 2)
    f.circle(x, y - 2, 2.5, c, c, 1)
    _lab(f, x, y + 16, label, sub)


def ic_phone(f, x, y, label=None, sub=None, c=IND):
    f.rect(x - 14, y - 28, 28, 52, GRY, c, 3, 6)
    f.rect(x - 10, y - 22, 20, 36, "#c5cae9", c, 1, 2)
    f.circle(x, y + 19, 2.5, WHITE, c, 1.5)
    _lab(f, x, y + 24, label, sub)


def ic_cloud(f, x, y, label=None, sub=None, c=IND_M):
    f.path(f"M{x - 40},{y + 14} a18,18 0 0 1 4,-35 a24,24 0 0 1 46,-6 a20,20 0 0 1 24,26 a14,14 0 0 1 -6,15 z", IND_L, c, 3)
    _lab(f, x, y + 16, label, sub)


def ic_user(f, x, y, label=None, sub=None, c=IND):
    f.circle(x, y - 16, 11, IND_L, c, 3)
    f.path(f"M{x - 20},{y + 16} a20,20 0 0 1 40,0 z", IND_L, c, 3)
    _lab(f, x, y + 16, label, sub)


def _lab(f, x, y, label, sub):
    if label:
        f.text(x, y + 19, label, 15, INK, "middle", "700")
    if sub:
        f.mono(x, y + 36, sub, 12.5, MUTED, "middle")


ICONS = {"pc": ic_pc, "laptop": ic_laptop, "switch": ic_switch, "hub": ic_hub, "router": ic_router,
         "box": ic_box, "server": ic_server, "printer": ic_printer, "ap": ic_ap, "phone": ic_phone,
         "cloud": ic_cloud, "user": ic_user}


def node(f, kind, x, y, label=None, sub=None, **kw):
    ICONS[kind](f, x, y, label, sub, **kw)


def cable(f, x1, y1, x2, y2, label=None, color=LINE, dash=None, sw=3, lx=0, ly=-8):
    f.line(x1, y1, x2, y2, color, sw, dash)
    if label:
        f.text((x1 + x2) / 2 + lx, (y1 + y2) / 2 + ly, label, 13, color if color != LINE else MUTED, "middle", "600")


def wifi_link(f, x1, y1, x2, y2, label=None):
    f.line(x1, y1, x2, y2, TEAL, 3, "3 7")
    if label:
        f.text((x1 + x2) / 2, (y1 + y2) / 2 - 8, label, 13, TEAL, "middle", "600")


def sequence(f, cols, msgs, top=50, y0=None, step=50, textsize=12.5):
    """Diagramme de séquence : cols = [(x, nom, sous-titre, couleur)], msgs = [(a, b, texte, couleur, pointillé)].
    Les étiquettes sont posées au-dessus de chaque flèche, avec un fond blanc."""
    y0 = y0 or top + 95
    bottom = y0 + step * len(msgs) + 10
    for x, n, sub, c in cols:
        f.rect(x - 105, top, 210, 50, WHITE, c, 3, 10); f.text(x, top + 22, n, 15, c, "middle", "700")
        if sub:
            f.mono(x, top + 41, sub, 11.5, MUTED, "middle")
        f.line(x, top + 50, x, bottom, GRY_D, 2, dash="6 5")
    for i, (a_, b_, t, c, dash) in enumerate(msgs):
        y = y0 + i * step; x1, x2 = cols[a_][0], cols[b_][0]
        f.arrow(x1 + (8 if x2 > x1 else -8), y, x2 - (8 if x2 > x1 else -8), y, c, 3, "6 4" if dash else None)
        f.halo = WHITE; f.text((x1 + x2) / 2, y - 9, t, textsize, c, "middle", "700", maxw=abs(x2 - x1) - 14); f.halo = None
    return bottom
