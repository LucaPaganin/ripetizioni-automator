---
titolo: Impulso di una forza, urti 1D elastici e nel centro di massa
data: '2026-01-22'
studente: Andrea Ferrando
materia: fisica
argomento: Dinamica dei sistemi e urti
sottoargomenti:
- Impulso di una forza
- Teorema dell'impulso
- Urti elastici unidimensionali
- Urto nel centro di massa (CM)
esercizi:
- Es 1D urto elastico
errori_tipici:
- Dimenticare di specificare su quale corpo agisce l'impulso e di chi è la variazione
  di quantità di moto
- Accettare soluzioni cinematiche prive di significato fisico come velocità finali
  identiche a quelle iniziali senza urto
fonte: https://drive.google.com/file/d/1VW8q-sUyTnhM8jl_J-ff0_3b2OMEDaUB/view?usp=drivesdk
generato: '2026-11-07'
---

# Impulso di una forza, urti 1D elastici e nel centro di massa

## Formule chiave

- **Definizione di impulso per una forza costante in 1D:**
  $$\vec{I} = \vec{F} \cdot T$$

- **Teorema dell'impulso:**
  $$\vec{I} = \Delta \vec{p}$$

- **Forza media per forza variabile in intervallo $T$:**
  $$\langle \vec{F}(t) \rangle = \frac{1}{T} \int_0^T \vec{F}(t) \, dt \quad (\text{area sottesa})$$
  $$\|\vec{I}\| = \langle F(t) \rangle \cdot T$$

- **Conservazione della quantità di moto totale per un sistema isolato:**
  $$\vec{P}_i = \vec{P}_f \implies m_1 \vec{v}_{1i} + m_2 \vec{v}_{2i} = m_1 \vec{v}_{1f} + m_2 \vec{v}_{2f}$$

- **Conservazione dell'energia cinetica in un urto elastico:**
  $$\frac{1}{2} m_1 v_{1i}^2 + \frac{1}{2} m_2 v_{2i}^2 = \frac{1}{2} m_1 v_{1f}^2 + \frac{1}{2} m_2 v_{2f}^2$$

- **Velocità del Centro di Massa (CM):**
  $$\vec{v}_{CM} = \frac{m_1 \vec{v}_{1i} + m_2 \vec{v}_{2i}}{m_1 + m_2}$$

---

## Esercizio: Urto elastico 1D

**Testo:**
Un sistema in 1D subisce un urto elastico tra due particelle con masse $m_1 = m_2 = m = 1\,\text{kg}$.
- Velocità iniziale particella 1: $v_{1i} = 3\,\text{m/s}$
- Velocità iniziale particella 2: $v_{2i} = 0\,\text{m/s}$

Trovare tutto compreso l'impulso scambiato e la forza media assumendo che l'urto duri $T = 10\,\text{ms} = 10 \cdot 10^{-3}\,\text{s} = 10^{-2}\,\text{s}$.

### Svolgimento

**1. Conservazione della quantità di moto:**
$$m v_{1i} = m v_{1f} + m v_{2f} \implies v_{1i} = v_{1f} + v_{2f} \quad \text{(1)}$$

**2. Conservazione dell'energia cinetica:**
$$\frac{1}{2} m v_{1i}^2 = \frac{1}{2} m v_{1f}^2 + \frac{1}{2} m v_{2f}^2 \implies v_{1i}^2 = v_{1f}^2 + v_{2f}^2 \quad \text{(2)}$$

Ricavando $v_{1f}$ dalla (1) ($v_{1f} = v_{1i} - v_{2f}$) e sostituendo nella (2):
$$v_{1i}^2 = (v_{1i} - v_{2f})^2 + v_{2f}^2$$
$$v_{1i}^2 = v_{1i}^2 + v_{2f}^2 - 2 v_{1i} v_{2f} + v_{2f}^2$$
$$2 v_{2f}^2 - 2 v_{1i} v_{2f} = 0$$
$$2 v_{2f} (v_{2f} - v_{1i}) = 0$$

