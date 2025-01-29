from flask import Flask, render_template, redirect, url_for, request
from models import db
#from models import Student
#from models import Table1, get_field_names
from models import Table1
import os

import fieldNamesInTable

app = Flask(__name__)

# Configure database connection (replace with your actual password)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school1.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# Create database (uncomment if necessary)
with app.app_context():
     db.create_all()

'''
tbName = Table1.get_table_name('students')
print ('tbName=')
print (tbName)
dbName = 'school1.db'
tbName = 'students'
'''


#table1 = Table1()
table1 = Table1(name='name1', email='a@mail.com')



@app.route('/')
#def student_list():
def list():
#def table_list():
    ##nameNoIds = Table1.get_field_names(tbName)
    #nameNoIds = fieldNamesInTable.namesNoId(dbName, tbName)
    #nameNoIds = fieldNamesInTable.namesNoId('school1.db', 'table1')
    ##print ('nameNoIds=')
    ##print (nameNoIds)

    # Get field names for YourModel
    #field_names = Table1.get_field_names(Table1)
    field_namesNoId = Table1.get_field_namesNoId(Table1)

    #print ('field_names=')
    print ('field_namesNoId=')
    #print (field_names)
    print (field_namesNoId)

    #students = Student.query.all()
    #tables = Table.query.all()
    #tables1 = Table1.query.all()
    records = Table1.query.all()
    #return render_template('list.html', tables1=tables1)
    #return render_template('list.html', tables1=tables1, field_namesNoId=field_namesNoId)
    return render_template('list.html', records=records, field_namesNoId=field_namesNoId)



@app.route('/create', methods=['GET', 'POST'])
#def create_student():
def create():
#def create_record():
    field_namesNoId = Table1.get_field_namesNoId(Table1)
    if request.method == 'POST':
        '''
        names = []
        for field_nameNoId in field_namesNoId:
            name = request.form[field_nameNoId]
            names.append(name)
      
        print ('names=')
        print (names)
        '''
        #name = request.form['name']
        #email = request.form['email']
        #print ('email=') 
        #print (email) 

        '''
        class Parent(Base):
            __tablename__ = 'parent'
            id = Column(Integer, primary_key=True)
            list_of_items = Column(JSON, nullabled=False)

        Adding an Array to your DB.

        parent_one = Parent(list_of_items=['item1', 'item2'])
        session.add(parent_one)
        session.commit()

        '''
                

        #new_student = Student(name=name, email=email)
        #new_table = Table(name=name, email=email)
        #new_table1 = Table1(name=name, email=email)	#ok
        ##names = name=name, email=email

        #new_table1 = Table1(names)
        data = {field_nameNoId: request.form[field_nameNoId] for field_nameNoId in field_namesNoId}
        #new_table1 = Table1(names)
        #new_table1 = Table1(data)
        new_table1 = Table1(**data)
        #print ('new_table1=')
        #print (new_table1)
        #db.session.add(new_student)
        db.session.add(new_table1)
        db.session.commit()

        #return redirect(url_for('student_list'))
        return redirect(url_for('list'))

    return render_template('create.html')


@app.route('/update/<int:id>', methods=['GET', 'POST'])
#def update_student(id):
def update(id):
    #table1 = Table1.query.get_or_404(id)
    record = Table1.query.get_or_404(id)
    id1 = record.id
    print ('id1=')
    print (id1)
    print ('record=')
    print (record)
    if request.method == 'POST':

        '''
        record.name = request.form['name']
        record.email = request.form['email']

        '''
        
        keyvalues = request.form
        #update_stmt = update(Table1).where (Table1.id == id)
        update_stmt = update(Table1).where (Table1.id == id1)
        print ('update_stmt=')
        print (update_stmt)
        for key, value in keyvalues.items():
            if hasattr(Table1, key):
                update_stmt = update_stmt.values(**{key: value})
        
        result = db.session.execute(update_stmt)           

        
        db.session.commit()


        
 
        return redirect(url_for('list'))

    #return render_template('update.html', record=record)
    return render_template('update.html', record=record, id1=id1)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
#def delete_student(id):
def delete(id):
    record = Table1.query.get_or_404(id)

    if request.method == 'POST':
        db.session.delete(record)
        db.session.commit()

        return redirect(url_for('list'))

    return render_template('delete.html', record=record)


if __name__ == '__main__':
    app.run(debug=True)
