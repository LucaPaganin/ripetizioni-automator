---
titolo: Principi della Termodinamica e Ciclo di Carnot
data: '2026-11-02'
studente: Andrea Ferrando
materia: fisica
argomento: Termodinamica
sottoargomenti:
- Primo principio della termodinamica
- Principio zero
- Secondo principio della termodinamica
- Macchine termiche e ciclo di Carnot
esercizi:
- 1
errori_tipici:
- Confusione con i segni del calore e del lavoro
fonte: https://drive.google.com/file/d/19EyDkhaXPdgLUez3qa4O9pGCaHd1zQV_/view?usp=drivesdk
generato: '2026-11-07'
---

# Principi della Termodinamica e Ciclo di Carnot

## Formule chiave

### Primo Principio della Termodinamica (Conservazione dell'energia)
$$\Delta U = Q - L$$

Dove:
- $\Delta U$ è la variazione di energia interna del sistema.
- $Q$ è il calore (energia in transito).
- $L$ è il lavoro (energia in transito).

**Convenzioni di segno:**
- **Calore ($Q$):** positivo se assorbito, negativo se ceduto.
- **Lavoro ($L$):** positivo se svolto dal sistema (ceduto), negativo se subito dal sistema (assorbito).

---

### Principio Zero
Due corpi a contatto termico raggiungono a regime (dopo un tempo sufficientemente lungo) l'equilibrio termico, ovvero la stessa temperatura ($T_{1,f} = T_{2,f} = T_f$).

Dall'uguaglianza dei calori scambiati ($Q_t = -Q_T$) e sfruttando la definizione di capacità termica ($Q = C \Delta T$):
$$T_f = \frac{C_t T_{t,i} + C_T T_{T,i}}{C_t + C_T}$$

---

### Secondo Principio della Termodinamica
- **Enunciato di Clausius:** Non può esistere una trasformazione termodinamica il cui unico risultato (spontaneamente) sia il passaggio di calore da una sorgente calda ad una più fredda. In altri termini, il calore si trasferisce spontaneamente solo dal caldo al freddo.
- **Enunciato di Kelvin:** Non esiste una trasformazione termodinamica il cui unico risultato sia la trasformazione integrale di calore in lavoro. Ogni processo che converte calore in lavoro deve sempre avere delle perdite di calore.

---

### Macchine termiche e Ciclo di Carnot
- Rendimento di una macchina termica:
  $$\eta = \frac{L}{Q_{ass}}$$
- Rendimento di Carnot (macchina ideale con rendimento massimo):
  $$\eta = 1 - \frac{T_{fredda}}{T_{calda}}$$

---

## Esercizio 1

**Testo:**
Una macchina termica lavora secondo un ciclo di Carnot ideale tra le temperature $T_1 = 650\text{ K}$ e $T_2 = 300\text{ K}$. Si valuti la quantità minima di calore $Q_1$ da fornire per ottenere un lavoro di $1,4\text{ kJ}$. Si valuti inoltre il calore $Q_2$ ceduto all'ambiente.

**Svolgimento:**
In un ciclo chiuso la macchina torna allo stato iniziale alla fine, quindi la variazione di energia interna è nulla:
$$\Delta U = 0 \implies Q_{tot} - L_{tot} = 0 \implies Q_1 + Q_2 = L$$

Il rendimento per definizione è:
$$\eta = \frac{L}{Q_{ass}} = \frac{L}{Q_1}$$

Trattandosi di una macchina di Carnot ideale:
$$\eta = 1 - \frac{T_2}{T_1} = 1 - \frac{300}{650} \simeq 0,54 \text{ (ovvero } 54\% \text{)}$$

Ricaviamo $Q_1$:
$$\frac{L}{Q_1} = \eta \implies Q_1 = \frac{L}{\eta} = \frac{T_1}{T_1 - T_2} L$$

