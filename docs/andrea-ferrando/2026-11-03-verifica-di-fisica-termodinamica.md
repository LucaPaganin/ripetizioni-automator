---
titolo: Verifica di Fisica sulla Termodinamica
data: '2026-11-03'
studente: Andrea Ferrando
materia: fisica
argomento: Termodinamica
sottoargomenti:
- Secondo principio della termodinamica
- Macchine termiche
- Entropia
esercizi:
- 1
- 2
- 3
- 4
- 5
- 6
errori_tipici: []
fonte: https://drive.google.com/file/d/1Mm4PjXGH7ozC3fgHYxPAVVXd-i3oB0Le/view?usp=drivesdk
generato: '2026-11-09'
---

# Verifica di Fisica sulla Termodinamica

## Formule chiave

- Rendimento di una macchina termica:
  $$\eta = \frac{L}{Q_{ass}} = 1 - \frac{|Q_{ced}|}{Q_{ass}}$$

- Lavoro in un ciclo termico (area del ciclo):
  $$L = Q_{ass} - |Q_{ced}|$$

- Potenza:
  $$P = \frac{L_{tot}}{\Delta t}$$

- Variazione di calore:
  $$Q = mc\Delta T$$

- Variazione di entropia e molteplicità (statistica):
  $$\Delta S = k_B \ln\left(\frac{W_f}{W_i}\right)$$

---

## Esercizio 1

**Testo:** Illustra brevemente l’enunciato di Kelvin del secondo principio della termodinamica.

**Soluzione:**
È impossibile realizzare una trasformazione il cui unico risultato sia quello di assorbire calore da un'unica sorgente e trasformarlo integralmente in lavoro.

---

## Esercizio 2

**Testo:** Una macchina termica compie il ciclo rappresentato nel grafico. In ogni ciclo cede $1800\text{ J}$ alla sorgente fredda.
a. Quanto lavoro compie tale macchina nella trasformazione AB? Nella trasformazione BC? Nella trasformazione CA? In un intero ciclo?
b. Calcola il rendimento della macchina.
c. Sapendo che la macchina compie $140$ cicli al minuto, calcolane la potenza.

**Soluzione:**
Dal grafico (ciclo sul piano $p\text{-}V$):
- $p_A = p_B = 4,0 \times 10^5\text{ Pa}$
- $V_A = 1,0\text{ dm}^3 = 1,0 \times 10^{-3}\text{ m}^3$
- $V_B = V_C = 6,0\text{ dm}^3 = 6,0 \times 10^{-3}\text{ m}^3$
- $p_C = 1,0 \times 10^5\text{ Pa}$

**a.** 
- Trasformazione AB (isobara):
  $$L_{AB} = p \Delta V = 4,0 \times 10^5\text{ Pa} \times (6,0 - 1,0) \times 10^{-3}\text{ m}^3 = 4,0 \times 10^5 \times 5,0 \times 10^{-3} = 2000\text{ J}$$

- Trasformazione BC (isocora):
  $$L_{BC} = 0\text{ J}$$

- Trasformazione CA (isoterma / lineare):
  Il lavoro corrisponde all'area sottostante la retta CA nel piano $p\text{-}V$ (tra $V_C$ e $V_A$):
  $$L_{CA} = -\frac{(p_A + p_C)}{2} (V_B - V_A) = -\frac{(4,0 + 1,0)\times 10^5}{2} \times 5,0 \times 10^{-3} = -1250\text{ J}$$

- Lavoro in un intero ciclo ($L_{ciclo}$):
  corrisponde all'area del triangolo ABC:
  $$L_{ciclo} = \frac{1}{2} \times \text{base} \times \text{altezza} = \frac{1}{2} \times (6,0 - 1,0) \times 10^{-3}\text{ m}^3 \times (4,0 - 1,0) \times 10^5\text{ Pa}$$
  $$L_{ciclo} = \frac{1}{2} \times 5,0 \times 10^{-3} \times 3,0 \times 10^5 = 750\text{ J}$$
  *(Verifica: $L_{tot} = L_{AB} + L_{BC} + L_{CA} = 2000 + 0 - 1250 = 750\text{ J}$)*.

**b.** 
Il calore assorbito si calcola come:
$$Q_{ass} = L_{ciclo} + |Q_{ced}| = 750\text{ J} + 1800\text{ J} = 2550\text{ J}$$

