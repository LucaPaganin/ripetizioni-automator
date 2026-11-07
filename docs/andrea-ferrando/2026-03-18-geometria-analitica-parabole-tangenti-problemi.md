---
titolo: 'Geometria analitica: parabole, tangenti e problemi con rettangoli iscritti'
data: '2026-03-18'
studente: Andrea Ferrando
materia: matematica
argomento: Geometria analitica nel piano cartesiano
sottoargomenti:
- Parabola
- Rette tangenti a una parabola
- Aree di regioni mistilinee
- Problemi di iscrizione (rettangoli e quadrati)
esercizi:
- '5'
- '6'
errori_tipici:
- Non considerare il valore assoluto o le condizioni di accettabilità (es. $d > 0$)
  per i parametri geometrici.
- Confondere i punti di intersezione delle tangenti con gli estremi dei segmenti parabolici.
fonte: https://drive.google.com/file/d/1DB4QU0p8d9eLjYffWPVTVvp2LWCs50pQ/view?usp=drivesdk
generato: '2026-11-07'
---

# Geometria analitica: parabole, tangenti e problemi con rettangoli iscritti

## Formule chiave

- **Equazione della retta passante per un punto $(x_0, y_0)$**:
  $$y - y_0 = m(x - x_0)$$

- **Condizione di tangenza**: Messa a sistema l'equazione della retta con quella della parabola, si impone che il discriminante dell'equazione risolvente sia nullo ($\Delta = 0$).

- **Teorema di Archimede per il segmento parabolico**: L'area racchiusa da un arco di parabola e una secante è pari a $\frac{4}{3}$ dell'area del triangolo inscritto che ha per vertici gli estremi del segmento parabolico e il punto della parabola in cui la tangente è parallela alla secante.

---

## Esercizio 5

### Testo
Data la parabola $y = x^2$, la retta $t$ tangente alla parabola nel punto $B(2,4)$ e la retta passante per $D(-1,1)$ e $V(0,0)$ si intersecano nel punto $A$. Determina l'area della zona colorata (triangolo mistilineo $VBA$), facendo opportune considerazioni.

### Svolgimento

1. **Equazione della retta passante per $V(0,0)$ e $D(-1,1)$**:
   Utilizziamo la formula del fascio passante per l'origine o retta per due punti:
   $$y - y_0 = \frac{y_1 - y_0}{x_1 - x_0}(x - x_0)$$
   Sostituendo $V(0,0)$ e $D(-1,1)$:
   $$y - 0 = \frac{1 - 0}{-1 - 0}(x - 0) \implies y = -x$$

2. **Equazione della tangente $t$ alla parabola passante per $B(2,4)$**:
   Consideriamo il fascio di rette per $B(2,4)$:
   $$y - 4 = m(x - 2) \implies y = mx + 4 - 2m$$
   Mettiamo a sistema con la parabola $y = x^2$:
   $$\begin{cases} y = mx + 4 - 2m \\ y = x^2 \end{cases} \implies x^2 - mx - 4 + 2m = 0$$
   Imponiamo $\Delta = 0$:
   $$\Delta = m^2 - 4(1)(-4 + 2m) = m^2 + 16 - 8m = (m - 4)^2 = 0 \implies m = 4$$
   Quindi la retta tangente è:
   $$t: y = 4x - 4$$

3. **Intersezione tra $t$ e la retta passante per $D$ e $V$**:
   $$\begin{cases} y = 4x - 4 \\ y = -x \end{cases} \implies -x = 4x - 4 \implies 5x = 4 \implies x = \frac{4}{5}, \; y = -\frac{4}{5}$$
   Otteniamo il punto di intersezione $A\left(\frac{4}{5}, -\frac{4}{5}\right)$.

4. **Calcolo delle aree**:
   - Area del triangolo formato da $C(0,4)$, $V(0,0)$ e $B(2,4)$:
     $$\text{Area}(CVB) = \frac{1}{2} \cdot \text{base} \cdot \text{altezza} = \frac{1}{2} \cdot 4 \cdot 2 = 4$$
   - Applicando il teorema di Archimede (il triangolo $CVB$ è metà del triangolo inscritto nel segmento parabolico tagliato da $y = 4$), l'area tra la parabola, l'asse $y$ e la retta $y = 4$ è:
     $$\text{Area} = \frac{4}{3} \cdot 4 = \frac{16}{3}$$
   - Sia $E(1, 0)$ l'intersezione della tangente $t$ con l'asse $x$. Area del trapezio $VCBE$ (basi $\overline{VE} = 1$ e $\overline{CB} = 2$, altezza $4$):
     $$\text{Area} = \frac{(b + B) \cdot h}{2} = \frac{(1 + 2) \cdot 4}{2} = 6$$
   - Sottraendo l'area del segmento parabolico dall'area del trapezio si ottiene la prima parte dell'area mistilinea:
     $$\text{Area}_1 = 6 - \frac{16}{3} = \frac{2}{3}$$
   - La seconda parte ($\text{Area}_2$ corrispondente al triangolo $VEA$):
     $$\text{Area}_2 = \frac{1}{2} \cdot 1 \cdot \frac{4}{5} = \frac{2}{5}$$
   - **Area finale**:
     $$\text{Area}_{\text{tot}} = \frac{2}{3} + \frac{2}{5} = \frac{10 + 6}{15} = \boxed{\frac{16}{15}}$$

