# Credentials and security

## The rule

**Never paste a password, API key, OAuth token, or session cookie into a chat.**

The agent should ask you to set an environment variable, connect an MCP server, or provide a CSV export. If it asks for a secret in chat, stop and correct it.

## Where secrets live

| Secret | Where |
|---|---|
| API keys | `.env` (gitignored) or the client's secret store |
| OAuth tokens | The MCP client's auth flow, not a file in the repo |
| GSC/GA4 credentials | A service account JSON outside the repo, or OAuth |
| Client data | Outside the repo, or a gitignored `data/private/` folder |

## `.env` pattern

Copy `.env.example` to `.env` and fill only what you use:

```bash
cp .env.example .env
```

`.env` is in `.gitignore`. Never commit it. Never include it in a ZIP you share.

## What the agent may ask for

- “Set `SPYFU_API_KEY` in your `.env`.”
- “Connect the Ubersuggest MCP server in your client.”
- “Export the GSC queries CSV and put it in `data/`.”
- “Authorize the Google account in the MCP client.”

## What the agent must not ask for

- A password.
- An API key pasted into the chat.
- A session cookie.
- A screenshot of a billing page with card details.
- A client’s personal data in a public issue.

## If a secret leaks

1. Revoke it at the provider.
2. Rotate it.
3. Remove it from the repo history (BFG or `git filter-repo`).
4. Check logs, issues, and forks.
5. Add the pattern to `.gitignore` and the validation script.

## Public repo hygiene

- `scripts/validate_kit.py` scans for common secret patterns.
- The CI workflow runs the validator on every push.
- Do not commit `data/private/`, `.env`, `*.pem`, `*.key`, or service-account JSON.
- Do not commit client exports with emails, phone numbers, or order data.

## Tool scopes

Use the minimum scope:

- GSC: read-only.
- GA4: read-only.
- SpyFu/Mangools: read-only API key if the provider supports scopes.
- Ubersuggest: use the official connector's permissions; do not share your login.

## Reporting a vulnerability

See `SECURITY.md`.
