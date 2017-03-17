import pymongo
import sys


conn = pymongo.MongoClient("mongodb://localhost")
db = conn.students
col = db.grades

try:
    iter = col.find({'type' : 'homework'}).sort([('student_id', 1), ('score', 1)])
    prev = -1
    for doc in iter:
        if doc['student_id'] != prev:
            prev = doc['student_id']
            col.delete_one({'_id' : doc['_id']})

except Exception as e:
    print "Error trying to read collection:", type(e), e
