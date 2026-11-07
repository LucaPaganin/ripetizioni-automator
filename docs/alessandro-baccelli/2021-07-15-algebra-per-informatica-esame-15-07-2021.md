---
titolo: 'Algebra per l''Informatica: Esame del 15/07/2021'
data: '2021-07-15'
studente: Alessandro Baccelli
materia: matematica
argomento: Algebra e Matematica Discreta
sottoargomenti:
- Teoria degli Insiemi e Funzioni
- Numeri Complessi e Radici
- Aritmetica Modulare e Teorema di Eulero
esercizi:
- 1
- 2
- 3
- 4
errori_tipici:
- Confondere la cardinalità dell'insieme delle parti con la cardinalità dell'insieme
  base
- Dimenticare che la suriettività richiede che ogni elemento del codominio sia raggiunto
fonte: https://drive.google.com/file/d/1lPCjYUgz3Rsy2TZG9hI8xjDk-K61kaTP/view?usp=drivesdk
generato: '2026-11-07'
---

# Algebra per l'Informatica: Esame del 15/07/2021

## Formule chiave

- **Cardinailtà dell'Insieme delle Parti**: Se $X$ è un insieme finito, allora $|\mathcal{P}(X)| = 2^{|X|}$.
- **Numero di Funzioni**: Date due insiemi finiti $X$ e $Y$, il numero di funzioni da $X$ a $Y$ è $|Y|^{|X|}$.
- **Radici $n$-esime di un numero complesso $z$**:
  $$z_k = \sqrt[n]{|z|} \left( \cos\left(\frac{\arg(z) + 2k\pi}{n}\right) + i\sin\left(\frac{\arg(z) + 2k\pi}{n}\right) \right), \quad k = 0, 1, \dots, n-1$$
- **Teorema di Eulero**: Sia $n \in \mathbb{N}$ e $x \in \mathbb{Z}$ tale che $\text{MCD}(x, n) = 1$. Allora $x^{\varphi(n)} \equiv 1 \pmod n$.

---

## Esercizio 1

**Testo:**
Siano dati gli insiemi $A = \{0, 1, 2, 3, 4, 5\}$ e $B = A \cap \{2x : x \in \mathbb{Z}\}$. Si determini la cardinalità dei seguenti insiemi:
(i) $R = \{f : \mathcal{P}(A) \to B \text{ funzione}\}$
(ii) $S = \{f : A \to B \text{ funzione} : f(1) = f(2)\}$
(iii) $T = \{f : A \to B \text{ funzione} : f(1) = f(2) = 2\}$

**Svolgimento:**
Calcoliamo innanzitutto la cardinalità degli insiemi di partenza e arrivo.
- $|A| = 6$
- $B = A \cap \{0, 2, 4, 6, \dots\} = \{0, 2, 4\}$, quindi $|B| = 3$.
- $|\mathcal{P}(A)| = 2^{|A|} = 2^6 = 64$.

(i) Il numero di funzioni da un insieme $X$ a un insieme $Y$ è $|Y|^{|X|}$. Pertanto:
$$|R| = |B|^{|\mathcal{P}(A)|} = \boxed{3^{64}}$$

(ii) Per costruire una funzione $f \in S$, imponiamo la condizione $f(1) = f(2)$. Abbiamo $3$ possibili scelte per questo valore comune. Per ciascuno degli altri $4$ elementi di $A$ ($\{0, 3, 4, 5\}$), abbiamo liberamente $3$ scelte possibili. In totale:
$$|S| = 3 \cdot 3 \cdot 3 \cdot 3 \cdot 3 = \boxed{3^5}$$

(iii) Per costruire una funzione $f \in T$, il valore $f(1) = f(2) = 2$ è fissato univocamente (1 sola scelta). Per gli altri $4$ elementi di $A$, abbiamo $3$ scelte possibili per ciascuno. In totale:
$$|T| = 1 \cdot 3^4 = \boxed{3^4}$$

---

## Esercizio 2

