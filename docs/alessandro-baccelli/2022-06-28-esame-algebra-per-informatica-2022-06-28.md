---
titolo: Esame di Algebra per Informatica
data: '2022-06-28'
studente: Alessandro Baccelli
materia: matematica
argomento: Algebra e Matematica Discreta
sottoargomenti:
- Teoria degli insiemi
- Funzioni (iniettività e suriettività)
- Numeri complessi
- Gruppi e sottogruppi quozienti
esercizi:
- 1
- 2
- 3
- 4
errori_tipici: []
fonte: https://drive.google.com/file/d/1EpLuMDF4VKBmuaTkkE1Ye6EG5gxSi1kF/view?usp=drivesdk
generato: '2026-11-07'
---

# Esame di Algebra per Informatica (28/06/2022)

## Formule chiave

- **Cardinalità delle funzioni:** Dati due insiemi finiti $A$ e $B$, il numero di funzioni possibili da $A$ a $B$ è $|B|^{|A|}$.
- **Intersezione e Unione:** Dati due insiemi $A = \{a, b, c\}$ e $B = \{1, 2\}$, essendo insiemi disgiunti, l'intersezione $A \cap B = \emptyset$.
- **Iniettività e Suriettività di funzioni lineari in $\mathbb{Z}$:** 
  - $f: \mathbb{Z} \to \mathbb{Z}$ con $f(x) = ax$ è iniettiva se $a \neq 0$, ed è suriettiva se e solo se $a = \pm 1$.
- **Forma esponenziale di un numero complesso:** $z = |z| e^{i\theta}$.
- **Teorema fondamentale dell'omomorfismo / Gruppo quoziente:** Per un gruppo abeliano $(G, +)$ e un sottogruppo $H$, il quoziente $G/H$ è formato dalle classi laterali $[g] = g + H$.

---

## Esercizio 1

Siano dati gli insiemi $A = \{a, b, c\}$ e $B = \{1, 2\}$. Determinare la cardinalità degli insiemi seguenti:

1. $R = \{f : A \to B\}$;
   $$\text{card}(R) = |B|^{|A|} = 2^3 = \boxed{8}$$

2. $S = A \cap B$;
   Poiché $A = \{a, b, c\}$ e $B = \{1, 2\}$ non hanno elementi in comune, $A \cap B = \emptyset$, quindi:
   $$\text{card}(S) = \boxed{0}$$

3. $T = \{f : A \to B : f(a) = f(b)\}$;
   Per determinare tali funzioni, scegliamo prima il valore comune per $f(a)$ e $f(b)$: ci sono $2$ possibilità (può essere $1$ oppure $2$). 
   Successivamente, per l'elemento $c$, abbiamo $2$ scelte possibili in $B$.
   Quindi:
   $$\text{card}(T) = 2 \times 2 = \boxed{4}$$

4. $Z = (A \cup B) \setminus (A \cap B)$.
   Poiché $A$ e $B$ sono disgiunti ($A \cap B = \emptyset$), $(A \cup B) \setminus (A \cap B) = A \cup B$.
   La cardinalità dell'unione di due insiemi disgiunti è la somma delle cardinalità:
   $$\text{card}(Z) = |A| + |B| = 3 + 2 = \boxed{5}$$

---

## Esercizio 2

Si considerino le seguenti funzioni:
$$f : \mathbb{Z} \to \mathbb{Z}, \quad x \mapsto 15x$$
$$g : \mathbb{Z} \times \mathbb{Z} \to \mathbb{Z}, \quad (x, y) \mapsto 15x + 22y$$

1. **Determinare se $f$ è iniettiva e/o suriettiva.**
   - **Iniettività:** Se $f(x_1) = f(x_2)$, allora $15x_1 = 15x_2 \implies x_1 = x_2$. Quindi $f$ è **iniettiva**.
   - **Suriettività:** Cerchiamo se per ogni $y \in \mathbb{Z}$ esiste $x \in \mathbb{Z}$ tale che $15x = y$. Ad esempio, per $y = 1$, $x = \frac{1}{15} \notin \mathbb{Z}$. Quindi $f$ **non è suriettiva**.

