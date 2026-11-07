---
titolo: Esame di Algebra per Informatica - 25/01/2022
data: '2022-01-25'
studente: Alessandro Baccelli
materia: matematica
argomento: Algebra Discreta
sottoargomenti:
- Funzioni
- Relazioni di equivalenza
- Poset
- Gruppi e ordine degli elementi
esercizi:
- 1
- 2
- 3
- 4
errori_tipici: []
fonte: https://drive.google.com/file/d/1himoU6nN9VY-py1qAdeVkpvNQIm_Zl5C/view?usp=drivesdk
generato: '2026-11-07'
---

# Esame di Algebra per Informatica - 25/01/2022

## Formule chiave

- **Funzione iniettiva**: $f: A \to B$ è iniettiva se $\forall x_1, x_2 \in A$, $f(x_1) = f(x_2) \implies x_1 = x_2$.
- **Funzione suriettiva**: $f: A \to B$ è suriettiva se $\forall y \in B, \exists x \in A$ tale che $f(x) = y$.
- **Prodotto cartesiano e relazioni**: Una relazione d'equivalenza partiziona un insieme in classi d'equivalenza.
- **Poset $(\mathbb{Z} \times \mathbb{Z}, \le \times \le)$**: L'ordine è definito componente per componente: $(a,b) \le (c,d) \iff a \le c$ e $b \le d$.
- **Ordine di un elemento in un gruppo**: L'ordine di un elemento $g$ in un gruppo $(G, +, 0)$ è il più piccolo intero positivo $k$ tale che $k \cdot g = 0$. In un gruppo moltiplicativo $(G, \cdot, 1)$ è il più piccolo $k \ge 1$ tale che $g^k = 1$.

---

## Esercizio 1

Si consideri la seguente funzione:
$$f: \mathbb{C} \to \mathbb{C}$$
$$z \mapsto z^4$$

1. **Stabilire se $f$ è iniettiva e/o suriettiva.**
   - **Iniettività**: La funzione non è iniettiva. Ad esempio, per $z_1 = 1$ e $z_2 = i$, si ha $f(1) = 1^4 = 1$ e $f(i) = i^4 = 1$, ma $1 \neq i$.
   - **Suriettività**: La funzione è suriettiva. Dato un qualsiasi $w \in \mathbb{C}$, cerchiamo $z \in \mathbb{C}$ tale che $z^4 = w$. Passando alla forma trigonometrica o polare, ogni numero complesso non nullo ammette radici quarte in $\mathbb{C}$ (il campo dei numeri complessi è algebricamente chiuso).

2. **Determinare $f^{-1}(-256)$.**
   Cerchiamo le soluzioni dell'equazione $z^4 = -256$.
   Scriviamo $-256$ in forma polare: $-256 = 256 (\cos(\pi) + i \sin(\pi))$.
   Le radici quarte sono date da:
   $$z_k = \sqrt[4]{256} \left( \cos\left(\frac{\pi + 2k\pi}{4}\right) + i \sin\left(\frac{\pi + 2k\pi}{4}\right) \right), \quad k = 0, 1, 2, 3$$
   Poiché $\sqrt[4]{256} = 4$, otteniamo:
   - Per $k=0$: $z_0 = 4\left(\cos\left(\frac{\pi}{4}\right) + i\sin\left(\frac{\pi}{4}\right)\right) = 4\left(\frac{\sqrt{2}}{2} + i\frac{\sqrt{2}}{2}\right) = 2\sqrt{2} + 2i\sqrt{2}$
   - Per $k=1$: $z_1 = 4\left(\cos\left(\frac{3\pi}{4}\right) + i\sin\left(\frac{3\pi}{4}\right)\right) = -2\sqrt{2} + 2i\sqrt{2}$
   - Per $k=2$: $z_2 = 4\left(\cos\left(\frac{5\pi}{4}\right) + i\sin\left(\frac{5\pi}{4}\right)\right) = -2\sqrt{2} - 2i\sqrt{2}$
   - Per $k=3$: $z_3 = 4\left(\cos\left(\frac{7\pi}{4}\right) + i\sin\left(\frac{7\pi}{4}\right)\right) = 2\sqrt{2} - 2i\sqrt{2}$

   $$\boxed{f^{-1}(-256) = \{2\sqrt{2} + 2i\sqrt{2}, -2\sqrt{2} + 2i\sqrt{2}, -2\sqrt{2} - 2i\sqrt{2}, 2\sqrt{2} - 2i\sqrt{2}\}}$$

---

## Esercizio 2

Si consideri la relazione d'equivalenza sull'insieme $\mathbb{N} \times \mathbb{N}$:
$$(a, b) \sim (c, d) \iff a \cdot b = c \cdot d$$

