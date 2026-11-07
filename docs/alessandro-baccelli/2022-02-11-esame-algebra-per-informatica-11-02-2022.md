---
titolo: Esame di Algebra per Informatica - 11/02/2022
data: '2022-02-11'
studente: Alessandro Baccelli
materia: matematica
argomento: Algebra e Matematica Discreta
sottoargomenti:
- numeri complessi
- relazioni d'ordine e divisibilità
- applicazioni e controimmagini
- teoria dei gruppi
esercizi:
- 1
- 2
- 3
- 4
errori_tipici:
- Confondere la forma algebrica con la forma esponenziale di un numero complesso
- Confondere elementi minimali e massimali con minimo e massimo in un insieme parzialmente
  ordinato
- Non verificare le condizioni di esistenza di inverse sinistre e destre per funzioni
  non iniettive o non suriettive
fonte: https://drive.google.com/file/d/1zR59LvjpKncOcFr1BgcsrNJ-8mEqxDT1/view?usp=drivesdk
generato: '2026-11-07'
---

# Esame di Algebra per Informatica - 11/02/2022

## Formule chiave

- **Numero complesso in forma algebrica:** $z = a + ib$, con $a, b \in \mathbb{R}$ e $i^2 = -1$.
- **Forma esponenziale di un numero complesso:** $z = \rho e^{i\theta}$, dove $\rho = |z| = \sqrt{a^2 + b^2}$ è il modulo e $\theta = \arg(z)$ è l'argomento.
- **Relazione di divisibilità:** Siano $a, b \in A$, $a \triangleleft b \iff a \mid b \iff \exists k \in \mathbb{Z} \text{ tale che } b = ka$.
- **Controimmagine di un elemento $y$:** $f^{-1}(y) = \{x \in \mathbb{Z}^2 \mid f(x) = y\}$.
- **Inversa sinistra:** Un'applicazione $g: B \to A$ è un'inversa sinistra di $f: A \to B$ se $g \circ f = \text{id}_A$ (richiede $f$ iniettiva).
- **Inversa destra:** Un'applicazione $g: B \to A$ è un'inversa destra di $f: A \to B$ se $f \circ g = \text{id}_B$ (richiede $f$ suriettiva).

## Esercizio 1

Sia dato il numero complesso
$$z = \frac{(6 + 12i)(4 + 12i)}{(\sqrt{3} + i)^3}.$$
Scrivere $z$ in forma $a + ib$ con $a, b \in \mathbb{R}$ e in forma esponenziale.

**Svolgimento:**

1. Sviluppiamo il numeratore:
$$(6 + 12i)(4 + 12i) = 24 + 72i + 48i + 144i^2 = 24 + 120i - 144 = -120 + 120i.$$

2. Sviluppiamo il denominatore portando prima $(\sqrt{3} + i)$ in forma esponenziale:
$$\sqrt{3} + i = 2 \left(\frac{\sqrt{3}}{2} + \frac{1}{2}i\right) = 2 e^{i\pi/6}.$$
Elevando al cubo:
$$(\sqrt{3} + i)^3 = \left(2 e^{i\pi/6}\right)^3 = 8 e^{i\frac{\pi}{2}} = 8i.$$

3. Calcoliamo $z$:
$$z = \frac{-120 + 120i}{8i} = \frac{-120}{8i} + \frac{120i}{8i} = \frac{-15}{i} + 15 = 15i + 15 = 15 + 15i.$$
Forma algebrica: $\boxed{z = 15 + 15i}$.

4. Passiamo alla forma esponenziale:
- Modulo: $\rho = |z| = \sqrt{15^2 + 15^2} = \sqrt{225 + 225} = \sqrt{450} = 15\sqrt{2}$.
- Argomento: $\theta = \arctan\left(\frac{15}{15}\right) = \frac{\pi}{4}$ (poiché il numero si trova nel primo quadrante).

Forma esponenziale: $\boxed{z = 15\sqrt{2} e^{i\frac{\pi}{4}}}$.

---

## Esercizio 2

Si consideri l'insieme $A = \{2, 4, 5, 20, 25, 100\}$ con la seguente relazione d'ordine:
$$a \triangleleft b \iff a \mid b \text{ (cioè esiste } k \in \mathbb{Z} \text{ tale che } b = ka \text{)}.$$
Si determinino (se esistono) massimo, minimo, elementi minimali ed elementi massimali di $A$.

**Svolgimento:**

