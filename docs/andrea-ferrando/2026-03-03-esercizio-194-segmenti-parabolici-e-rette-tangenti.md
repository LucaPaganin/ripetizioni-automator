---
titolo: 'Esercizio 194: segmenti parabolici e rette tangenti'
data: '2026-03-03'
studente: Andrea Ferrando
materia: matematica
argomento: 'Geometria analitica: parabola e rette tangenti'
sottoargomenti:
- Parabola
- Fascio proprio di rette
- Condizione di tangenza
- Area del segmento parabolico
esercizi:
- '194'
errori_tipici: []
fonte: https://drive.google.com/file/d/1NPDqQ_Ujh8gUh_01-3LziH0BTGGqPgY8/view?usp=drivesdk
generato: '2026-11-07'
---

# Esercizio 194: segmenti parabolici e rette tangenti

## Formule chiave

- **Equazione della parabola con asse parallelo all'asse $y$:**
  $$y = ax^2 + bx + c$$

- **Fascio proprio di rette passante per un punto $P(x_0, y_0)$:**
  $$y - y_0 = m(x - x_0) \quad \text{oppure} \quad y = mx + q$$

- **Condizione di tangenza tra una retta e una parabola:**
  Si mette a sistema la retta e la parabola, ottenendo un'equazione di secondo grado. La condizione di tangenza impone che il discriminante sia nullo:
  $$\Delta = 0$$

- **Area del segmento parabolico (Teorema di Archimede):**
  L'area compresa tra una parabola e una retta secante è data da:
  $$\text{Area} = \frac{2}{3} \cdot \text{Area del triangolo circoscritto}$$
  (il triangolo formato dalla corda e dalle tangenti nei suoi estremi), oppure in funzione delle ascisse $x_1$ e $x_2$ dei punti di intersezione tra parabola e retta secante:
  $$\text{Area} = \frac{|a|}{6} (x_2 - x_1)^3$$

---

## Esercizio 194

Dati la parabola $\gamma$ e il punto $P$:
$$\gamma: y = x^2$$
$$P(0, -1)$$

Si vuole determinare l'equazione del fascio di rette passante per $P$:
$$F: y = mx + q$$

Imponendo il passaggio per il punto $P(0, -1)$:
$$-1 = m \cdot 0 + q \implies q = -1$$

L'equazione del fascio diventa:
$$F: y = mx - 1$$

Mettiamo a sistema il fascio di rette con la parabola $\gamma$:
$$\begin{cases} y = mx - 1 \\ y = x^2 \end{cases}$$

Sostituendo la prima nell'equazione della parabola:
$$x^2 = mx - 1 \implies x^2 - mx + 1 = 0$$

Calcoliamo il discriminante $\Delta$ dell'equazione di secondo grado:
$$\Delta = m^2 - 4 = (m - 2)(m + 2)$$

Imponendo la condizione di tangenza ($\Delta = 0$), troviamo i valori del coefficiente angolare $m$:
- Se $m = -2$, otteniamo la prima retta tangente $t_1$:
  $$t_1: y = -2x - 1$$
- Se $m = 2$, otteniamo la seconda retta tangente $t_2$:
  $$t_2: y = 2x - 1$$

### Intersezioni e punti di tangenza

- **Intersezione $t_1 \cap \gamma$:**
  $$\begin{cases} y = -2x - 1 \\ y = x^2 \end{cases} \implies x^2 + 2x + 1 = 0 \implies (x + 1)^2 = 0 \implies x = -1$$
  Sostituendo $x = -1$ si ottiene $y = 1$. Il punto di tangenza è $P_1(-1, 1)$.

- **Intersezione $t_2 \cap \gamma$:**
  $$\begin{cases} y = 2x - 1 \\ y = x^2 \end{cases} \implies x^2 - 2x + 1 = 0 \implies (x - 1)^2 = 0 \implies x = 1$$
  Sostituendo $x = 1$ si ottiene $y = 1$. Il punto di tangenza è $P_2(1, 1)$.

### Calcolo delle aree

