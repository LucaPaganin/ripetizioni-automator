# Ripetizioni — appunti digitalizzati

Ogni sera una GitHub Action:

1. legge i PDF nuovi o modificati in `Classroom/<Studente>/…` su Google Drive (le cartelle che iniziano con `_` sono ignorate);
2. li trascrive con Gemini (free tier) in Markdown + LaTeX secondo `pipeline/prompt.md`;
3. salva le pagine in `docs/<studente>/AAAA-MM-GG-<slug>.md`, rigenera gli indici (per data, per argomento, errori ricorrenti) e fa commit;
4. builda il sito MkDocs Material e lo pubblica su GitHub Pages.

Lo stato dei file già elaborati è in `pipeline/state.json`: un PDF viene ritrascritto solo se cambia su Drive.

## Setup (una tantum, ~15 minuti)

### 1. Accesso a Drive senza chiavi (Workload Identity Federation)

La GitHub Action ottiene credenziali GCP a vita breve via OIDC e impersona una service account: nessuna chiave JSON da custodire o ruotare, e solo i workflow di questo repo sono autorizzati.

1. [console.cloud.google.com](https://console.cloud.google.com) → crea un progetto → apri **Cloud Shell** (icona `>_`).
2. Carica `pipeline/gcp-setup.sh` e lancia `bash gcp-setup.sh <PROJECT_ID> <owner/repo>`.
3. Lo script stampa l'email della service account (da condividere su Drive come **Visualizzatore** sulla cartella **Classroom**) e i valori delle variabili GitHub.

### 2. Chiave Gemini

[aistudio.google.com](https://aistudio.google.com) → *Get API key*. Il free tier basta.
Nota: sul free tier Google può usare i contenuti inviati per migliorare i propri modelli.

### 3. Repository GitHub

- **Secrets** (*Settings → Secrets and variables → Actions*):
  - `GEMINI_API_KEY`
- **Variables**:
  - `GCP_WIF_PROVIDER`, `GCP_SERVICE_ACCOUNT`: stampati da `gcp-setup.sh`
  - `DRIVE_ROOT_ID`: ID della cartella Classroom (dall'URL `drive.google.com/drive/folders/<ID>`)
  - `GEMINI_MODEL` (facoltativo, default `gemini-flash-latest`, alias che punta sempre all'ultimo Flash; per fissare un modello: es. `gemini-3.5-flash-lite`. Elenco aggiornato: [modelli Gemini](https://ai.google.dev/gemini-api/docs/models))
- *Settings → Pages → Source*: **GitHub Actions**.

### 4. Primo giro

*Actions → Sync appunti e pubblica sito → Run workflow*. Con `MAX_FILES=15` lo storico viene smaltito in qualche sera; se Gemini restituisce 429 il run si ferma e riprende la volta dopo.

## Personalizzazione

- Formato dell'output: `pipeline/prompt.md`. Per rigenerare tutto, svuota `pipeline/state.json` (`{}`).
- Orario: `cron` in `.github/workflows/sync.yml`.
- Test locale senza chiamare Gemini: `DRY_RUN=1 python pipeline/sync.py`.

## Privacy

Su un piano GitHub gratuito, GitHub Pages pubblica solo da repo **pubblici**: sito e appunti sono visibili a chiunque abbia il link, nomi degli studenti compresi. Alternative: rinominare le cartelle su Drive con il solo nome, oppure tenere il repo privato e pubblicare su Cloudflare Pages / Netlify (gratuiti anche da repo privati) al posto dei job `upload-pages-artifact` / `deploy`.
