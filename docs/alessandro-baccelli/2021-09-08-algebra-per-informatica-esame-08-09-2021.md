---
titolo: 'Algebra per Informatica: Esame del 08/09/2021'
data: '2021-09-08'
studente: Alessandro Baccelli
materia: matematica
argomento: Algebra e Matematica Discreta
sottoargomenti:
- Teoria dei numeri e congruenze
- Numeri complessi
- Teoria degli insiemi ordinati (poset)
- Funzioni, iniettività, surgettività e invertibilità
esercizi:
- 1
- 2
- 3
- 4
errori_tipici:
- Confondere le soluzioni intere di un'equazione diofantea con l'esistenza del MCD
- Scambiare elementi minimali/massimali con minimo e massimo in un poset
fonte: https://drive.google.com/file/d/1B8vM-NEHh7yhiYhEg5uMexDID36O98Y_/view?usp=drivesdk
generato: '2026-11-07'
---

# Algebra per Informatica: Esame del 08/09/2021

## Formule chiave

- **Teorema di Bézout per equazioni diofantee lineari:** L'equazione $ax + by = c$ ammette soluzioni intere $(x,y) \in \mathbb{Z}^2$ se e solo se $\text{MCD}(a,b) \mid c$.
- **Radici $n$-esime di un numero complesso $w = |w|e^{i\theta}$:**
  $$z_k = \sqrt[n]{|w|} \left( \cos\left(\frac{\theta + 2k\pi}{n}\right) + i\sin\left(\frac{\theta + 2k\pi}{n}\right) \right), \quad k = 0, 1, \dots, n-1$$
- **Poset $(\mathbb{Z} \times \mathbb{Z}, \le \times \le)$:** L'ordine prodotto è definito come $(x_1, y_1) \le (x_2, y_2) \iff x_1 \le x_2$ e $y_1 \le y_2$.

---

## Esercizio 1

Si determini la cardinalità dei seguenti insiemi:
1. $R = \{(x, y) \in \mathbb{Z}^2 : 51x - 69y = 4\}$
2. $S = \{x \in \mathbb{R} : x^6 = 64\}$
3. $T = \{x \in \mathbb{C} : x^6 = 64\}$

### Svolgimento

1. **Insieme $R$:** 
   L'equazione diofantea $51x - 69y = 4$ ammette soluzioni intere se e solo se $\text{MCD}(51, 69)$ divide $4$. 
   Con l'algoritmo euclideo troviamo $\text{MCD}(51, 69) = 3$. Poiché $3 \nmid 4$, l'equazione non ha soluzioni intere. 
   Pertanto, $R = \emptyset$ e $|R| = 0$.

2. **Insieme $S$ e $T$:**
   Cerchiamo le radici seste di $64$. Si ha $|64| = 64$ e $\arg(64) = 0$. Le formule delle radici seste danno:
   $$z_k = \sqrt[6]{64} \left( \cos\left(\frac{0 + 2k\pi}{6}\right) + i\sin\left(\frac{0 + 2k\pi}{6}\right) \right), \quad k = 0, 1, \dots, 5$$
   Le uniche radici reali (ossia appartenenti a $\mathbb{R}$, quindi a $S$) sono $z_0 = 2$ e $z_3 = -2$. Dunque $|S| = 2$.
   L'insieme $T$ comprende tutte le $6$ radici complesse distinte, quindi $|T| = 6$.

**Risultato:**
- $|R| = 0$
- $|S| = 2$
- $|T| = 6$

---

## Esercizio 2

Calcolare modulo e argomento del numero complesso:
$$z = i \left( \frac{1+i}{\sqrt{2}} \right)^{2020}$$

### Svolgimento

Scriviamo $i$ e $\frac{1+i}{\sqrt{2}}$ in forma polare:
- $i = e^{i\pi/2}$
- $\frac{1+i}{\sqrt{2}} = \frac{\sqrt{2}e^{i\pi/4}}{\sqrt{2}} = e^{i\pi/4}$

