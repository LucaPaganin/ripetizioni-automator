---
titolo: Modello microscopico della temperatura e primo principio della termodinamica
data: '2026-05-18'
studente: Andrea Ferrando
materia: fisica
argomento: Termodinamica
sottoargomenti:
- gas ideali
- teoria cinetica dei gas
- energia cinetica media
- primo principio della termodinamica
esercizi: []
errori_tipici: []
fonte: https://drive.google.com/file/d/1eb4ZLzdwd-ezRQEDD9OqfxdorWnQwijC/view?usp=drivesdk
generato: '2026-11-07'
---

# Modello microscopico della temperatura e primo principio della termodinamica

## Formule chiave

- **Equazione di stato dei gas ideali:**
  $$pV = nRT$$

- **Relazione tra numero di moli e numero di particelle:**
  $$N = n \cdot N_A \quad \Longrightarrow \quad n = \frac{N}{N_A}$$
  dove $N_A = 6{,}022 \cdot 10^{23} \text{ mol}^{-1}$ è la costante di Avogadro.

- **Equazione dei gas ideali con la costante di Boltzmann:**
  $$pV = N k_B T$$
  dove $k_B = \frac{R}{N_A}$ è la costante di Boltzmann.

- **Energia cinetica media molecolare:**
  $$\langle E_k \rangle = \frac{3}{2} k_B T$$
  Mostra che l'energia cinetica media delle particelle aumenta all'aumentare della temperatura (agitazione termica).

- **Primo principio della termodinamica:**
  $$\Delta U = Q - L$$
  dove:
  - $U$ è l'energia interna (energia immagazzinata nel sistema).
  - $Q$ è il calore (energia in transito): $Q > 0$ se assorbito dal sistema, $Q < 0$ se ceduto.
  - $L$ è il lavoro (energia in transito): $L > 0$ se eseguito (o ceduto) sull'esterno, $L < 0$ se assorbito.

---

## Modello microscopico della temperatura e Teoria Cinetica

### Gas ideale
Un gas si definisce *ideale* quando è sufficientemente rarefatto (poco denso) da poter assumere che non vi siano interazioni tra le particelle. In queste ipotesi vale l'equazione di stato:
$$pV = nRT$$

### Pressione
La pressione è definita come la forza media esercitata dagli urti delle particelle del gas contro le pareti del recipiente, per unità di superficie.

### Teoria cinetica dei gas
Si assume che le particelle abbiano velocità casuali estratte da una distribuzione di probabilità chiamata **distribuzione di Maxwell-Boltzmann**. Tramite l'integrazione di questa distribuzione si arriva a esprimere l'energia cinetica media delle particelle:
$$\langle E_k \rangle = \frac{3}{2} k_B T$$

- **Cosa è $k_B$:** La costante di Boltzmann.
- **Agitazione termica:** Più sale la temperatura, più aumenta l'energia cinetica media delle particelle che compongono il gas.

---

## Primo principio della termodinamica

In 1 sola parola: **conservazione dell'energia**.

$$\Delta U = Q - L$$

### Convenzione dei segni

- **Per il calore ($Q$):**
  - $Q > 0 \implies$ calore assorbito dal sistema $\implies \Delta U > 0$ (assorbo calore)
  - $Q < 0 \implies$ calore ceduto dal sistema $\implies \Delta U < 0$ (cedo calore)

- **Per il lavoro ($L$):**
  - $L > 0 \implies$ lavoro eseguito (o ceduto) sull'esterno $\implies \Delta U < 0$ (eseguo lavoro)
  - $L < 0 \implies$ lavoro assorbito dall'esterno $\implies \Delta U > 0$ (assorbo lavoro)

---

## Materiale generato

### Riepilogo
Il documento analizza il modello microscopico della temperatura attraverso la teoria cinetica dei gas, legando la temperatura all'energia cinetica media delle particelle. Successivamente introduce il primo principio della termodinamica come legge di conservazione dell'energia legata a calore e lavoro.

### Esercizi simili

1. Calcolare l'energia cinetica media di un gas ideale monoatomico alla temperatura di $300\text{ K}$ (usa $k_B = 1{,}38 \cdot 10^{-23}\text{ J/K}$).
   <details><summary>Soluzione</summary>
   Utilizziamo la formula dell'energia cinetica media:
   $$\langle E_k \rangle = \frac{3}{2} k_B T$$
   Sostituendo i valori:
   $$\langle E_k \rangle = \frac{3}{2} \cdot (1{,}38 \cdot 10^{-23}\text{ J/K}) \cdot 300\text{ K} = 6{,}21 \cdot 10^{-21}\text{ J}$$
   Risultato: $\boxed{6{,}21 \cdot 10^{-21}\text{ J}}$
   </details>

2. Un gas ideale assorbe $500\text{ J}$ di calore e contemporaneamente compie $200\text{ J}$ di lavoro sull'ambiente. Qual è la variazione di energia interna del gas?
   <details><summary>Soluzione</summary>
   Dal primo principio della termodinamica:
   $$\Delta U = Q - L$$
   Poiché il calore è assorbito, $Q = +500\text{ J}$. Poiché il lavoro è compiuto sull'ambiente, $L = +200\text{ J}$.
   $$\Delta U = 500\text{ J} - 200\text{ J} = 300\text{ J}$$
   Risultato: $\boxed{300\text{ J}}$
   </details>

3. Determinare il numero di moli presenti in un campione di gas ideale sapendo che il numero totale di particelle è $N = 1{,}806 \cdot 10^{24}$.
   <details><summary>Soluzione</summary>
   Usiamo la relazione con la costante di Avogadro ($N_A \approx 6{,}022 \cdot 10^{23}\text{ mol}^{-1}$):
   $$n = \frac{N}{N_A} = \frac{1{,}806 \cdot 10^{24}}{6{,}022 \cdot 10^{23}\text{ mol}^{-1}} \approx 3\text{ mol}$$
   Risultato: $\boxed{3\text{ mol}}$
   </details>

### Flashcard
- **D:** Qual è il significato microscopico della temperatura in un gas ideale? — **R:** È direttamente proporzionale all'energia cinetica media delle particelle ($\langle E_k \rangle = \frac{3}{2} k_B T$).
- **D:** Come si esprime l'equazione di stato dei gas ideali usando il numero di particelle $N$? — **R:** $pV = N k_B T$.
- **D:** Cosa esprime il primo principio della termodinamica? — **R:** Esprime la conservazione dell'energia sotto forma di calore e lavoro: $\Delta U = Q - L$.
- **D:** Qual è il segno di $Q$ quando un sistema cede calore? — **R:** $Q < 0$ (calore ceduto).
