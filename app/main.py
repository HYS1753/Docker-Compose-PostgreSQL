import os
from pgsqltool import Pgsqltool


def test():
    print(os.environ.get('pgsdbname', ''))
    print(os.environ.get('pgsdbuser', ''))
    print(os.environ.get('pgspassword', ''))
    print(os.environ.get('pgshost', ''))
    print(os.environ.get('pgsport', ''))

def main():
    dbname = os.environ.get('pgsdbname', '')
    user = os.environ.get('pgsdbuser', '')
    passwd = os.environ.get('pgspassword', '')
    host = os.environ.get('pgshost', '')
    port = os.environ.get('pgsport', '')
    
    db = Pgsqltool()
    
    # db setting
    db.pgsql_setting(dbname, user, passwd, host, port)
    
    # select from db
    qry = """select * from test limit 10"""
    rows, result, resultmsg = db.pgsql_select(qry)
    
    if len(rows) > 0:
        for row in rows:
            print(row)
    else:
        print(result, resultmsg)
        
if __name__ == '__main__':
    test()
    main()
    