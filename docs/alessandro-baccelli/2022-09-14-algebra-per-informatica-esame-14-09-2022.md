---
titolo: 'Algebra per Informatica: Esame del 14/09/2022'
data: '2022-09-14'
studente: Alessandro Baccelli
materia: matematica
argomento: Algebra
sottoargomenti:
- Relazioni d'equivalenza
- Numeri complessi
- Teoria dei poset
- Teoria dei gruppi
esercizi:
- 1
- 2
- 3
- 4
errori_tipici:
- Confondere elementi massimali con l'elemento massimo di un poset
- Dimenticare che l'ordine di un elemento in un gruppo deve dividere l'ordine del
  gruppo (Teorema di Lagrange)
fonte: https://drive.google.com/file/d/1-6MWkIcHLLVPJGFc0oXkGikPSM4-4RHY/view?usp=drivesdk
generato: '2026-11-07'
---

# Algebra per Informatica: Esame del 14/09/2022

## Formule chiave

- **Classe di equivalenza:** Data una relazione d'equivalenza $\sim$ su un insieme $X$, la classe di equivalenza di un elemento $x \in X$ è definita come $[x] = \{y \in X : y \sim x\}$.
- **Radici $n$-esime complesse:** Le radici $n$-esime di un numero complesso $z = |z|(\cos\theta + i\sin\theta)$ sono date da:
  $$z_k = \sqrt[n]{|z|} \left( \cos\left(\frac{\theta + 2k\pi}{n}\right) + i\sin\left(\frac{\theta + 2k\pi}{n}\right) \right)$$
  per $k = 0, 1, \dots, n-1$.
- **Teorema di Lagrange:** In un gruppo finito $(G, *)$, l'ordine di un qualsiasi elemento $g \in G$ divide l'ordine del gruppo $|G|$.

## Esercizio 1
Si consideri la seguente relazione d'equivalenza sull'insieme $\mathbb{N} \times \mathbb{N}$:
$$(a, b) \sim (c, d) \iff a + b = c + d.$$
Determinare la cardinalità di ciascuna delle seguenti classi d'equivalenza:
$$(0, 0), \quad (1, 1), \quad (5, 2), \quad (37, 13).$$

**Soluzione:**
Ricordiamo che per fissati $a, b \in \mathbb{N}$ si ha:
$$\overline{(a, b)} = \{(x, y) \in \mathbb{N}^2 : x + y = a + b\}.$$

Abbiamo pertanto:
$$\overline{(0, 0)} = \{(x, y) \in \mathbb{N}^2 : x + y = 0\} = \{(0, 0)\},$$
quindi $\#\overline{(0, 0)} = \boxed{1}$.

Analogamente, abbiamo:
$$\overline{(1, 1)} = \{(x, y) \in \mathbb{N}^2 : x + y = 2\} = \{(2, 0), (1, 1), (0, 2)\},$$
e pertanto $\#\overline{(1, 1)} = \boxed{3}$.

Poi abbiamo:
$$\overline{(5, 2)} = \{(x, y) \in \mathbb{N}^2 : x + y = 7\} = \{(7, 0), (6, 1), (5, 2), \dots, (1, 6), (0, 7)\},$$
e pertanto $\#\overline{(5, 2)} = \boxed{8}$.

Infine, abbiamo:
$$\overline{(37, 13)} = \{(x, y) \in \mathbb{N}^2 : x + y = 37 + 13 = 50\} = \{(50, 0), (49, 1), \dots, (1, 49), (0, 50)\},$$
e pertanto $\#\overline{(37, 13)} = \boxed{51}$.

In generale, notiamo che vale la formula $\#\overline{(a, b)} = a + b + 1$.

## Esercizio 2
Determinare tutte le radici terze complesse di $-i$. Scrivere ciascuna radice nella forma $a + ib$ con $a, b \in \mathbb{R}$.

