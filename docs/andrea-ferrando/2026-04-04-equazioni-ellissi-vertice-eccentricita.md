---
titolo: 'Equazioni delle ellissi: vertice ed eccentricità'
data: '2026-04-04'
studente: Andrea Ferrando
materia: matematica
argomento: Geometria analitica
sottoargomenti:
- Ellisse
- Eccentricità
- Semiassi
esercizi:
- 150
- 138
errori_tipici:
- Scambiare il semiasse maggiore con quello minore nell'impostare l'equazione dell'ellisse
- Confondere la posizione dell'asse maggiore rispetto all'asse x o y
fonte: https://drive.google.com/file/d/152RyBiAQ2j-iE66huZXqu_xWAQIcOoTA/view?usp=drivesdk
generato: '2026-11-07'
---

# Equazioni delle ellissi: vertice ed eccentricità

## Formule chiave

- Equazione canonica dell'ellisse con centro nell'origine:
  $$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$$

- Distanza focale $c$:
  $$c = \sqrt{|a^2 - b^2|}$$

- Eccentricità $e$:
  $$e = \frac{c}{\max(a, b)} = \frac{\sqrt{|a^2 - b^2|}}{\max(a, b)}$$

- Condizione di appartenenza di un punto $P(x_0, y_0)$ all'ellisse $\gamma$:
  $$\frac{x_0^2}{a^2} + \frac{y_0^2}{b^2} = 1$$

---

## Esercizio 150

**Testo:** Scrivi le equazioni delle ellissi con centro nell'origine, un vertice in $(2, 0)$ ed eccentricità $e = \frac{\sqrt{3}}{2}$.

**Svolgimento:**

Dal vertice $V(2, 0)$ sappiamo che uno dei semiassi interseca l'asse $x$ nel punto $2$. Chiamando $a_x$ e $a_y$ i semiassi rispettivamente lungo l'asse $x$ e l'asse $y$, abbiamo $a_x = 2$ oppure $a_y = 2$.
Dall'eccentricità $e = \frac{\sqrt{3}}{2}$ sappiamo che $e^2 = \frac{3}{4}$, ovvero:
$$\frac{|a^2 - b^2|}{\max(a,b)^2} = \frac{3}{4}$$

Analizziamo i due casi possibili a seconda che il semiasse orizzontale sia maggiore o minore di quello verticale.

### Caso 1: Asse orizzontale maggiore ($a > b$, quindi $\max(a,b) = a$)
Posto $a = 2$, l'equazione dell'eccentricità diventa:
$$\frac{\sqrt{4 - b^2}}{2} = \frac{\sqrt{3}}{2}$$
Elevando al quadrato e semplificando:
$$4 - b^2 = 3 \implies b^2 = 1 \implies b = 1$$
Poiché $a = 2$ e $b = 1$ verificano la condizione $a > b$, l'equazione dell'ellisse è:
$$\frac{x^2}{4} + \frac{y^2}{1} = 1$$

### Caso 2: Asse orizzontale minore ($a < b$, quindi $\max(a,b) = b$)
Posto $b = 2$, l'equazione dell'eccentricità diventa:
$$\frac{\sqrt{b^2 - 4}}{b} = \frac{\sqrt{3}}{2}$$
Sostituendo $b = 2$ nell'argomento della radice e imponendo $a = 2$ come semiasse orizzontale ($a_x = 2, a_y = b$):
$$\frac{\sqrt{a^2 - 4}}{a} = \frac{\sqrt{3}}{2} \implies \frac{4 - 4}{a} \dots$$
Rifacendoci allo svolgimento alternativo degli appunti (convenzione con $a_x, a_y$):
- Se $a_x = 2$ e $a_y = a$: si ottiene $\frac{a^2 - 4}{a^2} = \frac{3}{4} \implies 4(a^2 - 4) = 3a^2 \implies a^2 = 16 \implies a = 4$.
Poiché $a_x = 2$ e $a_y = 4$ (con $a_y > a_x$), l'equazione è:
$$\frac{x^2}{4} + \frac{y^2}{16} = 1$$

