---
titolo: Isometrie e Dilatazioni nel Piano Cartesiano
data: '2026-04-22'
studente: Andrea Ferrando
materia: matematica
argomento: Geometria analitica
sottoargomenti:
- Isometrie
- Traslazioni
- Dilatazioni
- Trasformazioni di curve e coniche
esercizi:
- 1
- 2
- 3
- 4
errori_tipici:
- Confondere la trasformazione degli assi con la trasformazione degli oggetti
- Dimenticare che un'equazione non ridotta in forma canonica non permette di leggere
  direttamente i semiassi
fonte: https://drive.google.com/file/d/1itQW3cC5xYuuEflB0Fvuoa1Eozvne_Kq/view?usp=drivesdk
generato: '2026-11-07'
---

# Isometrie e Dilatazioni nel Piano Cartesiano

## Formule chiave

- **Traslazione delle coordinate (cambio di riferimento):**
  Dato un vettore di traslazione $\vec{v} = (v_x, v_y)$, la relazione tra le vecchie coordinate $(x, y)$ e le nuove coordinate $(x', y')$ è:
  $$\begin{cases} x = x' - v_x \\ y = y' - v_y \end{cases}$$
  Viceversa, per traslare un oggetto geometrico:
  $$\begin{cases} x' = x - v_x \\ y' = y - v_y \end{cases}$$

- **Equazione canonica dell'ellisse con centro nell'origine:**
  $$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$$

- **Dilatazione (scaling):**
  $$\begin{cases} x' = A x \\ y' = B y \end{cases} \implies \begin{cases} x = \frac{x'}{A} \\ y = \frac{y'}{B} \end{cases}$$

---

## Esercizio 1 (Studio di funzione e riconduzione a conica)

Ddata la funzione:
$$y = |2 - \sqrt{25 - 4x^2}|$$

Analizziamo il dominio (condizioni di esistenza):
1. Radicale reale: $25 - 4x^2 \ge 0 \implies x^2 \le \frac{25}{4} \implies -\frac{5}{2} \le x \le \frac{5}{2}$.
2. Il dominio è dunque: $\text{Dom} = \left[-\frac{5}{2}, \frac{5}{2}\right]$.

Spezziamo il modulo:
$$y = \begin{cases} 2 - \sqrt{25 - 4x^2} & \text{se } 2 - \sqrt{25 - 4x^2} \ge 0 \\ -2 + \sqrt{25 - 4x^2} & \text{se } 2 - \sqrt{25 - 4x^2} < 0 \end{cases}$$

Consideriamo il primo caso ($2 - \sqrt{25 - 4x^2} \ge 0 \implies \sqrt{25 - 4x^2} \le 2$):
Elevando al quadrato ambo i membri:
$$25 - 4x^2 \le 4 \implies 4x^2 \ge 21 \implies x^2 \ge \frac{21}{4}$$

Isolando la radice nell'equazione:
$$y - 2 = -\sqrt{25 - 4x^2}$$
Elevando al quadrato:
$$(y - 2)^2 = 25 - 4x^2$$
$$4x^2 + (y - 2)^2 = 25$$

Dividendo tutto per $25$:
$$\frac{4x^2}{25} + \frac{(y - 2)^2}{25} = 1 \implies \frac{x^2}{\frac{25}{4}} + \frac{(y - 2)^2}{25} = 1$$

Da cui ricaviamo i parametri dell'ellisse traslata:
$$a^2 = \frac{25}{4} \implies a = \frac{5}{2}$$
$$b^2 = 25 \implies b = 5$$

---

## Esercizio 2 (Trasformazione tra ellissi con dilatazioni)

Vogliamo trovare la dilatazione che trasforma l'ellisse $\gamma_1: \frac{x^2}{9} + \frac{y^2}{9} = 1$ nella conica $\gamma_2: \frac{x^2}{4} + \frac{y^2}{25} = 1$.

Riscriviamo $\gamma_1$ mettendo in evidenza i denominatori desiderati:
$$\frac{x^2}{9} + \frac{y^2}{9} = \frac{x^2}{4 \cdot \frac{9}{4}} + \frac{y^2}{25 \cdot \frac{9}{25}} = \frac{\left(\frac{x}{\frac{3}{2}}\right)^2}{4} + \frac{\left(\frac{y}{\frac{3}{5}}\right)^2}{25} = 1$$

