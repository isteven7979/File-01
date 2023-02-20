import xlwings as xw
#wb = xw.Book()
#app = xw.App(visible=True,add_book=False)
#wb = app.books.add()
#path = r"D:\EXERCISE_PY\B4\using app\\"
#for i in range(1,11):
#    if i == 2:
    #if i == 2 or i == 8:
        #continue
   # wb.save(path + str(i) + ".xlsx")
#for i in range(1,11):
#    wb.save(path + str(i) + ".xlsx")
#wb.close()
a = 10
b = 9
#print(a>11 or b>12)
#print(a>11 or b>12) -->False or False --> False
#print(a>9 or b>10)
#print(a>9 or b>10)---> True or False --> True
#print(a>9 or b>8)
#print(a>9 or b>8)--> True or True --> True
print (not((not a<9 or not b<8)))
#print (not(not((a<11 or b<8))))-->not (true or false)-->true