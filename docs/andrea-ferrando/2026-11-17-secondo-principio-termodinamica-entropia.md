---
titolo: Secondo principio della termodinamica ed entropia
data: '2026-11-17'
studente: Andrea Ferrando
materia: fisica
argomento: termodinamica
sottoargomenti:
- secondo principio
- macchine termiche
- variazioni di entropia
esercizi:
- '3'
errori_tipici:
- Confondere il verso del calore ceduto e assorbito nei bilanci energetici
fonte: https://drive.google.com/file/d/1olheu5Tpw-aE5o5wBamblr89kikbHua0/view?usp=drivesdk
generato: '2026-11-17'
---

# Secondo principio della termodinamica ed entropia

## Formule chiave

- Relazione fondamentale tra pressione, volume e lavoro (energia):
  $$1\text{ Pa} \cdot 1\text{ m}^3 = 1\text{ J}$$
  Verifica dimensionale:
  $$\text{Pa} = \frac{\text{N}}{\text{m}^2} = \frac{\text{kg}\cdot\text{m/s}^2}{\text{m}^2} = \frac{\text{kg}}{\text{m}\cdot\text{s}^2}$$
  $$\text{Pa}\cdot\text{m}^3 = \frac{\text{kg}}{\text{m}\cdot\text{s}^2}\cdot\text{m}^3 = \text{kg}\cdot\frac{\text{m}^2}{\text{s}^2} = \text{J}$$

- Relazione tra calore e lavoro in una macchina termica:
  $$Q_{\text{ass}} + Q_{\text{ced}} = L \implies Q_{\text{ced}} = L - Q_{\text{ass}}$$

- Variazione di entropia per un passaggio di stato a temperatura costante:
  $$\Delta S = \frac{Q}{T}$$

- Enunciati del Secondo Principio:
  - **Clausius:** Spontaneamente il calore va dal corpo più caldo al corpo più freddo.
  - **Kelvin:** Non è possibile trasformare integralmente calore in lavoro (con trasformazione ciclica).
  - **Boltzmann:** Spontaneamente l'entropia aumenta o resta costante per un sistema isolato.

## Esercizio 3

**Testo:** Per produrre un lavoro di $2,79 \cdot 10^4\text{ J}$ una macchina termica assorbe $1,12 \cdot 10^5\text{ J}$ di calore. La variazione di temperatura della sorgente fredda, costituita da una massa $m$ di acqua a temperatura ambiente, non deve essere maggiore di un decimo di grado. Determina la quantità minima di acqua necessaria per realizzare la sorgente fredda.

**Svolgimento:**

Dati forniti dal testo:
- $L = 2,79 \cdot 10^4\text{ J}$
- $Q_{\text{ass}} = 1,12 \cdot 10^5\text{ J}$
- $\Delta T = 0,1^\circ\text{C}$
- $C_{\text{H}_2\text{O}} = 4186\text{ J}/(\text{kg}\cdot^\circ\text{C})$

Prima ricaviamo il calore ceduto $Q_{\text{ced}}$ dalla relazione del bilancio energetico della macchina termica:
$$Q_{\text{ass}} + Q_{\text{ced}} = L$$
$$Q_{\text{ced}} = L - Q_{\text{ass}} = 2,79 \cdot 10^4\text{ J} - 1,12 \cdot 10^5\text{ J} = 27900\text{ J} - 112000\text{ J} = -84100\text{ J} = -8,41 \cdot 10^4\text{ J}$$

Considerando il valore assoluto del calore ceduto alla sorgente fredda ($|Q_{\text{ced}}|$), impostiamo l'equazione del calore assorbito dall'acqua:
$$|Q_{\text{ced}}| = m_{\text{acqua}} \cdot C_{\text{H}_2\text{O}} \cdot \Delta T$$

