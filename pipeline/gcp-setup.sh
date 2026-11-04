#!/usr/bin/env bash
# Setup una tantum di Workload Identity Federation GitHub -> GCP.
# Eseguilo in Cloud Shell (console.cloud.google.com, icona >_ in alto a destra).
#   bash gcp-setup.sh <PROJECT_ID> <owner/repo>
set -euo pipefail

PROJECT_ID="${1:?PROJECT_ID}"
REPO="${2:?owner/repo, es. LucaPaganin/ripetizioni-site}"
SA_NAME="ripetizioni-drive"
POOL="github"
PROVIDER="github-oidc"

gcloud config set project "$PROJECT_ID"
PROJECT_NUMBER="$(gcloud projects describe "$PROJECT_ID" --format='value(projectNumber)')"

gcloud services enable drive.googleapis.com iamcredentials.googleapis.com sts.googleapis.com

gcloud iam service-accounts create "$SA_NAME" --display-name="Ripetizioni: lettura Drive" || true
SA_EMAIL="${SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"

gcloud iam workload-identity-pools create "$POOL" --location=global --display-name="GitHub" || true
gcloud iam workload-identity-pools providers create-oidc "$PROVIDER" \
  --location=global --workload-identity-pool="$POOL" \
  --issuer-uri="https://token.actions.githubusercontent.com" \
  --attribute-mapping="google.subject=assertion.sub,attribute.repository=assertion.repository" \
  --attribute-condition="assertion.repository == '${REPO}'" || true

# Solo i workflow di questo repo possono impersonare la service account.
gcloud iam service-accounts add-iam-policy-binding "$SA_EMAIL" \
  --role=roles/iam.workloadIdentityUser \
  --member="principalSet://iam.googleapis.com/projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${POOL}/attribute.repository/${REPO}"

cat <<EOF

Fatto. Ora:
1. Su Drive condividi la cartella Classroom con:  ${SA_EMAIL}  (Visualizzatore)
2. Nel repo GitHub, Settings → Secrets and variables → Actions → Variables:
     GCP_WIF_PROVIDER     = projects/${PROJECT_NUMBER}/locations/global/workloadIdentityPools/${POOL}/providers/${PROVIDER}
     GCP_SERVICE_ACCOUNT  = ${SA_EMAIL}
     DRIVE_ROOT_ID        = <ID cartella Classroom>
   Secret:
     GEMINI_API_KEY
EOF
