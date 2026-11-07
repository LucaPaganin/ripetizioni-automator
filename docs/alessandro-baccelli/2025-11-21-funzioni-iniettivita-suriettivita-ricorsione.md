---
titolo: 'Funzioni: iniettività, suriettività e ricorsione'
data: '2025-11-21'
studente: Alessandro Baccelli
materia: matematica
argomento: Teoria delle funzioni
sottoargomenti:
- Funzioni iniettive
- Funzioni suriettive
- Funzioni biettive
- Definizioni ricorsive
esercizi:
- 5
- 6
- 7
errori_tipici:
- Pensare che se il testo di un esercizio non specifica il valore di una funzione
  per certi input non si possa definire liberamente
fonte: https://drive.google.com/file/d/1FuQ5Rrix9moi055PHsZY41L-MnyC8Gl3/view?usp=drivesdk
generato: '2026-11-07'
---

# Funzioni: iniettività, suriettività e ricorsione

## Formule chiave

- **Funzione iniettiva**: $f: A \to B$ è iniettiva se $\forall x_1, x_2 \in A$, $x_1 \neq x_2 \implies f(x_1) \neq f(x_2)$ (elementi distinti hanno immagini distinte).
- **Funzione suriettiva**: $f: A \to B$ è suriettiva se $\forall y \in B, \exists x \in A$ tale che $f(x) = y$ (ogni elemento del codominio è raggiunto).
- **Funzione biettiva**: $f: A \to B$ è biettiva (o biunivoca) se è sia iniettiva che suriettiva.

---

## Esercizio 5

*Testo:* Costruire delle funzioni che soddisfino le richieste seguenti:
1. $f: \mathbb{Z} \to \mathbb{Z}$ iniettiva e non suriettiva;
2. $g: \mathbb{N} \to \N$ suriettiva e non iniettiva;
3. $h: \mathbb{Z} \times \mathbb{Z} \to \mathbb{Z}$ suriettiva e tale che $h(x,x) = 0$ per ogni $x \in \mathbb{Z}$;
4. $s: \mathbb{N} \to \mathbb{Z}$ biettiva;
5. $t: \mathbb{N} \to \mathcal{P}(\mathbb{N})$ iniettiva e tale che $\emptyset, \mathbb{N} \in t(\mathbb{N})$;

**Svolgimento:**

1. **$f: \mathbb{Z} \to \mathbb{Z}$ iniettiva e non suriettiva:**
   $$f(n) = n^3$$
   Non è suriettiva perché, ad esempio, $f^{-1}(3) = \emptyset$ (non esiste nessun intero il cui cubo sia $3$).

2. **$g: \mathbb{N} \to \mathbb{N}$ suriettiva e non iniettiva:**
   $$g(n) = \begin{cases} 0 & \text{se } n = 0 \\ n-1 & \text{se } n \ge 1 \end{cases}$$
   È suriettiva perché ogni naturale $y$ ha come controimmagine $y+1$. Non è iniettiva perché $g(0) = 0$ e $g(1) = 0$.

3. **$h: \mathbb{Z} \times \mathbb{Z} \to \mathbb{Z}$ suriettiva e $h(x,x) = 0$:**
   $$h(x,y) = \begin{cases} 0 & \text{se } x = y \\ x & \text{se } x \neq y \end{cases}$$

4. **$s: \mathbb{N} \to \mathbb{Z}$ biettiva:**
   Come suggerito negli appunti (tramite intelligenza artificiale), possiamo alternare i positivi e i negativi:
   $$s(n) = \begin{cases} n/2 & \text{se } n \pmod 2 = 0 \\ \frac{n+1}{2} & \text{se } n \pmod 2 = 1 \end{cases}$$
   *(Nota: la formula esatta per numerare $\mathbb{Z}$ con $\mathbb{N}$ solitamente mappa $0 \to 0, 1 \to 1, 2 \to -1, 3 \to 2, 4 \to -2$, ecc.)*

---

## Esercizio 6

*Testo:* Definire un'applicazione $f: \mathbb{N} \to \mathbb{N}$ diversa dall'identità e tale che $f(3n) = 3n$ per ogni $n \in \mathbb{N}$.