Analizziamo le relazioni di divisibilità tra gli elementi di $A$:
- $2 \mid 4$, $2 \mid 20$, $2 \mid 100$
- $4 \mid 20$, $4 \mid 100$
- $5 \mid 25$, $5 \mid 20$, $5 \mid 100$
- $20 \mid 100$
- $25 \mid 100$

Diagramma di Hasse (abbozzato):
- Elementi minimali (elementi da cui non parte alcuna freccia verso il basso, ovvero che non dividono nessun altro elemento se non se stessi): **$2$ e $5$**.
- Elementi massimali (elementi in cui non entra alcuna freccia dal basso, ovvero che non sono divisi da nessun altro elemento): **$100$**.
- Massimo: esiste ed è l'unico elemento massimale, ovvero $\boxed{100}$.
- Minimo: non esiste un unico elemento che divide tutti gli altri (poiché 2 e 5 sono incomparabili tra loro), quindi il minimo **non esiste**.

---

## Esercizio 3

Sia $f: \mathbb{Z}^2 \to \mathbb{Z}$ l'applicazione data da $f(x, y) = 24x - 20y$.

### 1. Determinare le seguenti controimmagini: $f^{-1}(10)$, $f^{-1}(8)$, $f^{-1}(f(5, 6))$.

- Per $f^{-1}(10)$: dobbiamo risolvere l'equazione diofantea $24x - 20y = 10$.
  Notiamo che il massimo comun divisore $\text{MCD}(24, -20) = 4$. Poiché $4 \nmid 10$, l'equazione non ammette soluzioni intere.
  Quindi: $\boxed{f^{-1}(10) = \emptyset}$.

- Per $f^{-1}(8)$: risolviamo $24x - 20y = 8$.
  Poiché $\text{MCD}(24, -20) = 4$ e $4 \mid 8$, l'equazione ammette soluzioni.
  Dividendo per 4 otteniamo: $6x - 5y = 2$.
  Una soluzione particolare si trova facilmente per tentativi o con l'identità di Bézout: per $x = 2, y = 2$ si ha $6(2) - 5(2) = 12 - 10 = 2$.
  La soluzione generale è quindi:
  $$\left\{ (2 + 5k, 2 + 6k) \mid k \in \mathbb{Z} \right\}$$
  Quindi: $\boxed{f^{-1}(8) = \{ (2 + 5k, 2 + 6k) \mid k \in \mathbb{Z} \}}$.

- Per $f^{-1}(f(5, 6))$: prima calcoliamo $f(5, 6) = 24(5) - 20(6) = 120 - 120 = 0$.
  Dobbiamo quindi risolvere $24x - 20y = 0$, ovvero $24x = 20y \implies 6x = 5y$.
  Poiché $\text{MCD}(6, 5) = 1$, le soluzioni sono della forma $x = 5k, y = 6k$ con $k \in \mathbb{Z}$.
  Quindi: $\boxed{f^{-1}(f(5, 6)) = \{ (5k, 6k) \mid k \in \mathbb{Z} \}}$.

### 2. Determinare (se esistono) un'inversa sinistra e un'inversa destra per $f$.

- **Inversa sinistra:** Esiste se e solo se $f$ è iniettiva. Verifichiamo l'iniettività: $f(x, y) = 0$ ha infinite soluzioni (es. $(5k, 6k)$), quindi $f$ non è iniettiva (il nucleo non è banale). Di conseguenza, **l'inversa sinistra non esiste**.
- **Inversa destra:** Esiste se e solo se $f$ è suriettiva. L'immagine di $f$ è data dai multipli del $\text{MCD}(24, -20) = 4$, ovvero $\text{Im}(f) = 4\mathbb{Z} \neq \mathbb{Z}$. Poiché $f$ non è suriettiva, **l'inversa destra non esiste**.

---

## Esercizio 4

Determinare tutti i sottogruppi di $(U(\mathbb{Z}_8), \cdot, \bar{1})$.

**Svolgimento:**

1. Determiniamo l'insieme $U(\mathbb{Z}_8)$ (gli elementi invertibili modulo 8):
   $$U(\mathbb{Z}_8) = \{ \bar{1}, \bar{3}, \bar{5}, \bar{7} \}.$$
   L'ordine del gruppo è $|U(\mathbb{Z}_8)| = 4$.

