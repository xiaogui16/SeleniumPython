#coding=utf-8
import sys
sys.path.append("E:/SELENIUMPYTHON")
from util.excel_util import ExcelUtil
from keywordselenium.actionMethod import ActionMethod
import time
class KeywordCase:
    def run_main(self):
        self.action_method = ActionMethod()
        handle_excel = ExcelUtil("E:/SELENIUMPYTHON/config/keyword.xls")
        case_line = handle_excel.get_lines()
        if case_line:
            for i in range(1,case_line):
                is_run = handle_excel.get_col_value(i,3)
                print("is_run",is_run)
                if is_run == 'yes':
                    method = handle_excel.get_col_value(i,4)
                    print("method",method)
                    send_value = handle_excel.get_col_value(i,5)
                    print("send_value",send_value)
                    hand_value = handle_excel.get_col_value(i,6)
                    print("hand_value",hand_value)
                    except_result_method = handle_excel.get_col_value(i,7)
                    print("except_result_method",except_result_method)
                    except_result = handle_excel.get_col_value(i,8)
                    print("except_result",except_result)
                    #''而不是None
                    #if send_value:
                    self.run_method(method,send_value,hand_value)
                    if except_result != '':
                        except_value = self.get_except_result_value(except_result)
                        print("except_value",except_value)
                        if except_value[0] == 'text':
                            result = self.run_method(except_result_method)
                            print("result",result)
                            if except_value[1] in result:
                                print("1")
                                handle_excel.write_value(i,'pass')
                                print('3')
                            else:
                                print("2")
                                handle_excel.write_value(i,'fail')
                        elif except_value[0] == 'element':
                            result = self.run_method(except_result_method,except_value[1])
                            if result:
                                handle_excel.write_value(i,'pass')
                            else:
                                handle_excel.write_value(i,'fail')
                        else:
                            print("没有else")
                    else:
                        print("预期结果为空")
    #获取预期结果值
    def get_except_result_value(self,data):
        return data.split("=")

   
    def run_method(self,method,send_value='',handle_value=''):
        #返回对象的方法
        method_value = getattr(self.action_method,method)
        print("method_value",method_value)
        if send_value == '' and handle_value != '':
           result = method_value(handle_value)
        elif send_value != '' and handle_value != '':
            result = method_value(send_value,handle_value)
        elif send_value !='' and handle_value == '':
            result = method_value(send_value)
        else:
            result = method_value()
        return result

if __name__ == '__main__':
    test = KeywordCase()
    test.run_main()
