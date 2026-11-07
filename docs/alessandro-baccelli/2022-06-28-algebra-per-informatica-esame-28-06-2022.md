---
titolo: 'Algebra per Informatica: Esame del 28/06/2022'
data: '2022-06-28'
studente: Alessandro Baccelli
materia: matematica
argomento: Algebra
sottoargomenti:
- Teoria degli insiemi
- Funzioni
- Numeri complessi
- Teoria dei gruppi
esercizi:
- 1
- 2
- 3
- 4
errori_tipici:
- Confondere la suriettività con l'iniettività
- Dimenticare che MCD(a,b) | c è condizione necessaria e sufficiente per la risolubilità
  di un'equazione diofantea lineare
fonte: https://drive.google.com/file/d/11SqZrgIBJ0nfuDdVlw1jsKLEz3Z2kdl7/view?usp=drivesdk
generato: '2026-11-07'
---

# Algebra per Informatica: Esame del 28/06/2022

## Formule chiave

- **Cardinatità dell'insieme delle funzioni:** Siano $A$ e $B$ insiemi finiti. L'insieme delle funzioni $f: A \to B$ è indicato con $B^A$ e la sua cardinalità è data da $|B^A| = |B|^{|A|}$.
- **Equazione diofantea lineare:** L'equazione $ax + by = c$ ammette soluzioni intere se e soltanto se $\text{MCD}(a,b) \mid c$.
- **Forma algebrica e trigonometrica dei numeri complessi:** Un numero complesso $z = a + ib$ ha modulo $|z| = \sqrt{a^2 + b^2}$ e argomento $\theta$ tale che $\cos\theta = \frac{a}{|z|}$ e $\sin\theta = \frac{b}{|z|}$. La forma esponenziale è $z = |z|e^{i\theta}$.
- **Quoziente di gruppi:** Dato un gruppo $(G, +)$ e un sottogruppo $H$, le classi laterali formano il gruppo quoziente $G/H = \{g + H \mid g \in G\}$.

## Esercizio 1

Siano dati gli insiemi $A = \{a, b, c\}$ e $B = {1, 2}$. Determinare la cardinalità degli insiemi seguenti:
1. $R = \{f : A \to B\}$;
2. $S = A \cap B$;
3. $T = \{f : A \to B \mid f(a) = f(b)\}$;
4. $Z = (A \cup B) \setminus (A \cap B)$.

### Soluzione
1. Abbiamo $R = B^A$, quindi $|R| = |B|^{|A|} = 2^3 = \mathbf{8}$.
2. Abbiamo $S = A \cap B = \emptyset$, quindi $|S| = \mathbf{0}$.
3. Calcoliamo quante sono le possibili funzioni $f : A \to B$ tali che $f(a) = f(b)$. Abbiamo $2$ possibili scelte tra gli elementi di $B$ per il valore $f(a) = f(b)$ e $2$ possibili scelte tra gli elementi di $B$ per il valore $f(c)$. Essendo scelte indipendenti, abbiamo un totale di $2 \cdot 2 = 4$ possibili funzioni. Quindi $|T| = \mathbf{4}$.
4. Siccome $A \cap B = \emptyset$, abbiamo $Z = (A \cup B) \setminus (A \cap B) = A \cup B = \{a, b, c, 1, 2\}$. Quindi $|Z| = \mathbf{5}$.

---

## Esercizio 2

Si considerino le seguenti funzioni:
$$f : \mathbb{Z} \longrightarrow \mathbb{Z}, \quad x \mapsto 15x$$
$$g : \mathbb{Z} \times \mathbb{Z} \longrightarrow \mathbb{Z}, \quad (x, y) \mapsto 15x + 22y$$

1. Determinare se $f$ è iniettiva e/o suriettiva.
2. Calcolare $f^{-1}(30)$.
3. Determinare se $g$ è iniettiva e/o suriettiva.
4. Calcolare $g^{-1}(30)$.

### Soluzione
1. La funzione $f$ è iniettiva. Infatti dati $x, y \in \mathbb{Z}$ tali che $f(x) = f(y)$, abbiamo $15x = 15y$, che implica $x = y$. La funzione $f$ non è suriettiva, ad esempio non esiste $x \in \mathbb{Z}$ tale che $f(x) = 2$ (cioè $15x = 2$). Pertanto $f^{-1}(2) = \emptyset$. Più precisamente, $\text{Im} f = 15\mathbb{Z} \subsetneq \mathbb{Z}$.
2. Per definizione $f^{-1}(30) = \{x \in \mathbb{Z} \mid f(x) = 30\} = \{x \in \mathbb{Z} \mid 15x = 30\} = \mathbf{\{2\}}$.
3. La funzione $g$ non è iniettiva. Ad esempio, $(0, 0) \neq (22, -15)$, ma $g(0,0) = 0 = g(22, -15)$. Per la suriettività, l'equazione diofantea $15x + 22y = c$ ha soluzioni intere poiché $\text{MCD}(15, 22) = 1$ divide ogni $c \in \mathbb{Z}$. Pertanto $g$ è ** suriettiva**.
4. Una soluzione particolare dell'equazione $15x + 22y = 30$ è $(2, 0) \in \mathbb{Z}^2$. Le soluzioni generali sono $(x, y) = (2 + 22k, -15k)$ con $k \in \mathbb{Z}$. Quindi:
$$g^{-1}(30) = \mathbf{\{(2 + 22k, -15k) \mid k \in \mathbb{Z}\}}$$

