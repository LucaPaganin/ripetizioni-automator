---
titolo: Esame di Algebra per Informatica - 14/07/2022
data: '2022-07-14'
studente: Alessandro Baccelli
materia: matematica
argomento: Algebra e Matematica Discreta
sottoargomenti:
- Teoria degli insiemi
- Funzioni
- Aritmetica modulare
- Monoidi
esercizi:
- 1
- 2
- 3
- 4
errori_tipici:
- Confusione tra cardinalità dell'insieme delle parti e numero di funzioni tra due
  insiemi
- Errata verifica dell'iniettività e suriettività di funzioni in campo complesso
- Confusione tra inverso additivo e inverso moltiplicativo in un anello/monoide
fonte: https://drive.google.com/file/d/18RMdva6VSDJDwFYPuE356AEJ2LH9FjVE/view?usp=drivesdk
generato: '2026-11-07'
---

# Esame di Algebra per Informatica - 14/07/2022

## Formule chiave
- **Numero di funzioni tra due insiemi finiti $A$ e $B$**: Siano $|A| = n$ e $|B| = m$. Il numero di funzioni $f: A \to B$ è dato da $|B|^{|A|} = m^n$.
- **Operazioni in $\mathbb{Z}_n$**: L'aritmetica modulare si basa sulle classi resto modulo $n$.
- **Elemento inverso in un monoide $(M, \cdot, e)$**: Un elemento $a \in M$ è invertibile se esiste $b \in M$ tale che $a \cdot b = b \cdot a = e$.

---

## Esercizio 1
Siano dati gli insiemi $A = \{1, 2, 3, 4, 5\}$ e $B = \{4, 5, 6\}$. Determinare la cardinalità degli insiemi seguenti:

1. $R = \{f : A \to B\}$
   $$\text{Card}(R) = |B|^{|A|} = 3^5 = 243$$

2. $S = \{f : B \to A\}$
   $$\text{Card}(S) = |A|^{|B|} = 5^3 = 125$$

3. $T = \{f : A \cap B \to B\}$
   Prima calcoliamo $A \cap B = \{4, 5\}$, quindi $|A \cap B| = 2$.
   $$\text{Card}(T) = |B|^{|A \cap B|} = 3^2 = 9$$

4. $Z = (A \cup B) \setminus (A \cap B)$
   Abbiamo $A \cup B = \{1, 2, 3, 4, 5, 6\}$ (cardinalità 6) e $A \cap B = \{4, 5\}$ (cardinalità 2).
   L'insieme $Z$ rappresenta la differenza simmetrica $A \Delta B$:
   $$Z = \{1, 2, 3, 6\} \implies \text{Card}(Z) = 4$$

---

## Esercizio 2
Si consideri la seguente funzione:
$$f : \mathbb{C} \longrightarrow \mathbb{C}$$
$$z \longmapsto z^2 + z$$

### 1. Determinare se $f$ è iniettiva e/o suriettiva.
- **Iniettività**: Verifichiamo se $f(z_1) = f(z_2) \implies z_1 = z_2$.
  $$z_1^2 + z_1 = z_2^2 + z_2 \implies z_1^2 - z_2^2 + z_1 - z_2 = 0 \implies (z_1 - z_2)(z_1 + z_2 + 1) = 0$$
  Questo è verificato se $z_1 = z_2$ oppure se $z_1 + z_2 + 1 = 0$. Ad esempio, per $z_1 = 0$ e $z_2 = -1$ si ha $f(0) = 0$ e $f(-1) = (-1)^2 - 1 = 0$. Poiché $f(0) = f(-1)$ con $0 \neq -1$, **la funzione non è iniettiva**.

- **Suriettività**: Dobbiamo determinare se per ogni $w \in \mathbb{C}$ esiste $z \in \mathbb{C}$ tale che $z^2 + z = w$, ovvero $z^2 + z - w = 0$.
  Calcoliamo il discriminante: $\Delta = 1 - 4(-w) = 1 + 4w$.
  Poiché in $\\mathbb{C}$ ogni numero ammette radice quadrata, l'equazione ammette sempre almeno una soluzione $z$ per ogni $w \in \mathbb{C}$. Pertanto, **la funzione è suriettiva**.

### 2. Calcolare $f^{-1}\left(-\frac{5}{2}\right)$
Cerchiamo i valori di $z \in \mathbb{C}$ tali che $f(z) = -\frac{5}{2}$:
$$z^2 + z = -\frac{5}{2} \implies 2z^2 + 2z + 5 = 0$$
Utilizziamo la formula ridotta o classica per le equazioni di secondo grado:
$$z = \frac{-2 \pm \sqrt{4 - 4(2)(5)}}{4} = \frac{-2 \pm \sqrt{4 - 40}}{4} = \frac{-2 \pm \sqrt{-36}}{4} = \frac{-2 \pm 6i}{4} = -\frac{1}{2} \pm \frac{3}{2}i$$
Risultato finale:
$$\boxed{\left\{-\frac{1}{2} + \frac{3}{2}i, -\frac{1}{2} - \frac{3}{2}i\right\}}$$

---

## Esercizio 3
Calcolare la seguente espressione in $\mathbb{Z}_{21}$:
$$\bar{4}^{50} + \bar{6} \cdot \bar{7} + \bar{3}^3$$

Semplifichiamo i singoli termini modulo $21$:
- Per $\bar{4}^{50}$: Notiamo che $4^3 = 64 = 3 \cdot 21 + 1 \equiv \bar{1} \pmod{21}$.
  Quindi $\bar{4}^{50} = \bar{4}^{3 \cdot 16 + 2} = (\bar{4}^3)^{16} \cdot \bar{4}^2 = \bar{1}^{16} \cdot \overline{16} = \overline{16}$.
