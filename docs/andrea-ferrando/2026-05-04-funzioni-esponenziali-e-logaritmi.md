---
titolo: Funzioni esponenziali e logaritmi
data: '2026-05-04'
studente: Andrea Ferrando
materia: matematica
argomento: Esponenziali e Logaritmi
sottoargomenti:
- Funzione esponenziale
- Proprietà degli esponenziali
- Numero di Eulero
- Definizione e proprietà dei logaritmi
- Logaritmo naturale
esercizi: []
errori_tipici:
- Basi negative con esponenti non interi (es. $(-1)^\pi$ non ha senso)
- Dimenticare che l'argomento di un logaritmo deve sempre essere positivo
fonte: https://drive.google.com/file/d/1b_wJQkRdDsI5buc4wvM3eeGy4pl9z_bz/view?usp=drivesdk
generato: '2026-11-07'
---

# Funzioni esponenziali e logaritmi

## Formule chiave

### Funzione Esponenziale
Data la funzione $f(x) = a^x$ con $Dom f: \mathbb{R}$:
- Se $a = 1$, allora $a^x = 1^x = 1 \quad \forall x \in \mathbb{R}$
- $a^x > 0 \quad \forall x \in \mathbb{R}, \forall a > 0$
- La base $a$ non può essere negativa.
- Proprietà:
  $$a^{x+y} = a^x \cdot a^y$$
  $$a^{-x} = \frac{1}{a^x} = \left(\frac{1}{a}\right)^x$$
  $$a^x = b^{-x} \iff b = \frac{1}{a}$$

### Numero di Eulero
Il numero di Eulero $e$ è definito come:
$$e = \lim_{n \to +\infty} \left(1 + \frac{1}{n}\right)^n \simeq 2,71$$
La funzione esponenziale naturale è $f(x) = e^x$.

### Logaritmi
Definizione: $\log_a b$ è l'esponente da dare ad $a$ per ottenere $b$.
Condizione di esistenza fondamentale: L'argomento di un logaritmo deve sempre essere positivo.

Proprietà dei logaritmi:
- $\log_a(bc) = \log_a b + \log_a c$
- $\log_a\left(\frac{b}{c}\right) = \log_a b - \log_a c$
- $\log_a(b^c) = c \cdot \log_a b$
- $\log_a a = 1$ (poiché $a^1 = a$)
- $\log_a 1 = 0$ (poiché $a^0 = 1$)
- $a^{\log_a b} = b$
- Cambiamento di base: $\log_b x = \frac{\log_a x}{\log_a b}$
- Logaritmo naturale: $\log_e x = \ln x$

---

## Materiale generato

### Riepilogo
Il documento riassume le proprietà fondamentali delle funzioni esponenziali e dei logaritmi, illustrando il loro comportamento in base ai parametri, i domini di validità e le principali regole di calcolo algebrico.

### Esercizi simili

1. **Esercizio 1:** Risolvere l'equazione esponenziale $2^x = 32$.
   <details><summary>Soluzione</summary>
   Riscriviamo $32$ come potenza di $2$: $32 = 2^5$.
   Quindi l'equazione diventa $2^x = 2^5$, da cui $\boxed{x = 5}$.
   </details>

2. **Esercizio 2:** Calcolare il valore dell'espressione $\log_3 81$.
   <details><summary>Soluzione</summary>
   Cerchiamo l'esponente da dare a $3$ per ottenere $81$. Poiché $3^4 = 81$, si ha $\log_3 81 = \boxed{4}$.
   </details>

3. **Esercizio 3:** Semplificare l'espressione $\log_2 8 + \log_2 4$.
   <details><summary>Soluzione</summary>
   Utilizzando la proprietà del logaritmo del prodotto: $\log_2(8 \cdot 4) = \log_2 32$.
   Poiché $2^5 = 32$, il risultato è $\boxed{5}$.
   </details>

### Flashcard
- **D:** Qual è il dominio di una funzione esponenziale $f(x) = a^x$ con $a > 0$? — **R:** $\mathbb{R}$
- **D:** Quanto vale $\log_a 1$ per ogni $a > 0$ e $a \neq 1$? — **R:** $0$
- **D:** Come si scrive il logaritmo in base $e$? — **R:** $\ln x$
- **D:** Qual è la condizione di esistenza per l'argomento di un logaritmo $\log_a(x)$? — **R:** L'argomento deve essere strettamente positivo ($x > 0$).
