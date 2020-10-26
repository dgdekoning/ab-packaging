# -*- coding: utf-8 -*-
import os
import sys

from activity_browser import run_activity_browser

# Add workaround for QtWebEngineProcess not being found.
if hasattr(sys, '_MEIPASS'):
    os.environ['QTWEBENGINEPROCESS_PATH'] = os.path.normpath(os.path.join(
                sys._MEIPASS, 'PySide2', 'bin'
            ))

run_activity_browser()