Determinare la cardinalità di ciascuna delle seguenti classi d'equivalenza:
- $\overline{(1, 1)}$: L'equazione è $a \cdot b = 1 \cdot 1 = 1$. Poiché $a, b \in \mathbb{N}$, l'unica soluzione è $a = 1, b = 1$.
  $$\boxed{|\overline{(1, 1)}| = 1}$$
- $\overline{(6, 6)}$: L'equazione è $a \cdot b = 6 \cdot 6 = 36$. Dobbiamo trovare le coppie $(a, b) \in \mathbb{N} \times \mathbb{N}$ tali che $a \cdot b = 36$. I divisori di $36$ sono $1, 2, 3, 4, 6, 9, 12, 18, 36$ (totale 9 divisori). Ad ogni divisore $a$ corrisponde un unico $b = 36/a$.
  $$\boxed{|\overline{(6, 6)}| = 9}$$
- $\overline{(0, 0)}$: L'equazione è $a \cdot b = 0 \cdot 0 = 0$. Il prodotto $a \cdot b = 0$ se e solo se $a = 0$ oppure $b = 0$. Le coppie sono del tipo $(0, b)$ con $b \in \mathbb{N}$ oppure $(a, 0)$ con $a \in \mathbb{N}$ (notando che $(0,0)$ è contata due volte). L'insieme è infinito numerabile.
  $$\boxed{|\overline{(0, 0)}| = \aleph_0 \text{ (infinita)또 numerabile}}$$

---

## Esercizio 3

Sia dato l'insieme $A = \{(7, 9), (7, 6), (10, 10), (8, 6), (8, 5), (8, 2)\}$. Si consideri $A$ come sottoinsieme del poset $(\mathbb{Z} \times \mathbb{Z}, \le \times \le)$.

- **Massimo**: Cerchiamo un elemento $m \in A$ tale che $x \le m$ per ogni $x \in A$. Verifichiamo tra i candidati "più grandi":
  Confrontiamo $(10, 10)$ con gli altri: $(7, 9) \not\le (10, 10)$ poiché $7 \le 10$ ma $9 \not\le 10$ è falso ($9 \le 10$ è vero, controlliamo bene: $7 \le 10$ e $9 \le 10$, quindi $(7,9) \le (10,10)$).
  Verifichiamo $(8,6) \le (10,10)$: $8 \le 10$ e $6 \le 10$ (vero).
  Verifichiamo $(8,5) \le (10,10)$: vero.
  Verifichiamo $(8,2) \le (10,10)$: vero.
  Verifichiamo $(7,6) \le (10,10)$: vero.
  Verifichiamo $(10,10) \le (10,10)$: vero.
  Quindi $(10,10)$ è maggiore o uguale a tutti gli elementi di $A$.
  $$\boxed{\text{Massimo} = (10, 10)}$$

- **Minimo**: Cerchiamo un elemento $m \in A$ tale che $m \le x$ per ogni $x \in A$.
  Verifichiamo $(8, 2)$:
  - $(8, 2) \le (8, 5)$ poiché $8 \le 8$ e $2 \le 5$ (vero).
  - $(8, 2) \le (8, 6)$ (vero).
  - $(8, 2) \le (7, 6)$ poiché $8 \le 7$ è falso! Quindi $(8,2)$ non è minore di $(7,6)$.
  Verifichiamo gli altri elementi minimali candidati: non esiste un unico elemento minore di tutti gli altri. L'insieme dei minoranti di $A$ non ha un massimo, oppure verifichiamo direttamente che nessun elemento è minore di tutti gli altri (es. $(7,9)$ e $(8,2)$ non sono comparabili).
  $$\boxed{\text{Minimo non esiste}}$$

- **Estremo inferiore ($\inf A$)**: È il massimo dell'insieme dei minoranti. I minoranti di $A$ sono le coppie $(x, y)$ tali che $(x, y) \le (7,9), (7,6), (10,10), (8,6), (8,5), (8,2)$.
  Dalla prima coordinata: $x \le 7$ (poiché compare $7$ in $(7,9)$ e $(7,6)$).
  Dalla seconda coordinata: $y \le 2$ (poiché compare $2$ in $(8,2)$).
  L'insieme dei minoranti è $\{(x, y) \in \mathbb{Z} \times \mathbb{Z} \mid x \le 7, y \le 2\}$. Il massimo di questo insieme è $(7, 2)$.
  $$\boxed{\inf A = (7, 2)}$$

- **Estremo superiore ($\sup A$)**: È il minimo dell'insieme dei maggioranti. Poiché $A$ ha massimo $(10, 10)$, il massimo è anche l'estremo superiore.
  $$\boxed{\sup A = (10, 10)}$$

