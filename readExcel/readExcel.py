import xlrd

# 读取excel文件
test_workbook = xlrd.open_workbook("../testCases/test.xlsx")
user_workbook = xlrd.open_workbook("../testCases/user.xlsx")

# 获取第一个sheet表

user_table = user_workbook.sheets()[0]

# 遍历该表，使用nrows代表行，ncols代表列
def read_excel(item, sheet):
    test_table = test_workbook.sheets()[sheet]
    item_col = 0
    value = []
    for i in range(test_table.nrows):
        for j in range(test_table.ncols):
            # 利用cell_value获得指定行列单元格的值
            if test_table.cell_value(i, j) == item:
                # 用一个值来保存该列的列数
                item_col = j
            # 获取路径这一列的值
            if j == item_col and i != 0:
                value.append(test_table.cell_value(i, j))
    return value

def chose_role(item, role): # 根据role选取要登录哪个管理员角色，获取该角色的登录信息并返回
    item_col = 0
    role_row = 0
    value = []
    for i in range(user_table.nrows): # 找到角色对应的行数
        for j in range(user_table.ncols):
            # 利用cell_value获得指定行列单元格的值
            if user_table.cell_value(i, j) == item:
                # 用一个值来保存该列的列数
                item_col = j
            # 获取路径这一列的值
            if j == item_col and user_table.cell_value(i, j) == role:
                role_row = i
    for i in range(user_table.nrows): #返回找到角色值的行对应的数据
        for j in range(user_table.ncols):
            if i == role_row:
                value.append(user_table.cell_value(i, j))
    return value

if __name__ == '__main__':
    # lujin = read_excel('路径')
    # json = read_excel('传参')
    # print(lujin)
    # print(json)
    guanli = chose_role('角色', 1)
    print(guanli)