**Testo:**
Calcolare le radici cubiche di $z = -8$ in $\mathbb{C}$.

**Svolgimento:**
Scriviamo $z = -8$ in forma trigonometrica o polare. Il modulo è $|z| = \sqrt{(-8)^2} = 8$ e l'argomento è $\arg(z) = \pi$.
Le radici cubiche $z_k$ di $z$ sono date dalla formula:
$$z_k = \sqrt[n]{|z|} \left( \cos\left(\frac{\pi + 2k\pi}{3}\right) + i\sin\left(\frac{\pi + 2k\pi}{3}\right) \right), \quad k = 0, 1, 2$$

- Per $k = 0$:
$$z_0 = 2 \left( \cos\left(\frac{\pi}{3}\right) + i\sin\left(\frac{\pi}{3}\right) \right) = 2 \left(\frac{1}{2} + i\frac{\sqrt{3}}{2}\right) = \boxed{1 + i\sqrt{3}}$$

- Per $k = 1$:
$$z_1 = 2 \left( \cos\left(\pi\right) + i\sin\left(\pi\right) \right) = 2(-1 + 0) = \boxed{-2}$$

- Per $k = 2$:
$$z_2 = 2 \left( \cos\left(\frac{5\pi}{3}\right) + i\sin\left(\frac{5\pi}{3}\right) \right) = 2 \left(\frac{1}{2} - i\frac{\sqrt{3}}{2}\right) = \boxed{1 - i\sqrt{3}}$$

---

## Esercizio 3

**Testo:**
Si consideri la funzione $f : \mathbb{Z} \to \mathbb{Z}^2$ tale che $f(x) = (2x^2, 3x^2 + 1)$.
(i) Stabilire se $f$ è iniettiva e/o suriettiva.
(ii) Calcolare $f^{-1}(f(2))$ e $f^{-1}(f(0))$.

**Svolgimento:**
(i) **Iniettività:** La funzione non è iniettiva. Ad esempio, $f(2) = (2(2)^2, 3(2)^2 + 1) = (8, 13)$ e $f(-2) = (8, 13)$, quindi $f(2) = f(-2)$ con $2 \neq -2$.
**Suriettività:** La funzione non è suriettiva. Notiamo che la prima componente di ogni elemento dell'immagine è del tipo $2x^2$, che è sempre un numero pari. Di conseguenza, l'elemento $(1, 0) \notin \text{Im}(f)$.

(ii) Calcoliamo la controimmagine di $f(2)$:
Poiché $f(2) = (8, 13)$, cerchiamo $x \in \mathbb{Z}$ tali che $2x^2 = 8$ e $3x^2 + 1 = 13$.
Entrambe le equazioni sono soddisfatte per $x = 2$ e $x = -2$. Pertanto:
$$f^{-1}(f(2)) = \boxed{\{-2, 2\}}$$

Calcoliamo la controimmagine di $f(0)$:
Poiché $f(0) = (0, 1)$, cerchiamo $x \in \mathbb{Z}$ tali che $2x^2 = 0$ e $3x^2 + 1 = 1$.
L'unica soluzione comune è $x = 0$. Pertanto:
$$f^{-1}(f(0)) = \boxed{\{0\}}$$

---

## Esercizio 4

**Testo:**
Si consideri $\mathbb{Z}_{24}$.
(1) Calcolare $7^{162}$.
(2) Determinare l'ordine dei seguenti elementi del gruppo degli elementi invertibili $(U(\mathbb{Z}_{24}), \cdot, \overline{1})$: $\overline{11}, \overline{13}$.

**Svolgimento:**
Calcoliamo innanzitutto $\varphi(24) = \varphi(8 \cdot 3) = \varphi(8)\varphi(3) = 4 \cdot 2 = 8$. Per il Teorema di Eulero, per ogni $x$ tale che $\text{MCD}(x, 24) = 1$, si ha $x^8 \equiv 1 \pmod{24}$.

