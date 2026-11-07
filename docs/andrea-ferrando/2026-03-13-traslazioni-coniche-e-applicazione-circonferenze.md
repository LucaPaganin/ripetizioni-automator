---
titolo: Traslazioni coniche e applicazione a circonferenze
data: '2026-03-13'
studente: Andrea Ferrando
materia: matematica
argomento: Geometria analitica
sottoargomenti:
- Traslazioni nel piano cartesiano
- Circonferenza
- Traslazione di coniche
esercizi:
- '73'
errori_tipici:
- Confondere la traslazione degli assi con la traslazione del vettore della figura
  geometrica
- Sbagliare il segno del vettore di traslazione quando si spostano gli assi
fonte: https://drive.google.com/file/d/19NXreTcS8OGkYq9m0RL9VIwLRpZZdZ-G/view?usp=drivesdk
generato: '2026-11-07'
---

# Traslazioni coniche e applicazione a circonferenze

## Formule chiave

Data una traslazione del piano che sposta l'origine dei assi $O(0,0)$ nel nuovo punto $O'(x_0, y_0)$, le equazioni generali della trasformazione (cambio di coordinate) sono:

$$T: \begin{cases} x' = x - x_0 \\ y' = y - y_0 \end{cases}$$

La trasformazione inversa, che esprime le vecchie coordinate in funzione delle nuove, è data da:

$$T^{-1}: \begin{cases} x = x' + x_0 \\ y = y' + y_0 \end{cases}$$

Se invece si vuole traslare una figura geometrica (come una circonferenza) nel piano mediante un vettore $\vec{v} = (v_x, v_y)$, si applica la trasformazione con il vettore opposto $-\vec{v}$ sugli assi (oppure si sostituiscono direttamente le coordinate con $x - v_x$ e $y - v_y$).

---

## Esercizio 73

**Testo dell'esercizio:**
La corrisponente della circonferenza di equazione $x^2 + y^2 - 2x + 6y + k = 0$ nella traslazione di vettore $\vec{v} = (-1, 2)$ passa per l'origine degli assi. Qual è il valore di $k$?

**Svolgimento:**

Scriviamo l'equazione della circonferenza in forma canonica completando i quadrati:

$$x^2 - 2x + y^2 + 6y + k = 0$$

$$(x - 1)^2 - 1 + (y + 3)^2 - 9 + k = 0$$

$$(x - 1)^2 + (y + 3)^2 = 10 - k$$

Il centro della circonferenza nel sistema di riferimento iniziale è $C = (1, -3)_s$.

Vogliamo traslare la circonferenza mediante il vettore $\vec{v} = (-1, 2)$. 
> ⚠️ Nota: Spostare la circonferenza di un vettore $\vec{v}$ equivale a traslare il sistema di assi cartesiani del vettore opposto $-\vec{v} = (1, -2)$.

Applichiamo la trasformazione $T(-\vec{v})$:

$$T(-\vec{v}): \begin{cases} x' = x - 1 \\ y' = y + 2 \end{cases} \implies \begin{cases} x = x' + 1 \\ y = y' - 2 \end{cases}$$

Sostituendo nell'equazione della circonferenza $\gamma$:

$$(x' + 1 - 1)^2 + (y' - 2 + 3)^2 = 10 - k$$

$${x'}^2 + (y' + 1)^2 = 10 - k$$

Il nuovo centro della circonferenza traslata è $C' = (0, -1)_{s'}$. 

Poiché la circonferenza traslata passa per l'origine degli assi del nuovo sistema ($x' = 0, y' = 0$), imponiamo il passaggio per $(0,0)$:

$$0^2 + (0 + 1)^2 = 10 - k$$

$$0 + 1 = 10 - k \implies k = 10 - 1 \implies \boxed{k = 9}$$

---

## ⚠️ Errori da evitare

- **Errore comune:** Confondere la direzione della traslazione. Se si sposta la figura geometrica di un vettore $\vec{v}$, l'equazione algebrica si ottiene sostituendo $x$ con $x - v_x$ e $y$ con $y - v_y$. Applicare direttamente i segni positivi del vettore senza invertire porta a risultati errati (come evidenziato nelle pagine iniziali degli appunti dove l'esercizio era stato impostato erroneamente scambiando il ruolo di assi e curva).

---

## Materiale generato

### Riepilogo
La traslazione di una conica nel piano cartesiano si gestisce mediante il cambiamento delle coordinate $(x', y')$. Per traslare una curva di un vettore $\vec{v}$, si sostituiscono le variabili con le componenti del vettore opposto, oppure si opera geometricamente traslando il sistema di riferimento.

### Esercizi simili

1. **Esercizio 1:** Data la circonferenza $x^2 + y^2 + 4x - 2y + p = 0$, determina il valore di $p$ affinché la sua traslata secondo il vettore $\vec{v} = (2, -1)$ passi per l'origine degli assi.
   <details><summary>Soluzione</summary>
   Completando i quadrati si ottiene $(x+2)^2 + (y-1)^2 = 5 - p$. 
   Applicando la traslazione con vettore $-\vec{v} = (-2, 1)$, l'equazione della circonferenza traslata diventa $(x')^2 + (y')^2 = 5 - p$. 
   Imponendo il passaggio per l'origine $(0,0)$, si ha $0 + 0 = 5 - p \implies \boxed{p = 5}$.
   </details>

2. **Esercizio 2:** Trova l'equazione della circonferenza $x^2 + y^2 - 6x = 0$ traslata dal vettore $\vec{v} = (-1, 3)$.
   <details><summary>Soluzione</summary>
   Sostituendo $x$ con $x - (-1) = x + 1$ e $y$ con $y - 3$, si ottiene:
   $(x + 1 - 3)^2 + (y - 3)^2 = 9 \implies (x - 2)^2 + (y - 3)^2 = 9$, ovvero $\boxed{x^2 + y^2 - 4x - 6y + 4 = 0}$.
   </details>

3. **Esercizio 3:** Determina il vettore di traslazione $\vec{v}$ che porta il centro della circonferenza $x^2 + y^2 - 2x - 4q = 0$ nel punto $C'(3, 0)$.
   <details><summary>Soluzione</summary>
   Il centro di partenza è $C(1, 0)$. Il vettore di traslazione che porta $C$ in $C'$ è $\vec{v} = C' - C = (3 - 1, 0 - 0) = \boxed{(2, 0)}$.
   </details>

### Flashcard
- **D:** Quali sono le equazioni di una traslazione che sposta l'origine in $(x_0, y_0)$? — **R:** $x' = x - x_0$ e $y' = y - y_0$.
- **D:** Se si sposta una circonferenza di un vettore $\vec{v} = (a, b)$, come si modificano le coordinate nell'equazione cartesiana? — **R:** Si sostituisce $x$ con $(x - a)$ e $y$ con $(y - b)$.
- **D:** Cosa significa geometricamente imporre che una curva passi per l'origine del nuovo sistema di riferimento? — **R:** Significa che le coordinate $(0,0)$ del nuovo sistema devono soddisfare l'equazione trasformata della curva.
