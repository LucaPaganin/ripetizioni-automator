---
titolo: 'Urti in 1D e 2D: Conservazione della Quantità di Moto ed Energia Cinetica'
data: '2026-01-21'
studente: Andrea Ferrando
materia: fisica
argomento: Dinamica e Urti
sottoargomenti:
- Urti anaelastici in 1D
- Urti elastici in 2D
- Conservazione della quantità di moto
- Dissipazione di energia cinetica
esercizi: []
errori_tipici: []
fonte: https://drive.google.com/file/d/1nwHk75IE5llvY8NZkPlIs_V4DFlQMyK-/view?usp=drivesdk
generato: '2026-11-07'
---

# Urti in 1D e 2D: Conservazione della Quantità di Moto ed Energia Cinetica

## Formule chiave

*   **Conversione unità di misura velocità:**
    $$1\text{ km/h} = \frac{1000\text{ m}}{3600\text{ s}} = \frac{1}{3,6}\text{ m/s}$$
    $$1\text{ m/s} = 3,6\text{ km/h}$$

*   **Variazione di energia cinetica ($\Delta E$):**
    $$\Delta E = E_i - E_f = \frac{1}{2}m_1 v_{1i}^2 + \frac{1}{2}m_2 v_{2i}^2 - \frac{1}{2}(m_1 + m_2)v_f^2$$

*   **Dissipazione percentuale di energia cinetica nell'urto anaelastico:**
    $$\text{Dissipazione \%} = \frac{\Delta E}{E_i} \cdot 100 = \frac{\frac{1}{2}m_1 v_{1i}^2 + \frac{1}{2}m_2 v_{2i}^2 - \frac{1}{2}(m_1 + m_2)v_f^2}{\frac{1}{2}m_1 v_{1i}^2 + \frac{1}{2}m_2 v_{2i}^2} \cdot 100$$

*   **Conservazione della quantità di moto (2D):**
    $$\vec{P}_i = \vec{P}_f$$
    In componenti cartesiane:
    $$\begin{cases} P_{ix} = P_{fx} \\ P_{iy} = P_{fy} \end{cases}$$

*   **Relazioni trigonometriche negli angoli (Urti 2D):**
    $$\sin^2\theta + \cos^2\theta = 1$$
    $$\sin(90^\circ - \theta) = \cos\theta$$
    $$\cos(90^\circ - \theta) = \sin\theta$$

## Urti anaelastici in 1D e Dissipazione Energetica

