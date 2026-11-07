---
titolo: Geometria dell'ellisse ed Eccentricità
data: '2026-03-12'
studente: Andrea Ferrando
materia: fisica
argomento: Orbite e Leggi di Keplero
sottoargomenti:
- Ellisse
- Eccentricità
- Terza legge di Keplero
esercizi:
- '25'
errori_tipici:
- Confondere la distanza al perielio e all'apoforo con il semiasse maggiore
fonte: https://drive.google.com/file/d/1_rRMuSoOS8eFV06JpFXqCXZOcTyWyYnL/view?usp=drivesdk
generato: '2026-11-07'
---

# Geometria dell'ellisse ed Eccentricità

## Formule chiave

- **Equazione canonica dell'ellisse:**
  $$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$$

- **Relazione tra i semiassi e i fuochi:**
  $$c = \sqrt{a^2 - b^2}$$
  dove $d(F_1, F_2) = 2c$ e $F_1(c,0)$, $F_2(-c,0)$.

- **Eccentricità ($e$):**
  $$e = \frac{c}{a} = \sqrt{1 - \frac{b^2}{a^2}}$$
  Con la condizione $0 \le e < 1$ (per $0 < b < a$).

- **Terza legge di Keplero:**
  $$K = \frac{a^3}{T^2}$$
  Il valore di $K$ dipende dal corpo centrale (es. il Sole).

---

## Esercizio (Luna - Terra)

Dal testo di un problema sulla Luna, si ricavano le distanze:
- Apogeo ($d_a$): $4,06 \cdot 10^5 \text{ km}$
- Perigeo ($d_p$): $3,63 \cdot 10^5 \text{ km}$

Relazioni geometriche:
$$2a = d_a + d_p \implies a = \frac{d_a + d_p}{2}$$

Sostituendo i valori numerici:
$$a = \frac{4,06 \cdot 10^5 + 3,63 \cdot 10^5}{2} = 3,845 \cdot 10^5 \text{ km} = 3,845 \cdot 10^8 \text{ m}$$

---

## Esercizio 25 (Cometa di Encke)

Dati della cometa:
- $d_a = 4,098 \text{ au}$
- $d_p = 0,3396 \text{ au}$

Semiasse maggiore:
$$a = \frac{d_a + d_p}{2} = \frac{4,098 + 0,3396}{2} = 2,2188 \text{ au}$$

Convertendo in metri ($1 \text{ au} = 1,5 \cdot 10^{11} \text{ m}$):
$$a = 2,2188 \cdot 1,5 \cdot 10^{11} \text{ m}$$

Periodo di rivoluzione ($T$):
Dalla costante di Keplero ricavata per il sistema solare ($K \approx 7,506 \cdot 10^{-6} \frac{\text{au}^3}{\text{d}^2}$ oppure usando direttamente $a$ in au e $T$ in anni):
$$T_{\text{cometa}} = \sqrt{\frac{a^3_{\text{cometa}}}{K}} = \sqrt{(2,2188)^3} \approx \boxed{3,305 \text{ y}}$$

---

## ⚠️ Errori da evitare

- Dimenticare che $a$ è il *semiasse* maggiore, quindi la somma della distanza all'apogeo e al perigeo dà il *diametro* maggiore ($2a$), non $a$.

---

## Materiale generato

### Riepilogo
Gli appunti trattano le proprietà geometriche dell'ellisse (semiassi, fuochi ed eccentricità) e applicano le leggi di Keplero, in particolare la terza legge, per calcolare il periodo di rivoluzione di corpi celesti noti i loro semiassi orbitali.

### Esercizi simili
1. Un pianeta orbita attorno al Sole con un semiasse maggiore $a = 5,2 \text{ au}$ (orbita di Giove). Calcola il suo periodo di rivoluzione in anni.
   <details><summary>Soluzione</summary>Usando la terza legge di Keplero in unità astronomiche e anni ($T^2 = a^3$): $T = \sqrt{5,2^3} \approx \sqrt{140,6} \approx 11,86 \text{ anni}$.</details>

2. Calcola l'eccentricità di un'ellisse con semiasse maggiore $a = 5 \text{ cm}$ e semiasse minore $b = 3 \text{ cm}$.
   <details><summary>Soluzione</summary>Si calcola prima $c = \sqrt{a^2 - b^2} = \sqrt{25 - 9} = \sqrt{16} = 4 \text{ cm}$. L'eccentricità è $e = \frac{c}{a} = \frac{4}{5} = 0,8$.</details>

3. Un asteroide ha una distanza al perigeo $d_p = 1 \text{ au}$ e all'apogeo $d_a = 3 \text{ au}$. Qual è il suo semiasse maggiore?
   <details><summary>Soluzione</summary>$a = \frac{d_a + d_p}{2} = \frac{3 + 1}{2} = \boxed{2 \text{ au}}$.</details>

### Flashcard
- **D:** — Qual è la formula dell'eccentricità di un'ellisse? — **R:** — $e = \frac{c}{a} = \sqrt{1 - \frac{b^2}{a^2}}$
- **D:** — Come si ricava il semiasse maggiore $a$ conoscendo perigeo $d_p$ e apogeo $d_a$? — **R:** — $a = \frac{d_a + d_p}{2}$
- **D:** — Cosa esprime la terza legge di Keplero? — **R:** — Che il rapporto $\frac{a^3}{T^2}$ è costante per tutti i pianeti che orbitano attorno allo stesso corpo centrale.
