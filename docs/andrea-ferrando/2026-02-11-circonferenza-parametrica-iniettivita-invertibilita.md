---
titolo: Circonferenza parametrica, iniettività, suriettività e funzioni inverse
data: '2026-02-11'
studente: Andrea Ferrando
materia: matematica
argomento: Geometria analitica e Analisi matematica
sottoargomenti:
- Circonferenza parametrica
- Funzioni iniettive e suriettive
- Funzioni inverse e restrizioni
esercizi:
- 1
errori_tipici:
- Confondere la condizione di esistenza del raggio con quella della circonferenza
  degenere
- Applicare l'invertibilità a funzioni non iniettive senza limitare il dominio
fonte: https://drive.google.com/file/d/1ZUyfn7xd2j0ygLMoqj8qZkCl2NPKGmmM/view?usp=drivesdk
generato: '2026-11-07'
---

# Circonferenza parametrica, iniettività, suriettività e funzioni inverse

## Formule chiave

- **Equazione canonica della circonferenza nel piano cartesiano:**
  $$(x - x_0)^2 + (y - y_0)^2 = R^2$$
  dove $C(x_0, y_0)$ è il centro e $R$ è il raggio.

- **Definizione di funzione iniettiva:**
  Una funzione $f: D \to C$ si dice iniettiva se associa a valori distinti del dominio $D$ valori distinti del codominio $C$:
  $$\forall x_1, x_2 \in D, \quad x_1 \neq x_2 \implies f(x_1) \neq f(x_2)$$

- **Definizione di funzione suriettiva:**
  Una funzione $f: D \to C$ si dice suriettiva se ogni elemento del codominio $C$ è immagine di almeno un elemento del dominio $D$:
  $$\forall y \in C, \quad \exists x \in D \text{ tale che } f(x) = y$$

- **Funzione biiettiva (o biunivoca):**
  Una funzione si dice biiettiva se è contemporaneamente iniettiva e suriettiva. Ammette sempre funzione inversa $f^{-1}$.

- **Inversione della parabola (restrizione):**
  La funzione $f(x) = x^2$ con dominio $\mathbb{R}$ non è iniettiva e quindi non è invertibile. Restringendo il dominio a $x \ge 0$, ossia $f: [0, +\infty) \to [0, +\infty)$, la funzione diventa biiettiva e la sua inversa è:
  $$f^{-1}(x) = \sqrt{x}$$

---

## Esercizio 1

**Testo:**
Determina i valori di $k$ per cui l'equazione $x^2 + y^2 - 2x + 2y + k + 3 = 0$ rappresenta:
1. una circonferenza (eventualmente degenere);
2. una circonferenza con il centro sull'asse $x$;
3. una circonferenza di raggio $2$.

**Svolgimento:**
Completiamo i quadrati per i termini in $x$ e in $y$:
$$x^2 - 2x + y^2 + 2y + k + 3 = 0$$

Aggiungiamo e sottraiamo i termini necessari per completare i quadrati $(x-1)^2$ e $(y-1)^2$:
$$(x^2 - 2x + 1) - 1 + (y^2 + 2y + 1) - 1 + k + 3 = 0$$
$$(x - 1)^2 - 1 + (y - 1)^2 - 1 + k + 3 = 0$$
$$(x - 1)^2 + (y - 1)^2 - 2 + k + 3 = 0$$
$$(x - 1)^2 + (y - 1)^2 + k + 1 = 0$$

Isoliamo i quadrati:
$$(x - 1)^2 + (y - 1)^2 = -(k + 1)$$

Il centro della circonferenza è $C(1, 1)$. L'ordinata del centro è $y_0 = 1$ (quindi il centro non si trova sull'asse $x$, a prescindere dal valore di $k$).

Affinché l'equazione rappresenti una circonferenza (reale o degenere), il termine noto a destra (che corrisponde a $R^2$) deve essere maggiore o uguale a zero:
$$R^2 = -(k + 1) \ge 0 \implies k + 1 \le 0 \implies k \le -1$$

- **Circonferenza degenere ($R = 0$):**
  $$-(k + 1) = 0 \implies k = -1$$
- **Circonferenza reale ($R > 0$):**
  $$-(k + 1) > 0 \implies k < -1$$

Per quanto riguarda il punto 3, imponiamo che il raggio sia $R = 2$:
$$R^2 = 2^2 = 4$$
Quindi:
$$-(k + 1) = 4 \implies k + 1 = -4 \implies k = -5$$

---

## ⚠️ Errori da evitare

- Confondere la condizione per cui una scrittura ha senso matematico: l'espressione $R = \sqrt{-(k+1)}$ ha senso solo se il radicando è non negativo, ovvero quando $k \le -1$. Per $k > -1$, il radicando è negativo e la radice nel campo reale non ha senso.
- Dimenticare che per rendere invertibile una funzione non iniettiva (come $f(x) = x^2$) è obbligatorio specificare una restrizione del dominio (es. $x \ge 0$).

---

## Materiale generato

### Riepilogo
Gli appunti affrontano lo studio dei parametri in una circonferenza cartesiana tramite il completamento dei quadrati e introducono i concetti fondamentali di analisi sulle funzioni: iniettività, suriettività, biettività e inversione di funzioni non invertibili mediante restrizione del dominio.

### Esercizi simili

1. **Esercizio:** Determina per quali valori di $k$ l'equazione $x^2 + y^2 + 4x - 6y + k + 9 = 0$ rappresenta una circonferenza reale.
   <details><summary>Soluzione</summary>
   Completiamo i quadrati: $(x+2)^2 - 4 + (y-3)^2 - 9 + k + 9 = 0 \implies (x+2)^2 + (y-3)^2 = 4 - k$.
   Condizione di realtà ($R^2 > 0$): $4 - k > 0 \implies k < 4$.
   </details>

2. **Esercizio:** Data la funzione $f(x) = 2x - 3$ con $f: \mathbb{R} \to \mathbb{R}$, dimostra che è iniettiva e trova la sua funzione inversa $f^{-1}(x)$.
   <details><summary>Soluzione</summary>
   Iniettività: $2x_1 - 3 = 2x_2 - 3 \implies x_1 = x_2$ (iniettiva).
   Inversa: ponendo $y = 2x - 3$, ricaviamo $x = \frac{y+3}{2}$, da cui $f^{-1}(x) = \frac{x+3}{2}$.
   </details>

3. **Esercizio:** Determina il valore di $k$ affinché la circonferenza $x^2 + y^2 - 2kx = 0$ abbia raggio pari a $3$.
   <details><summary>Soluzione</summary>
   Centro $C(k, 0)$, raggio $R = \sqrt{k^2 - 0} = |k|$. Ponendo $|k| = 3$, si ottiene $k = 3$ oppure $k = -3$.
   </details>

### Flashcard
- **D:** Quando un'equazione in forma canonica $(x-x_0)^2 + (y-y_0)^2 = \text{Termine Noto}$ rappresenta una circonferenza reale? — **R:** Quando il Termine Noto è strettamente maggiore di zero ($R^2 > 0$).
- **D:** Cos'è una funzione iniettiva? — **R:** Una funzione che associa elementi distinti del dominio a elementi distinti del codominio.
- **D:** Qual è la condizione per invertire una funzione? — **R:** La funzione deve essere biiettiva (iniettiva e suriettiva). Se non lo è sul dominio naturale, occorre ristringerla.
- **D:** Qual è l'inversa di $f(x) = x^2$ ristretta a $x \ge 0$? — **R:** $f^{-1}(x) = \sqrt{x}$.
