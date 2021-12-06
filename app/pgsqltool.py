try:
    import psycopg2
except Exception as e:
    print(e)
    
class Pgsqltool:
     
    pgsdbname = "" 
    pgsdbuser = "" 
    pgspassword = "" 
    pgshost = "" 
    pgsport = ""
    
    def pgsql_setting(self, dbname, user, passwd, host, port):
        self.pgsdbname = dbname
        self.pgsdbuser = user
        self.pgspassword = passwd
        self.pgshost = host
        self.pgsport = port
    
    # Select시 해당 메소드 사용    
    def pgsql_select(self, query):
        result = False
        try:
            db = psycopg2.connect(host=self.pgshost, dbname=self.pgsdbname, user=self.pgsdbuser, password=self.pgspassword, port=self.pgsport)
            cs = db.cursor()
            cs.execute(query)
            rows = cs.fetchall()
            cs.close()
            db.close()
            result = True
            resultmsg = ""
            return rows, result, resultmsg
        except Exception as e:
            rows = []
            return rows, result, e
    
    # Select 이외의 모든 쿼리는 해당 메소드 사용.(Ex. ALTER, UPDATE, DELETE, DROP ...)
    def pgsql_except_select(self, query):
        result = False
        try:
            db = psycopg2.connect(host=self.pgshost, dbname=self.pgsdbname, user=self.pgsdbuser, password=self.pgspassword, port=self.pgsport)
            cs = db.cursor()
            cs.execute(query)
            db.commit()
            cs.close()
            db.close()
            result = True
            resultmsg = ""
            return result, resultmsg
        except Exception as e:
            return result, e