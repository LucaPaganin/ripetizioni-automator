---
titolo: Equazioni esponenziali
data: '2026-07-22'
studente: Andrea Ferrando
materia: matematica
argomento: esponenziali
sottoargomenti:
- proprietà delle potenze
- equazioni esponenziali elementari
esercizi:
- 30
- 31
errori_tipici:
- Errata applicazione delle proprietà delle potenze nel prodotto tra esponenti
fonte: https://drive.google.com/file/d/1mhZxTTIpYuulTWNl9jVAIZvFz07AdM56/view?usp=drivesdk
generato: '2026-11-07'
---

# Equazioni esponenziali

## Formule chiave

- Proprietà degli esponenti negativi:
  $$\frac{1}{x} = x^{-1}$$

- Proprietà delle potenze:
  $$(a^b)^c = a^{b \cdot c}$$
  $$a^b \cdot a^c = a^{b+c}$$
  $$\frac{a^b}{a^c} = a^{b-c}$$

- Proprietà dei radicali scritta come potenza:
  $$\sqrt{2^x} = (2^x)^{\frac{1}{2}} = 2^{\frac{x}{2}}$$

- Proprietà generale richiamata negli appunti:
  $$\frac{x : y}{z} = \frac{x}{yz} = x \cdot y^{-1} \cdot z^{-1}$$

## Esercizio 30

Risolvere la seguente equazione esponenziale:

$$(2^{2x-1} \cdot 2^x)^2 = 2^{10x - 4}$$

**Svolgimento:**

1. Dentro la parentesi sommiamo gli esponenti ($a^m \cdot a^n = a^{m+n}$):
   $$2^{2x-1} \cdot 2^x = 2^{3x-1}$$

2. Applichiamo la potenza di potenza:
   $$(2^{3x-1})^2 = 2^{6x-2}$$

3. Uguagliamo gli esponenti:
   $$6x - 2 = 10x - 4 \implies 4x = 2 \implies x = \frac{1}{2}$$

**Soluzione:** $\boxed{x = \frac{1}{2}}$

> ⚠️ Nota: negli appunti compare anche il passaggio $\frac{1}{(2^y)^{1-2x}} = (2^y)^{2x-1}$, quindi il testo originale potrebbe contenere un fattore in più non trascritto. La soluzione sopra vale per il testo così come riportato.

---

## Esercizio 31

Risolvere la seguente equazione esponenziale:

$$(2^{1 - x + x^2} : \sqrt{2^x})^4 = 2^{\frac{x}{2}}$$

*Nota: a destra dell'equazione compare $\sqrt{2^x} = 2^{\frac{x}{2}}$.*

**Svolgimento:**

1. Riscriviamo la radice come potenza con esponente fratto:
   $$\sqrt{2^x} = 2^{\frac{x}{2}}$$

2. Sostituiamo e applichiamo la potenza di un quoziente all'interno della parentesi:
   $$(2^{1 - x + x^2} : 2^{\frac{x}{2}})^4 = 2^{\frac{x}{2}}$$

3. Sottraiamo gli esponenti della divisione in base $2$:
   $$(2^{1 - x + x^2 - \frac{x}{2}})^4 = 2^{\frac{x}{2}}$$

4. Applichiamo la potenza di potenza moltiplicando l'esponente per $4$:
   $$2^{(1 - \frac{3}{2}x + x^2) \cdot 4} = 2^{\frac{x}{2}}$$
   $$2^{4 - 6x + 4x^2} = 2^{\frac{x}{2}}$$

5. Uguagliando gli esponenti:
   $$4 - 6x + 4x^2 = \frac{x}{2}$$

6. Moltiplichiamo tutto per $2$ per eliminare il denominatore:
   $$8 - 12x + 8x^2 = x$$
   $$8x^2 - 13x + 8 = 0$$

7. Calcoliamo il discriminante ($\Delta$) dell'equazione di secondo grado:
   $$\Delta = (-13)^2 - 4(8)(8) = 169 - 256 = -87$$

**Soluzione:**
Essendo $\Delta < 0$, l'equazione non ammette soluzioni reali: **$\nexists x \in \mathbb{R}$**.

---

## ⚠️ Errori da evitare

- Confondere la somma degli esponenti nel prodotto di potenze con la moltiplicazione: $a^m \cdot a^n = a^{m+n}$ (e non $a^{m \cdot n}$).
- Dimenticare di convertire le radici in potenze con esponente frazionario prima di applicare le proprietà delle potenze.

---

## Materiale generato

### Riepilogo
Le equazioni esponenziali si risolvono riconducendo entrambi i membri alla stessa base tramite le proprietà delle potenze e dei radicali, per poi uguagliare gli esponenti.

### Esercizi simili

1. Risolvi l'equazione: $(2^{x-1} \cdot 4^x)^2 = 8^x$
   <details><summary>Soluzione</summary>
   Riconduciamo tutto in base $2$: $(2^{x-1} \cdot (2^2)^x)^2 = (2^3)^x \implies (2^{x-1+2x})^2 = 2^{3x} \implies (2^{3x-1})^2 = 2^{3x} \implies 2^{6x-2} = 2^{3x}$.
   Uguagliando gli esponenti: $6x - 2 = 3x \implies 3x = 2 \implies x = \frac{2}{3}$.
   </details>

2. Risolvi l'equazione: $\left(\frac{3^{x+1}}{9^x}\right)^2 = 3^{2-x}$
   <details><summary>Soluzione</summary>
   Riconduciamo in base $3$: $\left(\frac{3^{x+1}}{(3^2)^x}\right)^2 = 3^{2-x} \implies \left(\frac{3^{x+1}}{3^{2x}}\right)^2 = 3^{2-x} \implies (3^{x+1-2x})^2 = 3^{2-x} \implies (3^{1-x})^2 = 3^{2-x}$.
   $3^{2-2x} = 3^{2-x} \implies 2 - 2x = 2 - x \implies -x = 0 \implies x = 0$.
   </details>

3. Risolvi l'equazione: $\sqrt{5^x} \cdot 5^{x-1} = 25$
   <details><summary>Soluzione</summary>
   Riconduciamo in base $5$: $5^{\frac{x}{2}} \cdot 5^{x-1} = 5^2 \implies 5^{\frac{x}{2} + x - 1} = 5^2 \implies 5^{\frac{3}{2}x - 1} = 5^2$.
   Uguagliamo gli esponenti: $\frac{3}{2}x - 1 = 2 \implies \frac{3}{2}x = 3 \implies x = 3 \cdot \frac{2}{3} = 2$.
   </details>

### Flashcard
- **D:** Come si scrive una radice n-esima $\sqrt[n]{a^m}$ sotto forma di potenza? — **R:** $a^{\frac{m}{n}}$
- **D:** Come si semplifica l'espressione $(a^b)^c$? — **R:** Moltiplicando gli esponenti: $a^{b \cdot c}$
- **D:** Qual è la regola del quoziente di potenze con la stessa base $\frac{a^m}{a^n}$? — **R:** Si sottraggono gli esponenti: $a^{m-n}$
