---
titolo: 'Algebra per Informatica: Esame del 25/01/2022'
data: '2022-01-25'
studente: Alessandro Baccelli
materia: matematica
argomento: Algebra
sottoargomenti:
- Numeri complessi
- Teoria degli insiemi e relazioni d'equivalenza
- Poset e diagrammi di Hasse
- Teoria dei gruppi e ordine di un elemento
esercizi:
- 1
- 2
- 3
- 4
errori_tipici: []
fonte: https://drive.google.com/file/d/1KYiJYcK1E3ayUCfuCScAHY-PQZdDqWYJ/view?usp=drivesdk
generato: '2026-11-07'
---

# Algebra per Informatica: Esame del 25/01/2022

## Formule chiave

- **Radici $n$-esime di un numero complesso $z \in \mathbb{C}$**:
  Dato $z = |z|(\cos\theta + i\sin\theta)$, le radici $n$-esime $z_k$ sono date da:
  $$z_k = \sqrt[n]{|z|} \left( \cos\left(\frac{\theta + 2k\pi}{n}\right) + i\sin\left(\frac{\theta + 2k\pi}{n}\right) \right), \quad k = 0, 1, \dots, n-1$$

- **Classe d'equivalenza**:
  Dota una relazione d'equivalenza $\sim$ su un insieme $X$, la classe d'equivalenza di $x \in X$ è definita come:
  $$[x] = \{y \in X : y \sim x\}$$

- **Ordine di un elemento in un gruppo**:
  Sia $(G, *, \lambda)$ un gruppo e $g \in G$. L'ordine di $g$ è il più piccolo intero positivo $n$ tale che:
  $$\underbrace{g * g * \dots * g}_{n \text{ volte}} = \lambda$$

- **Teorema di Lagrange**:
  In un gruppo finito $G$, l'ordine di ogni sottogruppo di $G$ (e in particolare l'ordine di ogni elemento $g \in G$) divide l'ordine del gruppo $|G|$.

---

## Esercizio 1

Si consideri la seguente funzione:
$$f : \mathbb{C} \to \mathbb{C}$$
$$z \mapsto z^4$$

1. Stabilire se $f$ è iniettiva e/o suriettiva.
2. Determinare $f^{-1}(-256)$.

### Soluzione

1. **Iniettività e suriettività**:
   - La funzione $f$ **non è iniettiva** in quanto $f(1) = 1^4 = 1$ e $f(-1) = (-1)^4 = 1$, quindi $f(1) = f(-1)$ con $1 \neq -1$.
   - La funzione $f$ è **suriettiva**. Infatti, per ogni $z \in \mathbb{C}$ esiste sempre $w \in \mathbb{C}$ tale che $f(w) = w^4 = z$. L'esistenza di $w$ è garantita dal Teorema fondamentale dell'algebra (o dall'esistenza delle radici quarte complesse).

2. **Controimmagine $f^{-1}(-256)$**:
   Si ha che:
   $$f^{-1}(-256) = \{w \in \mathbb{C} : w^4 = -256\}$$
   Cioè l'insieme delle radici quarte di $z = -256$.
   Modulo e argomento di $z$:
   $$|z| = \sqrt{(-256)^2} = 256, \quad \arg(z) = \pi$$
   Pertanto le radici quarte $z_k$ di $z$ sono date dalla formula:
   $$z_k = \sqrt[4]{256} \left( \cos\left(\frac{\pi + 2k\pi}{4}\right) + i\sin\left(\frac{\pi + 2k\pi}{4}\right) \right), \quad k = 0, 1, 2, 3$$
   Siccome $\sqrt[4]{256} = 4$:
   - Per $k = 0$:
     $$z_0 = 4\left(\cos\left(\frac{\pi}{4}\right) + i\sin\left(\frac{\pi}{4}\right)\right) = 4\left(\frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2}\right) = 2\sqrt{2} + 2\sqrt{2}i$$
   - Per $k = 1$:
     $$z_1 = 4\left(\cos\left(\frac{3}{4}\pi\right) + i\sin\left(\frac{3}{4}\pi\right)\right) = 4\left(-\frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2}\right) = -2\sqrt{2} + 2\sqrt{2}i$$
   - Per $k = 2$:
     $$z_2 = 4\left(\cos\left(\frac{5}{4}\pi\right) + i\sin\left(\frac{5}{4}\pi\right)\right) = 4\left(-\frac{\sqrt{2}}{2} - i\frac{\sqrt{2}}{2}\right) = -2\sqrt{2} - 2\sqrt{2}i$$
   - Per $k = 3$:
     $$z_3 = 4\left(\cos\left(\frac{7}{4}\pi\right) + i\sin\left(\frac{7}{4}\pi\right)\right) = 4\left(\frac{\sqrt{2}}{2} - i\frac{\sqrt{2}}{2}\right) = 2\sqrt{2} - 2\sqrt{2}i$$

   Perciò, otteniamo:
   $$\boxed{f^{-1}(-256) = \{2\sqrt{2} + 2\sqrt{2}i, 2\sqrt{2} - 2\sqrt{2}i, -2\sqrt{2} - 2\sqrt{2}i, -2\sqrt{2} + 2\sqrt{2}i\}}$$

