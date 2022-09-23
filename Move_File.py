from importlib.resources import path
import os 
import shutil

pastaAtual = "C:\Users\fcmar\OneDrive\Downloads"
pastaNova = "C:\Users\fcmar\OneDrive\Documentos\Arquivos_Documentos"

list_of_files = os.listdir(pastaAtual)
print(list_of_files)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)
    print(name)
    print(extension)
    if extension == '':
        continue
    if extension in ['.txt', '.doc', '.docs', '.pdf']:
        path1 = pastaAtual + "/" + file_name
        path2 = pastaNova + "/" + "Arquivos_Imagem"
        path3 = pastaNova + "/" + "Arquivos_Imagem" + "/" + file_name
        if os.path.exists(path2):
            print("Movendo" + file_name + "....")
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Movendo" + file_name + ".....")
            shutil.move(path1, path3)