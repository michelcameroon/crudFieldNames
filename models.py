from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Table1(db.Model):
    #tableName = db.Model.__tablename__
    #tableName = self.__tablename__
    #__tablename__ = 'students'
    #__tablename__ = tableName
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    #email = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<Table1 {self.name}>"


    def __init__(self, name, email):
        self.name=name
        self.email=email

    def get_field_names(model):
         return [column.name for column in model.__table__.columns]
         #return [column.name for column in model.students.columns]

    def get_field_namesNoId(model):
         fieldNames = Table1.get_field_names(model)
         fieldNamesNoId = []
         for fieldName in fieldNames:
             if  fieldName != 'id':
                 fieldNamesNoId.append(fieldName)
         
         return fieldNamesNoId
         #return [column.name for column in model.students.columns]



    # Example usage:

    
    def get_table_name(tableName):
        print ('tableName=')
        print (tableName)
        __tablename__ = tableName
        return tableName

    def get_field_names(model):
        return [column.name for column in model.__table__.columns]
    

#field_names = Table1.get_field_names(Table1)
#print(field_names)  # Output: ['id', 'name', 'email']

