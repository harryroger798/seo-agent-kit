# Security policy

## Reporting a vulnerability

Do not open a public issue for a security problem. Email the maintainer at the address on the GitHub profile, or use GitHub’s private vulnerability reporting.

Include:

- what you found
- how to reproduce it
- the affected file or version
- whether a secret or personal data is exposed

## Secrets

If you find a committed secret:

1. Do not share it publicly.
2. Report it privately.
3. Revoke and rotate it at the provider.
4. Remove it from history.

## Scope

This repository contains prompts, scripts, and configuration examples. It does not run a hosted service. The main risks are:

- committed API keys or client data
- prompt injection through untrusted content
- tool calls that write to a live account
- directory submissions that violate a platform’s terms

## Safe use

- Use read-only scopes where possible.
- Never paste secrets into chat.
- Review a skill before enabling it.
- Run `python scripts/validate_kit.py` before publishing a fork.
