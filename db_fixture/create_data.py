f = open("data_test.sql", 'w')


try:
    for i in range(1, 1000):
        str_i = str(i)
        real_name = "alex" + str_i
        phone = 1780000000 + i
        email = "alex" + str_i +"@mail.com"
        sql = 'INSERT INTO sign_guest (id,real_name, phone, email, sign, event_id) VALUES ' \
              '('+str_i+',"'+real_name+'", '+str(phone)+', "'+email+'", 0, 1);'
        f.write(sql)
        f.write("\n")

except:
    print("数据新建失败。")


f.close()