**Soluzione:**
Sia $z = -i$, abbiamo $|z| = \sqrt{(-1)^2} = 1$ e $\arg(z) = -\frac{\pi}{2}$. Pertanto le radici terze $z_k$ (per $k = 0, 1, 2$) di $z$ sono date dalla formula:
$$z_k = \sqrt[3]{1} \left( \cos\left(\frac{-\pi/2 + 2k\pi}{3}\right) + i\sin\left(\frac{-\pi/2 + 2k\pi}{3}\right) \right) = \cos\left(-\frac{\pi}{6} + \frac{2k\pi}{3}\right) + i\sin\left(-\frac{\pi}{6} + \frac{2k\pi}{3}\right).$$

Abbiamo quindi:
- Per $k = 0$:
  $$z_0 = \cos\left(-\frac{\pi}{6}\right) + i\sin\left(-\frac{\pi}{6}\right) = \boxed{\frac{\sqrt{3}}{2} - \frac{1}{2}i}.$$
- Per $k = 1$:
  $$z_1 = \cos\left(-\frac{\pi}{6} + \frac{2\pi}{3}\right) + i\sin\left(-\frac{\pi}{6} + \frac{2\pi}{3}\right) = \cos\left(\frac{\pi}{2}\right) + i\sin\left(\frac{\pi}{2}\right) = \boxed{i}.$$
- Per $k = 2$:
  $$z_2 = \cos\left(-\frac{\pi}{6} + \frac{4\pi}{3}\right) + i\sin\left(-\frac{\pi}{6} + \frac{4\pi}{3}\right) = \cos\left(\frac{7\pi}{6}\right) + i\sin\left(\frac{7\pi}{6}\right) = \boxed{-\frac{\sqrt{3}}{2} - \frac{1}{2}i}.$$

## Esercizio 3
Sia dato l'insieme $A = \{(1, 2, 3), (2, 2, 3), (2, 2, 4), (2, 4, 4), (2, 3, 5)\}$. Si consideri $A$ come sottoinsieme del poset $(\mathbb{Z}^3, \le \times \le \times \le)$ e si determinino (se esistono) massimo, minimo, estremo inferiore, ed estremo superiore di $A$.

**Soluzione:**
Abbiamo il seguente diagramma di Hasse che rappresenta la struttura del poset $A$ (dove l'ordine $\le \times \le \times \le$ procede dal basso verso l'alto):
$$(2, 4, 4) \qquad (2, 3, 5)$$
$$\text{ \enspace } (2, 2, 4) \text{ \enspace }$$
$$\text{ \enspace } (2, 2, 3) \text{ \enspace }$$
$$\text{ \enspace } (1, 2, 3) \text{ \enspace }$$

Si vede che $A$ ha un minimo in $\boxed{(1, 2, 3)}$, che è pertanto anche l'estremo inferiore. 

Inoltre, $A$ ha due elementi massimali non confrontabili $(2, 3, 5)$ e $(2, 4, 4)$, pertanto $A$ **non ammette massimo**. 

L'insieme dei maggioranti di $A$ è dato da:
$$M = \{(x, y, z) \in \mathbb{Z}^3 : (x \ge 2) \land (y \ge 4) \land (z \ge 5)\},$$
che ha minimo in $(2, 4, 5)$. Pertanto l'estremo superiore di $A$ è $\sup A = \boxed{(2, 4, 5)}$.

## Esercizio 4
Si consideri il gruppo $(U(\mathbb{Z}_{18}), \cdot, \bar{1})$.
1. Determinare tutti gli elementi del gruppo.
2. Calcolare l'ordine dei seguenti elementi: $\bar{7}, \bar{11}$.

**Soluzione:**
1. Ricordiamo che $U(\mathbb{Z}_n) = \{\bar{x} \in \mathbb{Z}_n : \text{MCD}(x, n) = 1\}$, pertanto:
   $$U(\mathbb{Z}_{18}) = \{\boxed{\bar{1}, \bar{5}, \bar{7}, \bar{11}, \bar{13}, \bar{17}}\}.$$

