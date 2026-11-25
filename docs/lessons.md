# Lessons

| Date | What happened | Root cause | How to avoid |
|---|---|---|---|
| 2026-11-26 | `conda create` failed: couldn't write `~/.conda/tos/...` | `~/.conda` was owned by root, likely from an earlier `sudo conda ...` | Never run conda with `sudo`. If it happens: `sudo chown -R $(whoami) ~/.conda` |
