---
titolo: Intersezioni tra rette ed ellissi e problemi di corda
data: '2026-03-28'
studente: Andrea Ferrando
materia: matematica
argomento: 'Geometria analitica: l''ellisse'
sottoargomenti:
- Equazione canonica dell'ellisse
- Intersezione retta-ellisse
- Calcolo della lunghezza di una corda
- Condizioni di esistenza con radicali
esercizi:
- '82'
- '88'
- '89'
errori_tipici:
- Dimenticare il dominio di esistenza del radicale (C.E.) quando si parametrizzano
  le intersezioni con rette parallele
fonte: https://drive.google.com/file/d/1fpqPbrsKjy_fB-gw15d3n_nKIOv21CEq/view?usp=drivesdk
generato: '2026-11-07'
---

# Intersezioni tra rette ed ellissi e problemi di corda

## Formule chiave

- **Equazione canonica dell'ellisse con $a > b$ (fuochi sull'asse $x$):**
  $$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$$

- **Semidistanza focale $c$:**
  $$c = \sqrt{|a^2 - b^2|}$$

- **Distanza tra due punti $A(x_A, y_A)$ e $B(x_B, y_B)$:**
  $$\overline{AB} = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$$

---

## Esercizio 82

**Testo:** Data l'ellisse di equazione $\frac{x^2}{4} + \frac{y^2}{16} = 1$, determinare l'intersezione con la retta $r: y = 2x$ e calcolare la lunghezza della corda individuata.

### Svolgimento:

1. **Analisi dell'ellisse:**
   L'equazione è $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$, dove $a^2 = 4 \implies a = 2$ e $b^2 = 16 \implies b = 4$. (I fuochi sono sull'asse $y$ poiché $b > a$).

2. **Sistema per trovare le intersezioni tra retta ed ellisse:**
   $$\begin{cases} y = 2x \\ \frac{x^2}{4} + \frac{y^2}{16} = 1 \end{cases}$$

3. **Sostituzione:**
   $$\frac{x^2}{4} + \frac{(2x)^2}{16} = 1 \implies \frac{x^2}{4} + \frac{4x^2}{16} = 1 \implies \frac{x^2}{4} + \frac{x^2}{4} = 1 \implies \frac{2x^2}{4} = 1 \implies \frac{x^2}{2} = 1$$
   $$x^2 = 2 \implies x = \pm\sqrt{2}$$

4. **Ricerca delle coordinate dei punti $A$ e $B$:**
   Se $x = -\sqrt{2}$, allora $y = 2(-\sqrt{2}) = -2\sqrt{2} \implies A(-\sqrt{2}, -2\sqrt{2})$.
   Se $x = \sqrt{2}$, allora $y = 2(\sqrt{2}) = 2\sqrt{2} \implies B(\sqrt{2}, 2\sqrt{2})$.

5. **Calcolo della lunghezza della corda $\overline{AB}$:**
   $$\overline{AB} = \sqrt{(\sqrt{2} - (-\sqrt{2}))^2 + (2\sqrt{2} - (-2\sqrt{2}))^2}$$
   $$\overline{AB} = \sqrt{(2\sqrt{2})^2 + (4\sqrt{2})^2} = \sqrt{4 \cdot 2 + 16 \cdot 2} = \sqrt{8 + 32} = \sqrt{40} = 2\sqrt{10}$$

Risultato finale:
$$\boxed{\overline{AB} = 2\sqrt{10}}$$

---

## Esercizio 88

**Testo:** Determina le rette parallele all'asse $y$ che individuano sull'ellisse di equazione $\frac{x^2}{1} + \frac{y^2}{9} = 1$ un segmento di misura $2$.

### Svolgimento:

1. **Equazione dell'ellisse:**
   $$\frac{x^2}{1} + \frac{y^2}{9} = 1 \implies 9x^2 + y^2 = 9$$

2. **Rette parallele all'asse $y$ (verticali generiche):**
   $$x = K$$
   Condizione di esistenza sull'ascissa $K$ per l'intersezione con l'ellisse: $-1 \le K \le 1$ (altrimenti non interseca).

3. **Intersezione:**
   $$\begin{cases} x = K \\ 9K^2 + y^2 = 9 \end{cases} \implies \begin{cases} x = K \\ y^2 = 9 - 9K^2 = 9(1 - K^2) \end{cases} \implies \begin{cases} x = K \\ y = \pm 3\sqrt{1 - K^2} \end{cases}$$

4. **Punti di intersezione $A$ e $B$:**
   $$A\left(K, 3\sqrt{1-K^2}\right), \quad B\left(K, -3\sqrt{1-K^2}\right)$$

5. **Lunghezza della corda $\overline{AB}$:**
   $$\overline{AB} = 6\sqrt{1-K^2}$$