---

## Esercizio 6

### Testo
Il rettangolo $ABCD$ in figura è iscritto nelle due parabole. I lati del rettangolo sono paralleli agli assi cartesiani, e $\overline{AD} = 3\overline{AB}$. Determina l'area del rettangolo.

### Svolgimento

1. **Ricaviamo le equazioni delle parabole dal grafico**:
   - La parabola inferiore $\gamma_1: y = x^2 - 4$ (concavità verso l'alto, vertice in $(0,-4)$).
   - La parabola superiore $\gamma_2: y = -x^2 + 4$ (concavità verso il basso, vertice in $(0,4)$).

2. **Coordinate dei vertici del rettangolo**:
   Per simmetria rispetto all'asse $y$, poniamo l'ascissa del vertice $A$ pari a $d$ ($d > 0$).
   - $A(d, -d^2 + 4)$ appartenente a $\gamma_2$ (oppure impostando le coordinate generali simmetriche).
   - $B(-d, -d^2 + 4)$
   - $C(-d, d^2 - 4)$ appartenente a $\gamma_1$
   - $D(d, d^2 - 4)$ appartenente a $\gamma_1$

3. **Lunghezza dei lati**:
   - $\overline{AB} = 2d$
   - $\overline{AD} = y_A - y_D = (-d^2 + 4) - (d^2 - 4) = 8 - 2d^2$

4. **Impostazione della condizione del problema**:
   Sappiamo che $\overline{AD} = 3\overline{AB}$:
   $$8 - 2d^2 = 3(2d) \implies 8 - 2d^2 = 6d$$
   Riordinando l'equazione:
   $$2d^2 + 6d - 8 = 0 \implies d^2 + 3d - 4 = 0$$
   Scomponendo in fattori:
   $$(d + 4)(d - 1) = 0$$
   Le soluzioni sono $d = -4$ (da scartare perché $d > 0$) e $d = 1$.

5. **Calcolo dell'area**:
   Per $d = 1$:
   - $\overline{AB} = 2(1) = 2$
   - $\overline{AD} = 8 - 2(1)^2 = 6$
   - $\text{Area}(ABCD) = \overline{AB} \cdot \overline{AD} = 2 \cdot 6 = \boxed{12}$

---

## ⚠️ Errori da evitare
- Dimenticare di escludere le soluzioni negative nei parametri geometrici che rappresentano lunghezze o ascisse positive (es. $d = -4$ scartato).
- Confondere le intersezioni tra rette e curve nei calcoli algebrici dei sistemi.

---

## Materiale generato

### Riepilogo
Lo studio delle parabole nel piano cartesiano richiede la determinazione accurata delle intersezioni, l'uso delle condizioni di tangenza ($\Delta = 0$) e l'impostazione geometrica dei problemi con parametrici vincolati da relazioni di misura tra i lati.

### Esercizi simili

1. Data la parabola $y = x^2 - 1$ e il punto $P(2, 3)$, trova l'equazione della retta tangente passante per $P$ e verifica la validità della condizione di tangenza.
   <details><summary>Soluzione</summary>$y = 4x - 5$</details>

2. Calcola l'area della regione finita di piano delimitata dalla parabola $y = -x^2 + 4$ e dall'asse $x$.
   <details><summary>Soluzione</summary>$\frac{32}{3}$</details>

3. Un rettangolo con i lati paralleli agli assi è inscritto tra le parabole $y = x^2 - 3$ e $y = -x^2 + 3$. Sapendo che la base è la metà dell'altezza, determina l'area del rettangolo.
   <details><summary>Soluzione</summary>Con vertici di ascissa $\pm d$: base $2d$, altezza $6 - 2d^2$. Da $2d = \frac{6 - 2d^2}{2}$ si ottiene $d^2 + 2d - 3 = 0 \implies d = 1$ ($d = -3$ non accettabile). Base $2$, altezza $4$, area $\boxed{8}$.</details>

### Flashcard
- **D:** Come si impone la condizione di tangenza tra una retta e una parabola? — **R:** Si mette a sistema l'equazione della retta con quella della parabola e si pone il discriminante $\Delta = 0$ dell'equazione risolvente.
- **D:** Qual è la formula del fascio di rette passante per un punto $(x_0, y_0)$? — **R:** $y - y_0 = m(x - x_0)$
- **D:** A cosa equivale l'area di un segmento parabolico secondo Archimede? — **R:** A $\frac{4}{3}$ dell'area del triangolo inscritto con vertici gli estremi dell'arco e il punto di tangenza parallelo alla corda.
