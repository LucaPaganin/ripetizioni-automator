---
titolo: Funzioni esponenziali, equazioni, disequazioni e logaritmi
data: '2026-07-17'
studente: Andrea Ferrando
materia: matematica
argomento: Esponenziali e Logaritmi
sottoargomenti:
- Funzione esponenziale
- Equazioni esponenziali
- Logaritmi
- Proprietà dei logaritmi
- Cambio di base
- Disequazioni esponenziali
esercizi: []
errori_tipici:
- Confondere l'inversione del verso di una disequazione logaritmica o esponenziale
  quando la base è compresa tra 0 e 1.
fonte: https://drive.google.com/file/d/1NQ3WOnt5Hl9kpsVz0LdzHB56RNQBiEBa/view?usp=drivesdk
generato: '2026-11-07'
---

# Funzioni esponenziali, equazioni, disequazioni e logaritmi

## Formule chiave

### Funzione Esponenziale
La funzione esponenziale è definita come:
$$f(x) = a^x \quad \text{con } a > 0$$

Il dominio è $\mathbb{R}$. Per quanto riguarda la base:
- Se $a > 1$, la funzione è **crescente**.
- Se $0 < a < 1$, la funzione è **decrescente**.
- Se $a = 1$, si ha $1^x = 1$ $\forall x$.

### Proprietà dei Logaritmi
Dati $a > 0$ con $a \neq 1$, $x > 0$, $y > 0$:

- $\log_a(xy) = \log_a x + \log_a y$
- $\log_a\left(\frac{x}{y}\right) = \log_a x - \log_a y$
- $\log_a(x^x) = x \cdot \log_a a$ (più in generale $\log_a(x^b) = b \cdot \log_a x$)
- $\log_a\left(\frac{1}{x}\right) = -\log_a x$
- $\log_a a = 1$ $\forall a > 0, a \neq 1$
- $a^{\log_a x} = x$

### Cambio di Base
Per passare da una base $a$ a una base $b$:
$$\log_a x = \frac{\log_b x}{\log_b a}$$

---

## Trattazione degli Argomenti

### 1. Risoluzione di Equazioni Esponenziali
Quando ci troviamo di fronte a un'equazione elementare del tipo:
$$a^x = A \implies x = \log_a A$$

Ad esempio, per risolvere un'equazione con $4^x + 2^x - 1 = 0$, poniamo una variabile ausiliaria $t = 2^x \ge 0$, sapendo che $4^x = t^2$. L'equazione diventa:
$$t^2 + t - 1 = 0$$

Risolvendo rispetto a $t$:
$$t = \frac{-1 \pm \sqrt{1 - 4(1)(-1)}}{2} = \frac{-1 \pm \sqrt{5}}{2}$$

Otteniamo due soluzioni per $t$:
- $t_1 = \frac{1+\sqrt{5}}{2}$ (accettabile, poiché $> 0$)
- $t_2 = \frac{-1-\sqrt{5}}{2}$ (non accettabile, poiché negativo)

Tornando alla variabile $x$:
$$2^x = \frac{\sqrt{5}-1}{2} \implies x = \log_2 \left(\frac{\sqrt{5}-1}{2}\right)$$

---

### 2. Risoluzione di Disequazioni Esponenziali e Logaritmiche

#### Esempio 1: Base maggiore di 1
$$2^x > 4$$
Applicando il logaritmo in base 2 ad entrambi i membri (la base è $>1$, quindi il verso della disequazione si conserva):
$$\log_2(2^x) > \log_2(4)$$
$$x \cdot \log_2 2 > 2 \implies x > 2$$

#### Esempio 2: Base compresa tra 0 e 1
$$\left(\frac{1}{2}\right)^x > \frac{1}{4}$$
Applicando il logaritmo in base $\frac{1}{2}$ (la base è $<1$, quindi il verso della disequazione si inverte $> \to <$):
$$\log_{\frac{1}{2}}\left(\left(\frac{1}{2}\right)^x\right) < \log_{\frac{1}{2}}\left(\frac{1}{4}\right)$$
$$x < \log_{\frac{1}{2}}\left(\frac{1}{4}\right) \implies x < 2$$

---

## ⚠️ Errori da evitare
- Dimenticare di invertire il verso di una disequazione (esponenziale o logaritmica) quando la base è compresa tra $0$ e $1$.
- Accettare soluzioni negative per la variabile ausiliaria $t = a^x$ nelle equazioni esponenziali riconducibili a equazioni algebriche.

---

## Materiale generato

### Riepilogo
La lezione tratta le proprietà fondamentali delle funzioni esponenziali e logaritmiche, le regole del cambio di base e i metodi per risolvere equazioni e disequazioni esponenziali, evidenziando il ruolo cruciale del valore della base ($>1$ o compresa tra $0$ e $1$).

### Esercizi simili
1. Risolvere l'equazione esponenziale: $3^x = 81$
   <details><summary>Soluzione</summary>
   $$3^x = 3^4 \implies \boxed{x = 4}$$
   </details>

2. Risolvere la disequazione esponenziale: $\left(\frac{1}{3}\right)^x > \frac{1}{9}$
   <details><summary>Soluzione</summary>
   Passando ai logaritmi in base $\frac{1}{3}$ e invertendo il verso (base $< 1$):
   $$x < \log_{\frac{1}{3}}\left(\frac{1}{9}\right) \implies \boxed{x < 2}$$
   </details>

3. Applicare la proprietà del cambio di base per calcolare: $\log_2 8$ usando la base $2$ o $10$.
   <details><summary>Soluzione</summary>
   Sapendo che $8 = 2^3$:
   $$\log_2 8 = \log_2(2^3) = 3 \cdot \log_2 2 = \boxed{3}$$
   </details>

### Flashcard
- **D:** Qual è il dominio della funzione esponenziale $f(x) = a^x$ (con $a > 0$)? — **R:** $\mathbb{R}$.
- **D:** Cosa succede alla monotonia di $a^x$ se $0 < a < 1$? — **R:** La funzione è decrescente.
- **D:** Come si sviluppa il logaritmo di un quoziente $\log_a\left(\frac{x}{y}\right)$? — **R:** $\log_a x - \log_a y$.
- **D:** Come si esegue il cambio di base per $\log_a x$ alla base $b$? — **R:** $\frac{\log_b x}{\log_b a}$.