- Per $\bar{6} \cdot \bar{7}$:
  $$\bar{6} \cdot \bar{7} = \bar{42} = \bar{0} \pmod{21}$$
- Per $\bar{3}^3$:
  $$\bar{3}^3 = \bar{27} = \overline{21 + 6} = \bar{6}$$

Sommiamo i risultati ottenuti:
$$\overline{16} + \bar{0} + \bar{6} = \overline{22} = \bar{1} \pmod{21}$$

Risultato finale:
$$\boxed{\bar{1}}$$

---

## Esercizio 4
Determinare (se esiste) l'inverso dei seguenti elementi nei monoidi assegnati:

1. $\bar{3}$ nel monoide $(\mathbb{Z}_{15}, +, \bar{0})$
   L'inverso additivo di $\bar{3}$ è l'elemento che sommato a $\bar{3}$ dà $\bar{0}$.
   $$\bar{3} + \bar{x} = \bar{0} \implies \bar{x} = -\bar{3} = \overline{12}$$
   Risultato: **$\overline{12}$**

2. $\bar{3}$ nel monoide $(\mathbb{Z}_{15}, \cdot, \bar{1})$
   L'inverso moltiplicativo esiste se e solo se $\text{MCD}(3, 15) = 1$. Poiché $\text{MCD}(3, 15) = 3 \neq 1$, l'inverso **non esiste**.

3. $\bar{4}$ nel monoide $(\mathbb{Z}_{15}, \cdot, \bar{1})$
   Verifichiamo il MCD: $\text{MCD}(4, 15) = 1$, quindi l'inverso esiste.
   Cerchiamo $\bar{x}$ tale che $\bar{4} \cdot \bar{x} = \bar{1} \pmod{15}$.
   Notiamo che $4 \cdot 4 = 16 \equiv 1 \pmod{15}$, quindi l'inverso di $\bar{4}$ è $\bar{4}$ stesso.
   Risultato: **$\bar{4}$**

4. $f : \mathbb{Z} \to \mathbb{Z}$ tale che $f(x) = x + 1$ nel monoide $(\mathbb{Z}^\mathbb{Z}, \circ, \text{id}_\mathbb{Z})$
   L'inverso rispetto alla composizione di funzioni deve essere la funzione inversa $f^{-1}$ tale che $f \circ f^{-1} = f^{-1} \circ f = \text{id}_\mathbb{Z}$.
   Ricaviamo l'inversa ponendo $y = x + 1 \implies x = y - 1$, quindi $f^{-1}(x) = x - 1$.
   Risultato: **$f^{-1}(x) = x - 1$**

---

## Materiale generato

### Riepilogo
Il documento affronta esercizi fondamentali di matematica discreta: calcolo combinatorio di funzioni, analisi di iniettività e suriettività nel campo complesso, aritmetica modulare in $\mathbb{Z}_{21}$ e determinazione di elementi inversi in strutture algebriche (somma, prodotto modulare e composizione di funzioni).

### Esercizi simili

1. Siano $A = \{1, 2, 3\}$ e $B = \{a, b\}$. Determinare la cardinalità dell'insieme delle funzioni $f: A \to B$.
<details><summary>Soluzione</summary>
La cardinalità è data da $|B|^{|A|} = 2^3 = 8$.
</details>

2. Calcolare la seguente espressione in $\mathbb{Z}_{12}$:
   $$\bar{5}^{25} + \bar{3} \cdot \bar{4}$$
<details><summary>Soluzione</summary>
Si ha $5^2 = 25 \equiv 1 \pmod{12}$. Quindi $\bar{5}^{25} = (\bar{5}^2)^{12} \cdot \bar{5} = \bar{1}^{12} \cdot \bar{5} = \bar{5}$.
Inoltre $\bar{3} \cdot \bar{4} = \bar{12} = \bar{0}$.
Sommando: $\bar{5} + \bar{0} = \bar{5}$. Risultato: $\boxed{\bar{5}}$
</details>

3. Determinare (se esiste) l'inverso moltiplicativo di $\bar{5}$ nel monoide $(\mathbb{Z}_{12}, \cdot, \bar{1})$.
<details><summary>Soluzione</summary>
Poiché $\text{MCD}(5, 12) = 1$, l'inverso esiste. Cerchiamo $\bar{x}$ tale che $5x \equiv 1 \pmod{12}$. Tentando i valori, $5 \cdot 5 = 25 \equiv 1 \pmod{12}$. L'inverso è $\bar{5}$.
</details>

### Flashcard
- **D:** Come si calcola il numero di funzioni possibili da un insieme $A$ a un insieme $B$? — **R:** Si calcola elevando la cardinalità dell'insieme di arrivo $B$ alla cardinalità dell'insieme di partenza $A$ ($|B|^{|A|}$).
- **D:** Quando un elemento in un monoide moltiplicativo $\mathbb{Z}_n$ possiede un inverso? — **R:** Quando il massimo comun divisore tra l'elemento e il modulo $n$ è pari a $1$ ($\text{MCD}(a, n) = 1$).
- **D:** Qual è la differenza tra l'inverso additivo e l'inverso moltiplicativo di $\bar{3}$ in $\mathbb{Z}_{15}$? — **R:** L'inverso additivo è $\overline{12}$ (perché $3 + 12 = 15 \equiv 0$), mentre l'inverso moltiplicativo non esiste perché $\text{MCD}(3, 15) = 3 \neq 1$.
