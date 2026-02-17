from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QListWidget, QTextEdit
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from styles import setOutputStyle

class outputContainer(QWidget):

    def __init__(self):
        super().__init__()

                # HISTORY BUTTON
        self.his_button_widget: object = QPushButton()
        self.his_button_widget.setIcon(QIcon("icons/history.png"))
        self.out_sheet_style=setOutputStyle()
        self.his_button_widget.setStyleSheet(self.out_sheet_style.history_button)

                # LIST OF THE PREVIOUS EXPRESSIONS
        self.his_list_widget: object = QListWidget()
        self.his_list_widget.setVisible(False)
        self.his_list_widget.setMaximumHeight(200)
        self.his_list_widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.his_list_widget.setStyleSheet(self.out_sheet_style.history_list)

                # DISPLAY SCREEN
        self.dis_widget: object = QTextEdit()
        self.dis_widget.setReadOnly(True) 
        self.dis_widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.dis_widget.setMaximumHeight(100)
        self.dis_widget.setStyleSheet(self.out_sheet_style.display_box)

                # CREATING THE LAYOUT CONTAINING HISTORY BUTTON, HISTORY LIST, DISPLAY SCREEN THAT IS CONTAINED BY THE QWIDGET
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.his_button_widget, alignment = Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.his_list_widget)
        self.layout.addWidget(self.dis_widget)
        self.layout.addStretch(1)

        self.his_button_widget.clicked.connect(self.history_clicked)
        self.click_history=False
        self.update_dis_widget("", "", "DEG", None)

            # DEFINING THE FUNCTIONS THAT IS CALLED WHEN THE SPECIFIC BUTTONS AND LIST EXPRESSION ARE CLICKED
    def history_clicked(self):
        if self.click_history is False:
            self.click_history=True
        else:
            self.click_history=False
        if self.click_history:
            self.his_list_widget.setVisible(True)
        else:
            self.his_list_widget.setVisible(False)

    def update_dis_widget(self, expression, result, mode, quad):
        # USING THE HTML CONTENT TO SET UP THE DISPLAY SCREEN PROPERTY
        if mode is True:
            mode = "RAD"
        else:
            mode = "DEG"
        if quad and 'j' in result:
            html_content_to_display = f"""
            <div style='text-align: left; font-size: 8px; color: #888888; margin-bottom: -10px; line-height: 0.2;'>
                    {mode}
            </div>
            <div style='text-align: right;'>
                <span style='font-size: 24px; color: #00FF41; ine-height: 1'>{expression.replace('j', 'i')}</span>
                <br>
                <span style='font-size: 22px; font-weight: bold;'>{result}</span>
            </div>
            """
                
        else:
            html_content_to_display = f"""
                <div style='text-align: left; font-size: 8px; color: #888888; margin-bottom: -10px; line-height: 0.2;'>
                        {mode}
                </div>
                <div style='text-align: right;'>
                    <span style='font-size: 24px; color: #00FF41; ine-height: 1'>{expression}</span>
                    <br>
                    <span style='font-size: 40px; font-weight: bold;'>{result}</span>
                </div>
            """
        self.dis_widget.setHtml(html_content_to_display)

    def dis_his(self, expression, results):
        self.his_list_widget.addItems([f"{expression} | Ans: {results.replace('j', 'i')}"])