Isolando la massa $m_0$ della sorgente fredda:
$$m_0 = \frac{|Q_{\text{ced}}|}{C_{\text{H}_2\text{O}} \cdot \Delta T} = \frac{84100\text{ J}}{4186\text{ J}/(\text{kg}\cdot^\circ\text{C}) \cdot 0,1^\circ\text{C}} = \frac{84100}{418,6}\text{ kg} \approx 200,9\text{ kg}$$

La quantità minima di acqua necessaria è quindi:
$$\boxed{m_0 \approx 200,9\text{ kg}}$$

---

## ⚠️ Errori da evitare

- Dimenticare che il calore ceduto dalla macchina termica ha segno negativo nel bilancio energetico $Q_{\text{ass}} + Q_{\text{ced}} = L$.
- Confondere la temperatura assoluta ($K$) con quella Celsius ($^\circ\text{C}$) quando si calcolano le variazioni di entropia, ricordando che un incremento di $0,1^\circ\text{C}$ equivale a un incremento di $0,1\text{ K}$.

---

## Materiale generato

### Riepilogo
Il secondo principio della termodinamica stabilisce l'unidirezionalità dei processi fisici introducendo la funzione di stato entropia. Le macchine termiche non possono convertire tutto il calore assorbito in lavoro utile e richiedono sempre una sorgente fredda per dissipare l'energia residua.

### Esercizi simili

1. Una macchina termica compie un lavoro di $1,50 \cdot 10^4\text{ J}$ assorbendo $8,00 \cdot 10^4\text{ J}$ di calore da una sorgente calda. Calcola la massa minima di acqua della sorgente fredda (inizialmente a temperatura ambiente) affinché la sua temperatura aumenti al massimo di $0,2^\circ\text{C}$.
   <details><summary>Soluzione</summary>
   $Q_{\text{ced}} = L - Q_{\text{ass}} = 15000\text{ J} - 80000\text{ J} = -65000\text{ J}$.
   $m = \frac{65000}{4186 \cdot 0.2} \approx 77,6\text{ kg}$.
   </details>

2. Una macchina termica produce $5,00 \cdot 10^3\text{ J}$ di lavoro e cede $1,20 \cdot 10^4\text{ J}$ di calore a una sorgente fredda di acqua. Se la temperatura dell'acqua non deve variare di oltre $0,05^\circ\text{C}$, qual è la massa minima di acqua richiesta?
   <details><summary>Soluzione</summary>
   Il calore ceduto è già dato in modulo: $|Q_{\text{ced}}| = 12000\text{ J}$.
   $m = \frac{12000}{4186 \cdot 0.05} \approx 57,3\text{ kg}$.
   </details>

3. Calcola la variazione di entropia totale dell'universo se $500\text{ J}$ di calore fluiscono spontaneamente da un corpo a $400\text{ K}$ a un corpo a $200\text{ K}$ (supposti a temperatura costante).
   <details><summary>Soluzione</summary>
   $\Delta S_{\text{caldo}} = \frac{-500}{400} = -1,25\text{ J/K}$.
   $\Delta S_{\text{freddo}} = \frac{+500}{200} = +2,50\text{ J/K}$.
   $\Delta S_{\text{tot}} = -1,25 + 2,50 = +1,25\text{ J/K} > 0$.
   </details>

### Flashcard
- **D:** Cosa afferma l'enunciato di Kelvin del secondo principio? — **R:** Non è possibile trasformare integralmente calore in lavoro in una trasformazione ciclica.
- **D:** Come si calcola la variazione di entropia per un corpo a temperatura costante $T$ che scambia calore $Q$? — **R:** $\Delta S = \frac{Q}{T}$
- **D:** Perché il calore ha un "peso entropico" maggiore a basse temperature? — **R:** Perché a parità di calore scambiato $Q$, dividendo per una temperatura $T$ più piccola si ottiene una variazione di entropia maggiore.
- **D:** Qual è la relazione tra lavoro e calori in una macchina termica? — **R:** $Q_{\text{ass}} + Q_{\text{ced}} = L$ (con $Q_{\text{ced}}$ negativo).
