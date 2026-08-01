#!/usr/bin/env python3
"""
Calculadora de contraste WCAG 2.1.

Uso:
    python3 contraste.py                      -> revisa la paleta base
    python3 contraste.py "#566673" "#ffffff"  -> revisa dos colores
    python3 contraste.py --arregla "#6b7c8a" "#ffffff"
        -> oscurece el primero hasta que pase 4.5:1 y te da el hex

Sin dependencias. Funciona con cualquier Python 3.
"""
import sys


def _canal(v):
    v = v / 255
    return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4


def luminancia(hexcolor):
    h = hexcolor.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"Color invalido: {hexcolor}")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _canal(r) + 0.7152 * _canal(g) + 0.0722 * _canal(b)


def contraste(a, b):
    l1, l2 = sorted((luminancia(a), luminancia(b)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def veredicto(r):
    return {
        "texto normal (4.5:1)": "PASA" if r >= 4.5 else "FALLA",
        "texto grande (3:1)": "PASA" if r >= 3 else "FALLA",
        "bordes e iconos (3:1)": "PASA" if r >= 3 else "FALLA",
    }


def oscurecer(hexcolor, factor):
    h = hexcolor.strip().lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    r, g, b = (max(0, int(c * factor)) for c in (r, g, b))
    return f"#{r:02x}{g:02x}{b:02x}"


def arregla(color, fondo, objetivo=4.5):
    if contraste(color, fondo) >= objetivo:
        return color, contraste(color, fondo)
    for i in range(1, 100):
        cand = oscurecer(color, 1 - i / 100)
        if contraste(cand, fondo) >= objetivo:
            return cand, contraste(cand, fondo)
    return "#000000", contraste("#000000", fondo)


PALETA_BASE = [
    ("texto fuerte sobre blanco", "#0d1a23", "#ffffff", 4.5),
    ("texto cuerpo sobre blanco", "#39485a", "#ffffff", 4.5),
    ("texto suave sobre blanco", "#566673", "#ffffff", 4.5),
    ("texto suave sobre superficie 2", "#566673", "#f4f8fb", 4.5),
    ("marca sobre blanco", "#1a5479", "#ffffff", 4.5),
    ("blanco sobre marca", "#ffffff", "#1a5479", 4.5),
    ("exito sobre blanco", "#217a58", "#ffffff", 4.5),
    ("alerta sobre blanco", "#8a5a12", "#ffffff", 4.5),
    ("error sobre blanco", "#a1332b", "#ffffff", 4.5),
    ("borde de campo sobre blanco", "#8596a1", "#ffffff", 3.0),
]


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    modo_arregla = "--arregla" in sys.argv

    if modo_arregla and len(args) >= 2:
        nuevo, r = arregla(args[0], args[1])
        print(f"  {args[0]} sobre {args[1]}: {contraste(args[0], args[1]):.2f}:1")
        print(f"  propuesta: {nuevo}  ->  {r:.2f}:1  PASA")
        return

    if len(args) >= 2:
        r = contraste(args[0], args[1])
        print(f"\n  {args[0]} sobre {args[1]}  ->  {r:.2f}:1\n")
        for k, v in veredicto(r).items():
            print(f"    {v:5}  {k}")
        if r < 4.5:
            nuevo, nr = arregla(args[0], args[1])
            print(f"\n    Para pasar texto normal usa {nuevo} ({nr:.2f}:1)")
        print()
        return

    print("\n  CONTRASTE DE LA PALETA BASE  (WCAG 2.1 AA)\n")
    fallos = 0
    for nombre, fg, bg, minimo in PALETA_BASE:
        r = contraste(fg, bg)
        ok = r >= minimo
        fallos += 0 if ok else 1
        print(f"    {'PASA ' if ok else 'FALLA'}  {r:5.2f}:1  (min {minimo})  {nombre}")
        if not ok:
            nuevo, nr = arregla(fg, bg, minimo)
            print(f"             corrige {fg} por {nuevo} ({nr:.2f}:1)")
    print(f"\n  {'Todo pasa.' if not fallos else str(fallos) + ' color(es) por corregir.'}\n")


if __name__ == "__main__":
    main()
