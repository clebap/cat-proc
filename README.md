# Catálogo de procedimientos municipales de Tenerife

Este repositorio contiene el código fuente y los contenidos del **Catálogo de procedimientos municipales de Tenerife** de los ayuntamientos de Tenerife. Ha sido desarrollado por el **Cabildo Insular de Tenerife** como parte del servicio de **Asistencia Técnica en Modernización**, en colaboración con los ayuntamientos participantes.

Su propósito es ofrecer un **portal unificado, accesible y estructurado** para la consulta y tramitación de procedimientos administrativos comunes a nivel local.

---

## 📁 Estructura del repositorio

```
.
├── docs/                          # Contenidos del portal web
│   ├── assets/                    # Archivos estáticos
│   │   ├── estilos.css            # Estilos personalizados
│   │   └── filtros.js             # Lógica de búsqueda y filtrado
│   ├── fichas/                    # Fichas .md de cada procedimiento
│   ├── buscador.md                # Catálogo con buscador interactivo y filtros
│   ├── familias.md                # Página de presentación del portal
│   ├── index.md                   # Página de presentación del portal
│   ├── mantenimiento.md           # Página de presentación del portal
│   ├── plantilla_ficha.md         # Plantilla base para generar fichas
│   └── README_PASOS_DEPLOY.md     # Instrucciones de despliegue en GitHub Pages
├── utils/
│   ├── data/
│   │   └── Borrador_Propuesta catálogo_90 procedimientos.xlsx  # Fuente de datos centralizada
│   ├── templates/
│   │   ├── mkdocs.base.yml        # Plantilla para insertar navegación dinámica
│   │   └── ficha.base.md          # Plantilla importada por el script 
│   ├── tmp/
│   │   └── mkdocs.nav.yml         # Fragmento `nav:` generado automáticamente
│   └── gen_contents.py            # Script de generación automática de contenidos
├── mkdocs.yml                     # Configuración principal de MkDocs
└── README.md                      # Este documento

```

---

## ⚙️ Automatización de contenidos

La actualización del portal está completamente automatizada. El script `gen_contents.py`:

- Genera las fichas `.md` a partir de los datos del Excel.
- Inserta diagramas Mermaid para visualizar la tramitación.
- Crea el bloque de navegación (`nav:`) agrupado por familias temáticas.
- Actualiza dinámicamente la página `buscador.md` con los filtros activos y resultados disponibles.

### Requisitos

```bash
pip install pandas openpyxl
```

### Ejecución

```bash
python scripts/gen_contents.py
```

---

## 🛠 Construcción y pruebas

El sitio se construye utilizando [MkDocs](https://www.mkdocs.org/) y el tema [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

#### Para ver en local:

```bash
mkdocs serve
```

#### Para compilar el sitio estático:

```bash
mkdocs build
```

---

## 🚀 Publicación en GitHub Pages

1. Inicializa y sube el repositorio a GitHub.
2. Ejecuta el comando:

```bash
mkdocs gh-deploy
```

Esto crea y publica la rama `gh-pages` con el sitio compilado.

3. En GitHub, configura la publicación en **Settings → Pages** usando `gh-pages` como rama y raíz (`/`) como carpeta.

Consulta el archivo `docs/README_PASOS_DEPLOY.md` para más detalles.

---

## ⚠️ Aviso legal

Este portal tiene carácter **informativo y orientativo**. Su contenido **no sustituye ni tiene efecto jurídico vinculante** frente a la información oficial publicada en las sedes electrónicas municipales.

El catálogo es un recurso **vivo y colaborativo**, sujeto a revisión, validación y mejora continua.

---

## 🤝 Licencia y colaboración

Este repositorio promueve la **colaboración interadministrativa**. Su estructura y contenidos pueden ser reutilizados y adaptados por otras entidades públicas con fines de mejora de la gestión administrativa y la transparencia institucional.
