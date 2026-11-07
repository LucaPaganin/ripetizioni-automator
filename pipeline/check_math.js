// Valida formule LaTeX con KaTeX (stesso motore e versione del sito).
// stdin: JSON [[tex, display], ...]  ->  stdout: JSON [{tex, error}, ...] solo per quelle non valide.
const katex = require("katex");
let input = "";
process.stdin.on("data", (d) => (input += d)).on("end", () => {
  const bad = [];
  for (const [tex, display] of JSON.parse(input)) {
    try {
      katex.renderToString(tex, { displayMode: display, throwOnError: true, strict: "ignore" });
    } catch (e) {
      bad.push({ tex, error: String(e.message || e) });
    }
  }
  process.stdout.write(JSON.stringify(bad));
});
