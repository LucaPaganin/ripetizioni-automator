---
titolo: Grafici di funzioni esponenziali e trasformazioni geometriche
data: '2026-09-04'
studente: Andrea Ferrando
materia: matematica
argomento: Studio di funzioni esponenziali e trasformazioni geometriche elementari
sottoargomenti:
- Funzione esponenziale
- Traslazioni verticali e orizzontali
- Valore assoluto e simmetrie
- Composizione di funzioni per il tracciamento dei grafici
esercizi: []
errori_tipici: []
fonte: https://drive.google.com/file/d/1dFQx6Sm_860h-p-_i7TV14E0TlvMdxVR/view?usp=drivesdk
generato: '2026-11-07'
---

# Grafici di funzioni esponenziali e trasformazioni geometriche

## Formule chiave

- **Funzione esponenziale elementare:**
  $$f(x) = 2^x$$
  Il grafico passa per $(0,1)$ ed è sempre strettamente positivo, con un asintoto orizzontale a $y=0$ per $x \to -\infty$.

- **Traslazioni verticali:**
  Data una funzione $f(x)$, la trasformazione $f(x) \to f(x) + c$ con $c \in \mathbb{R}$ produce una traslazione verticale:
  - $c > 0$: verso l'alto
  - $c < 0$: verso il basso

- **Traslazioni orizzontali:**
  Data una funzione $f(x)$, la trasformazione $f(x) \to f(x-a)$ con $a \in \mathbb{R}$ produce una traslazione orizzontale:
  - $a > 0$: verso destra
  - $a < 0$: verso sinistra

- **Valore assoluto (argomento):**
  La trasformazione $f(x) \to f(|x|)$ crea una simmetria rispetto all'asse $y$: la parte di grafico per $x < 0$ viene sostituita dalla riflessione speculare della parte per $x > 0$.

## Studio e tracciamento delle funzioni

### 1. Studio della funzione $y = 2^{|x-1|} - 1$

La funzione può essere vista come la composizione di funzioni elementari applicate in sequenza a partire da $x$:

$$x \xrightarrow{f_1} x-1 \xrightarrow{f_2} |x-1| \xrightarrow{f_3} 2^{|x-1|} \xrightarrow{f_4} 2^{|x-1|} - 1$$

Definiamo le singole funzioni componenti:
- $f_1(x) = x - 1$ (traslazione orizzontale)
- $f_2(t) = |t|$ (valore assoluto)
- $f_3(t) = 2^t$ (esponenziale)
- $f_4(t) = t - 1$ (traslazione verticale)

L'espressione complessiva mediante la composizione di funzioni è:
$$y = (f_4 \circ f_3 \circ f_2 \circ f_1)(x)$$

### 2. Studio della funzione $y = |2^{x+1} - 1|$

Analizziamo la sequenza di trasformazioni per tracciare il grafico partendo da $2^x$:

1. $x \longrightarrow x+1$: traslazione a sinistra di $1$ unità.
2. $2^{x+1} \longrightarrow 2^{x+1} - 1$: traslazione in basso di $1$ unità.
3. $|2^{x+1} - 1|$: simmetrizzazione (modulo esterno), ovvero ribaltamento nel semipiano superiore $y \ge 0$ della parte di grafico che si trovava al di sotto dell'asse $x$.

### 3. Studio della funzione $y = 3^{-x} - 5$

La sequenza delle trasformazioni a partire da $x$ è:
- $f_1(x) = -x$ (riflessione rispetto all'asse $y$)
- $f_2(t) = 3^t$ (funzione esponenziale)
- $f_3(t) = t - 5$ (traslazione verticale verso il basso di $5$ unità)

---

## Materiale generato

### Riepilogo
Il documento illustra come tracciare il grafico di funzioni esponenziali complesse applicando sistematicamente le trasformazioni geometriche elementari: traslazioni (orizzontali e verticali), valori assoluti (simmetrie) e riflessioni.

### Esercizi simili

1. Tracciare il grafico della funzione $y = 2^{|x|} - 2$.
   <details><summary>Soluzione</summary>Partendo dal grafico di $2^x$, si applica il valore assoluto all'argomento (simmetria rispetto all'asse $y$ per $x<0$) ottenendo $2^{|x|}$, e infine si traspone l'intero grafico verso il basso di $2$ unità sottraendo $2$. Il grafico interseca l'asse $y$ in $y = 2^0 - 2 = -1$.
   </details>

2. Tracciare il grafico della funzione $y = |3^x - 3|$.
   <details><summary>Soluzione</summary>Si parte dal grafico di $3^x$. Si traccia prima $3^x - 3$ (traslazione verso il basso di $3$ unità, con asintoto a $y = -3$). Applicando il valore assoluto esterno $|\cdot|$, tutta la porzione di grafico che si trova sotto l'asse $x$ (per $x < 1$) viene ribaltata specularmente nel semipiano positivo.
   </details>

3. Tracciare il grafico della funzione $y = 2^{x-2} + 1$.
   <details><summary>Soluzione</summary>Si parte dalla funzione esponenziale elementare $2^x$. Si applica una traslazione orizzontale verso destra di $2$ unità ottenendo $2^{x-2}$, e successivamente una traslazione verticale verso l'alto di $1$ unità, ottenendo l'asintoto orizzontale in $y = 1$.
   </details>

### Flashcard
- **D:** Come si modifica il grafico di $f(x)$ se consideriamo $f(x - a)$ con $a > 0$? — **R:** Il grafico subisce una traslazione orizzontale verso destra di $a$ unità.
- **D:** Qual è l'effetto della trasformazione $f(x) \to |f(x)|$ sul grafico? — **R:** La parte di grafico situata al di sotto dell'asse $x$ viene riflessa specularmente nel semipiano positivo $y \ge 0$.
- **D:** Come si comporta la funzione esponenziale $f(x) = a^x$ con $a > 1$ per $x \to -\infty$? — **R:** Il grafico si avvicina indefinitamente all'asse $x$ ($y=0$), che costituisce un asintoto orizzontale sinistro.