Negli appunti vengono calcolate le seguenti aree geometriche relative ai punti $O(0,0)$, $P_1(-1,1)$, $P_2(1,1)$ e $P(0,-1)$:

- $\text{Area}(P_1 O P_2) = 1$
- $\text{Area}(P_1 \hat{O} P_2) = \frac{4}{3}$
- $\text{Area}(P_1 \hat{P} P_2) = \frac{1}{2} \cdot 2 \cdot 2 = 2$

Richiesta finale (area del segmento parabolico delimitato dalle tangenti):
$$\text{Area}(P_1 \hat{P} P_2) - \text{Area}(P_1 \hat{O} P_2) = 2 - \frac{4}{3} = \frac{2}{3}$$

---

## ⚠️ Errori da evitare

Nessun errore segnalato negli appunti.

---
## Materiale generato

### Riepilogo
Risoluzione di un problema di geometria analitica con una parabola e le rette tangenti condotte da un punto esterno. Vengono determinati i punti di tangenza e calcolata l'area del segmento parabolico tramite differenze di aree geometriche.

### Esercizi simili

1. Data la parabola $y = x^2$ e il punto $P(0, -4)$, trova le rette tangenti alla parabola passanti per $P$ e l'area del segmento parabolico delimitato dalle tangenti.
   <details><summary>Soluzione</summary>
   Fascio passante per $P(0,-4)$: $y = mx - 4$.
   Sistema con la parabola: $x^2 - mx + 4 = 0 \implies \Delta = m^2 - 16 = 0 \implies m = \pm 4$.
   Rette tangenti: $t_1: y = 4x - 4$, $t_2: y = -4x - 4$.
   Punti di tangenza: $P_1(2, 4)$ e $P_2(-2, 4)$.
   Come nell'esercizio 194: triangolo $P_1 P P_2$ con base $4$ e altezza $8$, area $16$; segmento parabolico tra $y = x^2$ e $y = 4$: $\frac{1}{6}\cdot 4^3 = \frac{32}{3}$.
   Area delimitata dalle tangenti e dalla parabola: $16 - \frac{32}{3} = \boxed{\frac{16}{3}}$.
   </details>

2. Data la parabola $y = \frac{1}{2}x^2$ e il punto $P(0, -2)$, calcola le equazioni delle rette tangenti condotte da $P$.
   <details><summary>Soluzione</summary>
   Fascio passante per $P(0,-2)$: $y = mx - 2$.
   Sistema: $\frac{1}{2}x^2 - mx + 2 = 0 \implies x^2 - 2mx + 4 = 0$.
   $\Delta = 4m^2 - 16 = 0 \implies m = \pm 2$.
   Rette tangenti: $y = 2x - 2$ e $y = -2x - 2$.
   </details>

3. Trova l'area del segmento parabolico delimitato dalla parabola $y = x^2$ e dalla retta secante $y = 4$.
   <details><summary>Soluzione</summary>
   Mettendo a sistema $y = x^2$ e $y = 4$ si trovano i punti di intersezione di ascissa $x_1 = -2$ e $x_2 = 2$.
   Applicando la formula di Archimede: $\text{Area} = \frac{|1|}{6}(2 - (-2))^3 = \frac{1}{6}(64) = \frac{32}{3}$.
   </details>

### Flashcard
- **D:** Qual è la condizione algebrica affinché una retta sia tangente a una parabola? — **R:** Il discriminante $\Delta$ dell'equazione risolvente del sistema deve essere uguale a zero ($\Delta = 0$).
- **D:** Come si scrive l'equazione di un fascio proprio di rette passante per un punto $P(0, q)$ sull'asse $y$? — **R:** $y = mx + q$, dove $q$ è l'ordinata del punto $P$.
- **D:** Cosa esprime il Teorema di Archimede per il segmento parabolico? — **R:** L'area racchiusa tra una parabola e una retta secante è i $\frac{2}{3}$ dell'area del triangolo circoscritto avente per vertici i punti di tangenza/intersezione e il vertice della parabola (o l'intersezione delle tangenti).
