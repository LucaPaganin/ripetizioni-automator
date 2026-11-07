---
titolo: 'Geometria Analitica e Calcolo Integrale: Circonferenza e Parabola'
data: '2026-04-18'
studente: Andrea Ferrando
materia: matematica
argomento: geometria analitica e calcolo integrale
sottoargomenti:
- completamento del quadrato
- equazione della circonferenza
- derivata e integrale indefinito e definito
- area sotto la parabola
esercizi: []
errori_tipici: []
fonte: https://drive.google.com/file/d/1J9QPd2Gvpa0JO8jhmKmqBv-3N2njb-tq/view?usp=drivesdk
generato: '2026-11-07'
---

# Geometria Analitica e Calcolo Integrale: Circonferenza e Parabola

## Formule chiave

### Completamento del quadrato per la circonferenza

Dato il polinomio in forma generale:
$$x^2 + y^2 + ax + by + c = 0$$

Completando il quadrato per $x$ e per $y$ si ottiene:
$$x^2 + 2\left(\frac{a}{2}\right)x + \frac{a^2}{4} + y^2 + 2\left(\frac{b}{2}\right)y + \frac{b^2}{4} = -c + \frac{a^2}{4} + \frac{b^2}{4}$$

Ovvero nella forma canonica della circonferenza:
$$\left(x + \frac{a}{2}\right)^2 + \left(y + \frac{b}{2}\right)^2 = \frac{a^2 + b^2 - 4c}{4}$$

Le coordinate del centro $C$ e il raggio $r$ sono:
$$C\left(-\frac{a}{2}, -\frac{b}{2}\right), \quad r = \frac{1}{2}\sqrt{a^2 + b^2 - 4c}$$

La condizione di esistenza della circonferenza è:
$$a^2 + b^2 - 4c \ge 0$$

---

### Derivate e Integrale Indefinito

* **Derivata di una potenza:**
  $$\frac{d}{dx}\left(x^m\right) = m x^{m-1}$$
  In particolare:
  $$\frac{d}{dx}(x^2) = 2x$$

* **Definizione di integrale indefinito:**
  Data una funzione $f(x)$, l'integrale indefinito è una funzione $F(x)$ tale che $F'(x) = f(x)$:
  $$\int f(x) \, dx = F(x) + c$$

* **Integrali notevoli:**
  $$\int x^2 \, dx = \frac{x^3}{3} + c$$

---

### Integrale Definito e Area sotto la parabola

Il Teorema Fondamentale del Calcolo Integrale stabilisce che:
$$\int_{a}^{b} f(x) \, dx = F(b) - F(a)$$

Per calcolare l'area sottesa dalla parabola $y = x^2$ tra $0$ e $x_A$:
$$\text{Area sotto la parabola} = \int_{0}^{x_A} x^2 \, dx = \left[ \frac{x^3}{3} \right]_{0}^{x_A} = \frac{x_A^3}{3}$$

Area del rettangolo circoscritto di lati $x_A$ e $x_A^2$:
$$\text{Area rettangolo} = x_A \cdot x_A^2 = x_A^3$$

Area compresa tra la parabola, l'asse $y$ e la retta $y = x_A^2$ (SP):
$$\text{SP} = x_A^3 - \int_{0}^{x_A} x^2 \, dx = x_A^3 - \frac{x_A^3}{3} = \frac{2}{3} x_A^3$$

---

## Esercizi Svolti negli Appunti

### Esercizio 1: Completamento del quadrato numerico
Data l'equazione:
$$x^2 + y^2 + 4x - 2y = 0$$

Raggruppiamo i termini in $x$ e in $y$ e completiamo i quadrati aggiungendo e sottraendo i termini opportuni:
$$x^2 + 4x + 2^2 - 2^2 + y^2 - 2y + 1^2 - 1^2 = 0$$
$$(x + 2)^2 - 4 + (y - 1)^2 - 1 = 0$$
$$(x + 2)^2 + (y - 1)^2 = 5$$

Confrontando con l'equazione canonica $(x - x_C)^2 + (y - y_C)^2 = r^2$, otteniamo:
* Centro: $C(-2, 1)$
* Raggio: $r = \sqrt{5}$

---

## ⚠️ Errori da evitare
*(Nessun errore esplicito segnalato negli appunti)*

---

## Materiale generato

### Riepilogo
Il documento riassume i procedimenti algebrici fondamentali per ricondurre l'equazione generale della circonferenza alla forma canonica tramite il completamento del quadrato, introducendo inoltre le basi del calcolo differenziale e integrale applicato al calcolo delle aree sotto la parabola.

### Esercizi simili
1. Trova centro e raggio della circonferenza di equazione $x^2 + y^2 - 6x + 4y - 3 = 0$.
   <details><summary>Soluzione</summary>
   Riscrivendo con il completamento del quadrato:
   $(x - 3)^2 - 9 + (y + 2)^2 - 4 - 3 = 0 \implies (x - 3)^2 + (y + 2)^2 = 16$.
   Centro $C(3, -2)$, $r = 4$.
   </details>

2. Calcola l'integrale indefinito $\int (3x^2 - 4x + 5) \, dx$.
   <details><summary>Soluzione</summary>
   Integrando termine a termine:
   $3\left(\frac{x^3}{3}\right) - 4\left(\frac{x^2}{2}\right) + 5x + c = x^3 - 2x^2 + 5x + c$.
   </details>

3. Calcola l'area della regione compresa tra la parabola $y = x^2$, l'asse $x$ e la retta $x = 3$.
   <details><summary>Soluzione</summary>
   Si calcola l'integrale definito:
   $\int_{0}^{3} x^2 \, dx = \left[ \frac{x^3}{3} \right]_{0}^{3} = \frac{3^3}{3} - 0 = \frac{27}{3} = 9$.
   </details>

### Flashcard
- **D:** Qual è la formula generale per trovare le coordinate del centro $C(x_C, y_C)$ di una circonferenza data in forma $x^2 + y^2 + ax + by + c = 0$? — **R:** $C\left(-\frac{a}{2}, -\frac{b}{2}\right)$
- **D:** Qual è la condizione di esistenza di una circonferenza in forma cartesiana? — **R:** $a^2 + b^2 - 4c \ge 0$
- **D:** Come si definisce l'integrale indefinito di una funzione $f(x)$? — **R:** $\int f(x) \, dx = F(x) + c$ tale che la derivata di $F(x)$ sia $f(x)$.
- **D:** Qual è l'area sottesa dalla parabola $y = x^2$ nell'intervallo $[0, x_A]$? — **R:** $\frac{x_A^3}{3}$
