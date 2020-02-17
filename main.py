from flask import Flask, render_template, request, url_for, redirect
import pygal
import psycopg2
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, Numeric, ForeignKey, DateTime
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@127.0.0.1:5432/ims'
db = SQLAlchemy(app)


# @app.before_first_request
# def create_table():
#     db.create_all()








@app.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database created')

@app.cli.command('db_drop')
def drop_db():
    db.drop_all()
    print('Database dropped')

@app.cli.command('db_seed')
def db_seed():    
    bread = Inventories(name = 'Bread',
    type = 'Product',
    buying_price = 45,
    selling_price = 56)

    db.session.add(bread)
    db.session.commit()
    print('Database seeded')

class Inventories(db.Model):
    __tablename__ = 'new_inventories'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    type = Column(String, nullable=False)
    buying_price = Column(Integer)
    selling_price = Column(Integer)

    stock = db.relationship('Stock', backref='inventories', lazy=True)
    sales = db.relationship('Sales', backref='inventories', lazy=True)


class Stock(db.Model):
    __tablename__ = 'new_stock'
    id = Column(Integer, primary_key=True)
    inv_id = Column(Integer, ForeignKey('new_inventories.id'))
    stock = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class Sales(db.Model):
    id = Column(Integer, primary_key=True)
    inv_id = Column(Integer, ForeignKey('new_inventories.id'))
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# conn = psycopg2.connect(dbname="ims", user="postgres", password="123456")
conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='123456'")
@app.route('/', methods=['GET','POST'])
def home():

    # conn = psycopg2.connect("dbname=d2olmc1g1ep2um user=lbklkxnrccbafn host=ec2-18-210-51-239.compute-1.amazonaws.com password=9ba141e9e03ccd7f51b9f445e0a471ae284159ab97b3997b85e6367a2417634c")
    cur = conn.cursor()
    # cur.execute("CREATE TABLE sales (id serial PRIMARY KEY, inventory_id integer, quantity varchar, created_at date);")

    


    # cur.execute("SELECT * FROM sales")
    # cur.execute("""SELECT EXTRACT (MONTHS FROM sales.created_at) AS months,
    # SUM(sales.quantity) as "Total Sales" 
    # FROM sales
    # GROUP BY 
    # months 
    # ORDER BY 
    # months""")

    cur.execute("""SELECT EXTRACT (MONTHS FROM sales.created_at) AS months,
    SUM(sales.quantity) as "Total Sales" 
    FROM public.sales 
    GROUP BY months 
    ORDER BY  months""")
    
    records = cur.fetchall()

    x = []
    y = []

    for i in records:
        x.append(i[0])
        y.append(i[1])




    line_chart = pygal.Line()
    line_chart.title = 'Sales total in each month'
    line_chart.x_labels = map(str, x)
    line_chart.add('Sales', y)
    line_data = line_chart.render_data_uri()



    data = [
    ('Internet Explorer', 19.5), 
    ('Firefox', 36.6),
    ('Chrome', 36.3), 
    ('Safari', 4.5), 
    ('Opera', 2.3)
    ]


    pie_chart = pygal.Pie()
    pie_chart.title = 'Browser usage in February 2012 (in %)'
    pie_chart.add(data[0][0], data[0][1])
    pie_chart.add(data[1][0], data[1][1])
    pie_chart.add(data[2][0], data[2][1])
    pie_chart.add(data[3][0], data[3][1])
    pie_chart.add(data[4][0], data[4][1])

    pie_data = pie_chart.render_data_uri()
    conn.commit()
    conn.close()
    
    

    return render_template('index.html', pie_data=pie_data, line_data=line_data )






@app.route('/inventories', methods=['GET','POST'])
def inventories():
    r = Inventories.query.all()

    if request.method == 'POST':
        name = request.form['name']
        type = request.form['type']
        buying_price = request.form['buying_price']
        selling_price = request.form['selling_price']

        records = Inventories(name=name, type=type, buying_price=buying_price, selling_price=selling_price)
        db.session.add(records)
        db.session.commit()

        return redirect(url_for('inventories'))


        
    #     print(name)
    #     print(type)
    #     print(buying_price)
    #     print(selling_price)
        
    return render_template('inventories.html', record=r)


     
    

if __name__ == '__main__':
    app.debug = True
    app.run()
    