Sostituendo nell'espressione di $z$:
$$z = e^{i\pi/2} \left( e^{i\pi/4} \right)^{2020} = e^{i\pi/2} \cdot e^{i \frac{2020\pi}{4}} = e^{i\pi/2} \cdot e^{505\pi i}$$

Scomponendo l'esponente $505\pi = \pi + 504\pi = \pi + 252(2\pi)$:
$$z = e^{i\pi/2} \cdot e^{i\pi} \cdot (e^{2i\pi})^{252} = e^{i\pi/2} \cdot e^{i\pi} \cdot (1)^{252} = e^{i(\pi/2 + \pi)} = e^{i \frac{3\pi}{2}}$$

**Risultato:**
- $|z| = 1$
- $\arg(z) = \frac{3}{2}\pi$

---

## Esercizio 3

Sia dato l'insieme $A = \{(3,8), (-1,3), (3,1), (10,8), (3,4), (3,9), (5,8)\}$. Si consideri $A$ come sottoinsieme del poset $(\mathbb{Z} \times \mathbb{Z}, \le \times \le)$ e si determinino (se esistono) massimo, minimo, estremo inferiore ed estremo superiore di $A$.

### Svolgimento

Analizzando le relazioni d'ordine (dal basso verso l'alto):
- Gli elementi minimali sono $(-1,3)$ e $(3,1)$. Essendo due e non confrontabili, **$A$ non ammette minimo**.
- Gli elementi massimali sono $(3,9)$ e $(10,8)$. Essendo due e non confrontabili, **$A$ non ammette massimo**.
- L'insieme dei maggioranti di $A$ è $\{(x,y) \in \mathbb{Z}^2 : x \ge 10 \text{ e } y \ge 9\}$, il cui minimo è $(10,9)$. Dunque $\sup A = (10,9)$.
- L'insieme dei minoranti di $A$ è $\{(x,y) \in \mathbb{Z}^2 : x \le -1 \text{ e } y \le 1\}$, il cui massimo è $(-1,1)$. Dunque $\inf A = (-1,1)$.

**Risultato:**
- $A$ non ammette minimo.
- $A$ non ammette massimo.
- $\inf A = (-1,1)$
- $\sup A = (10,9)$

---

## Esercizio 4

Si consideri la funzione:
$$f : \mathbb{Z}_{19} \times \mathbb{Z}_{39} \longrightarrow \mathbb{Z}_{19} \times \mathbb{Z}_{39}$$
$$(x, y) \longmapsto (4 \cdot x, 4 \cdot y)$$

1. Determinare se $f$ è iniettiva e/o surgettiva.
2. Trovare (se esiste) l'inversa di $f$ nel monoide $(X^X, \circ, \text{Id}_X)$, dove $X = \mathbb{Z}_{19} \times \mathbb{Z}_{39}$.

### Svolgimento

Poiché $\text{MCD}(4, 19) = 1$ e $\text{MCD}(4, 39) = 1$, la classe di $4$ è invertibile sia in $\mathbb{Z}_{19}$ che in $\mathbb{Z}_{39}$. 
Calcoliamo gli inversi moltiplicativi di $4$:
- In $\mathbb{Z}_{19}$: $4^{-1} = 5$ poiché $4 \cdot 5 = 20 \equiv 1 \pmod{19}$.
- In $\mathbb{Z}_{39}$: $4^{-1} = 10$ poiché $4 \cdot 10 = 40 \equiv 1 \pmod{39}$.

1. **Iniettività e Surgettività:**
   - **Iniettività:** Se $f(x, y) = f(a, b)$, allora $(4x, 4y) = (4a, 4b)$. Moltiplicando la prima componente per $5$ e la seconda per $10$ otteniamo $(x, y) = (a, b)$. Quindi $f$ è iniettiva.
   - **Surgettività:** Per ogni $(a, b) \in \mathbb{Z}_{19} \times \mathbb{Z}_{39}$, scegliendo $(x, y) = (5a, 10b)$ si ha $f(x, y) = (4 \cdot 5a, 4 \cdot 10b) = (a, b)$. Quindi $f$ è surgettiva.

