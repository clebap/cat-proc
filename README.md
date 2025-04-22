# Catálogo de procedimientos administrativos municipales 

Este repositorio contiene el código y los contenidos del **Catálogo de Procedimientos Administrativos** de los ayuntamientos de Tenerife. Ha sido desarrollado por el **Cabildo Insular de Tenerife** dentro del servicio de **Asistencia Técnica en Modernización**, en colaboración con los ayuntamientos participantes.

El portal tiene como finalidad ofrecer una plataforma unificada, accesible y estructurada para consultar los procedimientos administrativos comunes a los municipios de la isla.

---

## Estructura del repositorio

```
.
├── docs/                          # Contenidos publicados por MkDocs
│   ├── fichas/                    # Fichas individuales en Markdown (una por procedimiento)
│   ├── buscador.md                # Página con el buscador interactivo y filtros dinámicos
│   ├── index.md                   # Página de inicio del portal
│   ├── estilos.css                # Estilos personalizados
│   ├── filtros.js                 # Lógica de filtrado y buscador en JS
│   └── plantilla_ficha.md         # Plantilla base para generación de fichas
├── data/
│   └── Borrador_Propuesta catálogo_90 procedimientos.xlsx  # Excel con la información origen
├── scripts/
│   ├── gen_contents.py            # Generación automática de contenidos
│   └── otros scripts auxiliares...
├── mkdocs.yml                     # Configuración principal de MkDocs
├── mkdocs.base.yml               # Plantilla con marcador para inserción automática del bloque nav
├── mkdocs.nav.yml                # Fragmento YAML generado automáticamente con la navegación
└── README.md                      # Este documento
```

---

## Automatización del catálogo

La construcción del portal está automatizada a partir del contenido del Excel. El script principal se encarga de:

- Generar todas las fichas `.md` de procedimientos con estructura normalizada.
- Insertar los diagramas Mermaid definidos en la hoja de cálculo.
- Crear dinámicamente la estructura `nav:` de `mkdocs.yml`, agrupada por familias.
- Actualizar la página `buscador.md` con los filtros y procedimientos disponibles.

### Cómo ejecutar

Asegúrate de tener un entorno Python con pandas y openpyxl instalados:

```bash
pip install pandas openpyxl
```

Ejecuta el script principal:

```bash
python scripts/gen_contents.py
```

> El script leerá el Excel actualizado y generará automáticamente los contenidos en `docs/fichas/`, `mkdocs.nav.yml` y `buscador.md`.

---

## Construcción del sitio

Este proyecto utiliza [**MkDocs**](https://www.mkdocs.org/) junto con el tema [**Material for MkDocs**](https://squidfunk.github.io/mkdocs-material/).

### Servidor local para desarrollo

```bash
mkdocs serve
```

### Generar el sitio estático

```bash
mkdocs build
```

---

## Aviso legal

Este portal tiene carácter **informativo y orientativo**. Su contenido **no es jurídicamente vinculante** ni sustituye la información oficial publicada por los ayuntamientos en sus sedes electrónicas.

Además, el catálogo es un **elemento vivo** en constante evolución, sujeto a revisión y mejora progresiva por parte de los municipios y del Cabildo.

---

## Licencia y colaboración

El contenido de este repositorio forma parte de una iniciativa abierta a la colaboración institucional entre el **Cabildo de Tenerife** y los **ayuntamientos de la isla**. Puede ser reutilizado y adaptado por otras entidades públicas que persigan fines similares de mejora administrativa y transparencia.