(1) Eseguiamo la divisione euclidea dell'esponente per $\varphi(24) = 8$:
$$162 = 8 \cdot 20 + 2$$
Quindi:
$$7^{162} = 7^{8 \cdot 20 + 2} = (7^8)^{20} \cdot 7^2 \equiv 1^{20} \cdot 49 \equiv 49 \equiv \boxed{\overline{1}} \pmod{24}$$
*(poiché $49 = 2 \cdot 24 + 1$)*.

(2) L'ordine di un elemento in un gruppo deve dividere l'ordine del gruppo, che è $|U(\mathbb{Z}_{24})| = \varphi(24) = 8$. I possibili divisori sono $1, 2, 4, 8$.
- Per $\overline{11}$:
  $$\overline{11}^2 = 121 = 5 \cdot 24 + 1 \equiv \overline{1} \pmod{24}$$
  Poiché il quadrato è $\overline{1}$ e la base non è $\overline{1}$, l'ordine è $\text{ord}(\overline{11}) = \boxed{2}$.

- Per $\overline{13}$:
  $$\overline{13}^2 = 169 = 7 \cdot 24 + 1 \equiv \overline{1} \pmod{24}$$
  L'ordine è $\text{ord}(\overline{13}) = \boxed{2}$.

---

## Materiale generato

### Riepilogo
La lezione affronta problemi di cardinalità di insiemi di funzioni, calcolo di radici complesse mediante la formula di De Moivre, verifica di iniettività e suriettività di funzioni algebriche, e teoria dei gruppi con applicazione del Teorema di Eulero in $\mathbb{Z}_n$.

### Esercizi simili

1. Siano $A = \{1, 2, 3\}$ e $B = \{0, 1\}$. Determinare la cardinalità dell'insieme delle funzioni $f : A \to B$ tali che $f(1) = f(2)$.
<details><summary>Soluzione</summary>
Abbiamo 2 scelte per il valore comune $f(1) = f(2)$ e 2 scelte indipendenti per $f(3)$. In totale le funzioni sono $2 \cdot 2 = \boxed{4}$.
</details>

2. Calcolare le radici quadrate di $z = -4$ in $\mathbb{C}$.
<details><summary>Soluzione</summary>
Il modulo è $|z| = 4$ e l'argomento $\arg(z) = \pi$. Le radici sono $z_k = \sqrt{4} \left(\cos\left(\frac{\pi + 2k\pi}{2}\right) + i\sin\left(\frac{\pi + 2k\pi}{2}\right)\right)$ per $k=0,1$, ovvero $\boxed{\pm 2i}$.
</details>

3. Calcolare l'ordine moltiplicativo di $\overline{5}$ nel gruppo degli invertibili $U(\mathbb{Z}_{12})$.
<details><summary>Soluzione</summary>
L'ordine di $U(\mathbb{Z}_{12})$ è $\varphi(12) = 4$. Calcoliamo le potenze di $\overline{5}$: $\overline{5}^2 = 25 \equiv 1 \pmod{12}$. L'ordine è $\boxed{2}$.
</details>

### Flashcard
- **D:** Quante sono le funzioni da un insieme finito $A$ a un insieme finito $B$? — **R:** $|B|^{|A|}$.
- **D:** Qual è la formula per trovare le radici $n$-esime di un numero complesso $z$? — **R:** $z_k = \sqrt[n]{|z|} \left( \cos\left(\frac{\arg(z) + 2k\pi}{n}\right) + i\sin\left(\frac{\arg(z) + 2k\pi}{n}\right) \right)$ per $k = 0, \dots, n-1$.
- **D:** Cosa afferma il Teorema di Eulero per un elemento invertibile modulo $n$? — **R:** Se $\text{MCD}(x, n) = 1$, allora $x^{\varphi(n)} \equiv 1 \pmod n$.
- **D:** Come si calcola la cardinalità dell'insieme delle parti $\mathcal{P}(A)$ di un insieme finito $A$? — **R:** $|\mathcal{P}(A)| = 2^{|A|}$.