---

## Esercizio 4

### 1. Calcolare l'ordine dei seguenti elementi nel gruppo $(\mathbb{Z}_{26}, +, \bar{0})$:
L'ordine di un elemento $\bar{a}$ in $\mathbb{Z}_n$ è dato da $\frac{n}{\text{MCD}(a, n)}$.

- Per $\bar{2}$: $\text{MCD}(2, 26) = 2 \implies \text{ordine} = \frac{26}{2} = 13$.
  $$\boxed{\text{ordine di } \bar{2} \text{ è } 13}$$
- Per $\bar{9}$: $\text{MCD}(9, 26) = 1 \implies \text{ordine} = \frac{26}{1} = 26$.
  $$\boxed{\text{ordine di } \bar{9} \text{ è } 26}$$
- Per $\bar{13}$: $\text{MCD}(13, 26) = 13 \implies \text{ordine} = \frac{26}{13} = 2$.
  $$\boxed{\text{ordine di } \bar{13} \text{ è } 2}$$

### 2. Calcolare l'ordine dei seguenti elementi nel gruppo $(U(\mathbb{Z}_{26}), \cdot, \bar{1})$:
Il gruppo $U(\mathbb{Z}_{26})$ ha ordine $\phi(26) = \phi(2) \cdot \phi(13) = 1 \cdot 12 = 12$. L'ordine di un elemento deve dividere 12.

- Per $\bar{9}$:
  - $\bar{9}^1 = \bar{9} \neq \bar{1}$
  - $\bar{9}^2 = \overline{81} = \overline{3} \neq \bar{1}$ (poiché $81 = 3 \cdot 26 + 3$)
  - $\bar{9}^3 = \bar{9} \cdot \bar{3} = \overline{27} = \bar{1}$
  $$\boxed{\text{ordine di } \bar{9} \text{ è } 3}$$

- Per $\bar{21}$:
  - Notiamo che $\bar{21} = -\bar{5} \equiv \overline{-5} \pmod{26}$.
  - $\bar{21}^1 = \overline{21} \neq \bar{1}$
  - $\bar{21}^2 = \overline{441}$. Facciamo la divisione: $441 = 16 \cdot 26 + 25$, quindi $\overline{441} = \overline{25} = -\bar{1} \neq \bar{1}$.
  - $\bar{21}^4 = (\bar{21}^2)^2 = (\overline{-1})^2 = \bar{1}$.
  $$\boxed{\text{ordine di } \bar{21} \text{ è } 4}$$

---

## Materiale generato

### Riepilogo
Il documento affronta esercizi classici di algebra discreta: calcolo di immagini inverse di funzioni complesse, cardinalità di classi d'equivalenza, determinazione di estremi in un poset prodotto e calcolo dell'ordine di elementi in gruppi additivi e moltiplicativi modulari.

### Esercizi simili
1. Determinare l'immagine inversa $f^{-1}(16)$ della funzione $f: \mathbb{C} \to \mathbb{C}$ definita da $f(z) = z^4$.
   <details><summary>Soluzione</summary>Le soluzioni di $z^4 = 16$ sono $z \in \{2, 2i, -2, -2i\}$.</details>

2. Data la relazione d'equivalenza su $\mathbb{N} \times \mathbb{N}$ definita da $(a,b) \sim (c,d) \iff a+b = c+d$, determinare la cardinalità della classe d'equivalenza $\overline{(3, 2)}$.
   <details><summary>Soluzione</summary>$3+2=5$. Le coppie $(a,b)$ con $a+b=5$ sono $(0,5), (1,4), (2,3), (3,2), (4,1), (5,0)$, quindi la cardinalità è $6$.</details>

3. Calcolare l'ordine dell'elemento $\bar{8}$ nel gruppo $(\mathbb{Z}_{24}, +, \bar{0})$.
   <details><summary>Soluzione</summary>$\text{MCD}(8, 24) = 8$, quindi l'ordine è $\frac{24}{8} = 3$.</details>

### Flashcard
- **D:** Come si calcola l'ordine di un elemento $\bar{a}$ nel gruppo additivo $\mathbb{Z}_n$ — **R:** $o(\bar{a}) = \frac{n}{\text{MCD}(a, n)}$.
- **D:** Quando un sottoinsieme $A$ di un poset ammette massimo? — **R:** Quando esiste un elemento $m \in A$ tale che $x \le m$ per ogni $x \in A$.
- **D:** Qual è la cardinalità delle classi d'equivalenza $(a,b) \sim (c,d) \iff ab=cd$ per $(1,1)$? — **R:** 1, poiché l'unica soluzione in $\mathbb{N} \times \mathbb{N}$ di $ab=1$ è $(1,1)$.
