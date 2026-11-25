# Changelog

All notable changes per milestone release. Format: Added / Changed / Fixed.

## [Unreleased]

## [v0.0.1] — 2026-11-26 — M0 test build
First Windows build, released early so the `.exe` can be tested on the work laptop (M0 de-risk spike).

### Added
- Desktop launcher: FastAPI backend on a free `127.0.0.1` port, shown in a pywebview window.
- React 19 + Tailwind 4 hello screen that checks the backend (`/api/health`).
- PyInstaller build recipe (`executive_assistant.spec`, onedir).
- GitHub Actions workflow that builds the Windows app and publishes a Release on `v*` tags.
- Project docs: plan, decisions, progress, lessons; conda env with Python 3.12, Node and `gh`.