Sostituendo i valori ($L = 1400\text{ J}$):
$$Q_1 = \frac{650}{650 - 300} \cdot 1400\text{ J} = 2600\text{ J}$$

Adesso calcoliamo $Q_2$:
$$Q_2 = L - Q_1 = 1400\text{ J} - 2600\text{ J} = -1200\text{ J}$$

Risultati finali:
$$Q_1 = \boxed{2600\text{ J}}, \quad Q_2 = \boxed{-1200\text{ J}}$$

---

## ⚠️ Errori da evitare
- Dimenticare che il calore ceduto $Q_2$ nelle macchine termiche deve risultare negativo per rispettare il bilancio energetico.
- Confondere la temperatura assoluta in Kelvin con la temperatura in Celsius nel calcolo del rendimento di Carnot.

---

## Materiale generato

### Riepilogo
Il documento analizza il primo principio della termodinamica ($\Delta U = Q - L$), il principio zero sull'equilibrio termico e gli enunciati di Clausius e Kelvin del secondo principio. Viene infine applicato il ciclo di Carnot per determinare rendimento, calore assorbito e calore ceduto di una macchina termica ideale.

### Esercizi simili

1. Una macchina termica di Carnot lavora tra una sorgente calda a $T_1 = 500\text{ K}$ e una fredda a $T_2 = 300\text{ K}$. Sapendo che assorbe $2000\text{ J}$ di calore dalla sorgente calda, calcola il lavoro prodotto e il calore ceduto all'ambiente.
   <details><summary>Soluzione</summary>
   Il rendimento è $\eta = 1 - \frac{300}{500} = 0,4$. Il lavoro è $L = \eta \cdot Q_1 = 0,4 \cdot 2000\text{ J} = 800\text{ J}$. Il calore ceduto è $Q_2 = L - Q_1 = 800\text{ J} - 2000\text{ J} = -1200\text{ J}$.
   </details>

2. Due corpi di capacità termica $C_1 = 200\text{ J/K}$ e $C_2 = 300\text{ J/K}$ si trovano rispettivamente alle temperature iniziali $T_{1,i} = 80\text{ °C}$ e $T_{2,i} = 20\text{ °C}$ e vengono messi a contatto termico. Calcola la temperatura di equilibrio $T_f$.
   <details><summary>Soluzione</summary>
   Utilizzando la formula dell'equilibrio termico:
   $$T_f = \frac{C_1 T_{1,i} + C_2 T_{2,i}}{C_1 + C_2} = \frac{200 \cdot 80 + 300 \cdot 20}{200 + 300} = \frac{16000 + 6000}{500} = 44\text{ °C}$$
   </details>

3. Una macchina di Carnot ha un rendimento del $60\%$ e scarica calore a una temperatura di $27\text{ °C}$. Qual è la temperatura della sorgente calda espressa in Kelvin?
   <details><summary>Soluzione</summary>
   La temperatura fredda in Kelvin è $T_2 = 27 + 273 = 300\text{ K}$. Dalla formula $\eta = 1 - \frac{T_2}{T_1}$, ricaviamo $T_1 = \frac{T_2}{1 - \eta} = \frac{300}{1 - 0,6} = \frac{300}{0,4} = 750\text{ K}$.
   </details>

### Flashcard
- **D:** Cosa esprime il Primo Principio della Termodinamica? — **R:** La conservazione dell'energia attraverso la relazione $\Delta U = Q - L$.
- **D:** Qual è la convenzione dei segni per il calore $Q$? — **R:** È positivo se assorbito dal sistema e negativo se ceduto dal sistema.
- **D:** Cosa afferma l'enunciato di Clausius del secondo principio? — **R:** Il calore non può fluire spontaneamente da un corpo più freddo a uno più caldo senza l'apporto di lavoro esterno.
- **D:** Come si calcola il rendimento massimo di una macchina termica (Carnot)? — **R:** Con la formula $\eta = 1 - \frac{T_{fredda}}{T_{calda}}$, usando temperature in Kelvin.
