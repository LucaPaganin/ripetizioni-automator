---
titolo: 'Algebra per Informatica: Esame del 11/02/2021'
data: '2021-02-11'
studente: Alessandro Baccelli
materia: matematica
argomento: Algebra, Teoria degli Insiemi, Strutture Algebriche
sottoargomenti:
- Relazioni di equivalenza e insiemi quoziente
- Funzioni iniettive e suriettive
- Poset e elementi minimali/massimali
- Gruppi e isomorfismi
esercizi:
- 1
- 2
- 3
- 4
errori_tipici:
- Confondere elementi massimali con l'elemento massimo di un poset
- Confondere gruppi isomorfi basandosi solo sulla cardinalità senza verificare l'ordine
  degli elementi
fonte: https://drive.google.com/file/d/1ij6Hx1GsI-0E3CBU8hKc2M50gamlSqzD/view?usp=drivesdk
generato: '2026-11-07'
---

# Algebra per Informatica: Esame del 11/02/2021

## Formule chiave

- **Relazione di equivalenza diagonale:** Data una relazione $x \sim_1 y \iff x = y$, le classi di equivalenza sono singoletti e l'insieme quoziente ha cardinalità $|A|$.
- **Funzione suriettiva:** $f: A \to B$ è suriettiva se $\forall b \in B, \exists a \in A$ tale che $f(a) = b$.
- **Elementi minimali e massimali:** 
  - $m$ è minimale se non esiste $x$ tale che $x < m$.
  - $M$ è massimale se non esiste $x$ tale che $M < x$.
- **Gruppi ciclici e isomorfismi:** Due gruppi finiti di uguale cardinalità non sono necessariamente isomorfi; l'isomorfismo richiede la conservazione dell'ordine degli elementi. Ad esempio, $U_4 \not\cong \mathbb{Z}_2 \times \mathbb{Z}_2$ perché $U_4$ contiene elementi di ordine 4 (come $i$), mentre $\mathbb{Z}_2 \times \mathbb{Z}_2$ ha esponente 2.

## Esercizio 1

Sia dato l'insieme $A = \{1, 2, 3, 4, 5, 6, 7, 8\}$. Si determini la cardinalità dei seguenti insiemi:
1. $R = A/\sim_1$, dove $\sim_1$ è la relazione d'equivalenza diagonale ($x \sim_1 y \iff x = y$).
2. $S = A/\sim_2$, dove $\sim_2$ è data da $x \sim_2 y \iff x - y = 5k$ con $k \in \mathbb{Z}$.
3. $T = \{f : A \to A \mid f(1) = f(2) = f(3) = 7\}$.

**Soluzione:**
- (i) Siccome $x \sim_1 y \iff x = y$, ciascuna classe di equivalenza consiste di un solo elemento. Quindi $|R| = |A| = \boxed{8}$.
- (ii) Le classi di equivalenza nel quoziente $S = A/\sim_2$ sono 5: $\bar{1} = \{1,6\}$, $\bar{2} = \{2,7\}$, $\bar{3} = \{3,8\}$, $\bar{4} = \{4\}$, $\bar{5} = \{5\}$. Quindi si ha $|S| = \boxed{5}$.
- (iii) Per una funzione $f \in T$ si ha 1 scelta obbligata per $f(1), f(2), f(3)$, e 8 possibili scelte per ciascuno dei restanti 5 elementi del dominio. Quindi $|T| = 1^3 \cdot 8^5 = \boxed{8^5}$.

## Esercizio 2

Si considerino le funzioni:
1. $f: \mathbb{C} \to \mathbb{C}$ tale che $f(x) = x^3$.
2. $g: \mathbb{Z}^2 \to \mathbb{Z}$ tale che $g(x,y) = 91x - 84y$.

Si determini se ciascuna funzione è iniettiva e/o surgettiva.

**Soluzione:**
- (i) La funzione $f$ **non è iniettiva** (es. $f(1) = f(-\frac{1}{2} + i\frac{\sqrt{3}}{2}) = 1$). La funzione $f$ **è surgettiva** poiché ogni numero complesso ammette radici cubiche.
- (ii) La funzione $g$ **non è iniettiva** (es. $g(0,0) = g(84,91) = 0$). La funzione $g$ **non è surgettiva** poiché l'immagine è l'ideale generato da $\text{MCD}(91, 84) = 7$, quindi i numeri non divisibili per 7 (come il 2) non appartengono all'immagine.

## Esercizio 3

Si consideri $T = \{1, 2, 3, 4, 5\}$ ed il poset $(\mathcal{P}(T), \subseteq)$. Sia dato il sottoinsieme:
$$A = \{\emptyset, \{1\}, \{4\}, \{1, 2\}, \{2, 3\}, \{1, 2, 3, 5\}\}$$

Si determinino gli elementi minimali, massimali, massimo e minimo di $A$.

**Soluzione:**
- L'insieme $A$ ammette un unico elemento minimale e minimo che è $\boxed{\emptyset}$.
- L'insieme $A$ ha due elementi massimali non confrontabili: $\boxed{\{4\}}$ e $\boxed{\{1, 2, 3, 5\}}$.
- Poiché ci sono più elementi massimali, $\boxed{A \text{ non ammette massimo}}$.