6. **Imposizione della condizione $\overline{AB} = 2$:**
   $$6\sqrt{1-K^2} = 2 \implies \sqrt{1-K^2} = \frac{2}{6} = \frac{1}{3}$$
   Elevando al quadrato:
   $$1 - K^2 = \frac{1}{9} \implies K^2 = 1 - \frac{1}{9} = \frac{8}{9} \implies K = \pm \sqrt{\frac{8}{9}} = \pm \frac{2\sqrt{2}}{3}$$
   *(Nota: i valori rientrano nell'intervallo $[-1, 1]$, quindi la radice esiste).*

Risultato finale:
Le rette sono:
$$\boxed{x = -\frac{2\sqrt{2}}{3} \quad \text{e} \quad x = \frac{2\sqrt{2}}{3}}$$

---

## Esercizio 89

**Testo:** Determina le rette parallele all'asse $x$ che individuano sull'ellisse di equazione $\frac{x^2}{4} + \frac{y^2}{16} = 1$ un segmento di misura uguale alla semidistanza focale.

### Svolgimento:

1. **Parametri dell'ellisse e semidistanza focale $c$:**
   $a^2 = 4 \implies a = 2$
   $b^2 = 16 \implies b = 4$
   Poiché $b > a$, i fuochi sono sull'asse $y$:
   $$c = \sqrt{b^2 - a^2} = \sqrt{16 - 4} = \sqrt{12} = 2\sqrt{3}$$

2. **Rette parallele all'asse $x$ (orizzontali generiche):**
   $$y = K$$

3. **Intersezione:**
   $$\begin{cases} y = K \\ \frac{x^2}{4} + \frac{K^2}{16} = 1 \end{cases} \implies 4x^2 + K^2 = 16 \implies 4x^2 = 16 - K^2 \implies x^2 = \frac{16 - K^2}{4}$$
   $$x = \pm \frac{1}{2}\sqrt{16 - K^2}$$

4. **Punti d'intersezione $A$ e $B$:**
   $$A\left(-\frac{1}{2}\sqrt{16-K^2}, K\right), \quad B\left(\frac{1}{2}\sqrt{16-K^2}, K\right)$$

5. **Lunghezza della corda $\overline{AB}$:**
   $$\overline{AB} = \sqrt{16 - K^2}$$

6. **Imposizione della condizione $\overline{AB} = c = 2\sqrt{3}$:**
   $$\sqrt{16 - K^2} = 2\sqrt{3}$$
   Elevando al quadrato:
   $$16 - K^2 = (2\sqrt{3})^2 \implies 16 - K^2 = 4 \cdot 3 = 12$$
   $$K^2 = 16 - 12 = 4 \implies K = \pm 2$$

Risultato finale:
$$\boxed{y = \pm 2}$$

---

## ⚠️ Errori da evitare
- Dimenticare di verificare le condizioni di esistenza dei radicali ($1 - K^2 \ge 0$) quando si parametrizzano le intersezioni con rette parallele agli assi.

---

## Materiale generato

### Riepilogo
Il documento analizza le intersezioni tra rette e curve ellittiche impostando sistemi algebrici. Mostra come calcolare la lunghezza delle corde staccate da rette parallele agli assi cartesiani imponendo la misura richiesta dal problema.

### Esercizi simili

1. **Esercizio A:** Data l'ellisse $\frac{x^2}{9} + \frac{y^2}{4} = 1$, trova l'intersezione con la retta $y = x$ e la lunghezza della corda generata.
   <details><summary>Soluzione</summary>Mettendo a sistema si ottiene $x^2 = \frac{36}{13}$, da cui i punti $A\left(-\frac{6}{\sqrt{13}}, -\frac{6}{\sqrt{13}}\right)$ e $B\left(\frac{6}{\sqrt{13}}, \frac{6}{\sqrt{13}}\right)$. La lunghezza della corda è $\overline{AB} = \frac{12}{\sqrt{13}} = \frac{12\sqrt{13}}{13}$.</details>

2. **Esercizio B:** Determina le rette parallele all'asse $x$ che individuano sull'ellisse $\frac{x^2}{9} + \frac{y^2}{4} = 1$ una corda di lunghezza $4$.
   <details><summary>Soluzione</summary>Impostando $y = K$, la lunghezza della corda risulta $\frac{2}{3}\sqrt{9-K^2} = 4 \implies \sqrt{9-K^2} = 6$ (impossibile, poiché il massimo valore della corda è $6$ quando $K=0$). Non esistono rette con tali caratteristiche per la misura $4$, oppure se la misura fosse $2$ si otterrebbe $K = \pm\sqrt{6}$.</details>

3. **Esercizio C:** Trova la lunghezza della corda staccata dalla retta $y = 1$ sull'ellisse $\frac{x^2}{16} + \frac{y^2}{4} = 1$.
   <details><summary>Soluzione</summary>Sostituendo $y = 1$ si ottiene $\frac{x^2}{16} + \frac{1}{4} = 1 \implies x^2 = 12 \implies x = \pm 2\sqrt{3}$. I punti sono $\left(-2\sqrt{3}, 1\right)$ e $\left(2\sqrt{3}, 1\right)$, e la lunghezza della corda è $\overline{AB} = 4\sqrt{3}$.</details>

### Flashcard
- **D:** Come si impposta l'intersezione tra una retta $y = mx + q$ e un'ellisse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$? — **R:** Si sostituisce l'espressione di $y$ della retta nell'equazione dell'ellisse ottenendo un'equazione di secondo grado in $x$.
- **D:** Come si calcola la semidistanza focale $c$ di un'ellisse canonica? — **R:** Con la formula $c = \sqrt{|a^2 - b^2|}$.
- **D:** Qual è la condizione geometrica affinché una retta verticale $x = K$ intersechi un'ellisse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$? — **R:** L'ascissa $K$ deve appartenere all'intervallo $[-a, a]$.
