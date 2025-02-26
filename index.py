# -*- coding: latin-1 -*-
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QComboBox
import sys
import subprocess

class QAAutomationApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Automação de QA")
        self.setGeometry(100, 100, 500, 300)

        layout = QVBoxLayout()

        # ComboBox para selecionar o módulo
        self.module_selector = QComboBox()
        self.module_selector.addItems(["Módulo 1", "Módulo 2", "Módulo 3"])
        layout.addWidget(self.module_selector)

        # Botão para rodar os testes
        self.run_tests_btn = QPushButton("Rodar Testes")
        self.run_tests_btn.clicked.connect(self.run_tests)
        layout.addWidget(self.run_tests_btn)

        # Área de logs
        self.log_area = QTextEdit()
        self.log_area.setReadOnly(True)
        layout.addWidget(self.log_area)

        self.setLayout(layout)

    def run_tests(self):
        selected_module = self.module_selector.currentText()
        self.log_area.append(f"Executando testes no {selected_module}...\n")

        # Define qual script de teste rodar baseado no módulo escolhido
        module_tests = {
            "Módulo 1": "teste_modulo1.py",
            "Módulo 2": "teste_modulo2.py",
            "Módulo 3": "teste_modulo3.py"
        }

        script = module_tests.get(selected_module, "")
        
        if script:
            process = subprocess.run(["python", script], capture_output=True, text=True)
            self.log_area.append(process.stdout if process.stdout else "Nenhum output.\n")
            self.log_area.append(process.stderr if process.stderr else "Execução finalizada sem erros.\n")
        else:
            self.log_area.append("Erro: Script de teste não encontrado.\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QAAutomationApp()
    window.show()
    sys.exit(app.exec())