**Svolgimento:**
Il testo impone il comportamento di $f$ solo sui multipli di $3$. Per gli altri valori siamo liberi di scegliere.
Ad esempio, possiamo definire:
$$f(n) = \begin{cases} n & \text{se } n \pmod 3 = 0 \\ n-1 & \text{se } n \pmod 3 \neq 0 \end{cases}$$
Questa funzione è diversa dall'identità (ad esempio, per $n=4$ si ha $f(4) = 4-1 = 3 \neq 4$).

---

## Esercizio 7

*Testo:* Calcolare $f(5)$ dove $f: \mathbb{N} \to \mathbb{N}$ è l'applicazione definita da:
$$f(0) = 1, \quad f(n) = n \cdot f(n-1) \text{ per ogni } n > 0.$$

**Svolgimento:**
Calcoliamo passo dopo passo applicando la definizione ricorsiva:
- $f(5) = 5 \cdot f(4)$
- $f(4) = 4 \cdot f(3)$
- $f(3) = 3 \cdot f(2)$
- $f(2) = 2 \cdot f(1)$
- $f(1) = 1 \cdot f(0) = 1 \cdot 1 = 1$

Risalendo:
$$f(5) = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 \cdot f(0) = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 \cdot 1 = \boxed{120}$$
*Nota:* Questa è la definizione ricorsiva del fattoriale: $f(m) = m!$.

---

## ⚠️ Errori da evitare
- Pensare che se il testo di un esercizio assegna il valore di una funzione solo su un sottoinsieme del dominio (es. i multipli di 3), la funzione sia definita univocamente: si è liberi di scegliere il valore sugli altri input purché siano rispettate le consegne.

---

## Materiale generato

### Riepilogo
La lezione affronta la costruzione di funzioni con specifiche proprietà di iniettività e suriettività tra insiemi numerici, l'estensione di funzioni parzialmente definite e il calcolo ricorsivo tramite fattoriale.

### Esercizi simili

1. Trovare una funzione $f: \mathbb{N} \to \mathbb{N}$ che sia suriettiva ma non iniettiva.
   <details><summary>Soluzione</summary>
   Si può definire $f(n) = \lfloor \frac{n}{2} \rfloor$. Essa è suriettiva perché ogni naturale $y$ ha come immagine $2y$ (quindi $f(2y) = y$), ma non è iniettiva poiché $f(0) = 0$ e $f(1) = 0$.
   </details>

2. Data la funzione $f: \mathbb{Z} \to \mathbb{Z}$ definita da $f(n) = n + 2$, stabilire se è iniettiva e/o suriettiva.
   <details><summary>Soluzione</summary>
   - **Iniettiva:** Sì, se $n_1 + 2 = n_2 + 2$ allora $n_1 = n_2$.
   - **Suriettiva:** Sì, perché per ogni $y \in \mathbb{Z}$ esiste $x = y - 2 \in \mathbb{Z}$ tale che $f(x) = (y - 2) + 2 = y$.
   Dunque è biettiva.
   </details>

3. Calcolare $f(4)$ per la funzione definita da $f(0) = 2$ e $f(n) = 2 \cdot f(n-1) + 1$ per $n > 0$.
   <details><summary>Soluzione</summary>
   - $f(1) = 2 \cdot f(0) + 1 = 2(2) + 1 = 5$
   - $f(2) = 2 \cdot f(1) + 1 = 2(5) + 1 = 11$
   - $f(3) = 2 \cdot f(2) + 1 = 2(11) + 1 = 23$
   - $f(4) = 2 \cdot f(3) + 1 = 2(23) + 1 = \boxed{47}$
   </details>

### Flashcard
- **D:** Quando una funzione $f: A \to B$ si dice iniettiva? — **R:** Quando elementi distinti del dominio hanno immagini distinte ($x_1 \neq x_2 \implies f(x_1) \neq f(x_2)$).
- **D:** Quando una funzione $f: A \to B$ si dice suriettiva? — **R:** Quando ogni elemento del codominio $B$ è immagine di almeno un elemento del dominio $A$.
- **D:** Cos'è una funzione biettiva? — **R:** Una funzione sia iniettiva che suriettiva (corrispondenza biunivoca).
- **D:** Come si interpreta una definizione ricorsiva come $f(n) = n \cdot f(n-1)$? — **R:** Come un procedimento a catena che parte da un caso base noto (es. $f(0)$) per calcolare i valori successivi.
