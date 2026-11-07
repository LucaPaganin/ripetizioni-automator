---
titolo: Gas perfetti, leggi dei gas e analisi dimensionale
data: '2026-04-29'
studente: Andrea Ferrando
materia: fisica
argomento: termodinamica
sottoargomenti:
- equazione di stato dei gas perfetti
- legge di Gay-Lussac
- legge di Boyle
- analisi dimensionale
esercizi: []
errori_tipici: []
fonte: https://drive.google.com/file/d/1_5scQMZyjv6RUg9nUNqlyrPoDC_bFTVL/view?usp=drivesdk
generato: '2026-11-07'
---

# Gas perfetti, leggi dei gas e analisi dimensionale

## Formule chiave

### Equazione di stato dei gas perfetti
$$pV = nRT$$
oppure in funzione del numero di molecole:
$$pV = N k_B T$$

Dove:
- $p$: pressione ($[p] = \text{Pa} = \frac{\text{N}}{\text{m}^2}$)
- $V$: volume ($[V] = \text{m}^3$)
- $T$: temperatura assoluta ($[T] = \text{K}$)
- $n$: numero di moli ($[n] = \text{mol}$)
- $R$: costante universale dei gas ($R = 8,31 \, \frac{\text{J}}{\text{mol}\cdot\text{K}}$)
- $N$: numero di particelle
- $k_B$: costante di Boltzmann
- $N_A = 6,022 \cdot 10^{23} \, \text{mol}^{-1}$ (numero di Avogadro)

Conversione della temperatura:
$$t(^\circ\text{C}) = T(\text{K}) - 273,15$$
$$T(\text{K}) = t(^\circ\text{C}) + 273,15$$

Zero assoluto: $0 \, \text{K} = -273,15 \, ^\circ\text{C}$.

---

### Prima legge di Gay-Lussac (Isobara, $p = \text{cost}$, $n = \text{cost}$)
$$V = V_0(1 + \alpha t)$$
Dove $\alpha = \frac{1}{273,15} \, ^\circ\text{C}^{-1} = \frac{1}{T_0}$.

---

### Seconda legge di Gay-Lussac (Isocora, $V = \text{cost}$, $n = \text{cost}$)
$$p = p_0(1 + \alpha t)$$

---

### Legge di Boyle (Isoterma, $T = \text{cost}$)
$$pV = \text{cost} \implies p_0 V_0 = p_1 V_1$$
Inoltre: $p \propto \frac{1}{V}$ e $V \propto \frac{1}{p}$.

---

## Esercizi e Applicazioni

### Esercizio guida: Variazione di pressione in una trasformazione isoterma
Dato un gas ideale a temperatura costante ($pV = \text{cost}$), nello stato iniziale abbiamo pressione $p_0$ e volume $V_0$. Se la pressione viene portata a $p_1 = 2p_0$, qual è il nuovo volume $V_1$?

**Svolgimento:**
Dalla legge di Boyle per gli stati iniziale e finale:
$$p_1 V_1 = p_0 V_0$$

Sostituendo $p_1 = 2p_0$:
$$2p_0 V_1 = p_0 V_0$$

Dividendo entrambi i membri per $2p_0$:
$$V_1 = \frac{p_0 V_0}{2p_0} = \boxed{\frac{V_0}{2}}$$

---

## ⚠️ Errori da evitare

Nessun errore esplicito segnalato negli appunti.

---

## Materiale generato

### Riepilogo
Il documento riassume l'equazione di stato dei gas ideali, le leggi di Gay-Lussac (isobara e isocora), la legge di Boyle per le trasformazioni isoterme e richiama i concetti di analisi dimensionale applicata alla fisica.

### Esercizi simili
1. Un gas perfetto si trova alla pressione iniziale di $1,0 \times 10^5 \, \text{Pa}$ e occupa un volume di $2,0 \, \text{m}^3$ a temperatura costante. Se il volume viene triplicato ($V_1 = 3V_0$), qual è la pressione finale $p_1$?
   <details><summary>Soluzione</summary>Utilizzando la legge di Boyle $p_1 V_1 = p_0 V_0$:
   $$p_1 (3V_0) = p_0 V_0 \implies p_1 = \frac{p_0}{3} = \frac{1,0 \times 10^5 \, \text{Pa}}{3} \approx \boxed{3,33 \times 10^4 \, \text{Pa}}$$</details>

2. Trasforma la temperatura di $27 \, ^\circ\text{C}$ in Kelvin.
   <details><summary>Soluzione</summary>Usando la relazione $T(\text{K}) = t(^\circ\text{C}) + 273,15$:
   $$T = 27 + 273,15 = \boxed{300,15 \, \text{K}}$$</details>

3. Un recipiente rigido (volume costante) contiene un gas alla temperatura di $0 \, ^\circ\text{C}$ con pressione $p_0$. Calcola la pressione del gas a $100 \, ^\circ\text{C}$ sapendo che $\alpha = \frac{1}{273,15} \, ^\circ\text{C}^{-1}$.
   <details><summary>Soluzione</summary>Dalla seconda legge di Gay-Lussac:
   $$p = p_0(1 + \alpha t) = p_0 \left(1 + \frac{100}{273,15}\right) = p_0 \left(\frac{373,15}{273,15}\right) \approx \boxed{1,37 \, p_0}$$</details>

### Flashcard
- **D:** Qual è l'equazione di stato dei gas perfetti? — **R:** $pV = nRT$ oppure $pV = N k_B T$.
- **D:** A quanto corrisponde lo zero assoluto in gradi Celsius? — **R:** A $-273,15 \, ^\circ\text{C}$ ($0 \, \text{K}$).
- **D:** Cosa rimane costante in una trasformazione isoterma? — **R:** La temperatura ($T = \text{cost}$).
- **D:** Qual è il valore e l'unità di misura della costante universale dei gas $R$? — **R:** $R = 8,31 \, \frac{\text{J}}{\text{mol}\cdot\text{K}}$.
