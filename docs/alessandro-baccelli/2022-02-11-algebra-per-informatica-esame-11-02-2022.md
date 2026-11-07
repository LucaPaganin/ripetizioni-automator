---
titolo: 'Algebra per Informatica: Esame del 11/02/2022'
data: '2022-02-11'
studente: Alessandro Baccelli
materia: matematica
argomento: Algebra
sottoargomenti:
- Numeri complessi
- Teoria degli insiemi e relazioni d'ordine
- Applicazioni ed equazioni diofanteee
- Gruppi e sottogruppi
esercizi:
- 1
- 2
- 3
- 4
errori_tipici:
- Confondere la risolvibilità di un'equazione diofantea dimenticando la condizione
  sul massimo comun divisore.
- Dimenticare che la suriettività e l'iniettività sono necessarie per l'esistenza
  rispettivamente di inverse destre e sinistre.
fonte: https://drive.google.com/file/d/1B2Dq7shAy-So3oH6MFZsYES3EGmO9hd5/view?usp=drivesdk
generato: '2026-11-07'
---

# Algebra per Informatica - Esame 11/02/2022

## Formule chiave

- **Numeri complessi:** Dati $z = a + ib$, il modulo è $|z| = \sqrt{a^2 + b^2}$ e l'argomento è $\arg(z) = \arctan\left(\frac{b}{a}\right)$. La forma esponenziale è $z = |z|e^{i\theta}$.
- **Equazioni diofantee:** L'equazione $ax + by = c$ ammette soluzioni intere se e solo se $\text{MCD}(a, b) \mid c$.
- **Teorema di Lagrange:** Se $G$ è un gruppo finito e $H$ è un sottogruppo di $G$, allora l'ordine di $H$ divide l'ordine di $G$.

## Esercizio 1

Sia dato il numero complesso:
$$z = \frac{(6 + 12i)(4 + 12i)}{(\sqrt{3} + i)^3}$$
Scrivere $z$ in forma $a + ib$ con $a, b \in \mathbb{R}$ e in forma esponenziale.

**Soluzione:**

1. Calcoliamo il numeratore:
$$(6 + 12i)(4 + 12i) = 24 + 72i + 48i - 144 = -120 + 120i$$

2. Per calcolare la potenza al denominatore, scriviamo $\sqrt{3} + i$ in forma esponenziale:
$$|\sqrt{3} + i| = \sqrt{3 + 1} = 2, \quad \arg(\sqrt{3} + i) = \frac{\pi}{6}$$
Quindi:
$$(\sqrt{3} + i)^3 = \left(2e^{i\frac{\pi}{6}}\right)^3 = 2^3 e^{i\frac{3\pi}{6}} = 8e^{i\frac{\pi}{2}} = 8i$$

3. Sostituendo otteniamo:
$$z = \frac{120(-1 + i)}{8i} = \frac{15(-1 + i)}{i} = -15i(-1 + i) = 15(1 + i) = \boxed{15 + 15i}$$

4. Per la forma esponenziale di $z$:
$$|z| = \sqrt{15^2 + 15^2} = 15\sqrt{2}, \quad \arg(z) = \frac{\pi}{4}$$
Pertanto:
$$z = \boxed{15\sqrt{2}e^{i\frac{\pi}{4}}}$$

---

## Esercizio 2

Si consideri l'insieme $A = \{2, 4, 5, 20, 25, 100\}$ con la relazione d'ordine $a \preceq b \iff a \mid b$. Si determinino massimo, minimo, elementi minimali ed elementi massimali di $A$.

