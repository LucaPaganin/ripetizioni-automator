---
titolo: Dinamica del punto materiale e del corpo rigido
data: '2026-02-20'
studente: Andrea Ferrando
materia: fisica
argomento: Dinamica rotazionale
sottoargomenti:
- Seconda legge di Newton
- Momento meccanico
- Momento d'inerzia
- Moto rotatorio uniformemente accelerato
esercizi:
- '22'
errori_tipici:
- Confondere la dinamica lineare con quella rotazionale
- Applicare le formule del moto rotatorio partendo da velocità iniziale nulla quando
  il testo specifica che il corpo è già in moto
fonte: https://drive.google.com/file/d/1Nr29bCSKQY49t08mEneoff-cgJ04WorM/view?usp=drivesdk
generato: '2026-11-07'
---

# Dinamica del punto materiale e del corpo rigido

## Formule chiave

### Dinamica lineare (traslazionale)
- Seconda legge di Newton:
  $$\vec{F} = m\vec{a}$$
- Quantità di moto:
  $$\vec{p} = m\vec{v}$$
- Impulso della forza:
  $$\vec{I} = \Delta\vec{p} = \vec{F} \Delta t$$
- Condizione di moto rettilineo uniforme:
  $$\text{Se }\vec{F} = 0 \implies \vec{a} = 0 \implies \vec{v} = \text{cost}, \quad \vec{p} = \text{cost}$$

---

### Dinamica rotazionale (parallelismi)

