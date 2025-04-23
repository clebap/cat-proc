
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

# Función para limpiar contenido
def limpiar(texto):
    if pd.isna(texto) or str(texto).strip() == "":
        return "(sin datos)"
    return str(texto).strip()

def cargar_plantilla(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def generar_fichas(df, plantilla):
    for _, row in df.iterrows():

        diagrama = limpiar(row["Diagrama"])
        if diagrama != "(sin datos)":
            diagrama = f"```mermaid\n{diagrama}\n```"

        contenido = plantilla.format(
            codigo=limpiar(row["Clave"]),
            familia=limpiar(row["Familia"]),
            descripcion=limpiar(row["Objeto / Descripción"]),
            forma_presentacion=limpiar(row["Forma de presentación"]),
            plazo_presentacion=limpiar(row["Plazo de presentación"]),
            forma_iniciacion=limpiar(row["Forma de iniciación"]),
            requisitos=limpiar(row["Requisitos y documentación"]),
            organo_resolucion=limpiar(row["Órgano de resolución"]),
            efecto_silencio=limpiar(row["Efecto del silencio"]),
            normativa=limpiar(row["Normativa"]),
            recursos=limpiar(row["Recursos"]),
            diagrama=diagrama
        )
        cod = f"{row['Clave'].strip()}.md"
        with open(os.path.join(FICHAS_DIR, cod), "w", encoding="utf-8") as f:
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
        '          <p><strong>Familias</strong></p>'
        '          <div id="filtro-familias">'
        '               <label><input type="radio" name="familia" value="todas" checked> Todas las familias</label><br>'
    ]

    for fam in familias:
        valor = re.sub(r"[^\w]+", "-", fam.lower()).strip("-")
        filtro_html.append(f'               <label><input type="radio" name="familia" value="{valor}"> {fam}</label><br>')

    filtro_html += ['      </div>']

    procedimientos_html = []
    for _, row in df.iterrows():
        cod = str(row["Clave"]).strip()
        nombre = str(row["Procedimiento"]).strip()
        familia = str(row["Familia"]).strip().upper()
        valor = re.sub(r"[^\w]+", "-", familia.lower()).strip("-")
        procedimientos_html.append(
            f'       <div class="procedimiento" data-familia="{valor}">\n'
            f'         <a href="../fichas/{cod}">{nombre}</a><br/>\n'
            f'         Código: {cod}<br/>\n'
            f'         Familia: {familia}\n'
            f'       </div>'
        )

    final = '\n'.join([
        '<div id="contenedor-principal">',
        '    <div id="buscador-superior">',
        '        <input type="text" id="buscador" placeholder="Buscar procedimientos...">',
        '    </div>',
        '    <details id="contenedor-filtros">',
        '       <summary>Filtros disponibles</summary>',
        '       <div id="filtros">',
        *filtro_html,
        '    </div>', 
        '  </div>',
        '',
        '  <div style="flex: 1;">',
        '    <div id="contador-resultados" class="contador-resultados"></div>',
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
    plantilla = cargar_plantilla(TEMPLATE_FICHA)
    generar_fichas(df, plantilla)
    generar_nav_yml(df)
    build_mkdocs_yml()
    generar_buscador_md(df)
    print("Contenidos generados correctamente.")

if __name__ == "__main__":
    main()
