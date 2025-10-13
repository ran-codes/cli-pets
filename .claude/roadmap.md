# CLI-Pets PRD & Roadmap

## Overview
Python CLI package for animated terminal pets. Package name: `cli-pets`

## Core Functions

### 1. Walking Pet (MVP)
```bash
pet-walk          # single pet walks across screen
pet-walk --pet 🐱 # choose your pet
```

### 2. Pet Race
```bash
pet-race          # 3 pets race
pet-race -n 5     # 5 racers
```

## Roadmap

### Phase 1: MVP (Week 1)
- [ ] Package setup with `uv`
- [ ] `pet-walk` function with 3 animals
- [ ] Basic terminal animation (`rich`)
- [ ] Publish to PyPI

### Phase 2: Racing (Week 2)
- [ ] `pet-race` command
- [ ] 2-8 racers support
- [ ] Winner announcement

### Phase 3: Features (Week 3-4)
- [ ] Custom pet selection
- [ ] Speed/distance options
- [ ] Random events (powerups, obstacles)
- [ ] Leaderboard

### Phase 4: Polish (Week 5+)
- [ ] More animals (10+ options)
- [ ] Themes/backgrounds
- [ ] ASCII art
- [ ] Config file for defaults

## Success Metrics
- 100+ PyPI installs (month 1)
- Works on Windows/Mac/Linux
- <0.5s startup