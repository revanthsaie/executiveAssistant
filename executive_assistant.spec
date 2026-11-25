# PyInstaller build recipe. Run from the repo root AFTER `npm run build` in frontend/:
#     pyinstaller executive_assistant.spec --noconfirm
# Output: dist/ExecutiveAssistant/ (a folder with ExecutiveAssistant.exe + its libraries).
# "onedir" mode starts faster than a single-file exe, which unpacks itself on every launch.

a = Analysis(
    ["run_app.py"],
    pathex=["src"],
    datas=[("frontend/build", "frontend/build")],  # the built React UI, read via paths.frontend_dir()
    hiddenimports=[
        # uvicorn picks these by name at runtime, so PyInstaller can't see them statically.
        "uvicorn.logging",
        "uvicorn.loops.auto",
        "uvicorn.protocols.http.auto",
        "uvicorn.protocols.websockets.auto",
        "uvicorn.lifespan.on",
    ],
    excludes=["tkinter"],
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="ExecutiveAssistant",
    console=False,  # desktop app: no black console window
)
coll = COLLECT(exe, a.binaries, a.datas, name="ExecutiveAssistant")