---

## Esercizio 2

Si consideri la seguente relazione d'equivalenza sull'insieme $\mathbb{N} \times \mathbb{N}$:
$$(a, b) \sim (c, d) \iff a \cdot b = c \cdot d$$

Determinare la cardinalità di ciascuna delle seguenti classi d'equivalenza:
$$(1, 1), \quad (6, 6), \quad (0, 0)$$

### Soluzione

Per definizione, fissati $a, b \in \mathbb{N}$, si ha:
$$\overline{(a, b)} = \{(x, y) \in \mathbb{N}^2 : xy = ab\}$$

1. **Classe $\overline{(1, 1)}$**:
   $$\overline{(1, 1)} = \{(x, y) \in \mathbb{N}^2 : xy = 1\} = \{(1, 1)\}$$
   Pertanto $\boxed{\#\overline{(1, 1)} = 1}$.

2. **Classe $\overline{(6, 6)}$**:
   $$\overline{(6, 6)} = \{(x, y) \in \mathbb{N}^2 : xy = 36\} = \{(1, 36), (2, 18), (3, 12), (4, 9), (6, 6), (9, 4), (12, 3), (18, 2), (36, 1)\}$$
   Pertanto $\boxed{\#\overline{(6, 6)} = 9}$.

3. **Classe $\overline{(0, 0)}$**:
   $$\overline{(0, 0)} = \{(x, y) \in \mathbb{N}^2 : xy = 0\} = \{(0, x) : x \in \mathbb{N}\} \cup \{(x, 0) : x \in \mathbb{N}^*\}$$
   Che è un'unione disgiunta di due insiemi numerabili e quindi numerabile.
   Pertanto $\boxed{\#\overline{(0, 0)} = \aleph_0}$.

---

## Esercizio 3

Sia dato l'insieme $A = \{(7, 9), (7, 6), (10, 10), (8, 6), (8, 5), (8, 2)\}$. Si consideri $A$ come sottoinsieme del poset $(\mathbb{Z} \times \mathbb{Z}, \le \times \le)$ e si determinino (se esistono) massimo, minimo, estremo inferiore ed estremo superiore di $A$.

### Soluzione

Il diagramma di Hasse che rappresenta la struttura del poset $A$ (dove l'ordine $\le \times \le$ procede dal basso verso l'alto) è il seguente:
```text
      (10, 10)
      /      \
  (7, 9)    (8, 6)
    |         |
  (7, 6)    (8, 5)
              |
            (8, 2)
```

- **Massimo ed estremo superiore**: 
  L'insieme $A$ ha un massimo in $\boxed{(10, 10)}$, che è pertanto anche l'estremo superiore $\sup A = (10, 10)$.

- **Minimo ed estremo inferiore**: 
  L'insieme $A$ ha due elementi minimali non confrontabili: $(7, 6)$ e $(8, 2)$. Pertanto $A$ **non ammette minimo**.
  L'insieme dei minoranti di $A$ è dato da:
  $$M = \{(x, y) \in \mathbb{Z}^2 : (x \le 7) \land (y \le 2)\}$$
  che ha un massimo in $(7, 2)$. Pertanto l'estremo inferiore di $A$ è $\boxed{\inf A = (7, 2)}$.

---

## Esercizio 4

1. Calcolare l'ordine dei seguenti elementi nel gruppo $(\mathbb{Z}_{26}, +, \bar{0})$:
   $$\bar{2}, \quad \bar{9}, \quad \bar{13}$$
2. Calcolare l'ordine dei seguenti elementi nel gruppo $(U(\mathbb{Z}_{26}), \cdot, \bar{1})$:
   $$\bar{9}, \quad \bar{21}$$

### Soluzione

1. **Ordine in $(\mathbb{Z}_{26}, +, \bar{0})$**:
   - Per $\bar{2}$: $\underbrace{\bar{2} + \dots + \bar{2}}_{13 \text{ volte}} = \overline{26} = \bar{0}$, e $13$ è il più piccolo intero positivo tale che $n \cdot \bar{2} = \bar{0}$. Quindi $\boxed{\operatorname{ord}(\bar{2}) = 13}$.
   - Per $\bar{13}$: $\bar{13} + \bar{13} = \overline{26} = \bar{0}$. Quindi $\boxed{\operatorname{ord}(\bar{13}) = 2}$.
   - Per $\bar{9}$: siccome $9$ è coprimo con $26$, il più piccolo intero positivo $n$ per cui $n \cdot \bar{9} = \bar{0}$ è $26$. Quindi $\boxed{\operatorname{ord}(\bar{9}) = 26}$.

2. **Ordine in $(U(\mathbb{Z}_{26}), \cdot, \bar{1})$**:
   L'ordine del gruppo è $|U(\mathbb{Z}_{26})| = \varphi(26) = 12$. Per il Teorema di Lagrange, l'ordine di un elemento deve dividere $12$ (i divisori sono $1, 2, 3, 4, 6, 12$).
   - Per $\bar{9}$:
     $$\bar{9}^2 = 81 = 3 \pmod{26}$$
     $$\bar{9}^3 = \bar{9}^2 \cdot \bar{9} = 3 \cdot 9 = 27 = \bar{1}$$
     Quindi $\boxed{\operatorname{ord}(\bar{9}) = 3}$.
   - Per $\bar{21}$:
     Notiamo che $\bar{21} = -\bar{5} \pmod{26}$.
     $$\bar{21}^2 = (-\bar{5})^2 = 25 = -\bar{1} \pmod{26}$$
     $$\bar{21}^4 = (\bar{21}^2)^2 = (-\bar{1})^2 = \bar{1}$$
     Quindi $\boxed{\operatorname{ord}(\bar{21}) = 4}$.

---

## Materiale generato

### Riepilogo
La lezione affronta esercizi di algebra avanzata: calcolo di radici quarte complesse e studio dell'iniettività/suriettività di una funzione di $\mathbb{C}$, determinazione della cardinalità di classi d'equivalenza su $\mathbb{N} \times \mathbb{N}$, analisi di poset con diagrammi di Hasse per trovare estremi, e calcolo dell'ordine di elementi in gruppi additivi e moltiplicativi $\mathbb{Z}_n$.

### Esercizi simili

1. **Esercizio sui numeri complessi**: Determinare le soluzioni dell'equazione $z^3 = -8$ in $\mathbb{C}$ e studiare la suriettività di $g(z) = z^3$.
   <details><summary>Soluzione</summary> $|z| = 8$, $\arg(z) = \pi$. Le soluzioni sono $z_k = 2\left(\cos\left(\frac{\pi + 2k\pi}{3}\right) + i\sin\left(\frac{\pi + 2k\pi}{3}\right)\right)$ per $k = 0, 1, 2$. L'insieme delle soluzioni è $\{2i, -\sqrt{3} - i, \sqrt{3} - i\}$. La funzione $g(z) = z^3$ è suriettiva su $\mathbb{C}$ ma non iniettiva (es. $g(2) = g(2e^{i2\pi/3})$). </details>

2. **Esercizio sulle relazioni d'equivalenza**: Data la relazione su $\mathbb{N} \times \mathbb{N}$ definita da $(a, b) \sim (c, d) \iff a + b = c + d$, determinare la cardinalità della classe $\overline{(2, 3)}$.
   <details><summary>Soluzione</summary> $\overline{(2, 3)} = \{(x, y) \in \mathbb{N}^2 : x + y = 5\} = \{(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)\}$. La cardinalità è 6. </details>

3. **Esercizio sui gruppi**: Calcolare l'ordine dell'elemento $\bar{3}$ nel gruppo $(U(\mathbb{Z}_{10}), \cdot, \bar{1})$.
   <details><summary>Soluzione</summary> L'ordine del gruppo è $\varphi(10) = 4$. Calcoliamo le potenze di $\bar{3}$: $\bar{3}^1 = \bar{3}$, $\bar{3}^2 = 9 = -\bar{1}$, $\bar{3}^4 = (\bar{3}^2)^2 = (-\bar{1})^2 = \bar{1}$. Quindi l'ordine di $\bar{3}$ è $4$. </details>

### Flashcard
- **D:** Come si calcolano le radici $n$-esime di un numero complesso $z$? — **R:** Usando la formula $z_k = \sqrt[n]{|z|} \left( \cos\left(\frac{\theta + 2k\pi}{n}\right) + i\sin\left(\frac{\theta + 2k\pi}{n}\right) \right)$ con $k = 0, 1, \dots, n-1$.
- **D:** Cosa afferma il Teorema di Lagrange riguardo all'ordine di un elemento in un gruppo finito? — **R:** L'ordine di ogni elemento di un gruppo finito deve dividere l'ordine del gruppo stesso.
- **D:** In un poset, se un sottoinsieme ha un elemento massimo, questo è anche l'estremo superiore? — **R:** Sì, se il massimo esiste, esso coincide sempre con l'estremo superiore.
