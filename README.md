
# Catálogo de Procedimientos Administrativos Municipales · Tenerife

Este repositorio contiene el código y los contenidos del **Catálogo de Procedimientos Administrativos** de los ayuntamientos de Tenerife, una iniciativa desarrollada por el **Cabildo Insular de Tenerife** en el marco del servicio de **Asistencia Técnica en Modernización**.

Su objetivo es proporcionar un portal unificado, estructurado y accesible para consultar los procedimientos administrativos comunes a los municipios de la isla.

## 📂 Estructura del repositorio

```
.
├── docs/                    # Contenidos publicados en el portal
│   ├── fichas/              # Fichas Markdown de cada procedimiento (una por código)
│   ├── buscador.md          # Página de catálogo con buscador y filtros
│   ├── index.md             # Página de inicio del portal
│   └── ...                  # Otros contenidos complementarios
├── data/                    # Documentación y fuentes originales (Excel)
│   └── Borrador_Propuesta catálogo_90 procedimientos.xlsx
├── scripts/                 # Scripts de generación automática
│   └── generar_nav_y_fichas.py
├── mkdocs.yml               # Configuración principal de MkDocs
├── mkdocs.base.yml          # Plantilla base de mkdocs.yml con marcador dinámico
├── mkdocs.nav.yml           # Fragmento YAML generado automáticamente con el bloque nav:
└── README.md                # Este archivo
```

## ⚙️ Automatización

El repositorio incluye un proceso automático para generar:

- La navegación (`nav:`) de `mkdocs.yml` agrupada por familias.
- Las fichas Markdown de cada procedimiento (`docs/fichas/*.md`), a partir del Excel.

Este proceso se ejecuta con el script:

```bash
python scripts/generar_nav_y_fichas.py
```

> El script utiliza una plantilla externa (`plantilla_ficha_procedimiento.md`) para generar el contenido de cada ficha.

## 🏗 Construcción del portal

El sitio está construido con [**MkDocs**](https://www.mkdocs.org/) y el tema [**Material for MkDocs**](https://squidfunk.github.io/mkdocs-material/).

Para iniciar el portal en local:

```bash
mkdocs serve
```

Para generar el sitio estático:

```bash
mkdocs build
```

## ❗ Aviso legal

Este catálogo tiene carácter **informativo y orientativo**. Su contenido **no es jurídicamente vinculante** ni sustituye la información publicada por los ayuntamientos en sus sedes electrónicas.

## 🤝 Licencia y colaboración

Este proyecto es una iniciativa abierta a la colaboración entre el **Cabildo Insular de Tenerife** y los **ayuntamientos de la isla**. El contenido evoluciona de forma progresiva y colaborativa, y puede ser reutilizado y adaptado por otras entidades locales.
