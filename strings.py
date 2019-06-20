def connect():
    sname=input('enter servername')
    dbname=input('enter dbname')
    uname=input('enter username')
    pas=input('enter paasword')
    return ("servername="+sname+";"+"dbname="+dbname+":"+"username="+uname+";"+"password="+pas)
print(connect())
