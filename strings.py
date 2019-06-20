def connect():
    sname=input('enter servername')
    dbname=input('enter dbname')
    uname=input('enter username')
    pas=input('enter paasword')
    return (sname+dbname+uname+pas)
print(connect())