2. Calcoliamo gli ordini degli elementi (verificando i potenziamenti modulo 8):
   - $\bar{1}^1 = \bar{1}$ (ordine 1)
   - $\bar{3}^2 = \bar{9} \equiv \bar{1} \pmod 8$ (ordine 2)
   - $\bar{5}^2 = \bar{25} \equiv \bar{1} \pmod 8$ (ordine 2)
   - $\bar{7}^2 = \bar{49} \equiv \bar{1} \pmod 8$ (ordine 2)

3. Per il teorema di Lagrange, i sottogruppi possono avere solo ordine che divide 4 (quindi ordini 1, 2 o 4):
   - Sottogruppo banale di ordine 1: $H_0 = \{ \bar{1} \}$
   - Sottogruppi di ordine 2 (generati dagli elementi di ordine 2):
     - $H_1 = \langle \bar{3} \rangle = \{ \bar{1}, \bar{3} \}$
     - $H_2 = \langle \bar{5} \rangle = \{ \bar{1}, \bar{5} \}$
     - $H_3 = \langle \bar{7} \rangle = \{ \bar{1}, \bar{7} \}$
   - Sottogruppo improprio di ordine 4: $H_4 = U(\mathbb{Z}_8) = \{ \bar{1}, \bar{3}, \bar{5}, \bar{7} \}$

Elenco di tutti i sottogruppi: $\boxed{\{ \bar{1} \}, \{ \bar{1}, \bar{3} \}, \{ \bar{1}, \bar{5} \}, \{ \bar{1}, \bar{7} \}, U(\mathbb{Z}_8)}$.

---

## Materiale generato

### Riepilogo
Il documento affronta lo svolgimento completo di un esame di Algebra per Informatica, spaziando dai numeri complessi in forma trigonometrica/esponenziale, alle relazioni d'ordine parziale, passando per la risoluzione di equazioni diofantee e lo studio di proprietà delle applicazioni, fino alla determinazione dei sottogruppi di gruppi moltiplicativi di classi resto.

### Esercizi simili
1. Dato il numero complesso $z = \frac{(1 + i)^4}{1 - i\sqrt{3}}$, scriverlo in forma $a + ib$ e in forma esponenziale.
   <details><summary>Soluzione</summary>Calcolando le potenze si ottiene $z = -\frac{1}{2} - \frac{\sqrt{3}}{2}i = e^{i\frac{4\pi}{3}}$.</details>

2. Sia $f: \mathbb{Z}^2 \to \mathbb{Z}$ definita da $f(x, y) = 15x - 25y$. Determinare $f^{-1}(10)$ e stabilire se $f$ ammette inversa destra.
   <details><summary>Soluzione</summary>$\text{MCD}(15, -25) = 5$. Poiché $5 \mid 10$, $f^{-1}(10)$ non è vuota (soluzione generale: $(2 + 5k, 1 + 3k)$). L'inversa destra non esiste poiché l'applicazione non è suriettiva ($\text{Im}(f) = 5\mathbb{Z} \neq \mathbb{Z}$).</details>

3. Determinare tutti i sottogruppi del gruppo moltiplicativo $(U(\mathbb{Z}_{10}), \cdot, \bar{1})$.
   <details><summary>Soluzione</summary>$U(\mathbb{Z}_{10}) = \{\bar{1}, \bar{3}, \bar{7}, \bar{9}\}$. I sottogruppi sono $\{\bar{1}\}$, $\{\bar{1}, \bar{9}\}$, $\{\bar{1}, \bar{3}, \bar{7}, \bar{9}\}$ (notare che $\langle\bar{3}\rangle = \{\bar{1}, \bar{3}, \bar{7}, \bar{9}\}$ perché $\bar{3}$ è generatore di tutto il gruppo).</details>

### Flashcard
- **D:** Quando un'equazione diofantea $ax + by = c$ ammette soluzioni intere? — **R:** Se e solo se $\text{MCD}(a, b)$ divide $c$.
- **D:** Qual è la condizione necessaria e sufficiente affinché un'applicazione abbia un'inversa sinistra? — **R:** L'applicazione deve essere iniettiva.
- **D:** Come si passa da un numero complesso in forma algebrica $a + ib$ a quella esponenziale $\rho e^{i\theta}$? — **R:** Calcolando il modulo $\rho = \sqrt{a^2 + b^2}$ e l'argomento $\theta = \arctan(b/a)$ (tenendo conto del quadrante).
- **D:** In un insieme parzialmente ordinato, il massimo è sempre un elemento massimale? — **R:** Sì, se il massimo esiste è unico ed è anche l'unico elemento massimale dell'insieme.
