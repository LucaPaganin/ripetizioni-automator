---
titolo: Vettori e Conservazione della Quantità di Moto
data: '2026-01-21'
studente: Andrea Ferrando
materia: fisica
argomento: Vettori, Prodotto scalare e vettoriale, Urti elastici
sottoargomenti:
- Vettori e versori fondamentali
- Prodotto scalare
- Prodotto vettoriale
- Urti unidimensionali (quantità di moto ed energia cinetica)
esercizi: []
errori_tipici:
- Confondere il prodotto scalare (risultato scalare) con il prodotto vettoriale (risultato
  vettore)
- Conservare la velocità iniziale in un urto elastico senza considerare le masse
fonte: https://drive.google.com/file/d/1fBOKVarRg2FDkHSaaZWnv55ShL6O_cX3/view?usp=drivesdk
generato: '2026-11-07'
---

# Vettori e Conservazione della Quantità di Moto

## Formule chiave

### 1. Proprietà dei Vettori
* **Modulo:** lunghezza del vettore, intensità.
* **Direzione:** la retta su cui giace.
* **Verso:** orientazione lungo la direzione.

Dati due vettori in componenti cartesiane:
$$\vec{v} = v_x \hat{x} + v_y \hat{y} + v_z \hat{z}$$
$$\vec{w} = w_x \hat{x} + w_y \hat{y} + w_z \hat{z}$$

La somma vettoriale è:
$$\vec{v} + \vec{w} = (v_x + w_x)\hat{x} + (v_y + w_y)\hat{y} + (v_z + w_z)\hat{z}$$

### 2. Prodotto Scalare
Il prodotto scalare tra due vettori restituisce uno scalare:
$$\vec{v} \cdot \vec{w} = |\vec{v}| \cdot |\vec{w}| \cos\alpha = v_x w_x + v_y w_y + v_z w_z$$

Prodotti fondamentali tra versori:
$$\hat{x} \cdot \hat{x} = 1, \quad \hat{y} \cdot \hat{y} = 1, \quad \hat{z} \cdot \hat{z} = 1$$
$$\hat{x} \cdot \hat{y} = \hat{x} \cdot \hat{z} = \hat{y} \cdot \hat{z} = 0$$

### 3. Prodotto Vettoriale
Il prodotto vettoriale tra due vettori restituisce un vettore:
$$\vec{v} \times \vec{w} \text{ è un vettore}$$
* È ortogonale sia a $\vec{v}$ che a $\vec{w}$.
* Il verso e la direzione si ricavano con la regola della mano destra.
* È anticommutativo: se si cambia l'ordine dei fattori, il vettore cambia segno.

Il modulo è dato da:
$$|\vec{v} \times \vec{w}| = |\vec{v}| \cdot |\vec{w}| \sin\alpha$$

* Se $\alpha = 0^\circ$ ($\vec{v}$ e $\vec{w}$ paralleli): $|\vec{v} \times \vec{w}| = 0$ poiché $\sin(0^\circ) = 0$.
* Se $\alpha = 90^\circ$ ($\vec{v}$ e $\vec{w}$ ortogonali): $|\vec{v} \times \vec{w}| = |\vec{v}| \cdot |\vec{w}|$ poiché $\sin(90^\circ) = 1$.

Il calcolo tramite determinante in 3D:
$$\vec{v} \times \vec{w} = \begin{vmatrix} \hat{x} & \hat{y} & \hat{z} \\ v_x & v_y & v_z \\ w_x & w_y & w_z \end{vmatrix} = \hat{x}(v_y w_z - w_y v_z) - \hat{y}(v_x w_z - w_x v_z) + \hat{z}(v_x w_y - w_x v_y)$$

---

## Urto Elastico tra due corpi (Quantità di moto ed Energia Cinetica)

Negli urti si conserva sempre la quantità di moto. Per un urto elastico si conserva anche l'energia cinetica.

Siano dati due corpi $A$ e $C$:
* $m_A = 100\text{ kg}$
* $m_C = 125\text{ kg}$
* $\vec{v}_{Ai} = v_{Ai} \hat{x}$, con $v_{Ai} = 1.25\text{ m/s}$

### Stato Iniziale ($i$) e Finale ($f$)
* Quantità di moto iniziale:
  $$\vec{p}_i = m_A \vec{v}_{Ai} = m_A v_{Ai} \hat{x}$$
* Quantità di moto finale:
  $$\vec{p}_f = m_A \vec{v}_{Af} + m_C \vec{v}_{Cf} = (m_A v_{Af} + m_C v_{Cf}) \hat{x}$$

Imponendo la conservazione della quantità di moto (1) e dell'energia cinetica (2):
1) $\vec{p}_i = \vec{p}_f \implies m_A v_{Ai} = m_A v_{Af} + m_C v_{Cf}$
2) $E_{ki} = E_{kf} \implies \frac{1}{2} m_A v_{Ai}^2 = \frac{1}{2} m_A v_{Af}^2 + \frac{1}{2} m_C v_{Cf}^2$

