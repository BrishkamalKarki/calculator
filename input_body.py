from PyQt6.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication, QHBoxLayout, QVBoxLayout, QMenu
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize, Qt
from styles import setInputStyle

class inputContainer(QWidget):
    def __init__(self, pointer_of_screen_updater):
        super().__init__()
        # THIS IS THE MAIN GRID LAYOUT
        self.main_grid_layout = QGridLayout(self)
        self.upper_top1_layout = QGridLayout()
        self.upper_top_layout = QGridLayout()
        self.upper_down_grid_layout = QGridLayout()
        self.lower_grid_layout = QGridLayout()
        self.in_style_sheet = setInputStyle()
        self.pointer_of_screen_updater = pointer_of_screen_updater
        self.rad_state = False
        self.upperTopGridLayout()


    def upperTopGridLayout(self):
        self.rad_button = QPushButton()
        self.rad_button.setText("RAD")
        self.qad_button = QPushButton("QAD")
        self.trig_button = QPushButton("TRIG")
        self.trig_button.setIcon(QIcon(r"icons\right_angled_triangle"))
        self.trig_button.setIconSize(QSize(24,24))
        self.trig_button.setFixedSize(130,36)
        self.setStyleModes()

        # SETTING THE MENUS
        self.act_ = self.trig_menu = QMenu()
        self.act_sin = self.act_ = self.trig_menu.addAction("sin")
        self.act_cos = self.trig_menu.addAction("cos")
        self.act_tan = self.trig_menu.addAction("tan")
        self.act_csc = self.trig_menu.addAction("csc")
        self.act_sec = self.trig_menu.addAction("sec")
        self.act_cot = self.trig_menu.addAction("cot")
        self.act_arcsin = self.trig_menu.addAction("arcsin")
        self.act_arccos = self.trig_menu.addAction("arccos")
        self.act_arctan = self.trig_menu.addAction("arctan")
        self.trig_button.setMenu(self.trig_menu)
        self.setStyleMenu()

        self.upper_top1_layout.addWidget(self.rad_button, 0, 0)
        self.upper_top1_layout.addWidget(self.qad_button, 0, 1)
        self.upper_top_layout.addLayout(self.upper_top1_layout, 0, 0)
        self.upper_top_layout.addWidget(self.trig_button, 1, 0)
        self.main_grid_layout.addLayout(self.upper_top_layout, 0, 0, alignment=Qt.AlignmentFlag.AlignLeft)

        # CONNECTING THE RADIOBUTTONS WITH THE FUNCTION
        self.rad_button.clicked.connect(self.rad_deg_updater)
        self.rad_button.clicked.connect(lambda checked, index = 21 : self.pointer_of_screen_updater.deg_rad(index, self.rad_state))
        self.qad_button.clicked.connect(lambda checked, index = 22 : self.pointer_of_screen_updater.quad_simp(index))
        self.act_sin.triggered.connect(lambda checked, index = "sin" : self.pointer_of_screen_updater.quad_simp(index))
        self.act_cos.triggered.connect(lambda checked, index = "cos" : self.pointer_of_screen_updater.quad_simp(index))
        self.act_tan.triggered.connect(lambda checked, index = "tan" : self.pointer_of_screen_updater.quad_simp(index))
        self.act_csc.triggered.connect(lambda checked, index = "csc" : self.pointer_of_screen_updater.quad_simp(index))
        self.act_sec.triggered.connect(lambda checked, index = "sec" : self.pointer_of_screen_updater.quad_simp(index))
        self.act_cot.triggered.connect(lambda checked, index = "cot" : self.pointer_of_screen_updater.quad_simp(index))
        self.act_arcsin.triggered.connect(lambda checked, index = "arcsin" : self.pointer_of_screen_updater.quad_simp(index))
        self.act_arccos.triggered.connect(lambda checked, index = "arccos" : self.pointer_of_screen_updater.quad_simp(index))
        self.act_arctan.triggered.connect(lambda checked, index = "arctan" : self.pointer_of_screen_updater.quad_simp(index))
        self.upperDownGridLayout()

    def rad_deg_updater(self):
        if self.rad_state is False:
            self.rad_button.setText("DEG")
            self.rad_state = True 
        else: 
            self.rad_button.setText("RAD")
            self.rad_state = False

    def upperDownGridLayout(self):
        upper_button_texts_list = ["MOD","n!","nCr","nPr","ln","x²","xʸ","√x","³√x","log","%","(",")","π","e"]
        self.dict_for_upper_buttons = {}
        for self.upper_button_index in range(24,39):
            self.dict_for_upper_buttons[self.upper_button_index] = QPushButton(f"{upper_button_texts_list[self.upper_button_index-24]}")
        self.upper_button_num = 24

        for self.row_up in range(3):
            for self.column_up in range(5):
                self.setStyleUp()
                self.upper_down_grid_layout.addWidget(self.dict_for_upper_buttons[self.upper_button_num],self.row_up,self.column_up) 
                self.upper_button_num+=1

        self.main_grid_layout.addLayout(self.upper_down_grid_layout,1,0)

        for self.nums, self.buttons in self.dict_for_upper_buttons.items(): 
            self.buttons.clicked.connect(lambda checked, index = self.nums : self.pointer_of_screen_updater.quad_simp(index))

        self.lowerGridLayout()

    def lowerGridLayout(self):
        self.lower_buttons_text_list = ["7","8","9","DEL","AC","4","5","6","×","/","1","2","3","+","-","0",".","×10ˣ","+/-","="]
        self.dict_for_lower_buttons = {}
        for self.lower_button_index in range(20):
            self.dict_for_lower_buttons[self.lower_button_index+1] = QPushButton(f"{self.lower_buttons_text_list[self.lower_button_index]}")

        self.lower_button_number = 1
        for self.row_down in range(4):
            for self.column_down in range(5):
                self.setStyleDown()
                self.lower_grid_layout.addWidget(self.dict_for_lower_buttons[self.lower_button_number],self.row_down,self.column_down)
                self.lower_button_number+=1
        self.main_grid_layout.addLayout(self.lower_grid_layout,2,0)

        # CONNECTING THE FUNCTION WHEN THE SPECIFIC BUTTON IS CLICKED
        for self.nums, self.buttons in self.dict_for_lower_buttons.items():
            self.buttons.clicked.connect(lambda checked, index = self.nums : self.pointer_of_screen_updater.quad_simp(index))

    # SETTING UP THE STYLES PROPERTIES FOR ALL THE WIDGETS
    def setStyleUp(self):
        if self.row_up == 0 or self.row_up == 1:
                    self.dict_for_upper_buttons[self.upper_button_num].setStyleSheet(self.in_style_sheet.method_buttons_up)
        else:
            self.dict_for_upper_buttons[self.upper_button_num].setStyleSheet(self.in_style_sheet.method_buttons_down)

    def setStyleDown(self):
        if self.row_down == 0 and (self.column_down == 3 or self.column_down == 4):
                self.dict_for_lower_buttons[self.lower_button_number].setStyleSheet(self.in_style_sheet.delete_clear_button)
        else:
            self.dict_for_lower_buttons[self.lower_button_number].setStyleSheet(self.in_style_sheet.numbers_buttons)

    def setStyleModes(self):
        list_of_modes=[self.trig_button,self.qad_button,self.rad_button]
        for buttons_mode in list_of_modes:
            buttons_mode.setStyleSheet(self.in_style_sheet.modes_button)

    def setStyleMenu(self):
        self.act_ = self.trig_menu.setStyleSheet(self.in_style_sheet.modes_sheet)