| Lineare | Rotazionale |
| :--- | :--- |
| $\vec{F}$ (forza risultante) | $\vec{M}$ (momento risultante) |
| $m$ (massa / inerzia) | $I$ (momento d'inerzia) |
| $\vec{a}$ (accelerazione) | $\vec{\alpha}$ (accelerazione angolare) |
| $\vec{p} = m\vec{v}$ (quantità di moto) | $\vec{L} = I\vec{\omega}$ (momento angolare) |
| $\vec{v}$ (velocità lineare) | $\vec{\omega}$ (velocità angolare) |

*Nota: La relazione $\vec{L} = I\vec{\omega}$ vale quando la rotazione avviene attorno ad un asse di simmetria.*

---

### Definizione di momento meccanico (o momento di una forza)
$$\vec{M} = \vec{r} \wedge \vec{F}$$
In modulo:
$$|\vec{M}| = r F \sin\theta$$

Casi particolari per l'angolo $\theta$:
- Se $\theta = 0^\circ \implies \sin(0^\circ) = 0 \implies |\vec{M}| = 0$
- Se $\theta = 90^\circ \implies \sin(90^\circ) = 1 \implies |\vec{M}| = r F$

Relazione fondamentale della dinamica rotazionale:
$$\vec{M} = I \vec{\alpha}$$

Per un guscio cilindrico sottile, il momento d'inerzia rispetto all'asse di simmetria è:
$$I = m r^2$$

---

## Esercizio 22

**Testo del problema (tratto dagli appunti):**
Un guscio cilindrico, di raggio $16\text{ cm}$ e massa $12\text{ kg}$, è applicata una forza di $6.0\text{ N}$ in un punto del bordo del cilindro e giacente su un piano ortogonale all'asse del cilindro in modo da formare un angolo di $61^\circ$ con il raggio. La forza agisce per un tempo di $2.0\text{ s}$ e durante questo tempo causa una rotazione del cilindro di $15$ giri attorno al suo asse.
- Calcola la velocità angolare del cilindro nell'istante in cui la forza ha cessato di agire. [Risultato: $50\text{ rad/s}$]

### Svolgimento

Dati del problema:
- Raggio: $r = 16\text{ cm} = 0.16\text{ m}$
- Massa: $m = 12\text{ kg}$
- Forza: $F = 6.0\text{ N}$
- Angolo: $\theta = 61^\circ$
- Intervallo di tempo: $\Delta t = 2.0\text{ s}$
- Spostamento angolare: $\varphi_f = 15\text{ giri} = 15 \cdot 360^\circ = 15 \cdot 2\pi\text{ rad} = 30\pi\text{ rad}$

Momento d'inerzia del guscio cilindrico:
$$I = m r^2$$

Modulo del momento della forza:
$$M = r F \sin\theta$$

Dalla legge fondamentale della dinamica rotazionale $M = I \alpha$:
$$r F \sin\theta = m r^2 \alpha \implies \alpha = \frac{r F \sin\theta}{m r^2} = \frac{F \sin\theta}{m r}$$

Il moto angolare è uniformemente accelerato:
$$\begin{cases}
\varphi(t) = \varphi_0 + \omega_0 t + \frac{1}{2}\alpha t^2 \\
\omega(t) = \omega_0 + \alpha t
\end{cases}$$

Poiché il cilindro è già in moto iniziale ($\omega_0 \neq 0$), ricaviamo $\omega_0$ mettendo a sistema le informazioni note. Dalla prima equazione (ponendo $\varphi_0 = 0$):
$$\varphi_f = \omega_0 \Delta t + \frac{1}{2}\alpha \Delta t^2 \implies \omega_0 = \frac{\varphi_f - \frac{1}{2}\alpha \Delta t^2}{\Delta t}$$

Sostituendo nell'espressione della velocità finale $\omega_f = \omega_0 + \alpha \Delta t$:
$$\omega_f = \frac{\varphi_f - \frac{1}{2}\alpha \Delta t^2}{\Delta t} + \alpha \Delta t = \frac{\varphi_f + \frac{1}{2}\alpha \Delta t^2}{\Delta t}$$

Sostituendo i valori numerici si perviene al risultato atteso:
$$\omega_f = \boxed{50\text{ rad/s}}$$

---

## ⚠️ Errori da evitare
- Dimenticare che il modulo del momento meccanico dipende dal seno dell'angolo ($|\vec{M}| = r F \sin\theta$); se la forza è radiale ($\theta = 0^\circ$), il momento è nullo.
- Assumere che la velocità angolare iniziale $\omega_0$ sia sempre nulla: in presenza di corpi già in movimento, bisogna considerare l'intera equazione cinematica del moto rotatorio uniformemente accelerato.

---

## Materiale generato

### Riepilogo
La dinamica rotazionale specchia quella traslazionale: la forza diventa il momento meccanico ($\vec{M}$), la massa inerziale diventa il momento d'inerzia ($I$), e l'accelerazione lineare diventa quella angolare ($\vec{\alpha}$). Nei problemi con corpi estesi, l'uso combinato delle leggi di Newton per la rotazione e delle equazioni cinematiche angolari permette di risolvere moti uniformemente accelerati.

### Esercizi simili

1. Un disco uniforme di massa $m = 4.0\text{ kg}$ e raggio $r = 0.5\text{ m}$ (con momento d'inerzia $I = \frac{1}{2}mr^2$) è inizialmente fermo. Viene applicata una forza tangenziale di $10\text{ N}$ al bordo per un tempo $\Delta t = 3.0\text{ s}$. Calcola la velocità angolare finale del disco.
   <details><summary>Soluzione</summary>
   Il momento della forza è $M = rF$ (essendo $\theta = 90^\circ$). 
   $M = 0.5 \cdot 10 = 5\text{ N}\cdot\text{m}$.
   Il momento d'inerzia è $I = \frac{1}{2} \cdot 4.0 \cdot (0.5)^2 = 0.5\text{ kg}\cdot\text{m}^2$.
   L'accelerazione angolare è $\alpha = \frac{M}{I} = \frac{5}{0.5} = 10\text{ rad/s}^2$.
   La velocità angolare finale è $\omega_f = \omega_0 + \alpha \Delta t = 0 + 10 \cdot 3.0 = \mathbf{30\text{ rad/s}}$.
   </details>

2. Un'asta sottile e rigida di massa $m = 2.0\text{ kg}$ e lunghezza $L = 1.2\text{ m}$, imperniata a un estremo (momento d'inerzia $I = \frac{1}{3}mL^2$), è soggetta a un momento torcente risultante costante di $4.8\text{ N}\cdot\text{m}$. Calcola l'accelerazione angolare dell'asta.
   <details><summary>Soluzione</summary>
   Il momento d'inerzia è $I = \frac{1}{3} \cdot 2.0 \cdot (1.2)^2 = \frac{1}{3} \cdot 2.0 \cdot 1.44 = 0.96\text{ kg}\cdot\text{m}^2$.
   Dalla legge $\alpha = \frac{M}{I}$:
   $\alpha = \frac{4.8}{0.96} = \mathbf{5.0\text{ rad/s}^2}$.
   </details>

3. Una trottola cilindrica omogenea di massa $m = 0.5\text{ kg}$ e raggio $r = 0.1\text{ m}$ ruota attorno al suo asse di simmetria con un momento d'inerzia $I = \frac{1}{2}mr^2$. Se viene frenata da un momento d'attrito costante di $0.05\text{ N}\cdot\text{m}$, in quanto tempo $\Delta t$ si ferma partendo da una velocità angolare $\omega_0 = 20\text{ rad/s}$?
   <details><summary>Soluzione</summary>
   $I = \frac{1}{2} \cdot 0.5 \cdot (0.1)^2 = 0.0025\text{ kg}\cdot\text{m}^2$.
   L'accelerazione angolare (in questo caso frenante) è $\alpha = \frac{-M}{I} = \frac{-0.05}{0.0025} = -20\text{ rad/s}^2$.
   Dalla legge $\omega_f = \omega_0 + \alpha \Delta t$:
   $0 = 20 - 20\Delta t \implies \Delta t = \mathbf{1.0\text{ s}}$.
   </details>

### Flashcard
- **D:** Qual è l'analogo rotazionale della massa (inerzia) nella dinamica traslazionale? — **R:** Il momento d'inerzia ($I$).
- **D:** Qual è la formula vettoriale del momento meccanico generato da una forza $\vec{F}$ applicata a distanza $\vec{r}$ dal polo? — **R:** $\vec{M} = \vec{r} \wedge \vec{F}$.
- **D:** Quando il momento di una forza è massimo rispetto a un punto di applicazione? — **R:** Quando la forza è perpendicolare al braccio ($\theta = 90^\circ$), poiché $\sin(90^\circ) = 1$.
- **D:** Qual è l'espressione del momento d'inerzia di un guscio cilindrico sottile di massa $m$ e raggio $r$ attorno al proprio asse? — **R:** $I = m r^2$.
- **D:** Come si esprime la seconda legge di Newton applicata alla rotazione di un corpo rigido? — **R:** $\vec{M} = I \vec{\alpha}$.
