
import pandas as pd
import os
import re
import unicodedata

# Rutas
EXCEL_PATH = "./data/Borrador_Propuesta catálogo_90 procedimientos.xlsx"
TEMPLATE_FICHA = "./templates/ficha.base.md"
TEMPLATE_MKDOCS = "./templates/mkdocs.base.yml"
OUTPUT_NAV_YML = "./tmp/mkdocs.nav.yml"
OUTPUT_MKDOCS_YML = "../mkdocs.yml"
FICHAS_DIR = "../docs/fichas"
BUSCADOR_PATH = "../docs/buscador.md"

# Crear carpeta de fichas si no existe
os.makedirs(FICHAS_DIR, exist_ok=True)

def limpiar_enumerado(texto):
    if pd.isna(texto):
        return "(sin datos)"
    lineas = [line.strip("•–- 	") for line in str(texto).splitlines() if line.strip()]
    if not lineas:
        return "(sin datos)"
    return "\n" + "\n".join(f"- {l}" for l in lineas)

def limpiar_normativa(texto):
    if pd.isna(texto):
        return "(sin datos)"
    entradas = [line.strip("•–- 	") for line in str(texto).splitlines() if line.strip()]
    resultado = []
    leyes = []
    for line in entradas:
        l = unicodedata.normalize("NFKD", line.lower())
        if any(base in l for base in leyes):
            continue
        if "ley " in l:
            base = re.findall(r"ley\s[\d/]+", l)
            if base:
                leyes.append(base[0])
        elif "real decreto" in l:
            base = re.findall(r"real decreto\s[\d/]+", l)
            if base:
                leyes.append(base[0])
        resultado.append(line)
    if not resultado:
        return "(sin datos)"
    return "\n" + "\n".join(f"- {r}" for r in resultado)

def cargar_plantilla(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def generar_fichas(df, plantilla):
    for _, row in df.iterrows():
        cod = str(row["Clave"]).strip()
        nombre = str(row["Procedimiento"]).strip().capitalize()
        familia = str(row["Familia"]).strip().upper()
        requisitos = limpiar_enumerado(row.get("Requisitos y documentación", ""))
        normativa = limpiar_normativa(row.get("Normativa", ""))

        contenido = plantilla.format(
            titulo=nombre,
            codigo=cod,
            familia=familia,
            requisitos=requisitos,
            normativa=normativa
        )

        with open(os.path.join(FICHAS_DIR, f"{cod}.md"), "w", encoding="utf-8") as f:
            f.write(contenido)

def generar_nav_yml(df):
    familias = {}
    for _, row in df.iterrows():
        cod = str(row["Clave"]).strip()
        nombre = str(row["Procedimiento"]).strip().capitalize()
        familia = str(row["Familia"]).strip().upper()
        if familia not in familias:
            familias[familia] = []
        familias[familia].append((nombre, f"fichas/{cod}.md"))

    for k in familias:
        familias[k].sort()
    familias = dict(sorted(familias.items()))

    nav_lines = []
    for fam, items in familias.items():
        nav_lines.append(f"    - {fam}:")
        for nombre, ruta in items:
            nav_lines.append(f"        - {nombre}: {ruta}")

    with open(OUTPUT_NAV_YML, "w", encoding="utf-8") as f:
        f.write("\n".join(nav_lines))

def build_mkdocs_yml():
    with open(OUTPUT_NAV_YML, "r", encoding="utf-8") as nav:
        nav_contenido = nav.read()
    with open(TEMPLATE_MKDOCS, "r", encoding="utf-8") as base:
        base_contenido = base.read()
    final = base_contenido.replace("# === NAV_PLACEHOLDER ===", nav_contenido)
    with open(OUTPUT_MKDOCS_YML, "w", encoding="utf-8") as final_yml:
        final_yml.write(final)


def generar_buscador_md(df):
    familias = sorted(set(df["Familia"].dropna().str.strip().str.upper()))

    filtro_html = [
        '<div class="filtro-bloque">',
        '  <p><strong>Familias</strong></p>',
        '  <div id="filtro-familias">',
        '    <label><input type="radio" name="familia" value="todas" checked> Todas las familias</label><br>'
    ]

    for fam in familias:
        valor = re.sub(r"[^\w]+", "-", fam.lower()).strip("-")
        filtro_html.append(f'    <label><input type="radio" name="familia" value="{valor}"> {fam}</label><br>')

    filtro_html += ['  </div>', '</div>']

    procedimientos_html = []
    for _, row in df.iterrows():
        cod = str(row["Clave"]).strip()
        nombre = str(row["Procedimiento"]).strip()
        familia = str(row["Familia"]).strip().upper()
        valor = re.sub(r"[^\w]+", "-", familia.lower()).strip("-")
        procedimientos_html.append(
            f'<div class="procedimiento" data-familia="{valor}">\n'
            f'<a href="../fichas/{cod}">{nombre}</a><br/>\n'
            f'Código: {cod}<br/>\n'
            f'Familia: {familia}\n'
            f'</div>'
        )

    final = '\n'.join([
        '<div id="contenedor-principal">',
        '',
        '  <div id="filtros">',
        '    <h3 id="titulo-filtro">Filtrar resultados</h3>',
        *filtro_html,
        '  </div>',
        '',
        '  <div style="flex: 1;">',
        '    <div id="buscador-superior">',
        '      <input type="text" id="buscador" placeholder="Buscar procedimientos...">',
        '    </div>',
        '    <div id="contador-resultados" class="contador-resultados">Se han encontrado 0 procedimientos</div>',
        '    <div id="lista-procedimientos">',
        *procedimientos_html,
        '    </div>',
        '  </div>',
        '',
        '</div>'
    ])

    with open(BUSCADOR_PATH, "w", encoding="utf-8") as f:
        f.write(final)

def main():
    df = pd.read_excel(EXCEL_PATH, header=3)
    df.columns = [str(c).strip() for c in df.columns]
    df = df[df["Clave"].notna() & df["Procedimiento"].notna() & df["Familia"].notna()]
    plantilla = cargar_plantilla(TEMPLATE_FICHA)
    generar_fichas(df, plantilla)
    generar_nav_yml(df)
    build_mkdocs_yml()
    generar_buscador_md(df)
    print("Contenidos generados correctamente.")

if __name__ == "__main__":
    main()