2. **Calcolare $f^{-1}(30)$.**
   $$15x = 30 \implies x = 2$$
   $$\text{card}(f^{-1}(30)) = \{2\} \quad \text{ovvero } \boxed{2}$$

3. **Determinare se $g$ è iniettiva e/o suriettiva.**
   - **Iniettività:** Poiché il dominio ha dimensione 2 ($\mathbb{Z} \times \mathbb{Z}$) e il codominio ha dimensione 1 ($\mathbb{Z}$), la funzione non può essere iniettiva (es. $15(22) + 22(-15) = 0 = g(0,0)$). Quindi $g$ **non è iniettiva**.
   - **Suriettività:** Poiché $\text{MCD}(15, 22) = 1$, l'equazione $15x + 22y = c$ ammette sempre soluzioni intere per ogni $c \in \mathbb{Z}$ (per il Lemma di Bezout). Pertanto, per ogni elemento del codominio esiste una controimmagine. Quindi $g$ è **suriettiva**.

4. **Calcolare $g^{-1}(30)$.**
   Cerchiamo tutte le coppie $(x, y) \in \mathbb{Z} \times \mathbb{Z}$ tali che:
   $$15x + 22y = 30$$
   Una soluzione particolare si nota facilmente: per $x = 2, y = 0$, $15(2) + 22(0) = 30$.
   La soluzione generale dell'equazione diofantea è:
   $$x = 2 + 22k$$
   $$y = 0 - 15k$$
   con $k \in \mathbb{Z}$.
   $$\text{Pertanto: } g^{-1}(30) = \boxed{\{(2 + 22k, -15k) \mid k \in \mathbb{Z}\}}$$

---

## Esercizio 3

Sia dato il numero complesso:
$$z = \frac{(1 + i\sqrt{3})(-\sqrt{3} + i)}{i^7 (1 + i)^4}$$

Scriviamo numeratore e denominatore in forma trigonometrica/esponenziale o sviluppiamo direttamente:

- **Numeratore:**
  $1 + i\sqrt{3} = 2 \left(\frac{1}{2} + i\frac{\sqrt{3}}{2}\right) = 2 e^{i\frac{\pi}{3}}$
  $-\sqrt{3} + i = 2 \left(-\frac{\sqrt{3}}{2} + i\frac{1}{2}\right) = 2 e^{i\frac{5\pi}{6}}$
  Prodotto numeratore: $2 \cdot 2 \cdot e^{i(\frac{\pi}{3} + \frac{5\pi}{6})} = 4 e^{i\frac{7\pi}{6}}$

- **Denominatore:**
  $i^7 = i^3 = -i = e^{-i\frac{\pi}{2}}$
  $(1 + i)^4 = \left(\sqrt{2} e^{i\frac{\pi}{4}}\right)^4 = (\sqrt{2})^4 e^{i\pi} = 4 e^{i\pi} = -4$
  Denominatore: $(-i)(-4) = 4i = 4 e^{i\frac{\pi}{2}}$

- **Calcolo di $z$:**
  $$z = \frac{4 e^{i\frac{7\pi}{6}}}{4 e^{i\frac{\pi}{2}}} = e^{i\left(\frac{7\pi}{6} - \frac{\pi}{2}\right)} = e^{i\left(\frac{7\pi - 3\pi}{6}\right)} = e^{i\frac{4\pi}{6}} = e^{i\frac{2\pi}{3}}$$

- **Forma esponenziale:**
  $$z = \boxed{e^{i\frac{2\pi}{3}}}$$

- **Forma $a + ib$:**
  $$z = \cos\left(\frac{2\pi}{3}\right) + i\sin\left(\frac{2\pi}{3}\right) = -\frac{1}{2} + i\frac{\sqrt{3}}{2}$$
  $$\boxed{z = -\frac{1}{2} + i\frac{\sqrt{3}}{2}}$$

---

## Esercizio 4

