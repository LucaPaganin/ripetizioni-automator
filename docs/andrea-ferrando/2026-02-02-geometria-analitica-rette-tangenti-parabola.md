---
titolo: 'Geometria analitica: rette tangenti a una parabola e area del triangolo'
data: '2026-02-02'
studente: Andrea Ferrando
materia: matematica
argomento: Geometria analitica
sottoargomenti:
- Parabola
- Fascio di rette
- Condizione di tangenza
- Intersezione tra rette e area di un triangolo
esercizi:
- 1
errori_tipici: []
fonte: https://drive.google.com/file/d/1Lt3Jq9kGSVG8sNtHt4V6o4GWNSCZL6Z9/view?usp=drivesdk
generato: '2026-11-07'
---

# Geometria analitica: rette tangenti a una parabola e area del triangolo

## Formule chiave

- **Equazione della parabola con asse parallelo all'asse $y$:**
  $$y = ax^2 + bx + c$$

- **Coordinate del vertice $V$:**
  $$x_V = -\frac{b}{2a}, \quad y_V = -\frac{\Delta}{4a}$$

- **Fascio di rette passante per un punto $P(x_0, y_0)$:**
  $$y - y_0 = m(x - x_0)$$
  oppure, in forma esplicita conoscendo $q = y_0 - mx_0$:
  $$y = mx + q$$

- **Condizione di tangenza:**
  Per determinare la retta tangente a una parabola in un suo punto, si mette a sistema l'equazione della parabola e l'equazione del fascio di rette passante per quel punto. Sostituendo si ottiene un'equazione di secondo grado in $x$ (o $y$); la condizione di tangenza impone che il discriminante sia nullo:
  $$\Delta = 0$$

- **Area di un triangolo rettangolo:**
  Dati i cateti $c_1$ e $c_2$:
  $$\text{Area} = \frac{c_1 \cdot c_2}{2}$$

---

## Esercizio 1

**Testo:**
Determinare l'equazione delle rette tangenti alla parabola di equazione $y = x^2 - 3x + 2$ nei punti di intersezione della parabola stessa con gli assi cartesiani. Trovare inoltre l'area del triangolo individuato da tali rette.

### Svolgimento

#### 1. Studio della parabola e intersezioni con gli assi cartesiani

Data la parabola:
$$y = x^2 - 3x + 2 \quad (a = 1, \, b = -3, \, c = 2)$$

* **Vertice $V$:**
  $$x_V = -\frac{b}{2a} = -\frac{-3}{2(1)} = \frac{3}{2}$$
  $$y_V = \frac{-\Delta}{4a} = \frac{-(b^2 - 4ac)}{4a} = \frac{-(9 - 8)}{4} = -\frac{1}{4}$$
  $$V\left(\frac{3}{2}, -\frac{1}{4}\right)$$

* **Intersezioni con l'asse $x$ ($y = 0$):**
  $$\begin{cases} y = 0 \\ y = x^2 - 3x + 2 \end{cases} \implies x^2 - 3x + 2 = 0$$
  Formula risolutiva:
  $$x = \frac{3 \pm \sqrt{9 - 8}}{2} = \frac{3 \pm 1}{2}$$
  Si ottengono i punti:
  $$A(1, 0) \quad \text{e} \quad B(2, 0)$$

* **Intersezioni con l'asse $y$ ($x = 0$):**
  $$\begin{cases} x = 0 \\ y = 0^2 - 3(0) + 2 \end{cases} \implies y = 2$$
  Si ottiene il punto:
  $$C(0, 2)$$

---

#### 2. Tangente in $A(1, 0)$
Consideriamo il fascio di rette passante per $A(1, 0)$:
$$y = mx + q$$
Imponendo il passaggio per $A(1, 0)$:
$$0 = m(1) + q \implies q = -m \implies r: y = mx - m$$

Mettiamo a sistema con la parabola per imporre la tangenza ($\Delta = 0$):
$$\begin{cases} y = mx - m \\ y = x^2 - 3x + 2 \end{cases} \implies mx - m = x^2 - 3x + 2$$
$$x^2 - 3x - mx + 2 + m = 0$$
$$x^2 - (3 + m)x + (m + 2) = 0$$

