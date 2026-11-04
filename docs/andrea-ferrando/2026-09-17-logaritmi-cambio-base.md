---
titolo: 'Logaritmi: cambio di base'
data: '2026-09-17'
studente: Andrea Ferrando
materia: matematica
argomento: Logaritmi — cambio di base
esercizi:
- 360
- 363
- 364
errori_tipici:
- ln²(x²) confuso con un prodotto
- (ln π)² confuso con ln(π²)
fonte: https://drive.google.com/file/d/1nXTNrmR3EB35nhHMeAOlhypk8SZxRAYo/view
---

# Logaritmi: cambio di base — 17/09/2026

## Formule chiave

$$\log_a x = \frac{\log_b x}{\log_b a} \qquad\qquad \log_a b = \frac{1}{\log_b a}$$

Dimostrazione (dalla lezione): poiché $x = b^{\log_b x}$ per ogni $x>0$,
$$\log_a x = \log_a b^{\log_b x} = \log_b x \cdot \log_a b .$$
Ponendo $x = a$: $\;1 = \log_b a \cdot \log_a b$, da cui la formula del reciproco.

Caso utile — base potenza di 2:
$$\log_{2^n} 2 = \frac{1}{n} \quad\Rightarrow\quad \log_{2^n} x = \frac{\log_2 x}{n}$$

Logaritmo naturale: $\ln x = \log_e x$, con $e = \lim_{n\to\infty}\left(1+\frac1n\right)^n \simeq 2{,}718$.

## Esercizio 360

$$\left(\log_{1/2} 3 + \log_4 3 + \log_{1/2} 3 + \log_{16} 9\right)\ln 2$$

Tutte le basi sono potenze di 2: $\tfrac12 = 2^{-1}$, $4 = 2^2$, $16 = 2^4$.

- $\log_{1/2} 3 = -\log_2 3$
- $\log_4 3 = \tfrac12 \log_2 3$
- $\log_{16} 9 = 2\log_{16} 3 = 2\cdot\tfrac{\log_2 3}{4} = \tfrac12\log_2 3$

$$\left(-2 + \tfrac12 + \tfrac12\right)\log_2 3 \cdot \ln 2 = -\log_2 3\cdot\ln 2 = -\frac{\ln 3}{\ln 2}\cdot\ln 2 = \boxed{-\ln 3}$$

## Esercizio 363

$$\left[\log_{\pi^2}(e^2) + \log_\pi(e^2)\right]\ln\pi$$

$$\log_{\pi^2}(e^2) = \frac{\log_\pi e^2}{\log_\pi \pi^2} = \frac{2\log_\pi e}{2} = \log_\pi e = \frac{1}{\ln\pi}$$

$$\left(\log_\pi e + 2\log_\pi e\right)\ln\pi = 3\cdot\frac{1}{\ln\pi}\cdot\ln\pi = \boxed{3}$$

## Esercizio 364

$$\left(\frac{2\ln\sqrt\pi - \log_\pi e}{\ln\pi - 1} - 1\right)\ln\pi^2$$

Sostituzioni: $2\ln\sqrt\pi = \ln\pi$, $\;\log_\pi e = \frac{1}{\ln\pi}$, $\;\ln\pi^2 = 2\ln\pi$.

$$\left(\frac{(\ln\pi)^2 - 1}{\ln\pi\,(\ln\pi - 1)} - 1\right) 2\ln\pi
= 2\,\frac{(\ln\pi)^2 - 1 - (\ln\pi)^2 + \ln\pi}{\ln\pi - 1}
= 2\,\frac{\ln\pi - 1}{\ln\pi - 1} = \boxed{2}$$

## ⚠️ Errori da evitare

- $(\ln\pi)^2 \neq \ln(\pi^2)$: il primo è il quadrato del logaritmo, il secondo vale $2\ln\pi$.
- $\ln^2 x^2$ **non è un prodotto**: non si applica $(ab)^2 = a^2b^2$.
  $$\ln^2 x^2 = (\ln x^2)^2 = (2\ln x)^2 = 4\ln^2 x$$

---

## Materiale generato

### Riepilogo (3 righe)
Formula del cambio di base ricavata da $x = b^{\log_b x}$, con il caso particolare $\log_a b = 1/\log_b a$. Applicata a espressioni con basi potenze di 2 e con $\pi$, $e$. Chiarita la notazione $\ln^2 x$.

### Esercizi simili (con soluzione)

1. $\left(\log_{1/3} 2 + \log_9 2 + \log_{27} 8\right)\ln 3$
   <details><summary>Soluzione</summary>
   $(-1 + \tfrac12 + 1)\log_3 2 \cdot \ln 3 = \tfrac12 \ln 2$
   </details>

2. $\log_{e^3}(\pi^6)\cdot\log_\pi e$
   <details><summary>Soluzione</summary>
   $\frac{6\ln\pi}{3}\cdot\frac{1}{\ln\pi} = 2$
   </details>

3. Vero o falso: $\ln^2(e^3) = 6$.
   <details><summary>Soluzione</summary>
   Falso: $\ln^2(e^3) = (\ln e^3)^2 = 3^2 = 9$.
   </details>

### Flashcard
- **D:** $\log_a x$ in base $b$? — **R:** $\dfrac{\log_b x}{\log_b a}$
- **D:** $\log_8 2$? — **R:** $\tfrac13$
- **D:** $\ln^2 x^2$? — **R:** $4\ln^2 x$