Il rendimento $\eta$ è:
$$\eta = \frac{L_{ciclo}}{Q_{ass}} = \frac{750}{2550} \approx 0,294 \rightarrow \boxed{29,4\%}$$

**c.** 
Frequenza dei cicli: $f = 140\text{ cicli/min} = \frac{140}{60}\text{ s}^{-1} \approx 2,33\text{ Hz}$.
Il tempo per un ciclo è $\Delta t = \frac{60}{140}\text{ s} \approx 0,428\text{ s}$.
La potenza $P$ è:
$$P = \frac{L_{tot}}{\Delta t} = \frac{750\text{ J}}{\frac{60}{140}\text{ s}} = \frac{750 \times 140}{60} = \frac{105000}{60} = \boxed{1750\text{ W}}$$

---

## Esercizio 3

**Testo:** Per produrre un lavoro di $2,79 \times 10^4\text{ J}$ una macchina termica assorbe $1,12 \times 10^5\text{ J}$ di calore. La variazione di temperatura della sorgente fredda, costituita da una massa $m$ di acqua a temperatura ambiente, non deve essere maggiore di un decimo di grado. Determina la quantità minima di acqua necessaria per realizzare la sorgente fredda.

**Soluzione:**
Il calore ceduto dalla macchina termica alla sorgente fredda è:
$$|Q_{ced}| = Q_{ass} - L = 1,12 \times 10^5\text{ J} - 2,79 \times 10^4\text{ J} = 112000 - 27900 = 84100\text{ J}$$

Questo calore viene interamente assorbito dalla massa d'acqua della sorgente fredda:
$$|Q_{ced}| = m \cdot c \cdot \Delta T$$

Dalla formula ricaviamo la massa minima $m$:
$$m = \frac{|Q_{ced}|}{c \cdot \Delta T}$$

Con $c = 4186\text{ J}/(\text{kg}\cdot\text{K})$ e $\Delta T = 0,1\text{ K}$ ($0,1^\circ\text{C}$):
$$m = \frac{84100}{4186 \times 0,1} = \frac{84100}{418,6} \approx \boxed{200,9\text{ kg}}$$

---

## Esercizio 4

**Testo:** Un sistema subisce una trasformazione termodinamica che aumenta l’entropia di $4,143 \times 10^{-22}\text{ J/K}$. Calcola il rapporto tra la molteplicità del macrostato finale e quella del macrostato iniziale del sistema.

**Soluzione:**
Usiamo la formula di Boltzmann per l'entropia:
$$S = k_B \ln W$$

La variazione di entropia è:
$$\Delta S = S_f - S_i = k_B \ln W_f - k_B \ln W_i = k_B \ln\left(\frac{W_f}{W_i}\right)$$

Isoliamo il logaritmo del rapporto delle molteplicità:
$$\ln\left(\frac{W_f}{W_i}\right) = \frac{\Delta S}{k_B}$$

Applichiamo l'esponenziale per trovare il rapporto:
$$\frac{W_f}{W_i} = e^{\frac{\Delta S}{k_B}}$$

Sostituendo i valori ($\Delta S = 4,143 \times 10^{-22}\text{ J/K}$ e $k_B = 1,38 \times 10^{-23}\text{ J/K}$):
$$\frac{\Delta S}{k_B} = \frac{4,143 \times 10^{-22}}{1,38 \times 10^{-23}} = 30$$

Quindi:
$$\frac{W_f}{W_i} = e^{30} \approx \boxed{1,07 \times 10^{13}}$$

---

## Esercizio 5

**Testo:** Calcola l’entropia di un gas in due serbatoi collegati quando il serbatoio A contiene $7$ particelle e il serbatoio B $3$ particelle. Se si lascia evolvere il sistema spontaneamente, quale sarà la configurazione finale (ovvero, quante particelle di gas in A e quante in B)? Tale configurazione finale avrà entropia maggiore o minore di quella calcolata?

**Soluzione:**
Il numero totale di particelle è $N = 7 + 3 = 10$.
La molteplicità $W$ per una configurazione con $N_A$ particelle in A e $N_B = N - N_A$ in B è data dal coefficiente binomiale:
$$W = \binom{N}{N_A} = \frac{N!}{N_A! (N - N_A)!}$$

Per la configurazione iniziale ($N_A = 7$, $N_B = 3$):
$$W_i = \binom{10}{7} = \frac{10!}{7! \cdot 3!} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120$$