Da cui si ottengono due soluzioni:
1. $v_{2f} = 0 \implies$ scartato per motivi fisici (corrisponde al caso in cui l'urto non avviene).
2. $v_{2f} = v_{1i} = 3\,\text{m/s}$.

Sostituendo nella (1) per trovare $v_{1f}$:
$$v_{1f} = v_{1i} - v_{2f} = 3 - 3 = 0\,\text{m/s}.$$

**3. Calcolo dell'impulso e della variazione di quantità di moto:**
$$\Delta \vec{p}_1 = p_{1f} - p_{1i} = 0 - m v_{1i} = - (1\,\text{kg})(3\,\text{m/s}) = -3\,\text{kg}\cdot\text{m/s}$$
$$\Delta \vec{p}_2 = p_{2f} - p_{2i} = m v_{2f} - 0 = (1\,\text{kg})(3\,\text{m/s}) = +3\,\text{kg}\cdot\text{m/s}$$

Poiché $I_1 = \Delta p_1$ e $I_2 = \Delta p_2$, abbiamo:
$$I_1 = -3\,\text{N}\cdot\text{s} \quad (\text{impulso esercitato su 1 da 2})$$
$$I_2 = +3\,\text{N}\cdot\text{s} \quad (\text{impulso esercitato su 2 da 1})$$

**4. Calcolo della forza media:**
Sapendo che $T = 10\,\text{ms} = 10^{-2}\,\text{s}$:
$$\Delta p_1 = \langle F \rangle \cdot T \implies \langle F_1 \rangle = \frac{\Delta p_1}{T} = \frac{-3\,\text{kg}\cdot\text{m/s}}{10^{-2}\,\text{s}} = -300\,\text{N}$$

La massa $m = 1\,\text{kg}$ subisce quindi un'accelerazione media
$$\langle a \rangle = \frac{\Delta v}{T} = \frac{3\,\text{m/s}}{10^{-2}\,\text{s}} = 300\,\text{m/s}^2$$
Per rendersi conto dell'ordine di grandezza: se questa accelerazione durasse $\Delta t = 1\,\text{s}$, la velocità raggiunta sarebbe
$$v_f = \langle a \rangle \cdot \Delta t = 300\,\text{m/s} = 1080\,\text{km/h}$$

---

## ⚠️ Errori da evitare

- **Attenzione alle definizioni:** Va sempre specificato con precisione su quale corpo agisca l'impulso $\vec{I}$ e di quale corpo sia la variazione di quantità di moto $\Delta \vec{p}$.
- **Attenzione alle soluzioni banali:** Negli urti elastici, la risoluzione algebrica del sistema produce sempre una soluzione non fisica (velocità finali uguali a quelle iniziali, cioè nessuna interazione); ricordarsi di scartarla basandosi sul contesto fisico del problema.

---
## Materiale generato

### Riepilogo
L'impulso di una forza rappresenta la variazione della quantità di moto di un sistema ed è graficamente pari all'area sottostante il grafico $F(t)$. Negli urti elastici unidimensionali tra corpi di massa uguale, si verifica uno scambio totale delle velocità. Passando al sistema di riferimento del centro di massa (CM), l'analisi degli urti si semplifica notevolmente riducendosi a un'inversione dei vettori velocità relativi.

### Esercizi simili
1. Due corpi di masse $m_1 = 2\,\text{kg}$ e $m_2 = 3\,\text{kg}$ viaggiano frontalmente in 1D con velocità $v_{1i} = 5\,\text{m/s}$ e $v_{2i} = -2\,\text{m/s}$. Calcolare la velocità del centro di massa $\vec{v}_{CM}$ del sistema.
<details><summary>Soluzione</summary>
Applicando la formula del centro di massa:
$$v_{CM} = \frac{m_1 v_{1i} + m_2 v_{2i}}{m_1 + m_2} = \frac{(2 \cdot 5) + (3 \cdot (-2))}{2 + 3} = \frac{10 - 6}{5} = \frac{4}{5} = \boxed{0.8\,\text{m/s}}$$
</details>

2. Una forza costante pari a $F = 50\,\text{N}$ agisce su un blocco per un intervallo di tempo $\Delta t = 0.2\,\text{s}$. Calcolare l'impulso ricevuto dal blocco e la variazione della sua quantità di moto.
<details><summary>Soluzione</summary>
L'impulso è dato da $I = F \cdot \Delta t = 50\,\text{N} \cdot 0.2\,\text{s} = 10\,\text{N}\cdot\text{s}$. Per il teorema dell'impulso, la variazione di quantità di moto è numericamente uguale all'impulso: $\Delta p = 10\,\text{kg}\cdot\text{m/s}$. Risultato: $\boxed{I = 10\,\text{N}\cdot\text{s}, \, \Delta p = 10\,\text{kg}\cdot\text{m/s}}$.
</details>

3. Un corpo di massa $m = 2\,\text{kg}$ subisce una variazione di velocità da $v_i = 1\,\text{m/s}$ a $v_f = 7\,\text{m/s}$ in un tempo $T = 4\,\text{ms} = 4 \cdot 10^{-3}\,\text{s}$. Calcolare il modulo della forza media applicata.
<details><summary>Soluzione</summary>
Calcoliamo prima la variazione di quantità di moto: $\Delta p = m(v_f - v_i) = 2 \cdot (7 - 1) = 12\,\text{kg}\cdot\text{m/s}$. La forza media è $F_{med} = \frac{\Delta p}{T} = \frac{12}{4 \cdot 10^{-3}} = 3 \cdot 10^3 = \boxed{3000\,\text{N}}$.
</details>

### Flashcard
- **D:** Cos'è geometricamente l'impulso di una forza variabile nel tempo nel piano $F$-$t$? — **R:** È l'area sottesa dalla curva della forza in funzione del tempo tra l'istante iniziale e quello finale.
- **D:** Cosa afferma il teorema dell'impulso? — **R:** L'impulso totale applicato a un corpo è uguale alla variazione della sua quantità di moto ($\vec{I} = \Delta \vec{p}$).
- **D:** Cosa si conserva sempre in un urto elastico unidimensionale? — **R:** Si conservano sia la quantità di moto totale del sistema sia l'energia cinetica totale.
- **D:** Qual è il risultato di un urto elastico frontale tra due corpi di egual massa, dove il secondo è fermo? — **R:** Il primo corpo si ferma completamente e cede tutta la sua velocità al secondo corpo ($v_{1f} = 0$ e $v_{2f} = v_{1i}$).
