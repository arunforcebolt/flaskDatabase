from basic import db,Student

sanju = Student("Sanju",21)
db.session.add(sanju)
db.session.commit()

ayush = Student("ayush",21)
db.session.add(ayush)
db.session.commit()

allStudent= Student.query.all()
print(allStudent)


age21=Student.query.filter_by(age=21)
print(age21.all())