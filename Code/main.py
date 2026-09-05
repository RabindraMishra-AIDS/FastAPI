from fastapi import FastAPI #Core Fast api framework
from pydantic import BaseModel  #while sending data it gives us proper structure on which we override and validate the result.
from typing import List

app=FastAPI()

# Creatig a ReportCard Structure.
#These Structures can be Very complex.

class ReportCard(BaseModel): #Inheriting the BaseModel
    name:str
    marks:int
    student_id:int
    result:bool

records:List[ReportCard]=[] #records will be of type List where it will hold collection of Reportcard.

#Fast API Heavily works on Decorators.
@app.get("/")
def result_day():
    return {"Title":"Welcome to the Result Day"}
@app.get("/reportcard")
def report_card():
    return records


''' ################################ CRUD Operations in FAST API ######################################  '''


#POST Method
@app.post("/reportcard")
def add_records(card:ReportCard): #card of type ReportCard(will contain name,marks,..)
    records.append(card)
    return records

@app.put("/reportcard/{student_id}")
def update_records(student_id: int, updated_report: ReportCard):
    for index, record in enumerate(records):
        if record.student_id == student_id:  # Compare with the current record's student_id
            records[index] = updated_report
            return updated_report
    return {"error": "Record not found"}

@app.delete("/reportcard/{student_id}")
def delete_records(student_id: int):
    for index,card in enumerate(records):
        if card.student_id == student_id:  # Compare with the current record's student_id
           deleted_index= records.pop(index)
           return deleted_index
    return {"error": "Record not found"}