# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['app\\ProximaManager.py'],
    pathex=[],
    binaries=[],
    datas=[('app/gui', 'gui'), ('app/logic', 'logic'), ('assets/fonts/TechNoir-8dLD.ttf', 'assets/fonts'), ('assets/icons/iconPass.ico', 'assets/icons'), ('assets/img/account-protection.png', 'assets/img'), ('assets/img/cyber.png', 'assets/img'), ('assets/img/login-.png', 'assets/img'), ('assets/img/logout.png', 'assets/img'), ('assets/img/magnifying-glass.png', 'assets/img'), ('assets/img/settings.png', 'assets/img')],
    hiddenimports=['tkinter.ttk', 'tkinter.messagebox', 'ctypes', 'PIL', 'PIL.Image', 'PIL.ImageTk', 'mysql.connector'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='ProximaManager',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['assets\\icons\\iconPass.ico'],
)