Si consideri il gruppo $(\mathbb{Z}^3, +)$ e il sottogruppo:
$$H = \{(x, y, z) \in \mathbb{Z}^3 : x + y + z \equiv 0 \pmod 4\}$$

Determinare tutti gli elementi del quoziente $\mathbb{Z}^3 / H$.

Consideriamo l'applicazione $\phi: \mathbb{Z}^3 \to \mathbb{Z}_4$ definita da:
$$\phi(x, y, z) = [x + y + z]_4$$
È un omomorfismo di gruppi suriettivo il cui nucleo $\ker(\phi)$ è esattamente $H$.
Per il Primo Teorema di Isomorfismo per i gruppi:
$$\mathbb{Z}^3 / H \cong \text{Im}(\phi) = \mathbb{Z}_4$$

Il gruppo quoziente $\mathbb{Z}^3 / H$ è isomorfo a $\mathbb{Z}_4$, e i suoi elementi sono le classi laterali individuate dai possibili resti della somma $x+y+z$ modulo 4:
$$\mathbb{Z}^3 / H = \boxed{\{H, (1,0,0) + H, (2,0,0) + H, (3,0,0) + H\}} \quad (\text{o equivalentemente } \{[0], [1], [2], [3]\} \text{ in }\mathbb{Z}_4)$$

---

## Materiale generato

### Riepilogo
La prova affronta temi fondamentali di matematica discreta: cardinalità di insiemi e spazi di funzioni, proprietà di iniettività e suriettività con equazioni diofantee, calcolo con numeri complessi in forma esponenziale e determinazione di gruppi quozienti tramite omomorfismi.

### Esercizi simili

1. Siano dati gli insiemi $A = \{1, 2\}$ e $B = \{a, b, c, d\}$. Determinare la cardinalità di $R = \{f : A \to B\}$.
   <details><summary>Soluzione</summary>
   $\text{card}(R) = |B|^{|A|} = 4^2 = 16$.
   </details>

2. Si consideri la funzione $f : \mathbb{Z} \to \mathbb{Z}$ definita da $f(x) = 7x$. Determinare se è iniettiva, suriettiva e calcolare $f^{-1}(21)$.
   <details><summary>Soluzione</summary>
   La funzione è iniettiva (se $7x_1 = 7x_2 \implies x_1 = x_2$) ma non suriettiva (es. $7x = 1$ non ha soluzioni intere). 
   Per calcolare $f^{-1}(21)$: $7x = 21 \implies x = 3$, quindi $f^{-1}(21) = \{3\}$.
   </details>

3. Scrivere in forma cartesiana $a + ib$ il numero complesso $z = \frac{(1+i)^2}{1 - i}$.
   <details><summary>Soluzione</summary>
   $(1+i)^2 = 1 + 2i - 1 = 2i$. 
   Quindi $z = \frac{2i}{1-i} = \frac{2i(1+i)}{(1-i)(1+i)} = \frac{2i - 2}{1 + 1} = \frac{-2 + 2i}{2} = -1 + i$.
   </details>

### Flashcard
- **D:** Come si calcola il numero di funzioni possibili tra due insiemi finiti $A$ e $B$? — **R:** Con la formula $|B|^{|A|}$, dove la base è la cardinalità del codominio e l'esponente quella del dominio.
- **D:** Quando una funzione lineare intera $f(x) = ax$ su $\mathbb{Z}$ è suriettiva? — **R:** Solo quando $a = 1$ oppure $a = -1$.
- **D:** Come si risolve l'equazione diofantea $ax + by = c$? — **R:** Verificando che $\text{MCD}(a, b)$ divida $c$, trovando una soluzione particolare tramite l'Algoritmo di Euclide esteso, e aggiungendo la soluzione generale dell'omogenea.
- **D:** Qual è la relazione tra il nucleo di un omomorfismo $\phi: G \to G'$ e il gruppo quoziente? — **R:** Per il teorema fondamentale dell'isomorfismo, $G / \ker(\phi) \cong \text{Im}(\phi)$.
