# -*- mode: python ; coding: utf-8 -*-
import os
import importlib

block_cipher = None

ab_root = os.path.dirname(importlib.import_module('activity_browser').__file__)
bw2io_root = os.path.dirname(importlib.import_module('bw2io').__file__)

data_files = [
    (os.path.join(ab_root, 'icons'), 'activity_browser\\icons'),
    (os.path.join(ab_root, 'app\\ui\\web'), 'activity_browser\\app\\ui\\web'),
    (os.path.join(bw2io_root, 'data'), 'bw2io\\data')
]

a = Analysis(['run-activity-browser.py'],
             pathex=[],
             binaries=[],
             datas=data_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=["PyQt5"],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='activity-browser',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               name='activity-browser')
