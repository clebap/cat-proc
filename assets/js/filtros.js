function activarFiltros() {
    const estadoRadios = document.querySelectorAll('input[name="estado"]');
    const familiaRadios = document.querySelectorAll('input[name="familia"]');
    const buscador = document.getElementById("buscador");
    const procedimientos = document.querySelectorAll(".procedimiento");
  
    filtrar();

    function filtrar() {
      const estado = document.querySelector('input[name="estado"]:checked')?.value || "todos";
      const familia = document.querySelector('input[name="familia"]:checked')?.value || "todas";
      const texto = buscador.value.toLowerCase();
  
      procedimientos.forEach(procedimiento => {
        const titulo = procedimiento.textContent.toLowerCase();
        const estadoprocedimiento = procedimiento.getAttribute("data-estado");
        const familiaprocedimiento = procedimiento.getAttribute("data-familia");
  
        const coincideEstado = estado === "todos" || estado === estadoprocedimiento;
        const coincideFamilia = familia === "todas" || familia === familiaprocedimiento;
        const coincideTexto = titulo.includes(texto);
  
        procedimiento.style.display = (coincideEstado && coincideFamilia && coincideTexto) ? "block" : "none";
      });

      // Contar los procedimientos visibles
      const visibles = Array.from(procedimientos).filter(proc => proc.style.display !== "none");
      document.getElementById("contador-resultados").textContent = `Se han encontrado ${visibles.length} procedimiento${visibles.length !== 1 ? 's' : ''}`;
    }
  
    estadoRadios.forEach(r => r.addEventListener("change", filtrar));
    familiaRadios.forEach(r => r.addEventListener("change", filtrar));
    buscador.addEventListener("input", filtrar);
  }
  
  if (typeof document$ !== "undefined") {
    document$.subscribe(() => {
      if (window.location.pathname === '/') {
        document.body.classList.add("pagina-sin-rsidebar");
      }
      if (window.location.pathname.includes("/buscador")) {
        activarFiltros();
        document.body.classList.add("pagina-buscador");
      }
    });
  }