L'entropia iniziale è:
$$S_i = k_B \ln W_i = k_B \ln(120) \approx 4,79 \, k_B$$

Il sistema evolve spontaneamente verso la configurazione più probabile, ovvero quella di massimo disordine (distribuzione uniforme), in cui le particelle si dividono equamente:
- $N_A = 5$
- $N_B = 5$

La molteplicità finale sarà:
$$W_f = \binom{10}{5} = \frac{10!}{5! \cdot 5!} = 252$$

L'entropia finale $S_f = k_B \ln(252)$ sarà **maggiore** di quella calcolata inizialmente, in accordo con il secondo principio della termodinamica per i sistemi isolati ($\Delta S > 0$).

---

## Esercizio 6

**Testo:** Rispondi (anche + di 1 risposta è possibile) e spiega brevemente:
1. Un gas posto in un contenitore viene compresso:
2. Il secondo principio della termodinamica afferma l’impossibilità di:

**Soluzione:**

- **Primo quesito:** 
  - [x] *la sua energia interna aumenta perché viene fatto lavoro sul sistema*
  
  *Spiegazione:* Per il primo principio della termodinamica ($\Delta U = Q - L$), se il gas viene compresso si compie un lavoro negativo sul gas (o positivo *sul* sistema, $L < 0$). In assenza di scambi di calore significativi o se la compressione è rapida, l'energia interna aumenta.

- **Secondo quesito:**
  - [x] *trasformare, come unico risultato, il calore in lavoro.*
  
  *Spiegazione:* Questo corrisponde all'enunciato di Kelvin-Planck del secondo principio della termodinamica.

---

## Materiale generato

### Riepilogo
La verifica affronta i concetti chiave del secondo principio della termodinamica, il calcolo del rendimento e del lavoro per cicli termici sul piano $p\text{-}V$, la potenza di macchine termiche, il calore specifico applicato alle sorgenti e la relazione statistica di Boltzmann tra entropia e molteplicità dei macrostati.

### Esercizi simili

1. Una macchina termica compie un ciclo assorbendo $5000\text{ J}$ di calore da una sorgente calda e cedendone $3500\text{ J}$ alla sorgente fredda. Calcola il lavoro compiuto in un ciclo e il rendimento della macchina.
   <details><summary>Soluzione</summary>
   $L = Q_{ass} - |Q_{ced}| = 5000 - 3500 = 1500\text{ J}$.
   $\eta = \frac{L}{Q_{ass}} = \frac{1500}{5000} = 0,30 \rightarrow \boxed{30\%}$.
   </details>

2. Calcola la variazione di entropia di un sistema la cui molteplicità passa da $W_i = 10$ a $W_f = 1000$ (usa $k_B = 1,38 \times 10^{-23}\text{ J/K}$).
   <details><summary>Soluzione</summary>
   $\Delta S = k_B \ln\left(\frac{W_f}{W_i}\right) = 1,38 \times 10^{-23} \cdot \ln\left(\frac{1000}{10}\right) = 1,38 \times 10^{-23} \cdot \ln(100) \approx 1,38 \times 10^{-23} \cdot 4,605 = \boxed{6,36 \times 10^{-23}\text{ J/K}}$.
   </details>

3. Una sorgente fredda è costituita da $50\text{ kg}$ di acqua ($c = 4186\text{ J}/(\text{kg}\cdot\text{K})$). Se la sorgente assorbe $20930\text{ J}$ di calore da una macchina termica, qual è la variazione di temperatura $\Delta T$ dell'acqua?
   <details><summary>Soluzione</summary>
   $\Delta T = \frac{Q}{mc} = \frac{20930}{50 \times 4186} = \frac{20930}{209300} = \boxed{0,1\text{ K}}$.
   </details>

### Flashcard
- **D:** Cosa esprime l'enunciato di Kelvin del secondo principio della termodinamica? — **R:** L'impossibilità di trasformare integralmente in lavoro il calore estratto da un'unica sorgente.
- **D:** Come si calcola il lavoro in un ciclo termico rappresentato sul piano $p\text{-}V$? — **R:** Corrisponde all'area geometrica racchiusa dalla curva del ciclo.
- **D:** Qual è la formula di Boltzmann che collega l'entropia alla statistica microscopica? — **R:** $S = k_B \ln W$.
- **D:** Come varia l'entropia in un sistema isolato durante una trasformazione spontanea? — **R:** Aumenta sempre ($\Delta S > 0$), evolvendo verso la configurazione più probabile.
