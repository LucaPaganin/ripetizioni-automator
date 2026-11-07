---
titolo: Studio di funzione con radice e disequazioni irrazionali
data: '2026-01-27'
studente: Andrea Ferrando
materia: matematica
argomento: Studio di funzione
sottoargomenti:
- Dominio o Campo di Esistenza
- Zeri di una funzione
- Studio del segno
- Equazioni e disequazioni irrazionali
esercizi:
- 2
errori_tipici:
- Dimenticare le condizioni di esistenza (C.E.) nello studio del segno
- Confondere l'uso delle C.E. nelle equazioni irrazionali (per accettabilità) rispetto
  alle disequazioni (per impostare il sistema)
fonte: https://drive.google.com/file/d/1BtYRd433xofaKHYXU8KIN-ej2F2xwIAN/view?usp=drivesdk
generato: '2026-11-07'
---

# Studio di funzione con radice e disequazioni irrazionali

## Formule chiave

- **Definizione di zero di una funzione:** 
  Ogni soluzione dell'equazione $f(x) = 0$ si chiama zero di $f$. L'insieme delle soluzioni sono tutti e soli gli zeri di $f$.

- **Regola generale per lo studio del segno di una frazione algebrica $f(x) = \frac{N(x)}{D(x)}$:**
  - Per il Numeratore: si pone $N(x) \ge 0$ (o strettamente maggiore a seconda dei casi), usando però **solo le condizioni di esistenza (C.E.)**.
  - Per il Denominatore: si pone $D(x) > 0$ **contando tutto** (C.E. ed eventuali discussioni sui radicali) e poi si uniscono i risultati nel grafico dei segni.

---

## Esercizio 2

**Testo:**
Considera la funzione $f(x)$ a fianco:
2a) Calcola il dominio di $f(x)$.
2b) Calcola gli zeri e il segno della funzione.
2c) Riporta quanto trovato sul piano cartesiano con un grafico probabile di funzione, utilizzando la notazione opportuna.

$$f(x) = \frac{|x-2| - 3x}{2 - x - \sqrt{x^2 + 2x}}$$

---

### 2a) Calcolo del dominio (Campo di Esistenza)

Il numeratore è sempre definito. Per il denominatore e la radice quadrata si imposta il sistema delle condizioni:

$$\begin{cases} 
2 - x - \sqrt{x^2 + 2x} \neq 0 \\ 
x^2 + 2x \ge 0 
\end{cases}$$

Analizziamo la seconda disequazione (argomento della radice):
$$x(x+2) \ge 0 \iff x \le -2 \lor x \ge 0 \quad (1)$$

Isoliamo il radicale nella prima equazione (condizione di esistenza della frazione):
$$2 - x \neq \sqrt{x^2 + 2x} \quad (2)$$

Per risolvere la (2) con l'equazione associata elevata al quadrato (notando che se $2-x < 0$ l'equazione è impossibile o comunque verificata se il radicale è positivo, ma procediamo con il sistema dei casi):
Impostiamo le condizioni di accettabilità (c.c.s.):
$$\begin{cases} 
2 - x \ge 0 \\ 
(2 - x)^2 \neq x^2 + 2x 
\end{cases} \implies \begin{cases} 
x \le 2 \\ 
4 - 4x + x^2 \neq x^2 + 2x 
\end{cases} \implies \begin{cases} 
x \le 2 \\ 
-6x \neq -4 
\end{cases} \implies \begin{cases} 
x \le 2 \\ 
x \neq \frac{2}{3} 
\end{cases}$$

Mettendo a sistema la condizione (1) del radicando e la non-uguaglianza (2):
$$\text{C.E.: } \left(x \le -2 \lor x \ge 0\right) \land \left(x \le 2 \land x \neq \frac{2}{3}\right)$$

In sintesi, il dominio della funzione è:
$$\text{C.E.: } x \le -2 \lor 0 \le x < \frac{2}{3} \lor x > \frac{2}{3}$$
In formato insiemistico:
$$(-\infty, -2] \cup \left[0, \frac{2}{3}\right) \cup \left(\frac{2}{3}, +\infty\right)$$

---

### 2b) Zeri e Segno

#### Zeri della funzione ($f(x) = 0$)
Si pone il numeratore uguale a zero intersecato con il C.E.:
$$|x-2| - 3x = 0$$

Distinguiamo i casi del valore assoluto:
1. **Se $x - 2 \ge 0 \implies x \ge 2$:**
   $$(x - 2) - 3x = 0 \implies -2x - 2 = 0 \implies x = -1$$
   Ma $x = -1$ non è accettabile perché non soddisfa $x \ge 2$ (e non è nel C.E.).
   
2. **Se $x - 2 < 0 \implies x < 2$:**
   $$-(x - 2) - 3x = 0 \implies -x + 2 - 3x = 0 \implies -4x = -2 \implies x = \frac{1}{2}$$
   Verifichiamo se $x = \frac{1}{2}$ appartiene al C.E. ($\frac{1}{2} \neq \frac{2}{3}$ e $\frac{1}{2} \ge 0$). È accettabile.

**Zeri:** Solo $x = \frac{1}{2}$.

