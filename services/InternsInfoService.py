from psycopg2 import sql
from config.config import base_executor
from controller.dto.AddNewInternBody import AddNewInternBody
from controller.dto.UpdateInternBody import UpdateInternBody

class InternsInfoService():
    
    def getAllInterns(self):
        query = sql.SQL("SELECT id, name, mail_id, hobbies FROM interns_schema.interns_details")
        try:
            rows, message = base_executor.executeSelect(query=query)
            # Convert result to list of dicts
            interns_list = [{"id": r[0], "name": r[1], "mailId": r[2], "hobbies": r[3]} for r in rows]
            return interns_list
        except Exception as e:
            return {"error": str(e)}
        
    def addNewIntern(self, body:AddNewInternBody):
        query = sql.SQL("""
                    insert into interns_schema.interns_details(name,mail_id,hobbies)
                    values (%s, %s,%s)
                    """)
        values = (body.name, body.mailId, body.hobbies)
        try:
            rows_affected, message = base_executor.executeInsert(query=query, values=values)
            return {"rows_affected": rows_affected, "message": message}
        except Exception as e:
            return {"error": str(e)}
        
    def updateIntern(self, id:int, body:UpdateInternBody):
        query = sql.SQL("""
                    update interns_schema.interns_details
                    set name = %s, mail_id = %s, hobbies = %s
                    where id = %s
                    """)
        values = (body.name, body.mailId, body.hobbies, id)
        try:
            rows_affected, message = base_executor.executeUpdate(query=query, values=values)
            return {"rows_affected": rows_affected, "message": message}
        except Exception as e:
            return {"error": str(e)}
        
    def deleteIntern(self, id:int):
        query = sql.SQL("DELETE FROM interns_schema.interns_details WHERE id = %s")
        values = (id,)
        try:
            rows_affected, message = base_executor.executeUpdate(query=query, values=values)
            return {"rows_affected": rows_affected, "message": message}
        except Exception as e:
            return {"error": str(e)}