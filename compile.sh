python -m PyInstaller --console --onefile --name Bane-Of-Wargs source/main.py source/battle.py source/check_yaml.py source/colors.py source/map_item.py source/train.py source/logger_sys.py --add-data yamale/VERSION:yamale --collect-submodules fsspec