#### Segno della funzione ($f(x) > 0$)
*Ricordarsi di applicare il C.E. alla fine.*

- **Numeratore $> 0$ ($N > 0$):**
  Studiamo $|x-2| - 3x > 0$ spezzando nei due casi:
  - Caso $x \ge 2$: 
    $$x - 2 - 3x > 0 \implies -2x > 2 \implies x < -1 \quad (\text{nessuna soluzione con } x \ge 2)$$
  - Caso $x < 2$: 
    $$-(x - 2) - 3x > 0 \implies -4x > -4 \implies x < 1$$
    Mettendo a sistema con $x < 2$ otteniamo $x < 1$.
    
  Unendo i casi, il numeratore è positivo per $x < 1$. Tenendo conto del C.E., il numeratore si comporta positivamente dove definito.

- **Denominatore $> 0$ ($D > 0$):**
  $$2 - x - \sqrt{x^2 + 2x} > 0 \implies 2 - x > \sqrt{x^2 + 2x}$$
  Questa disequazione irrazionale si divide nei casi in cui il termine $2-x$ è positivo o negativo:
  - Se $2 - x < 0 \implies x > 2$: la radice (che è sempre positiva o nulla dove esiste) non può essere minore di un numero negativo. Quindi qui il denominatore è negativo.
  - Se $2 - x > 0 \implies x < 2$: elevando al quadrato si ottiene la disequazione risololta nello studio dei segni del denominatore, che risulta verificata per $x \le \frac{2}{3}$ (nei limiti del C.E.).

In definitiva, combinando il segno del numeratore e del denominatore con il grafico dei segni e intersecando con il dominio, si ottiene l'andamento del segno di $f(x)$ nel piano cartesiano.

---

## ⚠️ Errori da evitare

- Nelle equazioni irrazionali, le condizioni di accettabilità (c.c.s.) servono **solo** a capire se una soluzione trovata è accettabile o meno, non a determinare il dominio finale in modo autonomo se si è già fatto il C.E. del radicale.
- Nello studio del segno di una frazione, non dimenticare mai di riportare sul grafico finale le restrizioni imposte dal Campo di Esistenza (C.E.).

---

## Materiale generato

### Riepilogo
Lo studio di una funzione con radicali e valori assoluti richiede la determinazione preliminare del Dominio (C.E.), ponendo gli argomenti delle radici maggiori o uguali a zero e i denominatori diversi da zero. Per gli zeri si annulla il numeratore verificandone l'appartenenza al C.E., mentre per il segno si studiano separatamente numeratore e denominatore tenendo conto delle disequazioni irrazionali.

### Esercizi simili
1. Studiare il dominio, gli zeri e il segno della funzione:
   $$f(x) = \frac{x - 1}{1 - x - \sqrt{x^2 - 1}}$$
   <details><summary>Soluzione</summary>
   - C.E.: $(-\infty, -1] \cup \{1\}$ non ammissibile per denominatore nullo, procedere imponendo le condizioni di realtà del radicale $x^2 - 1 \ge 0 \implies x \le -1 \lor x \ge 1$ e la diversità da zero del denominatore $1 - x \neq \sqrt{x^2-1}$.
   - Zeri: $x = 1$ (da verificare l'accettabilità nel dominio).
   - Segno: studiare $N>0$ e $D>0$ unendo i risultati con il C.E.
   </details>

2. Trovare il dominio della funzione:
   $$f(x) = \frac{2x + 3}{\sqrt{4 - x^2} - x}$$
   <details><summary>Soluzione</summary>
   - C.E.: Sistema con il radicando $\ge 0$ ($4 - x^2 \ge 0 \implies -2 \le x \le 2$) e il denominatore non nullo ($\sqrt{4 - x^2} \neq x$).
   - Svolgendo la condizione del denominatore si ottiene l'intervallo di validità escludendo il punto in cui si annulla.
   </details>

3. Determinare gli zeri della funzione:
   $$f(x) = \frac{|2x - 1| - x}{x + \sqrt{x}}$$
   <details><summary>Soluzione</summary>
   - C.E.: $x \ge 0$ e $x + \sqrt{x} \neq 0 \implies x > 0$.
   - Zeri: porre $|2x - 1| - x = 0$ distinguendo i casi per $2x - 1 \ge 0$ ($x \ge \frac{1}{2}$) e $2x - 1 < 0$ ($x < \frac{1}{2}$), accettando solo le soluzioni strettamente maggiori di $0$.
   </details>

### Flashcard
- **D:** A cosa servono le condizioni di accettabilità (c.c.s.) in un'equazione irrazionale? — **R:** Servono esclusivamente a verificare se le soluzioni trovate algebricamente sono accettabili o vanno scartate.
- **D:** Come si imposta lo studio del segno di una frazione algebrica? — **R:** Si studiano separatamente $N > 0$ e $D > 0$, riportando i segni in un grafico finale e intersecando il tutto con il Campo di Esistenza (C.E.).
- **D:** Qual è la definizione di zero di una funzione $f(x)$? — **R:** È un valore del dominio $x$ tale che $f(x) = 0$, ovvero le ascisse delle intersezioni del grafico con l'asse $x$.
