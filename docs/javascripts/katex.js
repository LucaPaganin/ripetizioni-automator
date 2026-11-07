// Renderizza le formule preparate da hooks/math.py. document$ (Material) riesegue
// il rendering anche con la navigazione istantanea.
document$.subscribe(() => {
  document.querySelectorAll("span.math").forEach((el) => {
    if (el.dataset.rendered) return;
    renderMathInElement(el, {
      delimiters: [
        { left: "\\[", right: "\\]", display: true },
        { left: "\\(", right: "\\)", display: false },
      ],
      throwOnError: false, // formula non valida: mostrata in rosso, il resto della pagina va
      strict: "ignore",
    });
    el.dataset.rendered = "1";
  });
});