2. Ricordiamo che per il Teorema di Lagrange l'ordine di un elemento in un gruppo finito deve dividere l'ordine del gruppo, che in questo caso è $\#U(\mathbb{Z}_{18}) = 6$. Perciò calcoliamo soltanto le potenze $\bar{x}^d$ con $d | 6$ (quindi $d \in \{1, 2, 3, 6\}$):
   - Calcoliamo $\bar{7}^2 = \bar{49} = \bar{13}$. E poi $\bar{7}^3 = \bar{7}^2 \cdot \bar{7} = \bar{13} \cdot \bar{7} = \bar{91} = \bar{1}$. Pertanto $\text{ord}(\bar{7}) = \boxed{3}$.
   - Calcoliamo $\bar{11}^2 = \bar{121} = \bar{13}$. E poi $\bar{11}^3 = \bar{11}^2 \cdot \bar{11} = \bar{13} \cdot \bar{11} = \bar{143} = \bar{17}$. Infine calcoliamo:
     $$\bar{11}^6 = \bar{11}^3 \cdot \bar{11}^3 = \bar{17} \cdot \bar{17} = (\overline{-1}) \cdot (\overline{-1}) = \bar{1}.$$
     Pertanto $\text{ord}(\bar{11}) = \boxed{6}$.

## ⚠️ Errori da evitare
- Confondere la presenza di più elementi massimali con l'esistenza di un elemento massimo (se ci sono elementi massimali incomparabili, il massimo non esiste).
- Dimenticare che l'ordine di un elemento in un gruppo divide sempre l'ordine del gruppo (Teorema di Lagrange), utile per limitare i calcoli delle potenze.

---
## Materiale generato

### Riepilogo
- Le classi di equivalenza in $\mathbb{N} \times \mathbb{N}$ rispetto alla somma costante hanno cardinalità determinata dalla formula $\#\overline{(a,b)} = a+b+1$.
- Le radici complesse si calcolano sfruttando modulo e argomento in forma trigonometrica.
- In un poset, un insieme può avere molteplici elementi massimali senza possedere un massimo globale.

### Esercizi simili
1. Si consideri la relazione d'equivalenza su $\mathbb{N} \times \mathbb{N}$ definita da $(a, b) \sim (c, d) \iff a \cdot b = c \cdot d$. Determinare la classe d'equivalenza $\overline{(2, 3)}$.
   <details><summary>Soluzione</summary>$\overline{(2, 3)} = \{(x, y) \in \mathbb{N}^2 : x \cdot y = 6\} = \{(1, 6), (2, 3), (3, 2), (6, 1)\}$, con cardinalità 4.</details>

2. Determinare tutte le radici quarte complesse di $1$. Scrivere ciascuna nella forma $a + ib$.
   <details><summary>Soluzione</summary>Le radici quarte di $1$ sono $z_0 = 1$, $z_1 = i$, $z_2 = -1$, $z_3 = -i$.</details>

3. Determinare l'ordine dell'elemento $\bar{5}$ nel gruppo $(U(\mathbb{Z}_{18}), \cdot, \bar{1})$.
   <details><summary>Soluzione</summary>$\bar{5}^1 = \bar{5}$, $\bar{5}^2 = \bar{7}$, $\bar{5}^3 = \bar{17} = \overline{-1}$, $\bar{5}^6 = \bar{1}$. Pertanto $\text{ord}(\bar{5}) = 6$.</details>

### Flashcard
- **D:** Come si calcola la cardinalità della classe d'equivalenza $\overline{(a,b)}$ per la relazione $(a,b) \sim (c,d) \iff a+b=c+d$ su $\mathbb{N} \times \mathbb{N}$? — **R:** Tramite la formula $\#\overline{(a,b)} = a + b + 1$.
- **D:** Cosa afferma il Teorema di Lagrange riguardo all'ordine di un elemento in un gruppo finito? — **R:** L'ordine di un elemento divide sempre l'ordine del gruppo.
- **D:** Se un poset ha due elementi massimali distinti, ammette un massimo? — **R:** No, se ci sono due o più elementi massimali non confrontabili, l'insieme non ammette massimo.
