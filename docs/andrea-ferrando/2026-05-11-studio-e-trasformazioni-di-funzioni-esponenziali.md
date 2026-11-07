---
titolo: Studio e trasformazioni di funzioni esponenziali
data: '2026-05-11'
studente: Andrea Ferrando
materia: matematica
argomento: grafici di funzioni esponenziali e trasformazioni geometriche
sottoargomenti:
- esponenziali
- simmetrie e riflessioni
- traslazioni
- valore assoluto
- composizione di funzioni
esercizi:
- 80
- 82
- 84
- 85
errori_tipici:
- Applicare le trasformazioni nell'ordine errato anziché seguire la composizione di
  funzioni
fonte: https://drive.google.com/file/d/11jHSTOQ3abfg4oZq8ZYLWgF-1ptA9VQW/view?usp=drivesdk
generato: '2026-11-07'
---

# Studio e trasformazioni di funzioni esponenziali

## Formule chiave

Dato il grafico di una funzione elementare $f(x)$, le principali trasformazioni geometriche nel piano cartesiano sono:

- **Traslazione orizzontale di un vettore $\Delta x$**:
  $$y = f(x - \Delta x)$$

- **Traslazione verticale di un vettore $\Delta y$**:
  $$y = f(x) + \Delta y$$

- **Riflessione rispetto all'asse $x$**:
  $$y = -f(x)$$

- **Riflessione rispetto all'asse $y$**:
  $$y = f(-x)$$

- **Applicazione del valore assoluto sull'argomento**:
  $$y = f(|x|)$$

- **Applicazione del valore assoluto sull'intera funzione**:
  $$y = |f(x)|$$

La scomposizione di un'espressione complessa si esprime formalmente tramite la **composizione di funzioni** (es. $(i \circ h \circ g \circ f)(x)$).

---

## Esercizio 80

Studiare il grafico della funzione:
$$y = 2^{-|x|} + 1$$

### Passaggi e scomposizione:
La funzione può essere vista come la composizione di tre funzioni elementari:
1. $f_1(x) = -|x|$
2. $f_2(t) = 2^t$
3. $f_3(z) = z + 1$

Quindi la funzione finale è la composizione:
$$f(x) = f_3(f_2(f_1(x))) = (f_3 \circ f_2 \circ f_1)(x)$$

---

## Esercizio 82

Studiare il grafico della funzione:
$$y = |2 - 2^x|$$

### Passaggi e scomposizione:
1. Si parte dal grafico elementare:
   $$y_1 = 2^x$$
2. Si applica la riflessione e la traslazione verticale:
   $$y_2 = 2 - 2^x$$
3. Si applica il valore assoluto all'intera funzione (ribaltando nel semipiano positivo la parte di grafico che si trova sotto l'asse $x$):
   $$y_3 = |2 - 2^x|$$

---

## Esercizio 84

Studiare il grafico della funzione:
$$y = 2^{|x-1|} - 1$$

### Passaggi e scomposizione:
1. Si parte dal valore assoluto dell'esponente:
   $$y_1 = |x-1|$$
2. Si applica la base esponenziale:
   $$y_2 = 2^{|x-1|}$$
3. Si applica la traslazione verticale verso il basso di $1$ unità:
   $$y_3 = 2^{|x-1|} - 1$$

---

## Esercizio 85

Studiare il grafico della funzione:
$$y = -\left|4 - \left(\frac{1}{2}\right)^{2-x}\right|$$

### Passaggi e scomposizione:
Analizziamo la base e l'esponente:
$$\left(\frac{1}{2}\right)^{2-x} = 2^{-(2-x)} = 2^{x-2}$$

L'esponente $x-2$ indica una traslazione verso destra di $2$ unità ($ \Delta x = 2 $) del grafico di base $2^x$, che geometricamente equivale anche a una riflessione rispetto alla retta $x = 2$.

Progressione delle trasformazioni:
1. Funzione esponenziale iniziale con traslazione: $t_2(x) = x-2$ applicata a $2^x$.
2. Riflessione verticale data dal segno meno davanti a $4 - \dots$
3. Valore assoluto esterno $-\left| \dots \right|$ applicato per ultimo come operazione verticale.

---

## ⚠️ Errori da evitare

- Confondere l'ordine delle trasformazioni geometriche: applicare traslazioni o valori assoluti senza seguire il corretto ordine di composizione delle funzioni altera completamente il grafico finale.

---

## Materiale generato

### Riepilogo
Il tracciamento dei grafici di funzioni esponenziali complesse richiede l'analisi delle trasformazioni geometriche elementari (traslazioni, simmetrie e valori assoluti) applicate passo dopo passo attraverso la composizione di funzioni.

### Esercizi simili
1. Traccia il grafico della funzione:
   $$y = 3^{1-x} - 2$$
   <details><summary>Soluzione</summary>
   Si parte da $3^x$, si riflette rispetto all'asse $y$ e si trasla l'esponente ($3^{-(x-1)} = 3^{-x+1}$), infine si applica una traslazione verticale verso il basso di $2$ unità.
   </details>

2. Traccia il grafico della funzione:
   $$y = |2^{x-1} - 4|$$
   <details><summary>Soluzione</summary>
   Si traccia $2^x$, si trasla a destra di $1$ unità ($2^{x-1}$), si sottrae $4$ (traslazione verticale verso il basso di $4$) e infine si applica il valore assoluto globale che ribalta la parte di grafico sotto l'asse $x$.
   </details>

3. Traccia il grafico della funzione:
   $$y = 2^{-|x|} - 2$$
   <details><summary>Soluzione</summary>
   Si parte da $|x|$, si applica la riflessione all'esponente ($2^{-|x|}$) ottenendo una funzione simmetrica rispetto all'asse $y$, e si trasla l'intero grafico verso il basso di $2$ unità.
   </details>

### Flashcard
- **D:** Come si riflette un grafico rispetto all'asse $x$? — **R:** Moltiplicando l'intera funzione per $-1$, cioè $y = -f(x)$.
- **D:** Qual è l'effetto di un valore assoluto applicato all'intera funzione ($y = |f(x)|$)? — **R:** La parte di grafico che si trova sotto l'asse $x$ viene ribaltata specularmente nel semipiano positivo.
- **D:** Come si interpreta geometricamente l'esponente $2-x$ nella funzione $y = 2^{2-x}$? — **R:** Corrisponde a una riflessione orizzontale seguita da una traslazione, riconducibile a $2^{-(x-2)}$ (riflessione rispetto all'asse $y$ e traslazione orizzontale di $2$ unità).