Ponendo la trasformazione:
$$\begin{cases} x' = \frac{x}{\frac{3}{2}} \\ y' = \frac{y}{\frac{3}{5}} \end{cases} \implies \begin{cases} x = \frac{2}{3}x' \\ y = \frac{5}{3}y' \end{cases}$$

Sostituendo nell'equazione otteniamo l'equazione ridotta in forma canonica:
$$\frac{x'^2}{4} + \frac{y'^2}{25} = 1$$

---

## Esercizio 3 (Dilatazione da ellisse generica a circonferenza)

Data l'equazione dell'ellisse $E: \frac{x^2}{9} + 25y^2 = 1$ e la circonferenza $C: x^2 + y^2 = 1$.

Riscriviamo l'ellisse in forma canonica:
$$\frac{x^2}{9} + \frac{y^2}{\frac{1}{25}} = 1 \implies a = 3, \ b = \frac{1}{5}$$

Cerchiamo la trasformazione del tipo:
$$\begin{cases} x = \frac{x'}{A} \\ y = \frac{y'}{B} \end{cases}$$

Imponendo il passaggio alla forma canonica con $a'=1$ e $b'=1$:
$$\frac{x'^2}{9A^2} + \frac{y'^2}{\frac{1}{25}B^2} = 1$$
Da cui il sistema per determinare $A$ e $B$:
$$\begin{cases} 9A^2 = 1 \\ \frac{1}{25}B^2 = 1 \end{cases} \implies \begin{cases} A = \frac{1}{3} \\ B = 5 \end{cases}$$

---

## ⚠️ Errori da evitare

- Scrivere un'equazione non in forma canonica (ad esempio con coefficienti diversi da $1$ al RHS o coefficienti sui termini $x^2, y^2$) e pretendere di leggere direttamente i semiassi $a$ e $b$. Come evidenziato negli appunti: **NON È IN FORMA CANONICA** finché non si riconduce alla forma $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$.

---

## Materiale generato

### Riepilogo
Le isometrie e le dilatazioni permettono di trasformare figure geometriche nel piano cartesiano modificandone posizione o proporzioni. Le traslazioni spostano il centro della figura, mentre le dilatazioni agiscono sui semiassi tramite fattori di scala $A$ e $B$.

### Esercizi simili

1. Data l'ellisse $\frac{x^2}{16} + \frac{y^2}{4} = 1$, determinare l'equazione dopo la traslazione di vettore $\vec{v} = (1, -2)$.
   <details><summary>Soluzione</summary>Sostituendo $x = x'-1$ e $y = y'+2$, si ottiene: $\frac{(x'-1)^2}{16} + \frac{(y'+2)^2}{4} = 1$.</details>

2. Trovare i semiassi $a$ e $b$ dell'ellisse data dall'equazione $9x^2 + 4y^2 = 36$.
   <details><summary>Soluzione</summary>Dividendo per $36$ si ottiene $\frac{x^2}{4} + \frac{y^2}{9} = 1$, da cui $a = 2$ e $b = 3$.</details>

3. Applicare una dilatazione con fattori $A = 2$ e $B = \frac{1}{3}$ alla circonferenza $x^2 + y^2 = 1$.
   <details><summary>Soluzione</summary>Sostituendo $x = \frac{x'}{2}$ e $y = 3y'$, si ottiene l'ellisse $\frac{x'^2}{4} + 9y'^2 = 1$.</details>

### Flashcard
- **D:** Qual è la relazione tra le coordinate $(x,y)$ e $(x',y')$ in una traslazione con vettore $\vec{v}=(v_x, v_y)$ applicata alle coordinate? — **R:** $x = x' - v_x$ e $y = y' - v_y$.
- **D:** Quando un'ellisse si dice in forma canonica? — **R:** Quando è centrata nell'origine e ha equazione $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$.
- **D:** Come agisce una dilatazione di fattori $A$ e $B$ sulle coordinate $x$ e $y$? — **R:** $x' = Ax$ e $y' = By$.
