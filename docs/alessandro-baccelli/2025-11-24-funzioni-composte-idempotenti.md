---
titolo: Funzioni composte e funzioni idempotenti
data: '2025-11-24'
studente: Alessandro Baccelli
materia: matematica
argomento: Analisi matematica
sottoargomenti:
- Funzioni composte
- Proprietà delle funzioni
- Parabola e vertice
esercizi:
- 1
- 3
errori_tipici:
- Confondere l'ordine della composizione di funzioni (in generale $f \circ g \neq
  g \circ f$)
fonte: https://drive.google.com/file/d/1fOT9pndsd0VGuNzgvkQXqLepV6mULit9/view?usp=drivesdk
generato: '2026-11-07'
---

# Funzioni composte e funzioni idempotenti

## Formule chiave

- **Composizione di funzioni:** Delle funzioni $f: D_1 \to C_1$ e $g: D_2 \to C_2$ (con $C_1 \subseteq D_2$), la funzione composta $(f \circ g)(x) = f(g(x))$ ha come dominio l'insieme degli $x \in D_1$ tali che $f(x) \in D_2$.
- **Vertice della parabola** $y = ax^2 + bx + c$:
  $$x_V = -\frac{b}{2a}, \quad y_V = -\frac{\Delta}{4a}$$
- **Funzione idempotente:** Una funzione $f$ tale che $f \circ f = f$ (le potenze successive lasciano la funzione invariata).

---

## Esercizio 1

**Testo:** Siano $f, g: \mathbb{R} \to \mathbb{R}$ due funzioni date da $f(x) = x - 2$ e $g(x) = 1 + x^2$.
1. Come sono definite le funzioni $f \circ g$ e $g \circ f$?
2. Esistono numeri reali $x$ per cui $(f \circ g)(x) = (g \circ f)(x)$?
3. Le funzioni $f \circ g$ e $g \circ f$ sono uguali?

**Svolgimento:**

1. Calcoliamo la prima funzione composta $(f \circ g)(x)$:
   $$(f \circ g)(x) = f(g(x)) = f(1 + x^2) = (1 + x^2) - 2 = 1 + x^2 - 2 = \boxed{x^2 - 1}$$

   Calcoliamo la seconda funzione composta $(g \circ f)(x)$:
   $$\begin{aligned}
   (g \circ f)(x) &= g(f(x)) = g(x - 2) = 1 + (x - 2)^2 \\
   &= 1 + (x^2 - 4x + 4) = \boxed{x^2 - 4x + 5}
   \end{aligned}$$

2. Cerchiamo se esistono valori reali di $x$ tali che $(f \circ g)(x) = (g \circ f)(x)$:
   $$x^2 - 1 = x^2 - 4x + 5$$
   Semplificando $x^2$ da entrambi i membri:
   $$-1 = -4x + 5 \implies 4x = 6 \implies x = \frac{6}{4} = \boxed{\frac{3}{2}}$$
   Esiste quindi un unico valore reale $x = \frac{3}{2}$ per cui l'uguaglianza è verificata.

3. Le due funzioni **non** sono uguali, poiché coincidono soltanto nel punto $x = \frac{3}{2}$ e non per ogni $x \in \mathbb{R}$.

---

## Esercizio 3

**Testo:** Determinare un insieme $A$ e un'applicazione $f: A \to A$ tale che $f \circ f = f$, ma $f \neq \text{id}_A$.

**Svolgimento:**
Dobbiamo trovare una funzione idempotente, ovvero una funzione la cui composizione con sé stessa restituisce la funzione stessa ($f^n = f \quad \forall n \in \mathbb{N}^+$).

Consideriamo l'insieme $A = \mathbb{R}^2$ e definiamo l'applicazione $f: \mathbb{R}^2 \to \mathbb{R}^2$ tale che:
$$f(x, y) = (x, 0)$$

Verifichiamo la proprietà idempotente calcolando $(f \circ f)(x, y)$:
$$f(f(x, y)) = f(x, 0) = (x, 0) = f(x, y)$$
Poiché $f(f(x, y)) = f(x, y)$, la funzione è idempotente e chiaramente $f \neq \text{id}_{\mathbb{R}^2}$ (in quanto proietta ogni punto sull'asse $x$).

---

## ⚠️ Errori da evitare

- Pensare che la composizione di funzioni sia commutativa: in generale **$f \circ g \neq g \circ f$**.
- Confondere il punto in cui due funzioni composte assumono lo stesso valore con l'identità tra funzioni (due funzioni sono uguali se e solo se coincidono per *ogni* $x$ del loro dominio).

---

## Materiale generato

### Riepilogo
La composizione di funzioni $(f \circ g)(x)$ consiste nell'applicare prima $g$ e poi $f$, e in generale non gode della proprietà commutativa. Una funzione è detta idempotente se applicata due (o più) volte dà lo stesso risultato ($f \circ f = f$).

### Esercizi simili

1. Siano $f(x) = 2x + 1$ e $g(x) = x^2 - 3$. Determinare $(f \circ g)(x)$ e $(g \circ f)(x)$.
<details><summary>Soluzione</summary>
$(f \circ g)(x) = f(x^2 - 3) = 2(x^2 - 3) + 1 = 2x^2 - 6 + 1 = 2x^2 - 5$.
$(g \circ f)(x) = g(2x + 1) = (2x + 1)^2 - 3 = 4x^2 + 4x + 1 - 3 = 4x^2 + 4x - 2$.
</details>

2. Trovare i valori di $x$ per cui $(f \circ g)(x) = (g \circ f)(x)$ con $f(x) = 3x$ e $g(x) = x + 4$.
<details><summary>Soluzione</summary>
$(f \circ g)(x) = 3(x + 4) = 3x + 12$.
$(g \circ f)(x) = 3x + 4$.
L'equazione $3x + 12 = 3x + 4 \implies 12 = 4$ è impossibile. Non esistono valori di $x$.
</details>

3. Verificare se la funzione $f: \mathbb{R} \to \mathbb{R}$ definita come $f(x) = |x|$ è idempotente.
<details><summary>Soluzione</summary>
$(f \circ f)(x) = f(|x|) = ||x|| = |x| = f(x)$. Sì, la funzione valore assoluto è idempotente.
</details>

### Flashcard
- **D:** Cosa significa $(f \circ g)(x)$? — **R:** Significa $f(g(x))$, ovvero si applica prima la funzione $g$ e poi la funzione $f$.
- **D:** Come si trova l'ascissa del vertice di una parabola $y = ax^2 + bx + c$? — **R:** Tramite la formula $x_V = -\frac{b}{2a}$.
- **D:** Cos'è una funzione idempotente? — **R:** Una funzione $f$ tale che applicata a sé stessa non cambia il risultato, cioè $f(f(x)) = f(x)$.
