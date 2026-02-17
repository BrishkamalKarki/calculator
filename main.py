import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout
from PyQt6.QtGui import QIcon
from input_body import inputContainer
from ouput_body import outputContainer
from logic import buttons_clicked

class calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setStyleSheet("background-color: grey;")
        self.setWindowIcon(QIcon(r"icons\calculator"))
        self.master_layout: object = QVBoxLayout()
        self.upper_widget: object = outputContainer()
        self.screen_updater = buttons_clicked(self.upper_widget)
        self.lower_widget: object = inputContainer(self.screen_updater)
        # Adding the history panel and display screen as widget in main layout
        self.master_layout.addWidget(self.upper_widget)
        # Adding the widget of buttons in the master layout
        self.master_layout.addWidget(self.lower_widget)

        # For updating the screen size when the history box is shown  oand hidden
        self.upper_widget.his_button_widget.clicked.connect(self.update_window_size)

        self.central_widget: object = QWidget()
        self.master_layout.addStretch(1)
        self.central_widget.setLayout(self.master_layout)
        self.setCentralWidget(self.central_widget)

    def update_window_size(self):
        self.clk_his=self.upper_widget.click_history
        if self.clk_his is True:
            self.setFixedSize(360,687)
        if self.clk_his is False:
            self.setFixedSize(360,600)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator_window = calculator()
    calculator_window.resize(360,600)
    calculator_window.show()
    app.exec() 