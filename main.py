from flask import Flask, render_template
import pygal
import psycopg2

app = Flask(__name__)
# conn = psycopg2.connect("dbname='postgres' user='postgres' password='dbpass'")

@app.route('/', methods=['GET','POST'])
def home():

    conn = psycopg2.connect("dbname=d2olmc1g1ep2um user=lbklkxnrccbafn host=ec2-18-210-51-239.compute-1.amazonaws.com password=9ba141e9e03ccd7f51b9f445e0a471ae284159ab97b3997b85e6367a2417634c")
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
    
    cur.commit()
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
    
 
    

    return render_template('index.html',pie_data=pie_data, line_data=line_data)  

@app.route('/person/<name>/<int:age>')
def person(name, age):
    return f'{name} is {age} years old'


@app.route('/numbers/<int:firstNum>/<int:secondNum>')
def add(firstNum, secondNum):
    summation = firstNum + secondNum
    return f'the sum of {firstNum} and {secondNum} is {summation}'

@app.route('/about')
def about():
    return render_template('about.html', title = 'This is about page')

@app.route('/services')
def services():
    return render_template('services.html')




if __name__ == '__main__':
    app.debug = True
    app.run()
    