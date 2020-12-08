import datetime
print("本日は、", datetime.date.today(),"です。")
ol = datetime.date(2020, 7, 24)
print("東京オリンピックは", ol , "です。")
t = datetime.date.today()
print("本日は、", t.month,"月",t.day,"日です。")
print("本日は、{0:02d}月{1:02d}日です。".format(t.month, t.day)