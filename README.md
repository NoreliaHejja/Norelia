# Norelia – AI cég agent rendszer

Főnök (CEO) agent, alatta osztály-agentek. Egyetlen cél: több nettó pénz a projektekből.

- `CLAUDE.md` – közös szabályok, célok, szervezet
- `.claude/agents/` – fonok, marketing, sales, penzugy, palyazat, operacio
- `ceg/` – közös memória: célok, projektek, napló

## Használat
```bash
claude --agent fonok        # a Főnök a fő agent, ő delegál a többieknek
```
Vagy Claude Code-ban: „Főnök, készítsd el a heti áttekintést.”

Heti ritmus: hétfőn a Főnök áttekintést készít (pipeline, pénzügy, haladás, a hét 3 lépése).
