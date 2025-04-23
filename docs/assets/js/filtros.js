
function activarFiltros() {
  const estadoRadios = document.querySelectorAll('input[name="estado"]');
  const familiaRadios = document.querySelectorAll('input[name="familia"]');
  const buscador = document.getElementById("buscador");
  const procedimientos = document.querySelectorAll(".procedimiento");

  function filtrar() {
    const estado = document.querySelector('input[name="estado"]:checked')?.value || "todos";
    const familia = document.querySelector('input[name="familia"]:checked')?.value || "todas";
    const texto = buscador.value.toLowerCase();

    let contador = 0;
    procedimientos.forEach(proc => {
      const textoProc = proc.textContent.toLowerCase();
      const familiaProc = proc.getAttribute("data-familia");

      const visible = (familia === "todas" || familia === familiaProc) &&
                      textoProc.includes(texto);

      proc.style.display = visible ? "block" : "none";
      if (visible) contador++;
    });

    const contadorSpan = document.getElementById("contador-resultados");
    if (contadorSpan) {
      let mensaje = `${contador} procedimiento${contador !== 1 ? "s" : ""}`;
      
      if (familia !== "todas") {
        const labelSeleccionado = document.querySelector(`input[name="familia"][value="${familia}"]`);
        const nombreFamilia = labelSeleccionado?.parentElement?.textContent?.trim() || familia;
        mensaje += ` de la familia ${nombreFamilia}`;
      }
    
      contadorSpan.textContent = mensaje;
    }

    if (window.innerWidth <= 768) {
      const detalles = document.getElementById("contenedor-filtros");
      if (detalles && detalles.open) detalles.open = false;
    }
  }

  estadoRadios.forEach(radio => radio.addEventListener("change", filtrar));
  familiaRadios.forEach(radio => radio.addEventListener("change", filtrar));
  buscador.addEventListener("input", filtrar);
  filtrar(); // Ejecutar al cargar
}

if (typeof document$ !== "undefined") {
  document$.subscribe(() => {
    if (window.location.pathname.includes("/buscador")) {
      activarFiltros();
    }
  });
}