Calcoliamo il discriminante $\Delta$:
$$\Delta = (3 + m)^2 - 4(1)(m + 2) = m^2 + 6m + 9 - 4m - 8 = m^2 + 2m + 1 = (m + 1)^2$$

Imponiamo $\Delta = 0$:
$$(m + 1)^2 = 0 \implies m = -1$$

Sostituendo $m = -1$ nell'equazione del fascio si ottiene la retta $r$:
$$\mathbf{r: y = -x + 1}$$

---

#### 3. Tangente in $B(2, 0)$
Consideriamo il fascio di rette passante per $B(2, 0)$:
$$y = mx + q$$
Imponendo il passaggio per $B(2, 0)$:
$$0 = 2m + q \implies q = -2m \implies s: y = mx - 2m$$

Mettiamo a sistema con la parabola:
$$mx - 2m = x^2 - 3x + 2 \implies x^2 - 3x - mx + 2 + 2m = 0$$
$$x^2 - (3 + m)x + (2 + 2m) = 0$$

Calcoliamo $\Delta$:
$$\Delta = (3 + m)^2 - 4(1)(2 + 2m) = m^2 + 6m + 9 - 8 - 8m = m^2 - 2m + 1 = (m - 1)^2$$

Imponiamo $\Delta = 0$:
$$(m - 1)^2 = 0 \implies m = 1$$

Sostituendo $m = 1$:
$$\mathbf{s: y = x - 2}$$

---

#### 4. Tangente in $C(0, 2)$
Consideriamo il fascio di rette passante per $C(0, 2)$ ($q = 2$):
$$t: y = mx + 2$$

Mettiamo a sistema con la parabola:
$$mx + 2 = x^2 - 3x + 2 \implies x^2 - 3x - mx = 0 \implies x^2 - (3 + m)x = 0$$

Calcoliamo $\Delta$:
$$\Delta = (3 + m)^2 - 4(1)(0) = (3 + m)^2$$

Imponiamo $\Delta = 0$:
$$(3 + m)^2 = 0 \implies m = -3$$

Sostituendo $m = -3$:
$$\mathbf{t: y = -3x + 2}$$

---

#### 5. Calcolo dell'area del triangolo individuato dalle tre rette

Le tre rette tangenti sono:
- $r: y = -x + 1$ (pendenza $-1$)
- $s: y = x - 2$ (pendenza $+1$)
- $t: y = -3x + 2$ (pendenza $-3$)

Notiamo che i coefficienti angolari di $r$ e $s$ sono $m_r = -1$ e $m_s = 1$. Essendo $m_r \cdot m_s = -1$, le rette $r$ ed $s$ sono **perpendicolari** tra loro. Pertanto il triangolo formato dalle tre rette è un triangolo rettangolo, in cui i cateti giacciono sulle rette $r$ ed $s$.

Troviamo i vertici del triangolo intersecando le rette a due a due:
1. **Intersezione tra $r$ e $s$:**
   $$\begin{cases} y = -x + 1 \\ y = x - 2 \end{cases} \implies -x + 1 = x - 2 \implies 2x = 3 \implies x = \frac{3}{2}$$
   $y = \frac{3}{2} - 2 = -\frac{1}{2}$
   Punto $P_1\left(\frac{3}{2}, -\frac{1}{2}\right)$

2. **Intersezione tra $r$ e $t$:**
   $$\begin{cases} y = -x + 1 \\ y = -3x + 2 \end{cases} \implies -x + 1 = -3x + 2 \implies 2x = 1 \implies x = \frac{1}{2}$$
   $y = -\frac{1}{2} + 1 = \frac{1}{2}$
   Punto $P_2\left(\frac{1}{2}, \frac{1}{2}\right)$

3. **Intersezione tra $s$ e $t$:**
   $$\begin{cases} y = x - 2 \\ y = -3x + 2 \end{cases} \implies x - 2 = -3x + 2 \implies 4x = 4 \implies x = 1$$
   $y = 1 - 2 = -1$
   Punto $P_3(1, -1)$