## Esercizio 4

Si considerino i quattro gruppi:
1. $(U_4, \cdot)$ dove $U_4 = \{1, -1, i, -i\}$
2. $(\mathbb{Z}_2, +)$
3. $(\mathbb{Z}_2 \times \mathbb{Z}_2, +)$
4. $(U(\mathbb{Z}_6), \cdot)$ dove $U(\mathbb{Z}_6)$ sono gli elementi invertibili di $\mathbb{Z}_6$.

Si determinino le coppie di gruppi isomorfi.

**Soluzione:**
- Gli ordini dei gruppi sono: $|U_4| = 4$, $|\mathbb{Z}_2| = 2$, $|\mathbb{Z}_2 \times \mathbb{Z}_2| = 4$, $|U(\mathbb{Z}_6)| = \phi(6) = 2$.
- $U_4$ ha elementi di ordine 4 (es. $i$), mentre $\mathbb{Z}_2 \times \mathbb{Z}_2$ ha esponente 2, quindi non sono isomorfi.
- $U(\mathbb{Z}_6) = \{\bar{1}, \bar{5}\}$ ed è isomorfo a $\mathbb{Z}_2$, tramite l'isomorfismo $\varphi(0) = \bar{1}$, $\varphi(1) = \bar{5}$.
- Pertanto, l'unica coppia di gruppi isomorfi tra quelli dati è $\boxed{U(\mathbb{Z}_6) \text{ e } \mathbb{Z}_2 \text{ sono isomorfi}}$.

---

## Materiale generato

### Riepilogo
Il documento analizza relazioni d'equivalenza con calcolo di cardinalità quozienti, proprietà di iniettività e suriettività di funzioni in $\mathbb{C}$ e $\mathbb{Z}^2$, elementi notevoli nei poset tramite diagrammi di Hasse, e classificazione di gruppi finiti tramite isomorfismi e ordini degli elementi.

### Esercizi simili
1. Sia $A = \{1, 2, 3, 4, 6, 12\}$. Si determini la cardinalità del quoziente $A/\sim$ definito da $x \sim y \iff x \mid y$ e $y \mid x$ (relazione d'ordine associata).
   <details><summary>Soluzione</summary>La relazione è d'antisimmetria sugli elementi associati o semplicemente l'identità se ristretta ai divisori in modo opportuno; qui la relazione d'equivalenza associata è $x \sim y \iff x = y$ (poiché antisimmetrica), quindi la cardinalità è $|A| = 6$. (Nota: se si intende la relazione d'equivalenza derivata da un preordine, va ridefinita, ma con l'antisimmetria la classe di ogni elemento ha cardinalità 1, dunque il quoziente ha cardinalità 6).</details>

2. Si consideri la funzione $h: \mathbb{Z} \to \mathbb{Z}$ definita da $h(x) = 3x - 6$. Stabilire se $h$ è iniettiva e/o suriettiva.
   <details><summary>Soluzione</summary>Iniettiva: se $3x_1 - 6 = 3x_2 - 6$, allora $3x_1 = 3x_2 \implies x_1 = x_2$ (Sì). Suriettiva: $3x - 6 = y \implies 3x = y + 6 \implies x = \frac{y+6}{3}$, che non è sempre un intero (es. per $y = 1$) (No).</details>

3. Determinare gli elementi invertibili del monoide moltiplicativo $(\mathbb{Z}_8, \cdot)$ e verificare se il gruppo $U(\mathbb{Z}_8)$ è isomorfo a $\mathbb{Z}_2 \times \mathbb{Z}_2$.
   <details><summary>Soluzione</summary>$U(\mathbb{Z}_8) = \{\bar{1}, \bar{3}, \bar{5}, \bar{7}\}$. Tutti gli elementi non triviali hanno ordine 2 ($\bar{3}^2 = \bar{9} = \bar{1}$, ecc.), ed essendo di ordine 4 il gruppo è Kleiniano, dunque $\boxed{U(\mathbb{Z}_8) \cong \mathbb{Z}_2 \times \mathbb{Z}_2}$.</details>

### Flashcard
- **D:** Quando un poset ammette un unico elemento minimo, questo è anche l'unico elemento minimale? — **R:** Sì, l'elemento minimo è sempre l'unico elemento minimale del poset.
- **D:** Qual è la cardinalità del quoziente $A/\sim$ con $x \sim y \iff x = y$? — **R:** È uguale alla cardinalità dell'insieme $A$.
- **D:** Due gruppi finiti con la stessa cardinalità sono sempre isomorfi? — **R:** No, ad esempio $U_4$ e $\mathbb{Z}_2 \times \mathbb{Z}_2$ hanno entrambi cardinalità 4 ma non sono isomorfi perché hanno strutture di ordine degli elementi differenti.
- **D:** Come si dimostra che una funzione lineare $g: \mathbb{Z}^2 \to \mathbb{Z}$ non è suriettiva? — **R:** Si mostra che l'immagine è contenuta nel sottogruppo generato dal massimo comun divisore dei coefficienti, il quale non copre tutto $\mathbb{Z}$ se $\text{MCD} > 1$.
