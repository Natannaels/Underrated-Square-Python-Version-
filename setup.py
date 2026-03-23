import cx_Freeze

executables = [cx_Freeze.Executable('inicializador.py')]

cx_Freeze.setup(
    name="underrated square",
    options={'build_exe': {'packages':['pygame'],
                           'include_files':['telas', 'Ost','level1.py','level2.py','level3.py', 'level4.py', 'level5.py', 'level6.py', 'screen_manager.py', 'fontpixel.ttf', 'campo.py', 'enemy.py', 'player.py']}},

    executables = executables
    
)