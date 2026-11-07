---
titolo: Studio di funzione con radicali e geometria analitica della circonferenza
data: '2026-04-27'
studente: Andrea Ferrando
materia: matematica
argomento: Geometria analitica
sottoargomenti:
- Studio di funzioni irrazionali
- Circonferenza nel piano cartesiano
- Condizioni di tangenza
esercizi:
- 1
- 2
errori_tipici: []
fonte: https://drive.google.com/file/d/1ZwAnrw1GhSVPuhNMok2tmstgABE7o-w-/view?usp=drivesdk
generato: '2026-11-07'
---

# Studio di funzione con radicali e geometria analitica della circonferenza

## Formule chiave

- **Equazione canonica della circonferenza:**
  $$(x - x_C)^2 + (y - y_C)^2 = R^2$$
  dove $C(x_C, y_C)$ è il centro e $R$ è il raggio.

- **Equazione generale della circonferenza:**
  $$x^2 + y^2 + ax + by + c = 0$$
  con le coordinate del centro date da:
  $$x_C = -\frac{a}{2}, \quad y_C = -\frac{b}{2}$$

## Esercizio 1

Studiamo e tracciamo il grafico della funzione irrazionale:
$$y = \sqrt{-x^2 + 6x + 7} - 2$$

### 1. Dominio (Campi di esistenza)
Poniamo il radicando maggiore o uguale a zero:
$$-x^2 + 6x + 7 \ge 0 \implies x^2 - 6x - 7 \le 0$$

Risolviamo l'equazione associata:
$$x = \frac{3 \pm \sqrt{9 + 7}}{1} = 3 \pm \sqrt{16} = 3 \pm 4 = \begin{cases} -1 \\ 7 \end{cases}$$

Quindi il dominio della funzione è:
$$\text{Dom}: [-1, 7]$$

### 2. Riconoscimento geometrico (Circonferenza)
Isoliamo il radicale:
$$y + 2 = \sqrt{-x^2 + 6x + 7}$$

Eleviamo al quadrato entrambi i membri (notando che $y+2 \ge 0$):
$$(y + 2)^2 = -x^2 + 6x + 7$$

Spostiamo i termini in $x$ a sinistra e completiamo il quadrato:
$$x^2 - 6x + 9 - 9 + (y + 2)^2 = 7$$
$$(x - 3)^2 + (y + 2)^2 = 7 + 9$$
$$(x - 3)^2 + (y + 2)^2 = 16$$

Abbiamo ottenuto l'equazione di una circonferenza di centro $C(3, -2)$ e raggio $R = 4$.

### 3. Scomposizione nei due rami
La funzione originale rappresenta solo una parte della circonferenza (il ramo superiore):
$$(y + 2)^2 = -x^2 + 6x + 7 \implies |y + 2| = \sqrt{-x^2 + 6x + 7}$$

- Ramo superiore ($y \ge -2$):
  $$f: y + 2 = \sqrt{-x^2 + 6x + 7} \implies y = \sqrt{-x^2 + 6x + 7} - 2$$
- Ramo inferiore ($y < -2$):
  $$g: y + 2 = -\sqrt{-x^2 + 6x + 7} \implies y = -\sqrt{-x^2 + 6x + 7} - 2$$

---

## Esercizio 2

Determina l'equazione della circonferenza con centro sulla retta $s: y = 3x + 2$ e tangente alla retta $r: 2x + y - 2 = 0$ nel suo punto $P$ di ordinata nulla.

### Analisi delle condizioni
1. Il centro $C(x_C, y_C)$ appartiene alla retta $s$, quindi le sue coordinate soddisfano l'equazione di $s$:
   $$y_C = 3x_C + 2$$
2. Il punto $P$ appartiene alla retta $r$ ed ha ordinata $y_P = 0$:
   $$2x_P + 0 - 2 = 0 \implies x_P = 1 \implies P(1, 0)$$
3. La circonferenza è tangente alla retta $r$ nel punto $P$.

### Svolgimento (Metodo con fascio o condizioni algebriche)
Usando la forma canonica e imponendo le condizioni, oppure utilizzando l'equazione generale:
$$\gamma: x^2 + y^2 + ax + by + c = 0$$

Dalle coordinate del centro $x_C = -\frac{a}{2}$ e $y_C = -\frac{b}{2}$ applicate alla retta $s$ ($y = 3x + 2$):
$$-\frac{b}{2} = 3\left(-\frac{a}{2}\right) + 2 \implies b = 3a - 4$$

Sostituiamo $b$ nell'equazione generale della circonferenza:
$$\gamma: x^2 + y^2 + ax + (3a - 4)y + c = 0$$

Imponiamo il passaggio per il punto $P(1, 0)$:
$$1^2 + 0^2 + a(1) + (3a - 4)(0) + c = 0 \implies 1 + a + c = 0 \implies c = -(a + 1)$$

Mettiamo a sistema la circonferenza con la retta tangente $r$ ($y = -2x + 2$):
$$\begin{cases} y = -2x + 2 \\ x^2 + y^2 + ax + (3a - 4)y - (a + 1) = 0 \end{cases}$$

Sostituendo e imponendo la condizione di tangenza ($\Delta = 0$), si ottiene:
$$a = 2$$

Ricaviamo gli altri coefficienti:
- $b = 3(2) - 4 = 2$
- $c = -(2 + 1) = -3$

L'equazione finale della circonferenza è:
$$\boxed{x^2 + y^2 + 2x + 2y - 3 = 0}$$

---

## ⚠️ Errori da evitare
- Dimenticare di verificare la condizione sul codominio/segno quando si estrae la radice quadrata per passare da una funzione irrazionale all'equazione cartesiana di una conica.
- Confondere le condizioni di appartenenza del centro con quelle di tangenza della retta.

---

## Materiale generato

### Riepilogo
- Studio delle funzioni irrazionali riconducibili a semicirconferenze mediante elevamento al quadrato e limitazione del codominio.
- Risoluzione di problemi di tangenza per circonferenze imponendo il passaggio per un punto dato e l'appartenenza del centro a una retta assegnata.

### Esercizi simili
1. Studia e traccia il grafico della funzione $y = -\sqrt{4 - x^2} + 1$.
   <details><summary>Soluzione</summary>Circonferenza di centro $(0, 1)$ e raggio $2$, limitata al ramo inferiore: $y = -\sqrt{4 - x^2} + 1$ con $x \in [-2, 2]$.</details>

2. Trova l'equazione della circonferenza con centro sull'asse $x$ e passante per i punti $A(1, 2)$ e $B(3, 0)$.
   <details><summary>Soluzione</summary>$x^2 + y^2 - 4x - 3 = 0$</details>

3. Determina l'equazione della circonferenza tangente all'asse $y$ nell'origine e con centro sulla retta $y = 2x$.
   <details><summary>Soluzione</summary>$x^2 + y^2 - 4x - 2y = 0$</details>

### Flashcard
- **D:** Qual è il dominio della funzione $y = \sqrt{R^2 - x^2}$? — **R:** $[-R, R]$
- **D:** Come si ricava il centro $C(x_C, y_C)$ dall'equazione $x^2 + y^2 + ax + by + c = 0$? — **R:** $x_C = -\frac{a}{2}$, $y_C = -\frac{b}{2}$
- **D:** Qual è la condizione algebrica di tangenza tra una retta e una circonferenza in un sistema? — **R:** Il discriminante $\Delta$ dell'equazione risolvente deve essere uguale a zero ($\Delta = 0$).
