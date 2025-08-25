file_names = {elem: elem for elem in input("Введите названия файлов через пробел:").split()}
#file_names = ['file1.zip', 'main.py', 'ald.msi', 'isoft.cool', 'itransitiongal.era', 'ne.ver.gonna', 'give.u','u.p', 'never.gonna', 'l.et.u', 'do.w.n']
print(sorted(file_names, key=lambda string: (string[string.rfind('.'):], string[:string.rfind('.')])))
