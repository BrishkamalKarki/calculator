
class setOutputStyle():

    def __init__(self):
        self.history_button="""
            QPushButton {
                border: none;
                padding: 8px;
                background-color: #ADAB9F; 
                border-radius: 5px
            }
            
            QPushButton:enabled {
                color: red; 
            }
            
            QPushButton:hover {
                background-color: #444444; 
                border-radius: 5px;
            }
        """

        self.history_list="""
            QListWidget {
                border: none;
                background-color: #2b2b2b; /* Dark background */
                border-radius: 5px;
                color: white; 
                font-family: 'Segoe UI';   
                font-size: 16px; 
                font-weight: bold;
            }

            QListWidget::item {
                background-color: transparent;
                padding: 3px;
                border-radius: 3px;
            }

            QListWidget::item:hover {
                background-color: #3d3d3d;
            }

            QListWidget::item:selected {
                background-color: #FFD700; /* Yellow */
                outline: none; 
                color: black;
            }
            """

        self.display_box="""
            QTextEdit {
                background-color: #353839;
                color: #F5F5DC;
                border: 2px solid #4B4E52;
                border-radius: 5px;
                padding: 2px 8px;
                font-family: 'Inter', sans-serif;
            }
        """

class setInputStyle():

    def __init__(self):
        self.modes_button="""
            QPushButton{
                background-color: white;
                color: grey;
                border: none;
                border-radius: 4px;
                font-family: 'Arial';
                font-size: 18px;
                min-width: 60px;
                font-weight: bold;
                min-height: 40px;
                }
            QPushButton:hover {
                background-color: #3D3D3D;
                border: none;
                }
            QPushButton::menu-indicator {
                subcontrol-origin: padding;
                subcontrol-position: right center;  /* horizontal vertical */
                width: 12px;
                height: 12px;
                right: 8px;
                }
            """

        self.modes_sheet="""
            QMenu {
                background-color: #2b2b2b;
                color: white;
                border: 1px solid #444;
                font-family: 'Inter', sans-serif;
                font-weight: bold;
                border-radius: 8px;
            }

            QMenu::item {
                padding: 5px 20px;
                background-color: transparent;
            }

            QMenu::item:selected {
                background-color: #FFD700;
                color: white;
            }

            QMenu::separator {
                height: 1px;
                background: #555;
                margin: 4px 10px;
            }
            """

        self.method_buttons_up="""
                        QPushButton{
                            background-color: #202121;
                            color: white;
                            border: 1px solid #3D3D3D;
                            border-radius: 4px;
                            font-family: 'Arial';
                            font-size: 18px;
                            min-width: 60px;
                            font-weight: bold;
                            min-height: 40px;
                            }
                        QPushButton:hover {
                            background-color: #C8C5B5;
                            color: #202121;
                            border: none;
                            font-weight: bold;
                            }
                    """

        self.method_buttons_down="""
                QPushButton{
                    background-color: #202121;
                    color: white;
                    border: 1px solid #3D3D3D;
                    border-radius: 4px;
                    font-family: 'Inter', sans-serif;
                    font-size: 18px;
                    min-width: 60px;
                    min-height: 40px;
                    font-weight: bold;
                    }
                QPushButton:hover {
                    background-color: #C8C5B5;
                    color: #202121;
                    border: none;
                    font-weight: bold;
                    }
            """

        self.numbers_buttons="""
                QPushButton{
                    background-color: white;
                    color: black;
                    border: none;
                    border-radius: 4px;
                    font-family: 'Inter', sans-serif;
                    font-size: 18px;
                    min-width: 60px;
                    min-height: 40px;
                    font-weight: bold;
                    }
                QPushButton:hover {
                    background-color: #3D3D3D;
                    border: none;
                    }
            """

        self.delete_clear_button="""
                        QPushButton{
                            background-color: #0A7DF7;
                            color: white;
                            border: none;
                            border-radius: 4px;
                            font-family: 'Inter', sans-serif;
                            font-size: 18px;
                            font-weight: bold;
                            min-width: 60px;
                            min-height: 40px;
                            }
                        QPushButton:hover {
                            background-color: #3D3D3D;
                            border: none;
                            }
                        """
