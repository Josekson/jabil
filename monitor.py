import time
import subprocess
import psutil
import os

# Lista de programas a monitorar
programas = [
    {
        "nome": "EXCEL.exe",
        "caminho": r"c:\Program Files\Microsoft Office\root\Office16\EXCEL.exe"
    },
    {
        "nome": "WINWORD.exe",
        "caminho": r"c:\Program Files\Microsoft Office\root\Office16\WINWORD.exe"
    },
    {
        "nome": "POWERPNT.exe",
        "caminho": r"c:\Program Files\Microsoft Office\root\Office16\POWERPNT.exe"
    }
]

# Verifica se o processo está em execução
def esta_em_execucao(nome_exe):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and proc.info['name'].lower() == nome_exe.lower():
            return True
    return False

# Tenta abrir o programa se ele não estiver rodando
def monitorar_programas():
    while True:
        for prog in programas:
            if not esta_em_execucao(prog["nome"]):
                try:
                    subprocess.Popen(prog["caminho"])
                    print(f"{prog['nome']} foi reiniciado.")
                except Exception as e:
                    print(f"Erro ao tentar iniciar {prog['nome']}: {e}")
        time.sleep(5)

if __name__ == "__main__":
    monitorar_programas()
