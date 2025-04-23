# Catálogo de procedimientos municipales comunes de Tenerife

Este repositorio contiene el código fuente y los contenidos del **Catálogo Común de Procedimientos Administrativos** de los ayuntamientos de Tenerife. Ha sido desarrollado por el **Cabildo Insular de Tenerife** como parte del servicio de **Asistencia Técnica en Modernización**, en colaboración con los ayuntamientos participantes.

Su propósito es ofrecer un **portal unificado, accesible y estructurado** para la consulta y tramitación de procedimientos administrativos comunes a nivel local.

---

## 📁 Estructura del repositorio

```
.
├── docs/                          # Contenidos publicados en el portal
│   ├── assets/                    # Archivos estáticos
│   │  ├── estilos.css             # Estilos personalizados para el tema
│   │  └── filtros.js              # Lógica de búsqueda y filtrado en JS
│   ├── fichas/                    # Fichas Markdown de cada procedimiento
│   ├── buscador.md                # Catálogo con buscador y filtros dinámicos
│   ├── index.md                   # Página de inicio del portal
│   └── plantilla_ficha.md         # Plantilla base para las fichas
├── data/
│   └── Borrador_Propuesta catálogo_90 procedimientos.xlsx  # Fuente de datos
├── scripts/
│   └── gen_contents.py            # Generación automática de contenidos
├── mkdocs.yml                     # Configuración principal de MkDocs
├── mkdocs.base.yml                # Plantilla base con marcador para 'nav'
├── mkdocs.nav.yml                 # Fragmento generado automáticamente
└── README.md                      # Este documento
```

---

## ⚙️ Automatización del catálogo

El contenido del portal se genera automáticamente a partir de un fichero Excel mediante un script Python que:

- Crea todas las fichas `.md` normalizadas con información enriquecida.
- Inserta diagramas de flujo Mermaid desde el Excel.
- Genera el bloque `nav:` para `mkdocs.yml`, agrupado por familias.
- Actualiza la página `buscador.md` con filtros y listado de procedimientos.

### Requisitos

```bash
pip install pandas openpyxl
```

### Ejecución

```bash
python scripts/gen_contents.py
```

---

## 🚧 Construcción del portal

El proyecto utiliza [**MkDocs**](https://www.mkdocs.org/) con el tema [**Material for MkDocs**](https://squidfunk.github.io/mkdocs-material/).

### Para desarrollo local

```bash
mkdocs serve
```

### Para generar el sitio estático

```bash
mkdocs build
```

---

## 🌐 Publicación en GitHub Pages

### 1. Inicializa el repositorio

```bash
git init
git add .
git commit -m "Versión inicial"
```

### 2. Añade el remoto de GitHub

```bash
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
```

### 3. Sube el contenido a la rama `main`

```bash
git branch -M main
git push -u origin main
```

### 4. Publica con `gh-deploy`

```bash
mkdocs gh-deploy
```

Esto compilará el sitio y subirá el contenido generado a la rama `gh-pages`.

### 5. Configura GitHub Pages

En GitHub:

- Ve a **Settings → Pages**
- Fuente: rama `gh-pages`, carpeta `/ (root)`
- Guarda los cambios

Tu sitio estará disponible en: `https://TU_USUARIO.github.io/TU_REPO/`

---

## ℹ️ Aviso legal

Este portal tiene carácter **informativo y orientativo**. Su contenido **no tiene validez jurídica** y no sustituye a la información publicada en las sedes electrónicas oficiales de los ayuntamientos.

El catálogo es un recurso **vivo y en constante evolución**, sujeto a validaciones y mejoras por parte de los municipios y del Cabildo Insular de Tenerife.

---

## 🤝 Licencia y colaboración

Este repositorio promueve la **colaboración interadministrativa** entre el Cabildo y los ayuntamientos de la isla. Su contenido puede ser reutilizado, adaptado y ampliado por otras entidades públicas en el marco de iniciativas de modernización y mejora administrativa.
