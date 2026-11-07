---
titolo: Iperbole e funzione omografica
data: '2026-05-25'
studente: Andrea Ferrando
materia: matematica
argomento: Geometria analitica
sottoargomenti:
- Iperbole
- Asintoti
- Funzione omografica
esercizi: []
errori_tipici: []
fonte: https://drive.google.com/file/d/1fxXmdGlnsA6mbiUn09ztEwuMw8r9wPFz/view?usp=drivesdk
generato: '2026-11-07'
---

# Iperbole e funzione omografica

## Formule chiave

L'iperbole è il luogo geometrico dei punti $P$ del piano per cui è costante la differenza delle distanze da due punti fissi $F_1$ e $F_2$ (fuochi):

$$||PF_2| - |PF_1|| = 2a$$

- L'equazione canonica dell'iperbole si riconosce da quella delle altre coniche perché i termini al quadrato sono **discordi**:
  $$x^2 - y^2 = 1$$
  oppure:
  $$x^2 - y^2 = -1$$

- Ricavando $y$ da $x^2 - y^2 = 1$:
  $$-y^2 = 1 - x^2 \implies y^2 = x^2 - 1 \implies y = \pm\sqrt{x^2 - 1}$$
  con la condizione di esistenza:
  $$x^2 - 1 \ge 0 \implies x \le -1 \lor x \ge 1$$

- Riferendo l'iperbole ai suoi asintoti si ottiene l'equazione:
  $$xy = \frac{1}{2} \implies y = \frac{1}{2x}$$
  Questa è una funzione.

## Funzione omografica

Traslando l'iperbole riferita agli asintoti si ottiene la **funzione omografica**:

$$y = \frac{ax + b}{cx + d}$$

---

## Materiale generato

### Riepilogo
L'iperbole è una conica definita dalla differenza costante delle distanze dai fuochi e si riconosce per i termini quadratici discordi. Attraverso una rotazione e traslazione del sistema di riferimento si perviene alla funzione omografica.

### Esercizi simili

1. Data l'iperbole di equazione $x^2 - y^2 = 4$, determinare le intersezioni con gli assi cartesiani e il dominio della funzione $y = \pm\sqrt{x^2 - 4}$.
   <details><summary>Soluzione</summary>
   Dominio: $x^2 - 4 \ge 0 \implies x \le -2 \lor x \ge 2$. L'iperbole non interseca l'asse $y$ (non esiste per $x=0$), mentre interseca l'asse $x$ nei punti $(\pm 2, 0)$.
   </details>

2. Riconoscere e disegnare la conica di equazione $2x^2 - 2y^2 = 8$.
   <details><summary>Soluzione</summary>
   Dividendo per $8$ si ottiene l'equazione canonica dell'iperbole equilatera: $\frac{x^2}{4} - \frac{y^2}{4} = 1$, ovvero $x^2 - y^2 = 4$.
   </details>

3. Data la funzione omografica $y = \frac{2x + 1}{x - 1}$, determinare gli asintoti.
   <details><summary>Soluzione</summary>
   Asintoto verticale: $x = 1$. Asintoto orizzontale: $y = \frac{a}{c} = \frac{2}{1} = 2$.
   </details>

### Flashcard
- **D:** Qual è la definizione geometrica dell'iperbole? — **R:** Il luogo dei punti per cui il valore assoluto della differenza delle distanze da due fuochi è costante ($2a$).
- **D:** Come si riconosce l'equazione di un'iperbole rispetto ad un'ellisse? — **R:** Nell'iperbole i coefficienti dei termini al quadrato ($x^2$ e $y^2$) sono discordi (hanno segno opposto).
- **D:** Cos'è la funzione omografica? — **R:** È una funzione razionale fratta del tipo $y = \frac{ax+b}{cx+d}$, che rappresenta un'iperbole equilatera traslata con gli assi paralleli agli asintoti.
