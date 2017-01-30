
# pip install pymysql
import pymysql

class StarterCode():
    connection = None
    results = None

    def connect(self):
        self.connection = pymysql.connect(host='127.0.0.1',
            # whichever your root user and pw is
            user='root', password='root',
            db='cs121', charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

    def runScript(self):
        try:
            self.connect()
            with self.connection.cursor() as cursor:
                # Create a new record
                sql = "SELECT * FROM pages1"
                cursor.execute(sql)

                for row in cursor:
                    #do things with data
                    #row["url"]
                    #row["id"]
                    #row["plain_text"]


                cursor.close()
                self.connection.close()



        except:
            print "something went wrong :("