Calcoliamo le lunghezze dei due cateti (distanza tra $P_1$ e $P_2$ per il primo, e tra $P_1$ e $P_3$ per il secondo):
- Cateto $c_1$ (tra $P_1$ e $P_2$):
  $$c_1 = \sqrt{\left(\frac{3}{2} - \frac{1}{2}\right)^2 + \left(-\frac{1}{2} - \frac{1}{2}\right)^2} = \sqrt{1^2 + (-1)^2} = \sqrt{2}$$

- Cateto $c_2$ (tra $P_1$ e $P_3$):
  $$c_2 = \sqrt{\left(\frac{3}{2} - 1\right)^2 + \left(-\frac{1}{2} - (-1)\right)^2} = \sqrt{\left(\frac{1}{2}\right)^2 + \left(\frac{1}{2}\right)^2} = \sqrt{\frac{1}{4} + \frac{1}{4}} = \sqrt{\frac{1}{2}} = \frac{\sqrt{2}}{2}$$

Calcoliamo l'area:
$$\text{Area} = \frac{c_1 \cdot c_2}{2} = \frac{\sqrt{2} \cdot \frac{\sqrt{2}}{2}}{2} = \frac{1}{2}$$

$$\boxed{\text{Area} = \frac{1}{2}}$$

---

---

## Materiale generato

### Riepilogo
La lezione spiega come determinare le rette tangenti a una parabola nei suoi punti di intersezione con gli assi cartesiani utilizzando il metodo del fascio di rette e l'annullamento del discriminante ($\Delta = 0$). Infine, viene calcolata l'area del triangolo formato dalle rette intersecanti sfruttando la perpendicolarità tra i lati.

### Esercizi simili
1. Trovare l'equazione della retta tangente alla parabola $y = x^2 - 4x + 3$ nel suo punto di intersezione con l'asse $y$ e calcolarne la distanza dal vertice.
   <details><summary>Soluzione</summary>L'intersezione con l'asse $y$ è $P(0, 3)$. Il fascio per $P$ è $y = mx + 3$. Mettendo a sistema con la parabola si ottiene $x^2 - (4+m)x = 0$. Ponendo $\Delta = 0$ si ha $(4+m)^2 = 0 \implies m = -4$. La retta tangente è $\mathbf{y = -4x + 3}$.</details>

2. Data la parabola $y = -x^2 + 5x - 6$, determinare le equazioni delle rette tangenti condotte nei punti di intersezione con l'asse $x$.
   <details><summary>Soluzione</summary>Le intersezioni con l'asse $x$ sono $A(2, 0)$ e $B(3, 0)$. Applicando i fasci e ponendo $\Delta = 0$, le tangenti sono $y = x - 2$ (in $A$) e $y = -x + 3$ (in $B$).</details>

3. Trovare l'equazione della retta tangente alla parabola $y = x^2 - 2x$ nel punto di ascissa $x = 3$.
   <details><summary>Soluzione</summary>Per $x = 3$, $y = 3^2 - 2(3) = 3$, quindi il punto di tangenza è $P(3, 3)$. Il fascio passante per $P$ è $y - 3 = m(x - 3) \implies y = mx - 3m + 3$. Mettendo a sistema con la parabola e ponendo $\Delta = 0$, si trova $m = 4$. La retta tangente è $\mathbf{y = 4x - 9}$.</details>

### Flashcard
- **D:** Come si impone la condizione di tangenza tra una retta e una parabola? — **R:** Si mette a sistema l'equazione della parabola e l'equazione del fascio di rette, ottenendo un'equazione di secondo grado, e si pone il discriminante $\Delta = 0$.
- **D:** Qual è la formula del vertice di una parabola $y = ax^2 + bx + c$? — **R:** $V\left(-\frac{b}{2a}, -\frac{\Delta}{4a}\right)$.
- **D:** Come si calcola l'area di un triangolo rettangolo dati i cateti $c_1$ e $c_2$? — **R:** $\text{Area} = \frac{c_1 \cdot c_2}{2}$.
