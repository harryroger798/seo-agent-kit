# MCP and API connections

The kit can run on manual inputs. MCP and APIs make it faster. This folder contains example configs and the tool matrix.

## Files

| File | Use |
|---|---|
| `servers.example.json` | Generic MCP config with placeholders |
| `claude-desktop.example.json` | Claude Desktop shape |
| `cursor.example.json` | Cursor shape |
| `tool-matrix.md` | Tool-by-tool connection methods, auth, fallback |

## The rule

**Never put a real secret in a file you commit.** Use `${ENV_VAR}` references, the client’s secret store, or a local `.env` that is gitignored.

## The connection order

1. **MCP** — if the tool is connected, call it.
2. **API** — if you have a key, use the REST API.
3. **CSV** — export from the UI and read the file.
4. **Manual** — ask the operator for the numbers and cite the source.

If a tool is missing, say so. Do not invent the data.

## Test prompt

```text
List the tools you can call from each connected MCP server. For each,
show one read-only call and its parameters. Do not run a write call.
Do not ask for secrets.
```

## Security

See `docs/03-credentials-and-security.md`.
