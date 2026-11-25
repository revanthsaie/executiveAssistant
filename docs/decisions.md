# Decision log

| Date | Decision | Why | Alternatives rejected |
|---|---|---|---|
| 2026-11-26 | Builder mode: Claude writes the code | Tool for daily work; quality and speed first | Learning mode |
| 2026-11-26 | Build our own app, not Obsidian plugins | Your choice: custom UI, full control | Tasks/Dataview/AI-chat plugins |
| 2026-11-26 | Local-first AI, Haiku opt-in fallback | Work data stays on the laptop by default | Cloud-only |
| 2026-11-26 | Windows `.exe` built by GitHub Actions, not committed to Git | PyInstaller can't cross-compile from macOS; binaries bloat the repo | Commit the `.exe`; build on the work laptop |
| 2026-11-26 | Tasks parsed deterministically (no AI) | `[ ]`/`[X]` + folder date is structured data | LLM extraction |
| 2026-11-26 | Python 3.12 | Your choice | 3.11, 3.13 |
| 2026-11-26 | Accepted Anaconda ToS for `defaults` | Your choice | conda-forge |
| 2026-11-26 | secondBrain paused | Your choice, to focus on this project | Run both in parallel |
| 2026-11-26 | Plan approved; desktop stack **A**: FastAPI + React/Tailwind in pywebview, PyInstaller on a GitHub Actions Windows runner | Best UI control; data/AI logic stays in Python | B (Flet), C (Tauri + Python sidecar) |
| 2026-11-26 | Node.js installed inside the conda env, not globally | One env per project rule | Homebrew global Node |
| 2026-11-26 | PyInstaller "onedir" (folder + exe), zipped for download | Faster start than one-file exe, which unpacks itself on every launch | `--onefile` |
| 2026-11-26 | Release via `gh release create` in the workflow | Uses the CLI already on GitHub runners; no third-party action | softprops/action-gh-release |