Dalla (1) ricaviamo $v_{Cf}$:
$$m_C v_{Cf} = m_A v_{Ai} - m_A v_{Af} \implies v_{Cf} = \frac{m_A}{m_C}(v_{Ai} - v_{Af})$$

Sostituiamo $v_{Cf}$ nell'equazione dell'energia cinetica (2):
$$m_A v_{Af}^2 + m_C \left[\frac{m_A}{m_C}(v_{Ai} - v_{Af})\right]^2 = m_A v_{Ai}^2$$
$$m_A v_{Af}^2 + \frac{m_A^2}{m_C} (v_{Ai} - v_{Af})^2 = m_A v_{Ai}^2$$

Sviluppando e raccogliendo in forma di equazione di secondo grado in $v_{Af}$ ($ax^2 + bx + c = 0$):
$$\left(1 + \frac{m_A}{m_C}\right) v_{Af}^2 - 2\frac{m_A}{m_C} v_{Ai} v_{Af} + \left(\frac{m_A}{m_C} - 1\right) v_{Ai}^2 = 0$$

Applicando la formula risolutiva si ottengono due soluzioni: $v_{Af} = v_{Ai}$ (da scartare: corrisponde a nessun urto) e la soluzione fisica per la velocità del corpo $A$ dopo l'urto:
$$v_{Af} = \frac{m_A - m_C}{m_C + m_A} v_{Ai}$$
Con i dati: $v_{Af} = \frac{100 - 125}{225} \cdot 1{,}25 \approx -0{,}14\text{ m/s}$ (essendo $m_A < m_C$, il corpo $A$ rimbalza indietro).

---

## ⚠️ Errori da evitare
* **Velocità iniziale dell'urto:** Negli appunti è presente la nota *"No perchè Alice spende velocità da dare a Claudia. Non può avere stessa velocità iniziale"* riferita a un errore concettuale nel considerare le velocità dei corpi durante l'interazione.

---

## Materiale generato

### Riepilogo
La lezione introduce le operazioni fondamentali con i vettori (somma, prodotto scalare e vettoriale) e applica i principi di conservazione della quantità di moto e dell'energia cinetica per risolvere un problema di urto unidimensionale elastico tra due masse.

### Esercizi simili
1. Dati i vettori $\vec{a} = 3\hat{x} + 2\hat{y}$ e $\vec{b} = 1\hat{x} - 4\hat{y}$, calcolare il prodotto scalare $\vec{a} \cdot \vec{b}$ e il modulo del prodotto vettoriale $\vec{a} \times \vec{b}$ in 2D.
   <details><summary>Soluzione</summary>
   $\vec{a} \cdot \vec{b} = (3)(1) + (2)(-4) = 3 - 8 = -5$<br>
   In 2D, il prodotto vettoriale ha componente solo lungo $\hat{z}$: $\vec{a} \times \vec{b} = (3(-4) - (2)(1))\hat{z} = -14\hat{z}$, quindi il modulo è $|\vec{a} \times \vec{b}| = 14$.
   </details>

2. Calcolare il prodotto scalare tra $\vec{v} = 2\hat{x} + 3\hat{y} - \hat{z}$ e $\vec{w} = 4\hat{x} - 2\hat{y} + 5\hat{z}$.
   <details><summary>Soluzione</summary>
   $\vec{v} \cdot \vec{w} = (2)(4) + (3)(-2) + (-1)(5) = 8 - 6 - 5 = -3$.
   </details>

3. Un corpo di massa $m_1 = 2\text{ kg}$ viaggia a $v_{1i} = 5\text{ m/s}$ e urta elasticamente e frontalmente un corpo fermo di massa $m_2 = 3\text{ kg}$. Calcolare la velocità finale del primo corpo.
   <details><summary>Soluzione</summary>
   Utilizzando la formula $v_{1f} = \frac{m_1 - m_2}{m_1 + m_2} v_{1i}$:<br>
   $v_{1f} = \frac{2 - 3}{2 + 3} \cdot 5 = \frac{-1}{5} \cdot 5 = -1\text{ m/s}$ (il corpo inverte il moto).
   </details>

### Flashcard
- **D:** Cos'è il prodotto scalare tra due vettori? — **R:** Un'operazione che restituisce uno scalare pari al prodotto dei moduli per il coseno dell'angolo compreso ($|\vec{v}||\vec{w}|\cos\alpha$).
- **D:** Cosa indica un prodotto vettoriale pari a zero? — **R:** Indica che i due vettori sono paralleli (o uno dei due è nullo), poiché l'angolo $\alpha = 0^\circ$ rende il seno nullo.
- **D:** Quali leggi si conservano sempre in un urto? — **R:** La quantità di moto si conserva sempre; l'energia cinetica si conserva solo negli urti elastici.
- **D:** Come si ricava la direzione del vettore risultante da un prodotto vettoriale? — **R:** Applicando la regola della mano destra.