Risultati finali:
$$\boxed{\frac{x^2}{4} + \frac{y^2}{1} = 1} \quad \text{oppure} \quad \boxed{\frac{x^2}{4} + \frac{y^2}{16} = 1}$$

---

## Esercizio 138

**Testo:** Scrivi l'equazione dell'ellisse che passa per i punti $P(0, 3)$ e $Q(2, \sqrt{3})$.

**Svolgimento:**

L'equazione generica dell'ellisse è:
$$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$$

Imponiamo il passaggio per $P(0, 3)$ e $Q(2, \sqrt{3})$ sostituendo le coordinate nel fascio:

1. Per $P(0, 3)$:
   $$\frac{0^2}{a^2} + \frac{3^2}{b^2} = 1 \implies \frac{9}{b^2} = 1 \implies b^2 = 9 \implies b = 3$$

2. Per $Q(2, \sqrt{3})$:
   $$\frac{2^2}{a^2} + \frac{(\sqrt{3})^2}{b^2} = 1 \implies \frac{4}{a^2} + \frac{3}{b^2} = 1$$

Mettendo a sistema e sostituendo $b^2 = 9$:
$$\begin{cases} b^2 = 9 \\ \frac{4}{a^2} + \frac{3}{9} = 1 \end{cases} \implies \begin{cases} b = 3 \\ \frac{4}{a^2} + \frac{1}{3} = 1 \end{cases}$$

Risolviamo per $\frac{1}{a^2}$:
$$\frac{4}{a^2} = 1 - \frac{1}{3} = \frac{2}{3}$$
$$\frac{4}{a^2} = \frac{2}{3} \implies 2a^2 = 12 \implies a^2 = 6 \implies a = \sqrt{6}$$

Sostituendo $a^2 = 6$ e $b^2 = 9$ nell'equazione canonica:
$$\frac{x^2}{6} + \frac{y^2}{9} = 1$$

Moltiplicando per $18$ otteniamo la forma in forma intera:
$$\boxed{3x^2 + 2y^2 = 18}$$

---

## ⚠️ Errori da evitare

- Dimenticare che l'eccentricità $e$ ha sempre al denominatore il semiasse **maggiore** $\max(a, b)$, e non necessariamente $a$.
- Scambiare le coordinate dei punti quando si impone il passaggio per un punto $(x_0, y_0)$.

---

## Materiale generato

### Riepilogo
La lezione illustra il calcolo dell'equazione di un'ellisse con centro nell'origine a partire da un vertice e dall'eccentricità, e la determinazione dei parametri imponendo il passaggio per punti noti.

### Esercizi simili
1. Scrivi l'equazione dell'ellisse con centro nell'origine, vertice sull'asse $x$ in $(5, 0)$ ed eccentricità $e = \frac{3}{5}$.
   <details><summary>Soluzione</summary>$\frac{x^2}{25} + \frac{y^2}{16} = 1$</details>

2. Scrivi l'equazione dell'ellisse con centro nell'origine passante per $P(1, 2)$ e $Q(2, 1)$.
   <details><summary>Soluzione</summary>$\frac{x^2}{\frac{5}{3}} + \frac{y^2}{\frac{5}{3}} = 1$ (Circonferenza: $x^2 + y^2 = \frac{5}{3}$ — *Nota: i punti dati portano a $a^2=b^2$*)</details>

3. Scrivi l'equazione dell'ellisse con centro nell'origine, vertice in $(0, 4)$ ed eccentricità $e = \frac{\sqrt{7}}{4}$.
   <details><summary>Soluzione</summary>$\frac{x^2}{9} + \frac{y^2}{16} = 1$</details>

### Flashcard
- **D:** Qual è la formula dell'eccentricità dell'ellisse? — **R:** $e = \frac{\sqrt{|a^2 - b^2|}}{\max(a, b)}$
- **D:** Come si impone il passaggio di un'ellisse per un punto $(x_0, y_0)$? — **R:** Sostituendo $x_0$ alla $x$ e $y_0$ alla $y$ nell'equazione canonica $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$
- **D:** Quanto vale $c$ in un'ellisse se $a > b$? — **R:** $c = \sqrt{a^2 - b^2}$
