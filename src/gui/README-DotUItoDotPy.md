# How to make valid .py files from .ui files?

The .ui files in this directory can be converted to .py files:
- `pyuic6 -x dict_chooser.ui -o ui_dict_chooser.py`
- `pyuic6 -x dicts_setting.ui -o ui_dicts_setting.py`
- `pyuic6 -x options.ui -o ui_options.py`

However a few changes must be done before they can fully work with Anki. First you need to remove any importation of PyQt5 or PyQt6. In our case QtWidgets, QtCore and QtGui are imported. This is not needed because Anki itself has any Qt object you may need. For example, instead of "QtWidgets.QSizePolicy" (or any other object for that matter) QSizePolicy can directly be imported from "aqt.qt".

Because objects in python files generated from .ui files, all exist in aqt.qt, you just need to is to remove any mention of "QtWidgets.", "QtCore." and "QtGui." and add the line below to your file:
`from aqt.qt import *`
