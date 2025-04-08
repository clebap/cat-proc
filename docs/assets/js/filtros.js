function activarFiltros() {
    const estadoRadios = document.querySelectorAll('input[name="estado"]');
    const familiaRadios = document.querySelectorAll('input[name="familia"]');
    const buscador = document.getElementById("buscador-superior");
    const procedimientos = document.querySelectorAll(".procedimiento");
  
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
    }
  
    estadoRadios.forEach(r => r.addEventListener("change", filtrar));
    familiaRadios.forEach(r => r.addEventListener("change", filtrar));
    buscador.addEventListener("input", filtrar);
  }
  
  if (typeof document$ !== "undefined") {
    document$.subscribe(() => {
      activarFiltros();
      if (window.location.pathname.includes("/procedimientos")) {
        document.body.classList.add("pagina-procedimientos");
      }
    });
  }