Dati del problema iniziale:
*   $m_1 = 2,5\text{ kg}$
*   $m_2 = 30\text{ kg}$
*   $v_{1i} = 4,5\text{ m/s}$
*   $v_{2i} = 6\text{ m/s}$ (con verso opposto rispetto a $m_1$, quindi $v_{2i} = -6\text{ m/s}$ lungo l'asse $x$)
*   Nota: $m_2 > m_1$

Impostazione vettoriale iniziale:
$$\vec{v}_{1i} = v_{1i}\hat{x}$$
$$\vec{v}_{2i} = -v_{2i}\hat{x}$$

Se l'urto è anaelastico (i corpi restano attaccati):
$$\vec{v}_f = -v_f\hat{x}$$
$$m_{tot} = m_1 + m_2$$

Formula della variazione di energia cinetica e calcolo della percentuale dissipata:
Negli urti anaelastici si ha sempre $E_f < E_i$, quindi la variazione è $\Delta E = E_i - E_f$.

## Urti Elastici in 2D

Dati:
*   $m_1 = m_2 = m$
*   $\vec{v}_{1i} = v_{i}\hat{x}$
*   $\vec{v}_{2i} = 0$
*   $v_{1f} = 4,2\text{ m/s}$
*   $v_{2f} = 2,5\text{ m/s}$

Sviluppo algebrico della conservazione della quantità di moto lungo gli assi $x$ e $y$:
$$\begin{cases}
m v_i = m v_{1fx} + m v_{2fx} \\
0 = m v_{1fy} + m v_{2fy}
\end{cases}$$

Semplificando la massa $m$:
$$\begin{cases}
v_i = v_{1fx} + v_{2fx} \\
0 = v_{1fy} - v_{2fy} \implies v_{1fy} = -v_{2fy}
\end{cases}$$

Utilizzando le componenti polari ($v_{1fx} = v_{1f}\cos\alpha$, $v_{1fy} = v_{1f}\sin\alpha$, $v_{2fx} = v_{2f}\cos\beta$, $v_{2fy} = -v_{2f}\sin\beta$):
$$\begin{cases}
v_i = v_{1f}\cos\alpha + v_{2f}\cos\beta \quad (1) \\
v_{1f}\sin\alpha = -v_{2f}\sin\beta \quad (2) \\
v_i^2 = v_{1f}^2 + v_{2f}^2 \quad (3) \text{ (derivato dalla conservazione dell'energia cinetica)}
\end{cases}$$

Isolando e risolvendo per gli angoli $\alpha$ e $\beta$:
1. Da (2): $v_{2f}\sin\beta = -v_{1f}\sin\alpha \implies \sin\beta = -\frac{v_{1f}}{v_{2f}}\sin\alpha$
2. Da (1): $v_{2f}\cos\beta = v_i - v_{1f}\cos\alpha$
3. Elevando al quadrato e sommando le equazioni trigonometriche si ottiene l'angolo $\alpha$:
$$\alpha = \arccos\left(\frac{v_{1f}^2 + v_i^2 - v_{2f}^2}{2 v_i v_{1f}}\right)$$
4. Sostituendo si ricava l'angolo $\beta$:
$$\beta = \arcsin\left(-\frac{v_{1f}}{v_{2f}}\sin\alpha\right)$$

---

## Materiale generato

### Riepilogo
Gli appunti trattano la dinamica degli urti: nel caso anaelastico in 1D si analizza la dissipazione di energia cinetica in percentuale, mentre nell'urto elastico in 2D si applicano le leggi di conservazione della quantità di moto e dell'energia cinetica per determinare le velocità e gli angoli di deflessione tramite trigonometria.

### Esercizi simili

1. Due corpi di masse $m_1 = 2\text{ kg}$ e $m_2 = 3\text{ kg}$ si muovono uno contro l'altro su una retta con velocità rispettivamente $v_{1i} = 5\text{ m/s}$ e $v_{2i} = -3\text{ m/s}$. Dopo un urto completamente anaelastico, calcola l'energia cinetica dissipata.
<details><summary>Soluzione</summary>
Quantità di moto iniziale: $p_i = (2 \cdot 5) + (3 \cdot (-3)) = 10 - 9 = 1\text{ kg}\cdot\text{m/s}$.
Velocità finale: $v_f = \frac{p_i}{m_1 + m_2} = \frac{1}{5} = 0,2\text{ m/s}$.
Energia iniziale: $E_i = \frac{1}{2}(2)(5)^2 + \frac{1}{2}(3)(-3)^2 = 25 + 13,5 = 38,5\text{ J}$.
Energia finale: $E_f = \frac{1}{2}(5)(0,2)^2 = 0,1\text{ J}$.
$\Delta E = 38,5 - 0,1 = \mathbf{38,4\text{ J}}$.
</details>

2. Un corpo di massa $m$ urta elasticamente e frontalmente un corpo fermo di massa uguale ($m_2 = m_1$). Dimostra che la velocità finale del primo corpo è zero.
<details><summary>Soluzione</summary>
Per un urto elastico frontale tra masse uguali, valgono simultaneamente la conservazione della quantità di moto ($v_{1i} = v_{1f} + v_{2f}$) e dell'energia cinetica ($v_{1i}^2 = v_{1f}^2 + v_{2f}^2$). Mettendo a sistema si ottiene direttamente $v_{1f} = 0$ e $v_{2f} = v_{1i}$.
</details>

3. Calcola la trasformazione di velocità: quanti metri al secondo sono $72\text{ km/h}$?
<details><summary>Soluzione</summary>
Usando il fattore di conversione:
$$v = \frac{72}{3,6} = \mathbf{20\text{ m/s}}$$
</details>

### Flashcard
- **D:** Cos'è un urto anaelastico? — **R:** Un urto in cui i corpi rimangono uniti dopo l'impatto e l'energia cinetica non si conserva (si dissipa).
- **D:** Come si converte una velocità da km/h a m/s? — **R:** Dividendo per $3,6$.
- **D:** Negli urti elastici in 2D tra masse uguali, cosa si conserva? — **R:** Sia la quantità di moto vettoriale che l'energia cinetica totale del sistema.
- **D:** Qual è la relazione fondamentale tra seno e coseno usata per ricavare gli angoli negli urti 2D? — **R:** $\sin^2\theta + \cos^2\theta = 1$.
