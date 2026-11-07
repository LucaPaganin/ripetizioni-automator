---
titolo: 'Calore e Capacità Termica: Calcolo del Calore e Passaggi di Stato'
data: '2026-02-16'
studente: Andrea Ferrando
materia: fisica
argomento: termologia
sottoargomenti:
- calore specifico
- capacità termica
- calore latente di fusione
- passaggi di stato
esercizi:
- 1
errori_tipici: []
fonte: https://drive.google.com/file/d/1mWvqDnKwXOo4EI2uvjg0CLGGZAWlxnQ5/view?usp=drivesdk
generato: '2026-11-07'
---

# Calore e Capacità Termica: Calcolo del Calore e Passaggi di Stato

## Formule chiave

- **Quantità di calore:**
  $$Q = c \cdot m \cdot \Delta T$$
  Dove:
  - $Q$ = calore scambiato
  - $c$ = calore specifico della sostanza
  - $m$ = massa della sostanza (quanta sostanza)
  - $\Delta T$ = variazione di temperatura (quanto scaldo)

- **Calore per un passaggio di stato (fusione/solidificazione):**
  $$Q = \lambda_f \cdot m$$
  Dove $\lambda_f$ è il calore latente di fusione.

- **Equivalenze velocità:**
  $$1\text{ km/h} = \frac{1000\text{ m}}{3600\text{ s}} = \frac{1}{3,6}\text{ m/s} \approx 0,277\text{ m/s}$$

---

## Esercizio 1

**Testo:**
Quanto calore è necessario per fondere un blocco di ghiaccio di $10\text{ kg}$ che si trova ad una temperatura di $-10^\circ\text{C}$ ed avere acqua liquida alla temperatura di $60^\circ\text{C}$ sapendo che il calore specifico del ghiaccio è $2260\text{ J}/(\text{kg}\cdot^\circ\text{C})$ e il calore latente di fusione dell'acqua $\lambda_f = 335,2\text{ kJ/kg}$?

**Dati:**
- $m = 10\text{ kg}$
- $T_i = -10^\circ\text{C}$
- $T_f = 60^\circ\text{C}$
- $c_g = 2260\text{ J}/(\text{kg}\cdot^\circ\text{C})$
- $\lambda_f = 335,2\text{ kJ/kg} = 335200\text{ J/kg}$
- $c_a = 4186\text{ J}/(\text{kg}\cdot^\circ\text{C})$ [valore standard dell'acqua liquida utilizzato nei passaggi]

**Svolgimento:**
Il processo si divide in tre passaggi consecutivi:
1. **A $\to$ B:** Riscaldamento del ghiaccio da $-10^\circ\text{C}$ a $0^\circ\text{C}$
   $$\Delta T_{AB} = 0^\circ\text{C} - (-10^\circ\text{C}) = 10^\circ\text{C}$$
   $$Q_{AB} = c_g \cdot m \cdot \Delta T_{AB} = 2260 \cdot 10 \cdot 10 = 226000\text{ J} = 226\text{ kJ}$$

2. **B $\to$ C:** Fusione del ghiaccio a temperatura costante ($0^\circ\text{C}$)
   $$Q_{BC} = \lambda_f \cdot m = 335,2\text{ kJ/kg} \cdot 10\text{ kg} = 3352\text{ kJ} = 3352000\text{ J}$$

3. **C $\to$ D:** Riscaldamento dell'acqua liquida da $0^\circ\text{C}$ a $60^\circ\text{C}$
   $$\Delta T_{CD} = 60^\circ\text{C} - 0^\circ\text{C} = 60^\circ\text{C}$$
   $$Q_{CD} = c_a \cdot m \cdot \Delta T_{CD} = 4186 \cdot 10 \cdot 60 = 2511600\text{ J} = 2511,6\text{ kJ}$$

**Calcolo del calore totale:**
$$Q_{\text{tot}} = Q_{AB} + Q_{BC} + Q_{CD}$$
$$Q_{\text{tot}} = 226000\text{ J} + 3352\text{ kJ} + 2511600\text{ J}$$
Convertendo tutto in Joule ($3352\text{ kJ} = 3352000\text{ J}$):
$$Q_{\text{tot}} = 226000\text{ J} + 3352000\text{ J} + 2511600\text{ J} = 6089600\text{ J} = \boxed{6089,6\text{ kJ}} \approx 6,09\text{ MJ}$$

---

## ⚠️ Errori da evitare
- Non confondere il calore specifico $c$ (necessario per variare la temperatura di un corpo) con il calore latente $\lambda$ (utilizzato durante i passaggi di stato a temperatura costante).
- Ricordarsi di convertire correttamente le unità di misura tra Joule ($\text{J}$) e kiloJoule ($\text{kJ}$) prima di sommare i contributi energetici.

---
## Materiale generato

### Riepilogo
Il calore $Q$ scambiato da un corpo dipende dalla sua massa, dalla natura della sostanza ($c$) e dalla variazione di temperatura ($\Delta T$). Nei problemi con passaggi di stato (es. ghiaccio-acqua), l'energia totale è la somma del calore necessario per riscaldare le singole fasi e del calore latente di transizione.

### Esercizi simili

1. **Esercizio 1:**
   Calcola il calore necessario per portare $500\text{ g}$ di acqua da $20^\circ\text{C}$ a $80^\circ\text{C}$ ($c_{\text{acqua}} = 4186\text{ J}/(\text{kg}\cdot^\circ\text{C})$).
   <details><summary>Soluzione</summary>
   $m = 0,5\text{ kg}$, $\Delta T = 60^\circ\text{C}$
   $Q = c \cdot m \cdot \Delta T = 4186 \cdot 0,5 \cdot 60 = 125580\text{ J} = 125,58\text{ kJ}$
   </details>

2. **Esercizio 2:**
   Quanto calore serve per fondere completamente $2\text{ kg}$ di ghiaccio alla temperatura di fusione ($0^\circ\text{C}$)? (Calore latente di fusione del ghiaccio $\lambda_f = 334\text{ kJ/kg}$).
   <details><summary>Soluzione</summary>
   $Q = \lambda_f \cdot m = 334\text{ kJ/kg} \cdot 2\text{ kg} = \boxed{668\text{ kJ}}$
   </details>

3. **Esercizio 3:**
   Trasforma la velocità di $72\text{ km/h}$ in metri al secondo ($\text{m/s}$).
   <details><summary>Soluzione</summary>
   $72 \div 3,6 = \boxed{20\text{ m/s}}$
   </details>

### Flashcard
- **D:** Qual è la formula fondamentale del calore sensibile? — **R:** $Q = c \cdot m \cdot \Delta T$
- **D:** Da cosa dipende la capacità termica di un corpo? — **R:** Dalla massa del corpo e dal calore specifico della sostanza di cui è composto.
- **D:** Come si converte una velocità da $\text{km/h}$ a $\text{m/s}$? — **R:** Dividendo per $3,6$.
- **D:** Varia la temperatura di un corpo durante un passaggio di stato? — **R:** No, la temperatura rimane costante e il calore viene impiegato per rompere o formare i legami intermolecolari (calore latente).