**Soluzione:**
Il diagramma di Hasse del poset $A$ (con ordine dal basso verso l'alto) è:
- $100$ è ricoperto da nessuno, ed è il massimo ($100$ è multiplo di tutti gli elementi). Essendo massimo, è anche l'unico elemento massimale.
- Gli elementi minimali sono $2$ e $5$ (non sono divisibili per nessun altro elemento dell'insieme e non sono confrontabili tra loro).
- Poiché ci sono due elementi minimali, l'insieme **non ammette minimo**.

Risultati:
- Massimo: $\boxed{100}$
- Minimo: **Non esiste**
- Elementi massimali: $\boxed{\{100\}}$
- Elementi minimali: $\boxed{\{2, 5\}}$

---

## Esercizio 3

Sia $f: \mathbb{Z}^2 \to \mathbb{Z}$ l'applicazione data da $f(x, y) = 24x - 20y$.

1. Determinare le seguenti controimmagini: $f^{-1}(10)$, $f^{-1}(8)$, $f^{-1}(f(5, 6))$.
2. Determinare (se esistono) un'inversa sinistra e un'inversa destra per $f$.

**Soluzione:**

1. 
- Per $f^{-1}(10)$: l'equazione $24x - 20y = 10$ ha $\text{MCD}(24, -20) = 4$. Poiché $4 \nmid 10$, non ci sono soluzioni intere. Quindi $f^{-1}(10) = \boxed{\emptyset}$.
- Per $f^{-1}(8)$: l'equazione $24x - 20y = 8 \implies 6x - 5y = 2$. Una soluzione particolare è $(x_0, y_0) = (2, 2)$. Tutte le soluzioni sono:
$$f^{-1}(8) = \boxed{\{(2 - 5k, 2 - 6k) : k \in \mathbb{Z}\}}$$
- Per $f^{-1}(f(5, 6))$: $f(5, 6) = 24(5) - 20(6) = 120 - 120 = 0$. Dobbiamo risolvere $24x - 20y = 0 \implies 6x - 5y = 0$. Una soluzione particolare è $(0,0)$, quindi:
$$f^{-1}(f(5, 6)) = \boxed{\{(-5k, -6k) : k \in \mathbb{Z}\}}$$

2. La funzione $f$ non è suriettiva (poiché $f^{-1}(10) = \emptyset$), quindi **non ammette inverse destre**. Non è iniettiva (poiché $f(5,6) = f(0,0) = 0$), quindi **non ammette inverse sinistre**.

---

## Esercizio 4

Determinare tutti i sottogruppi di $(U(\mathbb{Z}_8), \cdot, \bar{1})$.

**Soluzione:**
L'insieme delle unità di $\mathbb{Z}_8$ è $U(\mathbb{Z}_8) = \{\bar{1}, \bar{3}, \bar{5}, \bar{7}\}$, con $\#U(\mathbb{Z}_8) = 4$.
Per il Teorema di Lagrange, l'ordine di un sottogruppo deve dividere $4$, quindi può essere $1, 2$ o $4$.

- Sottogruppi di ordine $1$: $\boxed{\{\bar{1}\}}$
- Sottogruppi di ordine $4$: $\boxed{U(\mathbb{Z}_8)}$
- Sottogruppi di ordine $2$: verifichiamo gli elementi di ordine $2$ ($\bar{x}^2 = \bar{1}$):
  - $\bar{3} \cdot \bar{3} = \bar{9} = \bar{1}$ $\implies$ sottogruppo $\{\bar{1}, \bar{3}\}$
  - $\bar{5} \cdot \bar{5} = \bar{25} = \bar{1}$ $\implies$ sottogruppo $\{\bar{1}, \bar{5}\}$
  - $\bar{7} \cdot \bar{7} = \bar{49} = \bar{1}$ $\implies$ sottogruppo $\{\bar{1}, \bar{7}\}$

In totale abbiamo 5 sottogruppi: $\boxed{\{\bar{1}\}, \{\bar{1}, \bar{3}\}, \{\bar{1}, \bar{5}\}, \{\bar{1}, \bar{7}\}, U(\mathbb{Z}_8)}$.

---

## ⚠️ Errori da evitare
- Dimenticare di controllare il $\text{MCD}(a,b)$ prima di risolvere un'equazione diofantea lineare.
- Confondere gli elementi minimali con il minimo in un insieme parzialmente ordinato (la presenza di più elementi minimali esclude l'esistenza del minimo).

---

## Materiale generato

### Riepilogo
La lezione affronta esercizi classici di algebra: calcoli con i numeri complessi in forma algebrica ed esponenziale, studio di insiemi ordinati (massimi, minimi, diagramma di Hasse), risoluzione di equazioni diofantee per determinare controimmagini e invertibilità di applicazioni, e individuazione dei sottogruppi di un gruppo finito tramite il Teorema di Lagrange.

### Esercizi simili

1. Calcolare e scrivere in forma algebrica ed esponenziale il numero complesso $z = \frac{(1+i)^4}{1 - i\sqrt{3}}$.
   <details><summary>Soluzione</summary>Utilizzando la forma esponenziale per numeratore e denominatore si ottiene $z = -1 + i\sqrt{3} = 2e^{i\frac{2\pi}{3}}$.</details>

2. Trovare tutte le soluzioni intere dell'equazione diofantea $15x - 9y = 6$.
   <details><summary>Soluzione</summary>Poiché $\text{MCD}(15, -9) = 3$ e $3 \mid 6$, le soluzioni esistono. Semplificando $5x - 3y = 2$, una soluzione particolare è $(1, 1)$, e l'insieme delle soluzioni è $\{(1 - 3k, 1 - 5k) : k \in \mathbb{Z}\}$.</details>

3. Determinare tutti i sottogruppi del gruppo moltiplicativo $(U(\mathbb{Z}_{10}), \cdot, \bar{1})$.
   <details><summary>Soluzione</summary>$U(\mathbb{Z}_{10}) = \{\bar{1}, \bar{3}, \bar{7}, \bar{9}\}$. I sottogruppi sono $\{\bar{1}\}$, $U(\mathbb{Z}_{10})$, $\{\bar{1}, \bar{9}\}$ (di ordine 2), e $\{\bar{1}, \bar{3}, \bar{7}, \bar{9}\}$ (generato da $\bar{3}$ o $\bar{7}$).</details>

### Flashcard
- **D:** Quando un'equazione diofantea $ax + by = c$ ammette soluzioni intere? — **R:** Se e solo se $\text{MCD}(a, b)$ divide $c$.
- **D:** Cosa afferma il Teorema di Lagrange per i gruppi? — **R:** L'ordine di un qualsiasi sottogruppo $H$ di un gruppo finito $G$ divide l'ordine di $G$.
- **D:** Come si passa da un numero complesso $z = a + ib$ alla forma esponenziale? — **R:** Calcolando il modulo $|z| = \sqrt{a^2+b^2}$ e l'argomento $\theta = \arctan(b/a)$, ottenendo $z = |z|e^{i\theta}$.
- **D:** Quando un poset ammette un unico elemento minimo, cosa si può dire dei suoi elementi minimali? — **R:** L'insieme ha un unico elemento minimale che coincide con il minimo.
