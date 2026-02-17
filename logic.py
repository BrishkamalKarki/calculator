import math
import re

class buttons_clicked():

    def __init__(self,pointer_of_display_screen):
        self.pointer_of_display_screen = pointer_of_display_screen
        self.is_pos = True
        self.temp_exp_for_10power = False
        self.is_pos_var_a = True
        self.is_pos_var_b = True
        self.is_pos_var_c = True
        self.is_pos_ang = True
        self.rad_state = False
        self.count_qad = 0
        self.var_a, self.var_b, self.var_c = "", "", ""
        self.quad_a, self.quad_b, self.quad_c = "", "", ""
        self.trig_mode = "OFF"
        self.prev_trig_val = ""
        self.expression = ""
        self.result = ""
        self.dummy_expression = ""
        self.spec_used_list = []
        self.nums_aft_fac = []

    def deg_rad(self, value: int, rad_state):
        self.value = value
        self.rad_state = rad_state
        if self.count_qad == 0:
            if self.expression == "" and self.result == "":
                self.pointer_of_display_screen.update_dis_widget("", "", self.rad_state)
            elif self.result == "":
                self.pointer_of_display_screen.update_dis_widget(self.expression, "", self.rad_state)
            else:
                self.pointer_of_display_screen.update_dis_widget(self.expression, self.result, self.rad_state)

    def quad_simp(self, value: int or str):
        # FOR THE BUTTONS OF THE LOWER SECTION
        self.value = value
        self.dict_down_button_values = {
            1: 7, 2: 8, 3: 9, 4: "del", 5: "ac",
            6: 4, 7: 5, 8: 6, 9: "×", 10: "/",
            11: 1, 12: 2, 13: 3, 14: "+", 15: "-",
            16: 0, 17: ".", 18: "×10ˣ", 19: "neg", 20: "=", 21: "deg/rad",
            22: "quad"
            }
        # FOR THE BUTTONS OF THE UPPER TOP SECTION
        self.dict_upper_button_values = {
            24: "MOD", 25: "n!", 26: "nCr", 27: "nPr", 28: "ln",
            29: "x²", 30: "xʸ", 31: "√x", 32: "³√x", 33: "log",
            34: "%", 35: "(", 36: ")", 37: "π", 38: "e"
            }
        self.spec_num_aft_list = [9, 10, 14, 15]



        self.trig_modes = ["sin", "cos", "tan", "csc", "sec", "cot", "arcsin", "arccos", "arctan"]
        self.valid_buttons = [1, 2, 3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]
        self.meth_valid_buttons = [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]
        self.valid_numbers = [1, 2, 3, 6, 7, 8, 11, 12, 13, 16, 17]
        self.valid_numbers_for_quad = [1, 2, 3, 6, 7, 8, 11, 12, 13, 16, 17]
        self.valid_buttons_for_quad = [1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 16, 17, 4, 5, 19, 20, 22]
        self.dict_trig_modes = {
            "sin": math.sin, "cos": math.cos, "tan": math.tan, "csc": math.sin,
            "sec": math.cos, "cot": math.tan, "arcsin": math.asin,
            "arccos": math.acos, "arctan": math.atan
            }

        # CASE FOR QUADRATIC EQUATION
        if self.count_qad == 1 or self.count_qad == 2 or self.count_qad == 3 or self.count_qad == 4:
            if self.value in self.valid_numbers_for_quad:
                if self.count_qad == 1:
                    self.var_a = str(self.dict_down_button_values[self.value])
                elif self.count_qad == 2:
                    self.var_b = str(self.dict_down_button_values[self.value])
                elif self.count_qad == 3:
                    self.var_c = str(self.dict_down_button_values[self.value])
            if self.value == 4:
                if self.count_qad == 1:
                        self.var_a = self.var_a[0:len(self.var_a)-1]
                elif self.count_qad == 2:
                        self.var_b = self.var_b[0:len(self.var_b)-1]
                elif self.count_qad == 3:
                        self.var_c = self.var_c[0:len(self.var_c)-1]

            if self.value in self.valid_buttons_for_quad:
                self.calculate()

        # CASE FOR THE TRIGNOMETRIC MODES
        elif self.value in self.trig_modes:
            if self.trig_mode == "OFF":
                self.trig_mode = "ON"
                self.expression =  self.value + "(" + ")"
                self.trig = self.value
        elif self.trig_mode == "ON":
            pass

        # CASE FOR SIMPLE CALCULATION 
        elif self.value in self.valid_buttons:
            if self.value in self.meth_valid_buttons:
                if self.value == 24:
                    self.expression = self.expression + str(self.dict_upper_button_values[self.value])

                elif self.value == 25 and self.expression != "":
                    self.expression = self.expression + "!"
    
                elif self.value == 26 and self.expression != "":
                    self.expression = self.expression + "C"

                elif self.value == 27 and self.expression != "":
                    self.expression = self.expression + "P"

                elif self.value == 28:
                    self.expression = self.expression + "ln("
                
                elif self.value == 29:
                    self.expression = self.expression + "^2"

                elif self.value == 30:
                    self.expression = self.expression + "^("
            
                elif self.value == 31:
                    self.expression = self.expression + "√("

                elif self.value == 32:
                    self.expression = self.expression + "³√("
                
                elif self.value == 33:
                    self.expression = self.expression + "log("

                elif self.value == 34 and self.expression != "":
                    self.expression = self.expression + "%"

                elif self.value == 35:
                    self.expression = self.expression + "("

                elif self.value == 36:
                    self.expression = self.expression + ")"
                    self.temp_prev_expression = self.expression

                elif self.value == 37:
                    self.expression = self.expression + "π"
                
                elif self.value == 38 :
                    self.expression = self.expression + "e"

                self.temp_prev_expression = self.expression
                self.spec_used_list.append(self.value)


            else:
                self.expression = self.expression + str(self.dict_down_button_values[self.value])
                self.temp_prev_expression = self.expression

        # CASE FOR THE POSITIVE TO NEGATIVE AND VICE-VERSA
        elif self.value == 19:
            if self.is_pos is False:
                self.expression = self.temp_prev_expression
                self.is_pos = True
            elif self.is_pos is True:
                self.expression = "-("+self.expression+")"
                self.is_pos = False

        #  CASE FOR THE BACKSPACE 
        elif self.value == 4: 
            self.expression = self.expression[0:len(self.expression)-1]
            self.temp_prev_expression = self.expression
            self.result = ""
            self.dummy_expression = ""

        #  CASE FOR THE CLEAR SCREEEN
        elif self.value == 5:
            self.expression = ""
            self.result = ""
            self.dummy_expression = ""
            self.spec_used_list = []

        # CASE FOR THE 10 POWER X
        elif self.value == 18:
            self.expression = self.expression+"E"
            self.temp_exp_for_10power = "E"
            self.nums_after_e = ""

        if self.count_qad != 1 and self.count_qad != 2 and self.count_qad != 3 and self.count_qad != 4:
            self.calculate()

    """----------------------------------------------------------------------------------------------------------------------"""

    def calculate(self):
        self.result = ""

        # STARTING FROM SOLVING THE QUADRATIC PART
        if self.value == 22:
            self.count_qad = 1
            self.expression = "ax² + bx + c = 0"
            self.result = "a=  "
            self.list_delete = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

            if self.count_qad == 1 or self.count_qad == 2 or self.count_qad == 3:
                self.quad_a, self.quad_b, self.quad_c = "", "", ""
                self.temp_prev_var_a, self.temp_prev_var_b, self.temp_prev_var_c = "", "", ""
                self.count_qad == 0

        elif self.count_qad == 1:
            self.expression = "ax² + bx + c = 0"
            if self.value == 20: # WHEN = IS CLICKED
                self.count_qad = 2 
                self.expression = f"{self.quad_a}x² + bx + c = 0"
                self.result = "b=  "

            else:
                # POSITIVE TO NEGATIVE AND VICE-VERSA
                if self.value == 19 and self.quad_a != "": 
                    if self.is_pos_var_a is False: 
                        self.quad_a = self.temp_prev_var_a
                        self.is_pos_var_a = True 
                    elif self.is_pos_var_b is True: 
                        self.quad_a = "-("+self.quad_a+")"
                        self.is_pos_var_a = False
                else:
                    self.quad_a = self.quad_a + self.var_a
                    self.temp_prev_var_a = self.quad_a

                # BACKSPACE
                if self.value == 4:
                    for items in self.list_delete:
                        if items in self.quad_a:
                            self.clear = True
                            break
                        else:
                            self.clear = False
                    if self.clear is True:
                        self.quad_a = self.quad_a[0:len(self.quad_a)-1] 
                    
                self.result = "a="+str(self.quad_a)
                # CLEAR THE DISPLAY
                if self.value == 5:
                    self.expression = ""
                    self.result = ""
                    self.quad_a = ""
                    self.count_qad = 0
                    self.temp_prev_var_a = ""

        elif self.count_qad == 2: 
            self.expression = f"{self.quad_a}x² + bx + c = 0"
            if self.value == 20: # WHEN = IS CLICKED
                self.count_qad = 3
                self.expression = f"{self.quad_a}x² + {self.quad_b}x + c = 0"
                self.result = "c=  "
            else:
                # POSITIVE TO NEGATIVE AND VICE-VERSA
                if self.value == 19 and self.quad_b != "": 
                    if self.is_pos_var_b is False: 
                        self.quad_b = self.temp_prev_var_b
                        self.is_pos_var_b = True
                    elif self.is_pos_var_b is True: 
                        self.quad_b = "-("+self.quad_b+")"
                        self.is_pos_var_b = False
                else:
                    self.quad_b = self.quad_b + self.var_b
                    self.temp_prev_var_b = self.quad_b

                # BACKSPACE
                if self.value == 4:
                    for items in self.list_delete:
                        if items in self.quad_a:
                            self.clear = True
                            break
                        else:
                            self.clear = False
                    if self.clear:
                        self.quad_b = self.quad_b[0:len(self.quad_b)-1] 
                self.result = "b="+str(self.quad_b)

                # CLEAR THE DISPLAY
                if self.value == 5:
                    self.expression = ""
                    self.result = ""
                    self.quad_b = ""
                    self.count_qad = 0
                    self.quad_a = ""
                    self.temp_prev_var_b = ""

        elif self.count_qad == 3:
            self.expression = f"{self.quad_a}x² + {self.quad_b}x + c = 0"
            if self.value == 20: # WHEN = IS CLICKED
                self.count_qad = 4
                self.expression = f"{self.quad_a}x² + {self.quad_b}x + {self.quad_c} = 0"
                a = str(self.quad_a)
                b = str(self.quad_b)
                c = str(self.quad_c)
                try:
                    num_a, num_b, num_c = eval(a), eval(b), eval(c)
                    if num_a == 0:
                        if num_b != 0:
                            self.x_1 = round(-num_c / num_b, 2)
                            self.result = f"x = {self.x_1:g}"
                        else:
                            self.result = "invalid eqn"
                    else:
                        d = num_b**2 - 4*num_a*num_c                        
                        if d < 0:
                            real_part = round(-num_b / (2 * num_a), 2)
                            imag_part = round((abs(d)**0.5) / (2 * num_a), 2)
                            self.result = f"x = {real_part:g}+{imag_part:g}i, {real_part:g}-{imag_part:g}i"
                            self.result = self.result.replace("i", "j")
                        else:
                            self.x_1 = str(round((-num_b + d**0.5) / (2 * num_a), 2))
                            self.x_2 = str(round((-num_b - d**0.5) / (2 * num_a), 2))
                            self.result = f"x = {float(self.x_1):g}, {float(self.x_2):g}"                
                except Exception:
                    self.result = "error"
            
            else:
                # POSITIVE TO NEGATIVE AND VICE-VERSA
                if self.value == 19 and self.quad_c != "": 
                    if self.is_pos_var_c is False: 
                        self.quad_c = self.temp_prev_var_c
                        self.is_pos_var_c = True
                    elif self.is_pos_var_c is True: 
                        self.quad_c = "-("+self.quad_c+")"
                        self.is_pos_var_c = False
                else:
                    self.quad_c = self.quad_c + self.var_c
                    self.temp_prev_var_c = self.quad_c

                # BACKSPACE
                if self.value == 4:
                    for items in self.list_delete:
                        if items in self.quad_c:
                            self.clear = True
                            break
                        else:
                            self.clear = False
                    if self.clear:
                        self.quad_c = self.quad_c[0:len(self.quad_c)-1]
                self.result = "c="+str(self.quad_c)

                # CLEAR THE SCREEN
                if self.value == 5:
                    self.expression = ""
                    self.result = ""
                    self.quad_c = ""
                    self.count_qad = 0
                    self.quad_a = ""
                    self.quad_c = ""
                    self.temp_prev_var_c = ""

        elif self.count_qad == 4:
            if self.value == 5:
                self.expression = ""
                self.result = ""
                self.quad_c = ""
                self.count_qad = 0
                self.quad_a = ""
                self.quad_b = ""

        # EVALUATES THE TRIGNOMETRIC VALUE
        elif self.trig_mode == "ON":
            # CLEAR THE SCREEN
            if self.value == 5:
                self.expression = ""
                self.result = ""
                self.trig_mode = "OFF"
                self.prev_trig_exp = ""
                self.prev_trig_val = ""
                self.trig = ""

            # EVALUATING THE ANSWER
            if self.value == 20:
                    self.fac_n = 0
                    try:
                        if self.trig != "arcsin" and self.trig != "arccos" and self.trig != "arctan":
                            if self.rad_state is False:
                                # GETTING THE RADIAN
                                self.temp_trig = self.prev_trig_val
                                self.trig_ang = float(self.temp_trig)*math.pi/180
                            else:
                                self.trig_ang = self.prev_trig_val

                            if self.trig == "csc" or self.trig == "sec" or self.trig == "cot":
                                self.result = (1/(self.dict_trig_modes[self.trig](float(self.trig_ang))))
                            else:
                                self.result = (self.dict_trig_modes[self.trig](float(self.trig_ang)))

                        else:
                            self.trig_ang = self.prev_trig_val
                            self.result = (self.dict_trig_modes[self.trig](float(self.trig_ang)))
                            # CONVEERTING TO DEGREE
                            if self.rad_state is False:
                                self.result = (float(self.result)*180)/math.pi

                        if self.result is not int:
                            self.result = str(round(self.result, 4))
                        else:
                            self.result = str(self.result)
                    except Exception as e:
                        self.result = "Error"
            
            elif self.value in self.valid_numbers:
                if self.value == 17:
                    self.expression = self.trig + "(" + self.prev_trig_val + "." + ")"
                    self.prev_trig_val = self.prev_trig_val + "."
                    self.temp_trig_val = self.prev_trig_val 
                else:
                    self.expression = self.trig + "(" + self.prev_trig_val + str(self.dict_down_button_values[self.value]) + ")"
                    self.prev_trig_val = self.prev_trig_val + str(self.dict_down_button_values[self.value])
                    self.temp_trig_val = self.prev_trig_val
                self.prev_trig_exp = self.expression

            # BACKSPACE
            elif self.value == 4:
                self.prev_trig_val = self.prev_trig_val[0:len(self.prev_trig_val)-1]
                self.expression = self.trig + "(" + self.prev_trig_val + ")"
                self.temp_trig_val = self.prev_trig_val

            # POSITIVE TO NEGATIVE AND VICE-VERSA
            elif self.value == 19:
                if self.is_pos_ang is False:
                    self.expression = self.prev_trig_exp
                    self.prev_trig_val = self.temp_trig_val
                    self.is_pos_ang = True
                elif self.is_pos_ang is True: 
                    self.expression = self.trig + "(" + "-" + self.prev_trig_val + ")"
                    self.prev_trig_val = "-" + self.prev_trig_val
                    self.is_pos_ang = False

            elif self.value in self.dict_trig_modes:
                self.expression =  self.value + "(" + ")"
                self.trig = self.value
                self.result = ""
                self.prev_trig_val = ""
                self.temp_trig = ""
                self.temp_trig_val = ""

        # WHEN QUADRATIC PART IS NOT VALID AND TRIG MODE IS OFF
        elif self.value == 20 and self.expression != "":
                if self.spec_used_list:
                    self.dummy_expression = self.expression
                # CASE FOR THE FACTORIAL
                if 25 in self.spec_used_list:
                        self.factorial_nums = []
                        self.nums_aft_fac = []
                        self.fac_dict = {}
                        self.factorial_nums = re.findall(r'(\(?\-?\d+\.?\d*\)?)!', self.expression)
                        self.nums_aft_fac = re.findall(r'!(\.*\d*)', self.expression)
                        self.count_fac_num = 0
                        for self.fac_num in self.factorial_nums:
                            try:
                                    self.fac_value = math.factorial(int(self.fac_num))
                                    self.fac_exp = f"{self.fac_num}!"
                                    self.fac_dict[self.fac_exp] = self.fac_valu
                                    if self.nums_aft_fac:
                                        if self.nums_aft_fac[self.count_fac_num] not in ['', '-', '+', '/', '×']:
                                            self.fac_dict[self.fac_exp] = "error"
                                    self.count_fac_num+=1
                            except:
                                self.fac_exp = f"{self.fac_num}!"
                                self.fac_dict[self.fac_exp] = "error" 
                        for exp, val in self.fac_dict.items():
                            self.expression = self.expression.replace(exp, str(val).replace("e","E"))
                # CASE FOR COMBINATION
                if 26 in self.spec_used_list:
                        self.combination_nums = {}
                        self.comb_dict = {}
                        self.combination_nums = re.findall(r'\(?(\d*\.*\d*)C(\d*\.*\d*)\)?', self.expression)
                        for self.comb_num_bef, self.comb_num_aft in self.combination_nums:
                            try:
                                    self.comb_exp = f"{self.comb_num_bef}C{self.comb_num_aft}"
                                    self.comb_value = math.comb(int(self.comb_num_bef),int(self.comb_num_aft))
                                    self.comb_dict[self.comb_exp]= self.comb_value
                            except:
                                    self.comb_exp = f"{self.comb_num_bef}C{self.comb_num_aft}"
                                    self.comb_value = "error"
                                    self.comb_dict[self.comb_exp]= self.comb_value  
                        for exp, val in self.comb_dict.items():
                            self.expression = self.expression.replace(exp, str(val).replace("e","E"))
                # CASE FOR PERMUTATION
                if 27 in self.spec_used_list:
                        self.permutation_nums = {}
                        self.perm_dict = {}
                        self.permutation_nums = re.findall(r'\(?(\d+)P(\d+)\)?', self.expression)
                        for self.perm_num_bef, self.perm_num_aft in self.permutation_nums:
                            try:
                                    self.perm_exp = f"{self.perm_num_bef}P{self.perm_num_aft}"
                                    self.perm_value = math.perm(int(self.perm_num_bef),int(self.perm_num_aft))
                                    self.perm_dict[self.perm_exp]= self.perm_value
                            except:
                                    self.perm_exp = f"{self.perm_num_bef}P{self.perm_num_aft}"
                                    self.perm_value = "error"
                                    self.perm_dict[self.perm_exp]= self.perm_value  
                        for exp, val in self.perm_dict.items():
                            self.expression = self.expression.replace(exp, str(val).replace("e","E"))
                # CASE FOR ln    
                if 28 in self.spec_used_list:
                    self.ln_nums = []
                    self.ln_dict = {}
                    self.ln_nums = re.findall(r'ln\(([-+]?\d*\.*\d*π?e?)\)', self.expression)
                    for self.ln_num in self.ln_nums:
                        try:
                            self.ln_exp = f"ln({self.ln_num})"
                            self.ln_value = math.log(float(self.ln_num.replace("e",str(round(math.e, 4))).replace("π",str(round(math.pi, 2)))))
                            self.ln_dict[self.ln_exp] = str(self.ln_value)
                        except:
                            self.ln_exp = f"ln({self.ln_num})"
                            self.ln_value = "error"
                            self.ln_dict[self.ln_exp] = self.ln_value
                    for exp, val in self.ln_dict.items():
                        self.expression = self.expression.replace(exp, str(val).replace("e","E"))
                # CASE FOR POWER
                if 30 in self.spec_used_list:
                    self.pow_nums = {}
                    self.pow_dict = {}
                    self.pow_nums = re.findall(r'(\(*[-+]?\d*\.*\d*π?e?\)*)\^(\(*[+-]?\d*\.*\d*π?e?\)*)', self.expression)
                    for self.pow_num_bef, self.pow_num_aft in self.pow_nums:
                        try:
                            self.pow_exp = f"{self.pow_num_bef}^{self.pow_num_aft}"
                            self.pow_num_bef = str(self.pow_num_bef.replace("(","").replace(")","").replace("e",str(round(math.e, 4))).replace("π",str(round(math.pi, 2))))
                            self.pow_num_aft = str(self.pow_num_aft.replace("(","").replace(")","").replace("e",str(round(math.e, 4))).replace("π",str(round(math.pi, 2))))
                            self.pow_value = eval(f"{self.pow_num_bef}**{self.pow_num_aft}")
                            self.pow_dict[self.pow_exp] = str(self.pow_value)
                        except:
                            self.pow_exp = f"{self.pow_num_bef}^{self.pow_num_aft}"
                            self.pow_value = "error"
                            self.pow_dict[self.pow_exp] = self.pow_value
                    
                    for exp, val in self.pow_dict.items():
                        self.expression = self.expression.replace(exp, str(val).replace("e","E"))

                if 32 in self.spec_used_list:
                    self.cube_root_nums = []
                    self.cube_root_dict = {}
                    self.cube_root_nums = re.findall(r'³√\(*([+-]*\d*\.*\d*π?e?)\)*', self.expression)
                    for self.cube_root_num in self.cube_root_nums:
                        try:
                                self.cube_root_exp = f"³√({self.cube_root_num})"
                                self.cube_root_num = self.cube_root_num.replace("e",str(round(math.e, 4))).replace("π",str(round(math.pi, 2)))
                                self.cube_root_value =str(math.cbrt(float(self.cube_root_num)))
                                self.cube_root_dict[self.cube_root_exp] = str(self.cube_root_value)
                        except:
                                self.cube_root_exp = f"³√({self.cube_root_num})"
                                self.cube_root_value = "error"
                                self.cube_root_dict[self.cube_root_exp] = self.cube_root_value
                    for exp, val in self.cube_root_dict.items():
                        self.expression = self.expression.replace(exp, str(val).replace("e", "E").replace("e",str(round(math.e, 4))))

                if 31 in self.spec_used_list:
                    self.sq_root_nums = []
                    self.sq_root_dict = {}
                    self.sq_root_nums = re.findall(r'√\(?([-+]?\d*\.?\d*π?e?)\)?', self.expression)
                    for self.sq_root_num in self.sq_root_nums:
                        try:
                                self.sq_root_exp = f"√({self.sq_root_num})"
                                self.sq_root_num = self.sq_root_num.replace("e",str(round(math.e, 4))).replace("π",str(round(math.pi, 2)))
                                self.sq_root_value =str(math.sqrt(float(self.sq_root_num)))
                                self.sq_root_dict[self.sq_root_exp] = str(self.sq_root_value)
                        except:
                                self.sq_root_exp = f"√({self.sq_root_num})"
                                self.sq_root_value = "error"
                                self.sq_root_dict[self.sq_root_exp] = self.sq_root_value
                    for exp, val in self.sq_root_dict.items():
                        self.expression = self.expression.replace(exp, str(val).replace("e","E"))


                if 33 in self.spec_used_list:
                    self.log_nums = []
                    self.log_dict = {}
                    self.log_nums = re.findall(r'log\(([+-]?π?e?\d*\.*\d*)\)', self.expression)
                    for self.log_num in self.log_nums:
                        try:
                                self.log_exp = f"log({self.log_num})"
                                self.log_value = math.log10(float(self.log_num.replace("e",str(round(math.e, 4))).replace("π",str(round(math.pi, 2)))))
                                self.log_dict[self.log_exp] = str(self.log_value)
                        except:
                                self.log_exp = f"log({self.log_num})"
                                self.log_value = "error"
                                self.log_dict[self.log_exp] = self.log_value
                    for exp, val in self.log_dict.items():
                        self.expression = self.expression.replace(exp, str(val).replace("e", "E").replace("e",str(round(math.e, 4))))

                try:
                    self.result = eval(self.expression.replace("×","*").replace("^2","**2").replace("%", "*0.01").replace("MOD","%").replace("e",str(round(math.e, 4))).replace("π",str(round(math.pi, 2))))
                    if "+" in str(self.result):
                        self.result = str(self.result).replace("+","")
                    if isinstance(self.result, float):
                        self.result = round(self.result, 4)
                        if str(self.result)[-2:] == ".0":
                            self.result = int(self.result)
                        if len(str(self.result)) > 11 and self.result > 1:
                            self.result = f"{self.result:.2e}"
                        elif len(str(self.result)) > 12 and self.result < -1:
                            self.result = f"{self.result:.2e}"
                    else:
                        if len(str(self.result)) > 10 and self.result > 1:
                            self.result = f"{self.result:.0e}"
                        elif len(str(self.result)) > 11 and self.result < -1:
                            self.result = f"{self.result:.0e}"
                            
                    if "+" in str(self.result):
                        self.result = str(self.result).replace("+","")

                    if len(str(self.result)) > 99:
                        self.result = "error"

                    self.nums_error = []
                    pattern = r'(\d[πe\(]|[πe]\d|[πe][πe]|\d[πe]|\)[0-9πe])'
                    self.nums_error = re.findall(pattern, self.expression)
                    if self.nums_error:
                        self.result = "error"
                except:
                    self.result= "error"
                if self.spec_used_list:
                    self.expression = self.dummy_expression

        self.expression = str(self.expression).replace("Error", "error").replace("Eqn", "eqn")
        self.result = str(self.result).replace("e", "E").replace("Error", "error")
        if self.count_qad != 0:
            self.pointer_of_display_screen.update_dis_widget(self.expression, self.result, "DEG", True)
            if self.count_qad == 4:
                self.pointer_of_display_screen.dis_his(self.expression, self.result)
        else:
            self.pointer_of_display_screen.update_dis_widget(self.expression, self.result, self.rad_state, False)
            if self.result != "":
                self.pointer_of_display_screen.dis_his(self.expression, self.result)