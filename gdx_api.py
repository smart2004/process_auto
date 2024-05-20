import gdxcc
# Открытие файла GDX
gdx_handle = gdxcc.gdxOpen("example.gdx", "r")
# Получение параметра из файла GDX
param_name = "demand"
values = gdxcc.gdxDataReadStr(gdx_handle, param_name)
print(f"Values of parameter {param_name}: {values}")
# Закрытие файла GDX
gdxcc.gdxClear(gdx_handle)