2. **Funzione Inversa:**
   L'inversa $g : \mathbb{Z}_{19} \times \mathbb{Z}_{39} \longrightarrow \mathbb{Z}_{19} \times \mathbb{Z}_{39}$ è definita da:
   $$g(x, y) = (5 \cdot x, 10 \cdot y)$$

**Risultato:**
- $f$ è iniettiva e surgettiva.
- L'inversa è $\boxed{g(x, y) = (5 \cdot x, 10 \cdot y)}$.

---

## ⚠️ Errori da evitare
- Confondere la non-esistenza di un unico elemento massimale/minimali con la non-esistenza di estremi superiori o inferiori nei poset.
- Dimenticare che un'equazione diofantea lineare $ax + by = c$ non ha soluzioni se $\text{MCD}(a,b)$ non divide $c$, anche se $a$ e $b$ sono coprimi tra loro.

---

## Materiale generato

### Riepilogo
La lezione affronta la risoluzione di equazioni diofantee lineari tramite il MCD, il calcolo delle radici complesse di un numero e la determinazione di estremi in un poset finito. Vengono inoltre studiate le proprietà di iniettività, surgettività e invertibilità di funzioni lineari su anelli di classi resto.

### Esercizi simili

1. **Determina la cardinalità dell'insieme $R = \{(x,y) \in \mathbb{Z}^2 : 12x + 18y = 10\}$.**
   <details><summary>Soluzione</summary>
   Si calcola $\text{MCD}(12, 18) = 6$. Poiché $6 \nmid 10$, l'equazione non ammette soluzioni intere. Dunque $|R| = 0$.
   </details>

2. **Calcola modulo e argomento del numero complesso $z = \left(\frac{1-i}{\sqrt{2}}\right)^{100}$.**
   <details><summary>Soluzione</summary>
   Scriviamo $\frac{1-i}{\sqrt{2}} = e^{-i\pi/4}$. 
   Allora $z = (e^{-i\pi/4})^{100} = e^{-25i\pi} = e^{-i\pi} \cdot (e^{-2i\pi})^{12} = -1$.
   Il modulo è $|z| = 1$ e l'argomento principale è $\arg(z) = \pi$.
   </details>

3. **Data la funzione $f : \mathbb{Z}_7 \times \mathbb{Z}_{11} \to \mathbb{Z}_7 \times \mathbb{Z}_{11}$ definita da $f(x, y) = (3x, 4y)$, determinare la funzione inversa.**
   <details><summary>Soluzione</summary>
   Troviamo gli inversi in $\mathbb{Z}_7$ e $\mathbb{Z}_{11}$: $3^{-1} = 5$ (poiché $3 \cdot 5 = 15 \equiv 1 \pmod 7$) e $4^{-1} = 3$ (poiché $4 \cdot 3 = 12 \equiv 1 \pmod{11}$).
   La funzione inversa è $g(x, y) = (5x, 3y)$.
   </details>

### Flashcard
- **D:** Quando un'equazione diofantea $ax + by = c$ ammette soluzioni in $\mathbb{Z}^2$? — **R:** Se e solo se $\text{MCD}(a,b)$ divide $c$.
- **D:** Quante soluzioni reali ha l'equazione $x^6 = 64$ in $\mathbb{R}$? — **R:** Esattamente 2 soluzioni ($x = 2$ e $x = -2$).
- **D:** Cos'è un minorante in un poset? — **R:** Un elemento del poset minore o uguale di tutti gli elementi del sottoinsieme considerato.
- **D:** Come si inverte una funzione lineare $f(x,y) = (ax, by)$ in $\mathbb{Z}_n \times \mathbb{Z}_m$? — **R:** Moltiplicando per gli inversi moltiplicativi $a^{-1} \pmod n$ e $b^{-1} \pmod m$, purché tali inversi esistano.
