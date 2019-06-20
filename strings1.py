def connect():
    sname=input('enter servername')
    dbname=input('enter dbname')
    uname=input('enter username')
    pas=input('enter paasword')
    return ("servername=%s;dbname=%s;username=%s;password=%s" %(sname,dbname,uname,pas))
print(connect())
