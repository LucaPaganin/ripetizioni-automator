---
titolo: 'Iperbole: Forma Canonica e Vertici Immaginari'
data: '2026-04-11'
studente: Andrea Ferrando
materia: matematica
argomento: Geometria analitica
sottoargomenti:
- Iperbole
- Forma canonica
- Fuochi
- Vertici immaginari
esercizi: []
errori_tipici:
- Confondere l'iperbole con fuochi sull'asse x con quella con fuochi sull'asse y
- Considerare intersezioni con l'asse y per un'iperbole con fuochi sull'asse x senza
  considerare i numeri complessi
fonte: https://drive.google.com/file/d/19z-k-PQZlZ76zUQ-P8-lQ1_OPflIuTWL/view?usp=drivesdk
generato: '2026-11-07'
---

# Iperbole: Forma Canonica e Vertici Immaginari

## Formule chiave

L'equazione in forma canonica dell'iperbole è data da:

$$\frac{x^2}{a^2} - \frac{y^2}{b^2} = \pm 1$$

Distinguiamo due casi principali a seconda della posizione dei fuochi:

1. **Fuochi sull'asse $x$**:
   $$\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$$
   - **Vertici reali**: $(\pm a, 0)$
   - **Intersezioni con l'asse $y$**: ponendo $x = 0$ si ottiene:
     $$\begin{cases} x = 0 \\ -\frac{y^2}{b^2} = 1 \end{cases} \implies \begin{cases} x = 0 \\ y^2 = -b^2 \end{cases} \implies \emptyset$$
     L'iperbole non interseca l'asse $y$ nei numeri reali.

2. **Fuochi sull'asse $y$**:
   $$\frac{x^2}{a^2} - \frac{y^2}{b^2} = -1$$

---

## Vertici immaginari e trasformazioni

Se consideriamo i punti d'intersezione con l'asse $y$ nel campo complesso ($\mathbb{C}$):
$$y^2 = -b^2 \implies y = \pm\sqrt{-b^2} = \pm i b \in \mathbb{C}$$
dove $i^2 = -1$ e $\sqrt{-b^2} = i b$.

Applicando una trasformazione di coordinate in cui si scambiano le variabili:
$$\begin{cases} x' = y \\ y' = x \end{cases}$$

L'equazione $x^2 - y^2 = 1$ diventa:
$$y'^2 - x'^2 = -(x'^2 - y'^2) = 1 \implies x'^2 - y'^2 = -1$$

Se introduciamo una trasformazione complessa del tipo:
$$\begin{cases} x' = i x \\ y' = i y \end{cases} \implies \begin{cases} x'^2 = -x^2 \\ y'^2 = -y^2 \end{cases}$$

Sostituendo nell'equazione canonica:
$$-\frac{x'^2}{a^2} + \frac{y'^2}{b^2} = 1 \implies \frac{x'^2}{a^2} - \frac{y'^2}{b^2} = -1$$

---

## ⚠️ Errori da evitare

- Dimenticare che l'intersezione con l'asse non trasversale (immaginario) produce valori complessi se considerata algebricamente nel piano reale ($\mathbb{R}$).

---

## Materiale generato

### Riepilogo
Questa lezione introduce la forma canonica dell'iperbole, la distinzione tra i fuochi sull'asse $x$ e sull'asse $y$, e l'analisi dei vertici immaginari tramite l'uso dei numeri complessi e delle trasformazioni di coordinate.

### Esercizi simili
1. Determinare i vertici reali e l'eventuale intersezione con gli assi dell'iperbole $\frac{x^2}{9} - \frac{y^2}{16} = 1$.
   <details><summary>Soluzione</summary>
   I fuochi sono sull'asse $x$. 
   Vertici reali: $(\pm 3, 0)$. 
   Intersezioni con l'asse $y$: $y = \pm 4i$ (vertici immaginari).
   </details>

2. Scrivere l'equazione canonica dell'iperbole con fuochi sull'asse $y$ sapendo che $a = 2$ e $b = 5$.
   <details><summary>Soluzione</summary>
   L'equazione per i fuochi sull'asse $y$ è $\frac{x^2}{a^2} - \frac{y^2}{b^2} = -1$.
   Sostituendo $a = 2$ e $b = 5$:
   $$\frac{x^2}{4} - \frac{y^2}{25} = -1$$
   </details>

3. Data l'iperbole $x^2 - 4y^2 = 4$, scriverla in forma canonica.
   <details><summary>Soluzione</summary>
   Dividendo entrambi i membri per $4$:
   $$\frac{x^2}{4} - \frac{y^2}{1} = 1$$
   </details>

### Flashcard
- **D:** Qual è l'equazione canonica dell'iperbole con i fuochi sull'asse $x$? — **R:** $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$
- **D:** Cosa rappresenta $i$ nei numeri complessi? — **R:** L'unità immaginaria tale che $i^2 = -1$.
- **D:** L'iperbole con fuochi sull'asse $x$ interseca l'asse $y$ nei numeri reali? — **R:** No, non interseca l'asse $y$ (le intersezioni sono immaginarie $\pm ib$).