---

## Esercizio 3

Sia dato il numero complesso
$$z = \frac{(1 + i\sqrt{3})(-\sqrt{3} + i)}{i^7(1 + i)^4}$$
Scrivere $z$ in forma $a + ib$ con $a, b \in \mathbb{R}$ e in forma esponenziale.

### Soluzione
Calcoliamo il numeratore:
$$(1 + i\sqrt{3})(-\sqrt{3} + i) = -\sqrt{3} + i - 3i - \sqrt{3} = -2\sqrt{3} - 2i$$
Calcoliamo il denominatore:
$$i^7(1 + i)^4 = i^3 \cdot ((1 + i)^2)^2 = -i \cdot (1 - 1 + 2i)^2 = -i \cdot (2i)^2 = -i \cdot (-4) = 4i$$
Quindi:
$$z = \frac{-2\sqrt{3} - 2i}{4i} = \frac{-\sqrt{3} - i}{2i} \cdot \frac{i}{i} = \frac{1 - \sqrt{3}i}{-2} = -\frac{1}{2} + \frac{\sqrt{3}}{2}i$$
Il modulo è $|z| = \sqrt{\left(-\frac{1}{2}\right)^2 + \left(\frac{\sqrt{3}}{2}\right)^2} = \sqrt{\frac{1}{4} + \frac{3}{4}} = 1$. L'argomento è $\theta = \frac{2}{3}\pi$. La forma esponenziale è:
$$z = \mathbf{e^{\frac{2}{3}\pi i}}$$

---

## Esercizio 4

Si consideri il gruppo $(\mathbb{Z}^3, +)$ e il seguente sottogruppo:
$$H = \{(x, y, z) \in \mathbb{Z}^3 \mid x + y + z \equiv 0 \pmod 4\}$$
Determinare tutti gli elementi del quoziente $\mathbb{Z}^3/H$.

### Soluzione
Gli elementi del quoziente sono quattro:
$$\mathbb{Z}^3/H = \mathbf{\{\overline{(0, 0, 0)}, \overline{(1, 0, 0)}, \overline{(2, 0, 0)}, \overline{(3, 0, 0)}\}}$$
Infatti, dato $(x,y,z) \in \mathbb{Z}^3$, indicando con $k \in \{0, 1, 2, 3\}$ il resto di $x+y+z \pmod 4$, si ha $(x,y,z) - (k,0,0) \in H$.

---

## ⚠️ Errori da evitare
- Non confondere l'iniettività con la suriettività nello studio delle applicazioni lineari tra spazi numerici o insiemi $\mathbb{Z}$.
- Prestare attenzione ai segni nel calcolo delle potenze di $i$ ($i^7 = i^3 = -i$).

---
## Materiale generato

### Riepilogo
Il documento raccoglie la risoluzione dettagliata di esercizi d'esame di Algebra per Informatica riguardanti insiemi e cardinalità, proprietà delle funzioni, numeri complessi in forma algebrica ed esponenziale, e gruppi quozienti.

### Esercizi simili

1. Siano $A = \{1, 2\}$ e $B = \{a, b, c, d\}$. Determinare la cardinalità dell'insieme delle funzioni $f: A \to B$ tali che $f(1) = a$.
   <details><summary>Soluzione</summary>Per il valore $f(1)$ c'è $1$ sola scelta obbligata ($a$), mentre per $f(2)$ ci sono $4$ scelte possibili in $B$. Essendo indipendenti, il totale è $1 \cdot 4 = \mathbf{4}$.</details>

2. Trovare tutte le soluzioni intere dell'equazione diofantea $12x + 18x = 6$ (nota: $12x + 18y = 6$).
   <details><summary>Soluzione</summary>Poiché $\text{MCD}(12, 18) = 6$ e $6 \mid 6$, le soluzioni esistono. Dividendo per $6$ si ottiene $2x + 3y = 1$. Una soluzione particolare è $(-1, 1)$, quindi la soluzione generale è $\mathbf{\{(-1 + 3k, 1 - 2k) \mid k \in \mathbb{Z}\}}$.</details>

3. Scrivere in forma algebrica il numero complesso $z = \frac{(1+i)^2}{1 - i}$.
   <details><summary>Soluzione</summary>Semplificando si ottiene $z = \mathbf{1 + i}$.</details>

### Flashcard
- **D:** Quando un'equazione diofantea lineare $ax + by = c$ ammette soluzioni intere? — **R:** Se e solo se $\text{MCD}(a,b) \mid c$.
- **D:** Qual è la cardinalità dell'insieme delle funzioni $B^A$? — **R:** $|B|^{|A|}$.
- **D:** Come si calcola il modulo di un numero complesso $z = a + ib$? — **R:** $|z| = \sqrt{a^2 + b^2}$.
