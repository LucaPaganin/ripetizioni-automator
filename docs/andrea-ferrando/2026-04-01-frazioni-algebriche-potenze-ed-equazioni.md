---
titolo: Frazioni algebriche, potenze ed equazioni
data: '2026-04-01'
studente: Andrea Ferrando
materia: matematica
argomento: Frazioni algebriche e potenze
sottoargomenti:
- Condizioni di esistenza
- Proprietà delle potenze
- Equazioni di secondo grado
esercizi:
- 2
- 3
- 4
errori_tipici:
- Applicare scorrettamente la proprietà della potenza negativa
- Dimenticare di escludere le soluzioni che annullano il denominatore nelle C.E.
fonte: https://drive.google.com/file/d/1W428uWQ2Ma0EbEP11rMvJ-vND3pjja1S/view?usp=drivesdk
generato: '2026-11-07'
---

# Frazioni algebriche, potenze ed equazioni

## Formule chiave

- **Proprietà delle potenze con esponente negativo:**
  $$a^{-b} = \frac{1}{a^b}$$
  $$a^{-1} = \frac{1}{a}$$
  $$\left(\frac{1}{m}\right)^{-x} = \left(\frac{m}{1}\right)^x = m^x$$

- **Esponente nullo:**
  $$a^0 = 1 \quad (\text{per } a \neq 0)$$

- **Condizioni di esistenza (C.E.) per frazioni algebriche:**
  Data una frazione algebrica della forma $\frac{A(x)}{B(x)}$ dove $A(x)$ e $B(x)$ sono polinomi, le condizioni di esistenza si trovano ponendo il denominatore diverso da zero:
  $$B(x) \neq 0$$

## Esercizio 2

Data la frazione algebrica:
$$\frac{1}{x - 1}$$
Determiniamo le Condizioni di Esistenza (C.E.):
1. $A(x) = 1$
2. $B(x) = x - 1$

Poniamo $B(x) = 0$ per trovare i valori da escludere:
$$x - 1 = 0 \implies x = 1$$

Quindi le condizioni di esistenza sono:
$$\boxed{x \neq 1}$$

## Esercizio 3

Data la frazione algebrica:
$$\frac{x + 1}{x^2 - 4}$$
Determiniamo le C.E. ponendo il denominatore diverso da zero ($B(x) \neq 0$):
$$x^2 - 4 \neq 0$$

Risolviamo l'equazione associata:
$$x^2 - 4 = 0 \implies x^2 = 4 \implies x = -2 \lor x = 2$$

Metodo alternativo con scomposizione (differenza di quadrati):
$$x^2 - 4 = (x - 2)(x + 2) = 0$$
Da cui:
$$(x - 2) = 0 \lor (x + 2) = 0 \implies x = 2 \lor x = -2$$

Pertanto, le condizioni di esistenza sono:
$$\boxed{x \neq -2 \land x \neq 2}$$

## Esercizio 4

Data la frazione algebrica:
$$\frac{x + 1}{x^2 + 4x}$$
Poniamo il denominatore uguale a zero per trovare i valori da escludere:
$$x^2 + 4x = 0$$

Raccogliamo la $x$ a fattor comune:
$$x(x + 4) = 0$$

Applichiamo la legge dell'annullamento del prodotto:
$$x = 0 \lor x + 4 = 0 \implies x = 0 \lor x = -4$$

Le condizioni di esistenza sono quindi:
$$\boxed{x \neq 0 \land x \neq -4}$$

---
## Materiale generato

### Riepilogo
Questa lezione introduce le frazioni algebriche e la determinazione delle condizioni di esistenza (C.E.) imponendo il denominatore diverso da zero. Vengono inoltre ripassate le proprietà delle potenze con esponente intero negativo e richiamate le equazioni di secondo grado utili per la scomposizione.

### Esercizi simili

1. Determina le condizioni di esistenza della frazione algebrica:
   $$\frac{2x - 3}{x^2 - 9}$$
   <details><summary>Soluzione</summary>
   Pongo il denominatore diverso da zero: $x^2 - 9 \neq 0$. Risolvo l'equazione associata $x^2 - 9 = 0 \implies x^2 = 9 \implies x = \pm 3$.
   C.E.: $\boxed{x \neq -3 \land x \neq 3}$
   </details>

2. Semplifica la seguente espressione applicando le proprietà delle potenze:
   $$\left(\frac{2}{3}\right)^{-2}$$
   <details><summary>Soluzione</summary>
   Inverto la frazione cambiando segno all'esponente: $\left(\frac{3}{2}\right)^2 = \frac{3^2}{2^2} = \boxed{\frac{9}{4}}$.
   </details>

3. Determina le condizioni di esistenza della frazione algebrica:
   $$\frac{5x}{x^2 - 5x}$$
   <details><summary>Soluzione</summary>
   Pongo il denominatore diverso da zero: $x^2 - 5x \neq 0$. Raccolgo a fattor comune: $x(x - 5) \neq 0$. Da cui $x \neq 0$ e $x - 5 \neq 0 \implies x \neq 5$.
   C.E.: $\boxed{x \neq 0 \land x \neq 5}$
   </details>

### Flashcard
- **D:** Cosa rappresenta la C.E. di una frazione algebrica? — **R:** L'insieme dei valori che si possono assegnare all'incognita senza che il denominatore si annulli.
- **D:** Quanto vale $a^{-b}$ con $a \neq 0$? — **R:** $\frac{1}{a^b}$
- **D:** Come si risolve l'equazione $x^2 + 2x = 0$? — **R:** Raccogliendo a fattor comune $x(x + 2) = 0$, ottenendo le soluzioni $x = 0 \lor x = -2$.
- **D:** Quanto vale $m^0$ per $m \neq 0$? — **R:** $1$
