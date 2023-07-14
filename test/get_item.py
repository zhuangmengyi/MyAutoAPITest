from readExcel.readExcel import read_excel

print(read_excel('路径'))
print(read_excel('传参'))
data = list(zip(read_excel('路径'),read_excel('传参')))
print(data)

# a = [1,2,3]
# b = [4,5,6]
# c = [4,5,6,7,8]
# A = zip(a,b)     # 打包为元组的列表
#
# print(list(A))
