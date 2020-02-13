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

    cur.execute(""" create table inventories (
	id INT,
	name VARCHAR(50),
	bp DECIMAL(5,2),
	sp DECIMAL(5,2),
	type VARCHAR(10)
    );
    insert into inventories (id, name, bp, sp, type) values (1, 'Millicent', 195.95, 274.33, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (2, 'Alexina', 112.99, 158.186, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (3, 'Alfy', 140.9, 197.26, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (4, 'Reynold', 120.03, 168.042, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (5, 'Kendell', 118.84, 166.376, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (6, 'Bink', 144.36, 202.104, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (7, 'Emmie', 157.22, 220.108, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (8, 'Elianore', 198.57, 277.998, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (9, 'Uta', 151.16, 211.624, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (10, 'Ericka', 180.5, 252.7, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (11, 'Blaine', 152.69, 213.766, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (12, 'Rachel', 181.29, 253.806, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (13, 'Ignacius', 153.25, 214.55, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (14, 'Demetria', 159.86, 223.804, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (15, 'Sawyere', 104.33, 146.062, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (16, 'Ana', 181.66, 254.324, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (17, 'Jeanine', 140.34, 196.476, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (18, 'Elijah', 157.14, 219.996, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (19, 'Nikolos', 167.0, 233.8, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (20, 'Arline', 186.12, 260.568, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (21, 'Kimberley', 159.01, 222.614, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (22, 'Derrik', 145.2, 203.28, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (23, 'Julietta', 190.76, 267.064, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (24, 'Lenette', 158.97, 222.558, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (25, 'Reagan', 144.99, 202.986, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (26, 'Ardella', 174.89, 244.846, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (27, 'Clementina', 107.0, 149.8, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (28, 'Klara', 187.44, 262.416, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (29, 'Orly', 156.71, 219.394, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (30, 'Rhiamon', 177.93, 249.102, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (31, 'Dex', 129.29, 181.006, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (32, 'Christin', 140.32, 196.448, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (33, 'Marina', 196.32, 274.848, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (34, 'Alon', 147.38, 206.332, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (35, 'Vivian', 183.71, 257.194, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (36, 'Rudiger', 118.15, 165.41, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (37, 'Ellissa', 184.0, 257.6, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (38, 'Correna', 136.53, 191.142, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (39, 'Mabelle', 150.03, 210.042, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (40, 'Yevette', 115.22, 161.308, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (41, 'Addi', 129.95, 181.93, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (42, 'Lee', 183.03, 256.242, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (43, 'Aldous', 199.07, 278.698, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (44, 'Kacey', 116.45, 163.03, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (45, 'Mack', 179.68, 251.552, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (46, 'Tiffanie', 116.89, 163.646, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (47, 'Clemmie', 129.1, 180.74, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (48, 'Bourke', 119.01, 166.614, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (49, 'Elane', 122.24, 171.136, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (50, 'Hanson', 138.82, 194.348, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (51, 'Jo-ann', 118.29, 165.606, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (52, 'Cherice', 120.21, 168.294, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (53, 'Idette', 156.76, 219.464, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (54, 'Goddard', 112.19, 157.066, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (55, 'Toma', 161.51, 226.114, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (56, 'Raphaela', 136.5, 191.1, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (57, 'Drake', 157.01, 219.814, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (58, 'Jaquith', 106.39, 148.946, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (59, 'Brandtr', 106.23, 148.722, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (60, 'Nikki', 126.05, 176.47, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (61, 'Arnoldo', 162.21, 227.094, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (62, 'Axel', 164.57, 230.398, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (63, 'Joel', 195.6, 273.84, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (64, 'Olly', 122.49, 171.486, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (65, 'Buddy', 178.28, 249.592, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (66, 'Yank', 139.38, 195.132, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (67, 'Thomas', 132.88, 186.032, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (68, 'Carce', 158.25, 221.55, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (69, 'Gui', 108.11, 151.354, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (70, 'Ruby', 186.38, 260.932, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (71, 'Natassia', 164.03, 229.642, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (72, 'Shandeigh', 153.17, 214.438, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (73, 'Nanette', 148.66, 208.124, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (74, 'Pip', 153.14, 214.396, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (75, 'Adena', 107.0, 149.8, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (76, 'Trip', 189.84, 265.776, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (77, 'Lindsy', 168.88, 236.432, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (78, 'Ramsay', 125.37, 175.518, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (79, 'Devan', 184.26, 257.964, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (80, 'Ignatius', 179.74, 251.636, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (81, 'Mei', 182.34, 255.276, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (82, 'Andonis', 143.31, 200.634, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (83, 'Rosa', 152.62, 213.668, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (84, 'Elga', 199.71, 279.594, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (85, 'Catlin', 172.08, 240.912, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (86, 'Jemie', 175.29, 245.406, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (87, 'Fara', 125.67, 175.938, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (88, 'Alick', 178.34, 249.676, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (89, 'Correy', 115.83, 162.162, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (90, 'Darlene', 165.39, 231.546, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (91, 'Colene', 182.18, 255.052, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (92, 'Antonio', 132.63, 185.682, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (93, 'Jerry', 155.16, 217.224, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (94, 'Dell', 195.52, 273.728, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (95, 'Tabby', 118.52, 165.928, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (96, 'Christalle', 179.26, 250.964, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (97, 'Josee', 161.94, 226.716, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (98, 'Ciel', 142.24, 199.136, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (99, 'Almire', 146.27, 204.778, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (100, 'Tally', 194.06, 271.684, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (101, 'Shandy', 151.27, 211.778, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (102, 'Yorke', 177.59, 248.626, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (103, 'Verene', 188.64, 264.096, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (104, 'Gustav', 189.64, 265.496, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (105, 'Sibylle', 162.81, 227.934, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (106, 'Lauri', 189.16, 264.824, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (107, 'Guendolen', 138.88, 194.432, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (108, 'Cchaddie', 160.52, 224.728, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (109, 'Dannye', 156.68, 219.352, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (110, 'Charmian', 189.3, 265.02, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (111, 'Dorelle', 138.36, 193.704, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (112, 'Jade', 160.18, 224.252, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (113, 'Erda', 185.36, 259.504, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (114, 'Mitzi', 194.03, 271.642, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (115, 'Bryan', 192.46, 269.444, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (116, 'Graig', 108.59, 152.026, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (117, 'Maiga', 158.3, 221.62, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (118, 'Guinevere', 198.45, 277.83, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (119, 'Aretha', 120.75, 169.05, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (120, 'Eddy', 154.92, 216.888, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (121, 'Willem', 190.79, 267.106, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (122, 'Joel', 187.6, 262.64, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (123, 'Torrey', 109.19, 152.866, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (124, 'Jeromy', 188.04, 263.256, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (125, 'Aeriela', 134.19, 187.866, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (126, 'Reynolds', 107.14, 149.996, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (127, 'Avivah', 114.74, 160.636, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (128, 'Mel', 190.11, 266.154, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (129, 'Ketti', 171.72, 240.408, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (130, 'Josepha', 190.46, 266.644, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (131, 'Nariko', 118.64, 166.096, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (132, 'Agathe', 168.33, 235.662, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (133, 'Davidde', 179.54, 251.356, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (134, 'Gasparo', 185.68, 259.952, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (135, 'Emerson', 114.14, 159.796, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (136, 'Sim', 197.14, 275.996, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (137, 'Sula', 124.39, 174.146, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (138, 'Ulla', 180.01, 252.014, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (139, 'Emelita', 147.11, 205.954, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (140, 'Krisha', 153.09, 214.326, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (141, 'Karry', 155.33, 217.462, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (142, 'Alfy', 129.57, 181.398, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (143, 'Artair', 191.68, 268.352, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (144, 'Charlotta', 171.67, 240.338, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (145, 'Lexie', 147.92, 207.088, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (146, 'Morgan', 136.27, 190.778, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (147, 'Kelley', 147.82, 206.948, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (148, 'Deanna', 156.72, 219.408, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (149, 'Harris', 146.41, 204.974, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (150, 'Mortimer', 166.85, 233.59, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (151, 'Cele', 158.93, 222.502, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (152, 'Nickey', 127.5, 178.5, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (153, 'Kendricks', 102.67, 143.738, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (154, 'Dorella', 185.98, 260.372, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (155, 'Nathaniel', 177.35, 248.29, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (156, 'Sean', 127.57, 178.598, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (157, 'Shaina', 128.98, 180.572, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (158, 'Ginnifer', 164.11, 229.754, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (159, 'Eleanor', 179.91, 251.874, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (160, 'Aundrea', 151.02, 211.428, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (161, 'Breanne', 158.33, 221.662, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (162, 'Haskel', 139.75, 195.65, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (163, 'Everard', 159.3, 223.02, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (164, 'Zaneta', 140.97, 197.358, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (165, 'Leland', 155.7, 217.98, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (166, 'Brett', 124.48, 174.272, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (167, 'Ofelia', 116.66, 163.324, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (168, 'Yardley', 196.44, 275.016, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (169, 'Standford', 167.96, 235.144, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (170, 'Benson', 151.69, 212.366, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (171, 'Abbe', 121.31, 169.834, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (172, 'Ferguson', 115.01, 161.014, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (173, 'Dori', 135.26, 189.364, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (174, 'Winnie', 152.11, 212.954, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (175, 'Dreddy', 135.43, 189.602, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (176, 'Todd', 179.3, 251.02, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (177, 'Clay', 123.55, 172.97, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (178, 'Ulrike', 139.94, 195.916, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (179, 'Waneta', 142.53, 199.542, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (180, 'Marietta', 163.9, 229.46, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (181, 'Terrel', 197.12, 275.968, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (182, 'Almira', 184.06, 257.684, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (183, 'Kurtis', 144.01, 201.614, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (184, 'Debee', 182.14, 254.996, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (185, 'Rochelle', 170.25, 238.35, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (186, 'Aldis', 186.44, 261.016, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (187, 'Keelby', 199.25, 278.95, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (188, 'Jacquelyn', 154.88, 216.832, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (189, 'Lodovico', 158.65, 222.11, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (190, 'Tory', 167.41, 234.374, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (191, 'Renado', 169.26, 236.964, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (192, 'Gun', 114.8, 160.72, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (193, 'Ambros', 193.8, 271.32, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (194, 'Katti', 194.56, 272.384, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (195, 'Deva', 147.5, 206.5, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (196, 'Herold', 183.39, 256.746, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (197, 'Sidney', 172.7, 241.78, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (198, 'Rickey', 181.08, 253.512, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (199, 'Carmine', 137.96, 193.144, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (200, 'Lydon', 176.53, 247.142, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (201, 'Brent', 157.65, 220.71, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (202, 'Kasey', 150.53, 210.742, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (203, 'Kirbie', 117.33, 164.262, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (204, 'Boone', 174.87, 244.818, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (205, 'Petey', 103.64, 145.096, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (206, 'Agretha', 159.35, 223.09, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (207, 'Bradly', 139.04, 194.656, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (208, 'Emlynne', 145.49, 203.686, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (209, 'Georas', 116.19, 162.666, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (210, 'Sanson', 150.0, 210.0, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (211, 'Mavis', 136.97, 191.758, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (212, 'Twila', 180.91, 253.274, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (213, 'Leticia', 114.26, 159.964, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (214, 'Hetti', 184.22, 257.908, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (215, 'Luis', 118.53, 165.942, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (216, 'Donelle', 160.89, 225.246, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (217, 'Barris', 119.79, 167.706, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (218, 'Philis', 185.25, 259.35, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (219, 'Rick', 182.62, 255.668, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (220, 'Kathlin', 159.86, 223.804, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (221, 'Lorita', 149.49, 209.286, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (222, 'Gaylord', 150.92, 211.288, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (223, 'Boycey', 162.75, 227.85, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (224, 'Davidson', 132.47, 185.458, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (225, 'Lynnelle', 146.79, 205.506, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (226, 'Fairleigh', 184.88, 258.832, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (227, 'Engelbert', 124.0, 173.6, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (228, 'Nicky', 104.03, 145.642, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (229, 'Culley', 173.67, 243.138, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (230, 'Ive', 122.22, 171.108, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (231, 'Mick', 159.92, 223.888, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (232, 'Edita', 153.64, 215.096, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (233, 'Brockie', 125.81, 176.134, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (234, 'Tabor', 125.36, 175.504, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (235, 'Lennard', 136.11, 190.554, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (236, 'Cristal', 144.12, 201.768, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (237, 'Belvia', 103.36, 144.704, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (238, 'Sascha', 149.3, 209.02, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (239, 'Blake', 168.02, 235.228, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (240, 'Brietta', 112.06, 156.884, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (241, 'Bret', 194.08, 271.712, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (242, 'Alissa', 122.46, 171.444, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (243, 'Thurston', 153.39, 214.746, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (244, 'Binni', 119.66, 167.524, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (245, 'Amii', 164.5, 230.3, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (246, 'Myrilla', 172.4, 241.36, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (247, 'Lavinia', 199.14, 278.796, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (248, 'Jamie', 195.92, 274.288, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (249, 'Marcel', 145.24, 203.336, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (250, 'Chick', 193.48, 270.872, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (251, 'Randie', 194.46, 272.244, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (252, 'Devi', 191.82, 268.548, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (253, 'Serge', 169.76, 237.664, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (254, 'Jabez', 161.26, 225.764, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (255, 'Putnem', 159.79, 223.706, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (256, 'Lutero', 191.61, 268.254, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (257, 'Alicia', 194.43, 272.202, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (258, 'Robert', 106.88, 149.632, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (259, 'Leesa', 185.84, 260.176, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (260, 'Che', 183.9, 257.46, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (261, 'Napoleon', 101.13, 141.582, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (262, 'Leilah', 194.82, 272.748, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (263, 'Gertrud', 185.55, 259.77, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (264, 'Pierce', 101.66, 142.324, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (265, 'Lotti', 167.47, 234.458, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (266, 'Kurtis', 193.34, 270.676, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (267, 'Raffaello', 145.22, 203.308, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (268, 'Cos', 102.23, 143.122, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (269, 'Finn', 166.03, 232.442, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (270, 'Sharai', 121.68, 170.352, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (271, 'Fredericka', 146.05, 204.47, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (272, 'Alano', 116.36, 162.904, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (273, 'Deva', 196.79, 275.506, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (274, 'Nyssa', 110.47, 154.658, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (275, 'Tisha', 115.79, 162.106, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (276, 'Ginnifer', 123.76, 173.264, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (277, 'Wylie', 148.93, 208.502, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (278, 'Naomi', 115.74, 162.036, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (279, 'Bonny', 129.32, 181.048, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (280, 'Tarrah', 165.21, 231.294, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (281, 'Tabb', 180.99, 253.386, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (282, 'Jolee', 156.69, 219.366, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (283, 'Jefferey', 100.76, 141.064, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (284, 'Florenza', 129.41, 181.174, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (285, 'Gun', 160.98, 225.372, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (286, 'Sal', 145.54, 203.756, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (287, 'Karil', 172.84, 241.976, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (288, 'Netty', 141.09, 197.526, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (289, 'Mariel', 108.82, 152.348, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (290, 'Reeba', 194.37, 272.118, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (291, 'Cecilia', 117.51, 164.514, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (292, 'Henderson', 184.16, 257.824, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (293, 'Siegfried', 105.52, 147.728, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (294, 'Merilyn', 164.85, 230.79, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (295, 'Floyd', 159.14, 222.796, 'fruits');
    insert into inventories (id, name, bp, sp, type) values (296, 'Truda', 175.14, 245.196, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (297, 'Flora', 129.88, 181.832, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (298, 'Gerty', 197.49, 276.486, 'vegetables');
    insert into inventories (id, name, bp, sp, type) values (299, 'Raffarty', 185.74, 260.036, 'cereals');
    insert into inventories (id, name, bp, sp, type) values (300, 'Margarethe', 156.8, 219.52, 'cereals'); """)
    

    cur.execute(""" create table sales (
	id INT,
	inv_id INT,
	quantity INT,
	created_at DATE
    );
    insert into sales (id, inv_id, quantity, created_at) values (1, 29, 153, '2019-03-09 13:02:39');
    insert into sales (id, inv_id, quantity, created_at) values (2, 222, 222, '2019-03-27 16:49:22');
    insert into sales (id, inv_id, quantity, created_at) values (3, 20, 534, '2019-02-05 07:39:50');
    insert into sales (id, inv_id, quantity, created_at) values (4, 201, 396, '2019-04-27 17:34:03');
    insert into sales (id, inv_id, quantity, created_at) values (5, 108, 563, '2019-02-07 18:34:27');
    insert into sales (id, inv_id, quantity, created_at) values (6, 141, 135, '2019-06-26 14:17:13');
    insert into sales (id, inv_id, quantity, created_at) values (7, 229, 389, '2019-05-29 20:22:56');
    insert into sales (id, inv_id, quantity, created_at) values (8, 49, 397, '2019-03-18 03:39:28');
    insert into sales (id, inv_id, quantity, created_at) values (9, 127, 515, '2019-02-03 14:58:57');
    insert into sales (id, inv_id, quantity, created_at) values (10, 267, 352, '2019-04-16 01:06:13');
    insert into sales (id, inv_id, quantity, created_at) values (11, 101, 401, '2019-08-15 09:33:43');
    insert into sales (id, inv_id, quantity, created_at) values (12, 300, 196, '2019-06-15 00:11:57');
    insert into sales (id, inv_id, quantity, created_at) values (13, 133, 402, '2019-04-04 00:22:54');
    insert into sales (id, inv_id, quantity, created_at) values (14, 170, 289, '2019-10-12 07:14:41');
    insert into sales (id, inv_id, quantity, created_at) values (15, 292, 562, '2019-08-21 02:45:23');
    insert into sales (id, inv_id, quantity, created_at) values (16, 136, 518, '2019-05-01 11:56:02');
    insert into sales (id, inv_id, quantity, created_at) values (17, 145, 166, '2019-09-09 20:02:25');
    insert into sales (id, inv_id, quantity, created_at) values (18, 256, 326, '2019-08-26 08:04:27');
    insert into sales (id, inv_id, quantity, created_at) values (19, 71, 494, '2019-01-12 13:40:56');
    insert into sales (id, inv_id, quantity, created_at) values (20, 200, 561, '2019-04-20 16:07:28');
    insert into sales (id, inv_id, quantity, created_at) values (21, 226, 285, '2019-04-17 15:55:59');
    insert into sales (id, inv_id, quantity, created_at) values (22, 51, 414, '2019-01-07 05:51:37');
    insert into sales (id, inv_id, quantity, created_at) values (23, 256, 268, '2019-02-15 21:17:49');
    insert into sales (id, inv_id, quantity, created_at) values (24, 187, 284, '2019-03-15 02:10:40');
    insert into sales (id, inv_id, quantity, created_at) values (25, 30, 162, '2019-02-18 00:04:50');
    insert into sales (id, inv_id, quantity, created_at) values (26, 87, 382, '2019-07-30 09:13:56');
    insert into sales (id, inv_id, quantity, created_at) values (27, 28, 411, '2019-02-24 08:17:38');
    insert into sales (id, inv_id, quantity, created_at) values (28, 7, 206, '2019-06-07 00:27:53');
    insert into sales (id, inv_id, quantity, created_at) values (29, 133, 119, '2019-09-24 03:07:20');
    insert into sales (id, inv_id, quantity, created_at) values (30, 117, 574, '2019-10-03 12:30:56');
    insert into sales (id, inv_id, quantity, created_at) values (31, 276, 267, '2019-08-22 08:45:43');
    insert into sales (id, inv_id, quantity, created_at) values (32, 228, 160, '2019-10-20 06:00:53');
    insert into sales (id, inv_id, quantity, created_at) values (33, 222, 526, '2019-06-25 06:59:10');
    insert into sales (id, inv_id, quantity, created_at) values (34, 156, 413, '2019-05-19 08:05:31');
    insert into sales (id, inv_id, quantity, created_at) values (35, 82, 195, '2019-04-14 20:41:30');
    insert into sales (id, inv_id, quantity, created_at) values (36, 63, 322, '2019-11-05 16:07:21');
    insert into sales (id, inv_id, quantity, created_at) values (37, 131, 416, '2019-05-14 10:57:12');
    insert into sales (id, inv_id, quantity, created_at) values (38, 85, 305, '2019-02-07 23:46:50');
    insert into sales (id, inv_id, quantity, created_at) values (39, 132, 123, '2019-02-05 19:49:53');
    insert into sales (id, inv_id, quantity, created_at) values (40, 68, 317, '2019-01-21 07:59:40');
    insert into sales (id, inv_id, quantity, created_at) values (41, 44, 374, '2019-04-21 03:02:31');
    insert into sales (id, inv_id, quantity, created_at) values (42, 10, 279, '2019-10-05 19:13:54');
    insert into sales (id, inv_id, quantity, created_at) values (43, 222, 336, '2019-11-10 20:47:18');
    insert into sales (id, inv_id, quantity, created_at) values (44, 192, 394, '2019-02-09 02:06:50');
    insert into sales (id, inv_id, quantity, created_at) values (45, 291, 526, '2019-09-20 02:09:48');
    insert into sales (id, inv_id, quantity, created_at) values (46, 277, 304, '2019-06-11 04:12:48');
    insert into sales (id, inv_id, quantity, created_at) values (47, 186, 533, '2019-07-11 21:52:09');
    insert into sales (id, inv_id, quantity, created_at) values (48, 81, 213, '2019-03-29 07:59:22');
    insert into sales (id, inv_id, quantity, created_at) values (49, 65, 206, '2019-05-03 09:41:49');
    insert into sales (id, inv_id, quantity, created_at) values (50, 137, 403, '2019-10-11 02:28:09');
    insert into sales (id, inv_id, quantity, created_at) values (51, 298, 303, '2019-11-05 03:23:44');
    insert into sales (id, inv_id, quantity, created_at) values (52, 240, 260, '2019-06-16 11:49:02');
    insert into sales (id, inv_id, quantity, created_at) values (53, 3, 124, '2019-05-19 02:19:10');
    insert into sales (id, inv_id, quantity, created_at) values (54, 119, 486, '2019-06-01 10:04:59');
    insert into sales (id, inv_id, quantity, created_at) values (55, 194, 410, '2019-06-21 00:59:30');
    insert into sales (id, inv_id, quantity, created_at) values (56, 70, 482, '2019-03-31 06:45:54');
    insert into sales (id, inv_id, quantity, created_at) values (57, 10, 203, '2019-05-31 23:06:49');
    insert into sales (id, inv_id, quantity, created_at) values (58, 78, 599, '2019-03-09 19:13:09');
    insert into sales (id, inv_id, quantity, created_at) values (59, 148, 213, '2019-11-12 05:12:15');
    insert into sales (id, inv_id, quantity, created_at) values (60, 41, 295, '2019-11-13 11:33:51');
    insert into sales (id, inv_id, quantity, created_at) values (61, 76, 244, '2019-03-28 03:03:01');
    insert into sales (id, inv_id, quantity, created_at) values (62, 77, 525, '2019-02-08 11:49:12');
    insert into sales (id, inv_id, quantity, created_at) values (63, 267, 299, '2019-09-23 21:53:16');
    insert into sales (id, inv_id, quantity, created_at) values (64, 195, 441, '2019-01-24 01:42:54');
    insert into sales (id, inv_id, quantity, created_at) values (65, 155, 498, '2019-10-04 20:34:48');
    insert into sales (id, inv_id, quantity, created_at) values (66, 50, 594, '2019-10-10 05:19:05');
    insert into sales (id, inv_id, quantity, created_at) values (67, 261, 175, '2019-10-17 12:22:14');
    insert into sales (id, inv_id, quantity, created_at) values (68, 220, 376, '2019-11-27 07:39:32');
    insert into sales (id, inv_id, quantity, created_at) values (69, 191, 586, '2019-03-26 18:28:36');
    insert into sales (id, inv_id, quantity, created_at) values (70, 149, 432, '2019-07-15 23:25:28');
    insert into sales (id, inv_id, quantity, created_at) values (71, 278, 300, '2019-05-18 14:41:45');
    insert into sales (id, inv_id, quantity, created_at) values (72, 224, 191, '2019-02-13 10:46:34');
    insert into sales (id, inv_id, quantity, created_at) values (73, 135, 285, '2019-02-22 18:00:03');
    insert into sales (id, inv_id, quantity, created_at) values (74, 245, 565, '2019-10-17 22:31:51');
    insert into sales (id, inv_id, quantity, created_at) values (75, 285, 149, '2019-02-17 19:38:43');
    insert into sales (id, inv_id, quantity, created_at) values (76, 253, 179, '2019-07-20 07:51:17');
    insert into sales (id, inv_id, quantity, created_at) values (77, 244, 541, '2019-05-06 09:41:58');
    insert into sales (id, inv_id, quantity, created_at) values (78, 273, 102, '2019-03-10 05:07:00');
    insert into sales (id, inv_id, quantity, created_at) values (79, 188, 500, '2019-08-02 22:00:36');
    insert into sales (id, inv_id, quantity, created_at) values (80, 221, 378, '2019-01-03 02:32:09');
    insert into sales (id, inv_id, quantity, created_at) values (81, 6, 458, '2019-11-13 13:14:02');
    insert into sales (id, inv_id, quantity, created_at) values (82, 175, 535, '2019-10-09 07:03:47');
    insert into sales (id, inv_id, quantity, created_at) values (83, 230, 289, '2019-04-01 10:51:27');
    insert into sales (id, inv_id, quantity, created_at) values (84, 58, 595, '2019-08-08 23:55:18');
    insert into sales (id, inv_id, quantity, created_at) values (85, 112, 598, '2019-03-08 19:11:28');
    insert into sales (id, inv_id, quantity, created_at) values (86, 64, 247, '2019-09-13 03:36:56');
    insert into sales (id, inv_id, quantity, created_at) values (87, 276, 438, '2019-08-26 22:51:57');
    insert into sales (id, inv_id, quantity, created_at) values (88, 240, 383, '2019-10-28 09:39:10');
    insert into sales (id, inv_id, quantity, created_at) values (89, 211, 587, '2019-12-02 02:07:45');
    insert into sales (id, inv_id, quantity, created_at) values (90, 36, 158, '2019-02-16 08:18:49');
    insert into sales (id, inv_id, quantity, created_at) values (91, 279, 551, '2019-05-27 14:11:37');
    insert into sales (id, inv_id, quantity, created_at) values (92, 214, 189, '2019-11-24 19:05:36');
    insert into sales (id, inv_id, quantity, created_at) values (93, 200, 387, '2019-02-07 19:55:15');
    insert into sales (id, inv_id, quantity, created_at) values (94, 51, 348, '2019-06-10 20:29:04');
    insert into sales (id, inv_id, quantity, created_at) values (95, 171, 332, '2019-04-22 02:36:28');
    insert into sales (id, inv_id, quantity, created_at) values (96, 111, 569, '2019-02-05 10:23:08');
    insert into sales (id, inv_id, quantity, created_at) values (97, 86, 588, '2019-05-22 16:39:34');
    insert into sales (id, inv_id, quantity, created_at) values (98, 2, 462, '2019-10-10 12:44:29');
    insert into sales (id, inv_id, quantity, created_at) values (99, 151, 427, '2019-04-08 16:42:53');
    insert into sales (id, inv_id, quantity, created_at) values (100, 81, 212, '2019-01-20 18:16:56');
    insert into sales (id, inv_id, quantity, created_at) values (101, 168, 210, '2019-06-28 08:40:44');
    insert into sales (id, inv_id, quantity, created_at) values (102, 231, 114, '2019-12-14 02:46:24');
    insert into sales (id, inv_id, quantity, created_at) values (103, 216, 395, '2019-02-22 12:16:26');
    insert into sales (id, inv_id, quantity, created_at) values (104, 76, 158, '2019-08-10 08:56:22');
    insert into sales (id, inv_id, quantity, created_at) values (105, 220, 223, '2019-01-28 16:13:51');
    insert into sales (id, inv_id, quantity, created_at) values (106, 227, 130, '2019-11-18 22:48:25');
    insert into sales (id, inv_id, quantity, created_at) values (107, 12, 461, '2019-08-21 05:57:35');
    insert into sales (id, inv_id, quantity, created_at) values (108, 26, 268, '2019-03-07 07:34:59');
    insert into sales (id, inv_id, quantity, created_at) values (109, 64, 390, '2019-01-04 13:55:45');
    insert into sales (id, inv_id, quantity, created_at) values (110, 82, 232, '2019-03-08 05:23:23');
    insert into sales (id, inv_id, quantity, created_at) values (111, 29, 567, '2019-03-30 05:53:43');
    insert into sales (id, inv_id, quantity, created_at) values (112, 186, 357, '2019-06-23 01:13:26');
    insert into sales (id, inv_id, quantity, created_at) values (113, 52, 350, '2019-10-03 02:31:24');
    insert into sales (id, inv_id, quantity, created_at) values (114, 81, 417, '2019-02-19 23:40:55');
    insert into sales (id, inv_id, quantity, created_at) values (115, 199, 113, '2019-01-24 14:26:19');
    insert into sales (id, inv_id, quantity, created_at) values (116, 136, 171, '2019-06-03 09:13:26');
    insert into sales (id, inv_id, quantity, created_at) values (117, 7, 578, '2019-07-04 16:25:49');
    insert into sales (id, inv_id, quantity, created_at) values (118, 165, 292, '2019-07-21 18:20:49');
    insert into sales (id, inv_id, quantity, created_at) values (119, 70, 496, '2019-05-22 06:33:51');
    insert into sales (id, inv_id, quantity, created_at) values (120, 95, 591, '2019-02-05 19:13:07');
    insert into sales (id, inv_id, quantity, created_at) values (121, 121, 308, '2019-10-23 00:21:05');
    insert into sales (id, inv_id, quantity, created_at) values (122, 284, 382, '2019-07-18 16:45:26');
    insert into sales (id, inv_id, quantity, created_at) values (123, 50, 219, '2019-01-05 01:34:32');
    insert into sales (id, inv_id, quantity, created_at) values (124, 268, 135, '2019-09-26 08:22:22');
    insert into sales (id, inv_id, quantity, created_at) values (125, 230, 381, '2019-04-01 09:43:18');
    insert into sales (id, inv_id, quantity, created_at) values (126, 43, 580, '2019-03-09 19:12:05');
    insert into sales (id, inv_id, quantity, created_at) values (127, 298, 400, '2019-10-16 05:01:15');
    insert into sales (id, inv_id, quantity, created_at) values (128, 278, 174, '2019-09-18 17:51:08');
    insert into sales (id, inv_id, quantity, created_at) values (129, 49, 232, '2019-10-27 08:04:32');
    insert into sales (id, inv_id, quantity, created_at) values (130, 150, 398, '2019-08-06 10:02:06');
    insert into sales (id, inv_id, quantity, created_at) values (131, 76, 472, '2019-10-24 07:17:10');
    insert into sales (id, inv_id, quantity, created_at) values (132, 299, 377, '2019-09-27 05:14:15');
    insert into sales (id, inv_id, quantity, created_at) values (133, 18, 555, '2019-09-27 11:06:09');
    insert into sales (id, inv_id, quantity, created_at) values (134, 139, 402, '2019-02-18 02:39:16');
    insert into sales (id, inv_id, quantity, created_at) values (135, 213, 596, '2019-04-25 10:12:29');
    insert into sales (id, inv_id, quantity, created_at) values (136, 58, 364, '2019-05-16 09:46:27');
    insert into sales (id, inv_id, quantity, created_at) values (137, 93, 442, '2019-12-06 15:54:14');
    insert into sales (id, inv_id, quantity, created_at) values (138, 197, 564, '2019-11-12 21:49:42');
    insert into sales (id, inv_id, quantity, created_at) values (139, 243, 343, '2019-06-16 18:07:33');
    insert into sales (id, inv_id, quantity, created_at) values (140, 99, 515, '2019-11-20 06:28:24');
    insert into sales (id, inv_id, quantity, created_at) values (141, 227, 231, '2019-05-03 11:22:16');
    insert into sales (id, inv_id, quantity, created_at) values (142, 11, 383, '2019-11-26 23:25:14');
    insert into sales (id, inv_id, quantity, created_at) values (143, 204, 198, '2019-06-10 06:12:38');
    insert into sales (id, inv_id, quantity, created_at) values (144, 55, 553, '2019-01-14 13:21:31');
    insert into sales (id, inv_id, quantity, created_at) values (145, 279, 387, '2019-03-03 22:08:03');
    insert into sales (id, inv_id, quantity, created_at) values (146, 63, 415, '2019-04-04 05:50:08');
    insert into sales (id, inv_id, quantity, created_at) values (147, 76, 532, '2019-09-05 16:15:34');
    insert into sales (id, inv_id, quantity, created_at) values (148, 210, 120, '2019-09-18 16:05:41');
    insert into sales (id, inv_id, quantity, created_at) values (149, 232, 128, '2019-10-28 00:18:18');
    insert into sales (id, inv_id, quantity, created_at) values (150, 194, 212, '2019-05-24 03:32:13');
    insert into sales (id, inv_id, quantity, created_at) values (151, 259, 117, '2019-01-30 00:30:15');
    insert into sales (id, inv_id, quantity, created_at) values (152, 74, 529, '2019-10-14 07:45:20');
    insert into sales (id, inv_id, quantity, created_at) values (153, 30, 399, '2019-09-11 07:07:34');
    insert into sales (id, inv_id, quantity, created_at) values (154, 170, 335, '2019-05-07 10:34:51');
    insert into sales (id, inv_id, quantity, created_at) values (155, 47, 449, '2019-06-11 14:11:08');
    insert into sales (id, inv_id, quantity, created_at) values (156, 6, 489, '2019-04-17 11:04:40');
    insert into sales (id, inv_id, quantity, created_at) values (157, 274, 378, '2019-08-27 21:47:35');
    insert into sales (id, inv_id, quantity, created_at) values (158, 244, 568, '2019-06-02 07:56:24');
    insert into sales (id, inv_id, quantity, created_at) values (159, 112, 263, '2019-12-14 08:28:34');
    insert into sales (id, inv_id, quantity, created_at) values (160, 271, 269, '2019-03-06 10:51:14');
    insert into sales (id, inv_id, quantity, created_at) values (161, 246, 226, '2019-09-07 03:12:26');
    insert into sales (id, inv_id, quantity, created_at) values (162, 85, 246, '2019-04-19 01:36:41');
    insert into sales (id, inv_id, quantity, created_at) values (163, 160, 513, '2019-02-17 04:19:09');
    insert into sales (id, inv_id, quantity, created_at) values (164, 186, 300, '2019-01-21 06:20:01');
    insert into sales (id, inv_id, quantity, created_at) values (165, 300, 288, '2019-03-01 14:51:08');
    insert into sales (id, inv_id, quantity, created_at) values (166, 218, 210, '2019-11-20 12:04:13');
    insert into sales (id, inv_id, quantity, created_at) values (167, 251, 204, '2019-06-07 03:30:59');
    insert into sales (id, inv_id, quantity, created_at) values (168, 181, 422, '2019-08-16 05:54:10');
    insert into sales (id, inv_id, quantity, created_at) values (169, 299, 398, '2019-08-12 04:46:57');
    insert into sales (id, inv_id, quantity, created_at) values (170, 62, 501, '2019-06-11 15:16:13');
    insert into sales (id, inv_id, quantity, created_at) values (171, 203, 143, '2019-09-04 17:27:35');
    insert into sales (id, inv_id, quantity, created_at) values (172, 96, 539, '2019-07-25 21:52:47');
    insert into sales (id, inv_id, quantity, created_at) values (173, 110, 414, '2019-07-27 21:47:56');
    insert into sales (id, inv_id, quantity, created_at) values (174, 182, 350, '2019-06-08 03:28:19');
    insert into sales (id, inv_id, quantity, created_at) values (175, 183, 376, '2019-09-03 23:45:57');
    insert into sales (id, inv_id, quantity, created_at) values (176, 52, 373, '2019-08-30 22:35:17');
    insert into sales (id, inv_id, quantity, created_at) values (177, 213, 305, '2019-06-17 17:00:54');
    insert into sales (id, inv_id, quantity, created_at) values (178, 174, 564, '2019-05-26 01:58:04');
    insert into sales (id, inv_id, quantity, created_at) values (179, 4, 155, '2019-02-11 18:18:31');
    insert into sales (id, inv_id, quantity, created_at) values (180, 20, 124, '2019-11-03 00:42:40');
    insert into sales (id, inv_id, quantity, created_at) values (181, 75, 214, '2019-07-16 15:25:03');
    insert into sales (id, inv_id, quantity, created_at) values (182, 278, 169, '2019-04-25 03:53:07');
    insert into sales (id, inv_id, quantity, created_at) values (183, 205, 509, '2019-03-11 03:30:32');
    insert into sales (id, inv_id, quantity, created_at) values (184, 90, 104, '2019-08-29 05:10:24');
    insert into sales (id, inv_id, quantity, created_at) values (185, 275, 572, '2019-03-18 06:55:35');
    insert into sales (id, inv_id, quantity, created_at) values (186, 45, 550, '2019-09-08 01:37:39');
    insert into sales (id, inv_id, quantity, created_at) values (187, 178, 267, '2019-09-06 15:20:41');
    insert into sales (id, inv_id, quantity, created_at) values (188, 296, 121, '2019-08-10 23:16:14');
    insert into sales (id, inv_id, quantity, created_at) values (189, 4, 296, '2019-02-24 17:31:24');
    insert into sales (id, inv_id, quantity, created_at) values (190, 94, 382, '2019-04-13 21:56:10');
    insert into sales (id, inv_id, quantity, created_at) values (191, 81, 157, '2019-05-09 00:53:20');
    insert into sales (id, inv_id, quantity, created_at) values (192, 230, 278, '2019-05-22 22:06:00');
    insert into sales (id, inv_id, quantity, created_at) values (193, 130, 152, '2019-04-17 06:44:03');
    insert into sales (id, inv_id, quantity, created_at) values (194, 10, 187, '2019-07-12 23:28:27');
    insert into sales (id, inv_id, quantity, created_at) values (195, 233, 349, '2019-05-14 07:48:56');
    insert into sales (id, inv_id, quantity, created_at) values (196, 215, 116, '2019-11-16 10:26:17');
    insert into sales (id, inv_id, quantity, created_at) values (197, 71, 288, '2019-08-15 16:30:53');
    insert into sales (id, inv_id, quantity, created_at) values (198, 167, 357, '2019-02-07 08:31:09');
    insert into sales (id, inv_id, quantity, created_at) values (199, 79, 343, '2019-12-27 21:31:13');
    insert into sales (id, inv_id, quantity, created_at) values (200, 57, 410, '2019-10-15 02:59:06');
    insert into sales (id, inv_id, quantity, created_at) values (201, 14, 351, '2019-11-17 01:36:47');
    insert into sales (id, inv_id, quantity, created_at) values (202, 215, 303, '2019-05-23 03:32:39');
    insert into sales (id, inv_id, quantity, created_at) values (203, 30, 421, '2019-02-13 11:31:21');
    insert into sales (id, inv_id, quantity, created_at) values (204, 54, 379, '2019-02-16 09:17:03');
    insert into sales (id, inv_id, quantity, created_at) values (205, 66, 430, '2019-09-16 07:05:33');
    insert into sales (id, inv_id, quantity, created_at) values (206, 216, 288, '2019-05-16 23:44:31');
    insert into sales (id, inv_id, quantity, created_at) values (207, 159, 157, '2019-09-19 10:09:07');
    insert into sales (id, inv_id, quantity, created_at) values (208, 166, 432, '2019-05-16 04:55:52');
    insert into sales (id, inv_id, quantity, created_at) values (209, 201, 497, '2019-04-06 14:27:03');
    insert into sales (id, inv_id, quantity, created_at) values (210, 107, 136, '2019-06-12 11:04:18');
    insert into sales (id, inv_id, quantity, created_at) values (211, 226, 419, '2019-04-30 05:43:02');
    insert into sales (id, inv_id, quantity, created_at) values (212, 104, 545, '2019-04-29 03:56:41');
    insert into sales (id, inv_id, quantity, created_at) values (213, 135, 478, '2019-03-19 17:19:57');
    insert into sales (id, inv_id, quantity, created_at) values (214, 191, 346, '2019-04-20 20:58:47');
    insert into sales (id, inv_id, quantity, created_at) values (215, 142, 167, '2019-11-12 21:13:36');
    insert into sales (id, inv_id, quantity, created_at) values (216, 104, 106, '2019-06-13 00:42:24');
    insert into sales (id, inv_id, quantity, created_at) values (217, 223, 395, '2019-05-04 23:26:17');
    insert into sales (id, inv_id, quantity, created_at) values (218, 197, 114, '2019-07-21 19:07:39');
    insert into sales (id, inv_id, quantity, created_at) values (219, 128, 417, '2019-06-25 05:14:10');
    insert into sales (id, inv_id, quantity, created_at) values (220, 291, 315, '2019-03-29 02:56:33');
    insert into sales (id, inv_id, quantity, created_at) values (221, 72, 322, '2019-11-18 16:46:02');
    insert into sales (id, inv_id, quantity, created_at) values (222, 85, 476, '2019-06-05 03:03:41');
    insert into sales (id, inv_id, quantity, created_at) values (223, 4, 132, '2019-12-25 18:44:01');
    insert into sales (id, inv_id, quantity, created_at) values (224, 82, 129, '2019-03-24 13:01:38');
    insert into sales (id, inv_id, quantity, created_at) values (225, 175, 556, '2019-01-31 09:41:43');
    insert into sales (id, inv_id, quantity, created_at) values (226, 194, 523, '2019-07-18 07:55:48');
    insert into sales (id, inv_id, quantity, created_at) values (227, 248, 375, '2019-01-11 16:50:41');
    insert into sales (id, inv_id, quantity, created_at) values (228, 234, 525, '2019-05-13 16:43:05');
    insert into sales (id, inv_id, quantity, created_at) values (229, 167, 393, '2019-06-29 09:04:14');
    insert into sales (id, inv_id, quantity, created_at) values (230, 151, 103, '2019-01-10 07:53:36');
    insert into sales (id, inv_id, quantity, created_at) values (231, 288, 203, '2019-09-04 04:04:40');
    insert into sales (id, inv_id, quantity, created_at) values (232, 78, 600, '2019-03-17 08:44:25');
    insert into sales (id, inv_id, quantity, created_at) values (233, 258, 270, '2019-08-11 23:11:16');
    insert into sales (id, inv_id, quantity, created_at) values (234, 209, 458, '2019-04-21 07:56:55');
    insert into sales (id, inv_id, quantity, created_at) values (235, 13, 351, '2019-03-30 07:49:56');
    insert into sales (id, inv_id, quantity, created_at) values (236, 258, 405, '2019-02-01 21:39:02');
    insert into sales (id, inv_id, quantity, created_at) values (237, 208, 458, '2019-02-11 05:56:55');
    insert into sales (id, inv_id, quantity, created_at) values (238, 217, 224, '2019-06-12 04:03:56');
    insert into sales (id, inv_id, quantity, created_at) values (239, 195, 119, '2019-11-01 10:38:23');
    insert into sales (id, inv_id, quantity, created_at) values (240, 3, 142, '2019-08-21 19:23:59');
    insert into sales (id, inv_id, quantity, created_at) values (241, 285, 266, '2019-02-26 18:20:43');
    insert into sales (id, inv_id, quantity, created_at) values (242, 22, 460, '2019-03-31 08:27:00');
    insert into sales (id, inv_id, quantity, created_at) values (243, 121, 267, '2019-03-26 01:23:19');
    insert into sales (id, inv_id, quantity, created_at) values (244, 11, 176, '2019-12-17 14:00:13');
    insert into sales (id, inv_id, quantity, created_at) values (245, 248, 231, '2019-05-19 00:16:00');
    insert into sales (id, inv_id, quantity, created_at) values (246, 241, 376, '2019-05-07 21:54:07');
    insert into sales (id, inv_id, quantity, created_at) values (247, 190, 105, '2019-02-06 03:45:23');
    insert into sales (id, inv_id, quantity, created_at) values (248, 164, 312, '2019-08-26 04:35:26');
    insert into sales (id, inv_id, quantity, created_at) values (249, 266, 359, '2019-08-17 22:49:50');
    insert into sales (id, inv_id, quantity, created_at) values (250, 92, 349, '2019-04-02 00:26:19');
    insert into sales (id, inv_id, quantity, created_at) values (251, 76, 505, '2019-08-18 13:32:37');
    insert into sales (id, inv_id, quantity, created_at) values (252, 119, 531, '2019-04-23 05:42:55');
    insert into sales (id, inv_id, quantity, created_at) values (253, 29, 525, '2019-11-30 19:19:21');
    insert into sales (id, inv_id, quantity, created_at) values (254, 212, 372, '2019-03-21 10:44:48');
    insert into sales (id, inv_id, quantity, created_at) values (255, 273, 571, '2019-05-22 06:53:49');
    insert into sales (id, inv_id, quantity, created_at) values (256, 117, 521, '2019-02-22 22:12:56');
    insert into sales (id, inv_id, quantity, created_at) values (257, 3, 362, '2019-08-26 04:18:22');
    insert into sales (id, inv_id, quantity, created_at) values (258, 274, 547, '2019-01-21 04:26:12');
    insert into sales (id, inv_id, quantity, created_at) values (259, 108, 168, '2019-08-02 12:09:49');
    insert into sales (id, inv_id, quantity, created_at) values (260, 27, 584, '2019-05-23 14:51:44');
    insert into sales (id, inv_id, quantity, created_at) values (261, 64, 532, '2019-11-18 08:41:22');
    insert into sales (id, inv_id, quantity, created_at) values (262, 178, 117, '2019-04-06 20:03:56');
    insert into sales (id, inv_id, quantity, created_at) values (263, 134, 552, '2019-06-09 04:54:26');
    insert into sales (id, inv_id, quantity, created_at) values (264, 266, 109, '2019-07-29 04:58:41');
    insert into sales (id, inv_id, quantity, created_at) values (265, 111, 202, '2019-07-13 19:50:03');
    insert into sales (id, inv_id, quantity, created_at) values (266, 230, 148, '2019-01-03 09:07:01');
    insert into sales (id, inv_id, quantity, created_at) values (267, 241, 326, '2019-06-18 22:06:21');
    insert into sales (id, inv_id, quantity, created_at) values (268, 158, 419, '2019-03-29 10:36:25');
    insert into sales (id, inv_id, quantity, created_at) values (269, 6, 210, '2019-10-06 02:44:21');
    insert into sales (id, inv_id, quantity, created_at) values (270, 28, 253, '2019-01-24 05:44:51');
    insert into sales (id, inv_id, quantity, created_at) values (271, 16, 147, '2019-08-10 02:50:40');
    insert into sales (id, inv_id, quantity, created_at) values (272, 76, 380, '2019-02-28 21:31:09');
    insert into sales (id, inv_id, quantity, created_at) values (273, 129, 397, '2019-06-29 07:28:13');
    insert into sales (id, inv_id, quantity, created_at) values (274, 88, 335, '2019-10-22 00:27:40');
    insert into sales (id, inv_id, quantity, created_at) values (275, 267, 459, '2019-02-04 20:29:22');
    insert into sales (id, inv_id, quantity, created_at) values (276, 152, 497, '2019-02-22 17:01:50');
    insert into sales (id, inv_id, quantity, created_at) values (277, 148, 572, '2019-06-08 13:15:01');
    insert into sales (id, inv_id, quantity, created_at) values (278, 94, 547, '2019-12-29 09:53:32');
    insert into sales (id, inv_id, quantity, created_at) values (279, 82, 479, '2019-07-28 13:06:36');
    insert into sales (id, inv_id, quantity, created_at) values (280, 167, 340, '2019-03-29 12:39:53');
    insert into sales (id, inv_id, quantity, created_at) values (281, 283, 370, '2019-01-19 20:13:45');
    insert into sales (id, inv_id, quantity, created_at) values (282, 182, 575, '2019-09-21 11:19:31');
    insert into sales (id, inv_id, quantity, created_at) values (283, 132, 312, '2019-10-17 18:03:27');
    insert into sales (id, inv_id, quantity, created_at) values (284, 152, 172, '2019-10-08 15:54:16');
    insert into sales (id, inv_id, quantity, created_at) values (285, 31, 120, '2019-01-19 16:35:00');
    insert into sales (id, inv_id, quantity, created_at) values (286, 88, 519, '2019-09-13 03:25:54');
    insert into sales (id, inv_id, quantity, created_at) values (287, 247, 255, '2019-11-25 19:13:52');
    insert into sales (id, inv_id, quantity, created_at) values (288, 69, 131, '2019-02-01 05:41:48');
    insert into sales (id, inv_id, quantity, created_at) values (289, 225, 224, '2019-05-25 13:44:00');
    insert into sales (id, inv_id, quantity, created_at) values (290, 125, 552, '2019-01-29 21:37:03');
    insert into sales (id, inv_id, quantity, created_at) values (291, 293, 299, '2019-03-30 07:24:42');
    insert into sales (id, inv_id, quantity, created_at) values (292, 105, 480, '2019-03-10 07:15:55');
    insert into sales (id, inv_id, quantity, created_at) values (293, 112, 154, '2019-09-26 14:07:00');
    insert into sales (id, inv_id, quantity, created_at) values (294, 27, 173, '2019-03-24 23:36:23');
    insert into sales (id, inv_id, quantity, created_at) values (295, 290, 212, '2019-03-25 01:36:06');
    insert into sales (id, inv_id, quantity, created_at) values (296, 252, 518, '2019-10-01 05:11:42');
    insert into sales (id, inv_id, quantity, created_at) values (297, 200, 207, '2019-05-05 08:54:43');
    insert into sales (id, inv_id, quantity, created_at) values (298, 292, 208, '2019-07-15 01:32:09');
    insert into sales (id, inv_id, quantity, created_at) values (299, 100, 473, '2019-07-05 20:09:54');
    insert into sales (id, inv_id, quantity, created_at) values (300, 294, 268, '2019-05-24 22:07:14'); """)


    cur.execute(""" create table stock (
	id INT,
	inv_id INT,
	stock INT,
	created_at DATE
);
    insert into stock (id, inv_id, stock, created_at) values (1, 48, 400, '2019-11-11 17:07:18');
    insert into stock (id, inv_id, stock, created_at) values (2, 226, 451, '2019-12-15 19:29:33');
    insert into stock (id, inv_id, stock, created_at) values (3, 56, 578, '2019-02-11 21:58:10');
    insert into stock (id, inv_id, stock, created_at) values (4, 173, 244, '2019-07-02 00:55:31');
    insert into stock (id, inv_id, stock, created_at) values (5, 41, 375, '2019-03-15 20:04:45');
    insert into stock (id, inv_id, stock, created_at) values (6, 76, 479, '2019-11-05 04:08:25');
    insert into stock (id, inv_id, stock, created_at) values (7, 23, 249, '2019-01-27 09:01:47');
    insert into stock (id, inv_id, stock, created_at) values (8, 188, 525, '2019-08-13 09:48:31');
    insert into stock (id, inv_id, stock, created_at) values (9, 64, 186, '2019-04-04 06:27:04');
    insert into stock (id, inv_id, stock, created_at) values (10, 140, 121, '2019-04-22 01:43:42');
    insert into stock (id, inv_id, stock, created_at) values (11, 202, 246, '2019-02-03 14:58:08');
    insert into stock (id, inv_id, stock, created_at) values (12, 259, 263, '2019-06-20 17:56:35');
    insert into stock (id, inv_id, stock, created_at) values (13, 275, 311, '2019-08-05 00:43:40');
    insert into stock (id, inv_id, stock, created_at) values (14, 90, 473, '2019-03-25 00:20:47');
    insert into stock (id, inv_id, stock, created_at) values (15, 106, 347, '2019-01-28 17:01:39');
    insert into stock (id, inv_id, stock, created_at) values (16, 111, 175, '2019-07-22 10:58:21');
    insert into stock (id, inv_id, stock, created_at) values (17, 57, 356, '2019-02-02 20:16:34');
    insert into stock (id, inv_id, stock, created_at) values (18, 98, 463, '2019-10-28 05:03:48');
    insert into stock (id, inv_id, stock, created_at) values (19, 219, 473, '2019-05-29 00:12:54');
    insert into stock (id, inv_id, stock, created_at) values (20, 104, 144, '2019-05-03 21:43:29');
    insert into stock (id, inv_id, stock, created_at) values (21, 39, 407, '2019-11-22 16:29:04');
    insert into stock (id, inv_id, stock, created_at) values (22, 110, 460, '2019-09-06 10:51:55');
    insert into stock (id, inv_id, stock, created_at) values (23, 160, 407, '2019-09-03 00:28:13');
    insert into stock (id, inv_id, stock, created_at) values (24, 36, 460, '2019-08-02 17:49:50');
    insert into stock (id, inv_id, stock, created_at) values (25, 46, 110, '2019-11-28 19:29:36');
    insert into stock (id, inv_id, stock, created_at) values (26, 264, 489, '2019-11-15 02:29:56');
    insert into stock (id, inv_id, stock, created_at) values (27, 194, 497, '2019-06-01 19:47:43');
    insert into stock (id, inv_id, stock, created_at) values (28, 108, 525, '2019-02-03 16:56:05');
    insert into stock (id, inv_id, stock, created_at) values (29, 19, 469, '2019-02-22 23:25:01');
    insert into stock (id, inv_id, stock, created_at) values (30, 66, 283, '2019-10-17 17:11:47');
    insert into stock (id, inv_id, stock, created_at) values (31, 204, 235, '2019-03-23 04:11:23');
    insert into stock (id, inv_id, stock, created_at) values (32, 240, 389, '2019-08-12 12:27:00');
    insert into stock (id, inv_id, stock, created_at) values (33, 267, 570, '2019-07-23 21:18:34');
    insert into stock (id, inv_id, stock, created_at) values (34, 60, 364, '2019-11-10 21:27:12');
    insert into stock (id, inv_id, stock, created_at) values (35, 209, 415, '2019-10-17 08:38:17');
    insert into stock (id, inv_id, stock, created_at) values (36, 136, 127, '2019-03-25 02:45:01');
    insert into stock (id, inv_id, stock, created_at) values (37, 183, 300, '2019-03-12 03:53:09');
    insert into stock (id, inv_id, stock, created_at) values (38, 11, 250, '2019-01-18 07:55:16');
    insert into stock (id, inv_id, stock, created_at) values (39, 230, 155, '2019-01-07 23:32:37');
    insert into stock (id, inv_id, stock, created_at) values (40, 178, 322, '2019-09-11 04:53:38');
    insert into stock (id, inv_id, stock, created_at) values (41, 293, 175, '2019-03-26 06:52:32');
    insert into stock (id, inv_id, stock, created_at) values (42, 38, 193, '2019-09-16 12:38:36');
    insert into stock (id, inv_id, stock, created_at) values (43, 274, 241, '2019-07-26 21:33:12');
    insert into stock (id, inv_id, stock, created_at) values (44, 94, 226, '2019-02-28 02:41:26');
    insert into stock (id, inv_id, stock, created_at) values (45, 246, 463, '2019-04-08 03:32:26');
    insert into stock (id, inv_id, stock, created_at) values (46, 292, 168, '2019-11-03 12:37:53');
    insert into stock (id, inv_id, stock, created_at) values (47, 38, 366, '2019-11-15 22:07:32');
    insert into stock (id, inv_id, stock, created_at) values (48, 143, 312, '2019-04-10 08:24:50');
    insert into stock (id, inv_id, stock, created_at) values (49, 159, 431, '2019-07-08 01:56:17');
    insert into stock (id, inv_id, stock, created_at) values (50, 254, 116, '2019-05-30 09:26:59');
    insert into stock (id, inv_id, stock, created_at) values (51, 126, 379, '2019-05-20 15:27:34');
    insert into stock (id, inv_id, stock, created_at) values (52, 181, 589, '2019-05-02 01:25:48');
    insert into stock (id, inv_id, stock, created_at) values (53, 111, 152, '2019-03-20 23:25:34');
    insert into stock (id, inv_id, stock, created_at) values (54, 134, 395, '2019-09-05 07:49:44');
    insert into stock (id, inv_id, stock, created_at) values (55, 290, 256, '2019-05-23 06:45:27');
    insert into stock (id, inv_id, stock, created_at) values (56, 13, 559, '2019-02-27 17:39:17');
    insert into stock (id, inv_id, stock, created_at) values (57, 280, 218, '2019-11-19 16:36:06');
    insert into stock (id, inv_id, stock, created_at) values (58, 67, 542, '2019-07-26 21:21:19');
    insert into stock (id, inv_id, stock, created_at) values (59, 192, 255, '2019-11-06 12:01:23');
    insert into stock (id, inv_id, stock, created_at) values (60, 128, 552, '2019-10-30 21:05:12');
    insert into stock (id, inv_id, stock, created_at) values (61, 34, 401, '2019-09-13 01:24:49');
    insert into stock (id, inv_id, stock, created_at) values (62, 142, 505, '2019-04-14 05:41:12');
    insert into stock (id, inv_id, stock, created_at) values (63, 204, 467, '2019-03-10 02:47:10');
    insert into stock (id, inv_id, stock, created_at) values (64, 246, 374, '2019-09-04 07:34:59');
    insert into stock (id, inv_id, stock, created_at) values (65, 158, 266, '2019-03-05 15:44:22');
    insert into stock (id, inv_id, stock, created_at) values (66, 258, 453, '2019-08-31 20:23:08');
    insert into stock (id, inv_id, stock, created_at) values (67, 226, 456, '2019-01-24 11:46:16');
    insert into stock (id, inv_id, stock, created_at) values (68, 109, 555, '2019-06-06 04:06:18');
    insert into stock (id, inv_id, stock, created_at) values (69, 251, 268, '2019-08-05 07:08:12');
    insert into stock (id, inv_id, stock, created_at) values (70, 63, 383, '2019-07-24 07:00:21');
    insert into stock (id, inv_id, stock, created_at) values (71, 59, 266, '2019-07-11 14:17:18');
    insert into stock (id, inv_id, stock, created_at) values (72, 62, 103, '2019-12-26 11:39:27');
    insert into stock (id, inv_id, stock, created_at) values (73, 273, 544, '2019-01-13 12:20:17');
    insert into stock (id, inv_id, stock, created_at) values (74, 159, 214, '2019-06-05 07:48:36');
    insert into stock (id, inv_id, stock, created_at) values (75, 251, 288, '2019-12-29 07:24:17');
    insert into stock (id, inv_id, stock, created_at) values (76, 32, 387, '2019-03-21 05:38:49');
    insert into stock (id, inv_id, stock, created_at) values (77, 211, 193, '2019-07-23 22:26:22');
    insert into stock (id, inv_id, stock, created_at) values (78, 20, 183, '2019-02-11 01:58:07');
    insert into stock (id, inv_id, stock, created_at) values (79, 94, 445, '2019-11-12 17:16:28');
    insert into stock (id, inv_id, stock, created_at) values (80, 136, 353, '2019-09-03 01:29:41');
    insert into stock (id, inv_id, stock, created_at) values (81, 19, 328, '2019-02-04 09:05:40');
    insert into stock (id, inv_id, stock, created_at) values (82, 268, 107, '2019-04-16 15:56:27');
    insert into stock (id, inv_id, stock, created_at) values (83, 202, 546, '2019-09-24 23:30:37');
    insert into stock (id, inv_id, stock, created_at) values (84, 197, 253, '2019-06-26 18:31:57');
    insert into stock (id, inv_id, stock, created_at) values (85, 176, 393, '2019-09-19 00:17:34');
    insert into stock (id, inv_id, stock, created_at) values (86, 151, 542, '2019-07-18 14:24:00');
    insert into stock (id, inv_id, stock, created_at) values (87, 153, 168, '2019-03-09 16:07:43');
    insert into stock (id, inv_id, stock, created_at) values (88, 105, 235, '2019-11-21 13:48:20');
    insert into stock (id, inv_id, stock, created_at) values (89, 183, 213, '2019-02-11 22:56:32');
    insert into stock (id, inv_id, stock, created_at) values (90, 295, 275, '2019-05-27 07:26:56');
    insert into stock (id, inv_id, stock, created_at) values (91, 141, 402, '2019-07-07 04:32:08');
    insert into stock (id, inv_id, stock, created_at) values (92, 208, 470, '2019-01-27 19:38:43');
    insert into stock (id, inv_id, stock, created_at) values (93, 299, 594, '2019-12-10 09:43:53');
    insert into stock (id, inv_id, stock, created_at) values (94, 159, 238, '2019-06-09 05:44:30');
    insert into stock (id, inv_id, stock, created_at) values (95, 72, 165, '2019-04-26 00:54:33');
    insert into stock (id, inv_id, stock, created_at) values (96, 270, 504, '2019-11-12 07:10:52');
    insert into stock (id, inv_id, stock, created_at) values (97, 216, 516, '2019-04-03 20:38:07');
    insert into stock (id, inv_id, stock, created_at) values (98, 262, 357, '2019-03-06 04:44:21');
    insert into stock (id, inv_id, stock, created_at) values (99, 109, 315, '2019-09-12 09:53:51');
    insert into stock (id, inv_id, stock, created_at) values (100, 26, 527, '2019-02-06 07:44:33');
    insert into stock (id, inv_id, stock, created_at) values (101, 3, 132, '2019-08-05 15:49:02');
    insert into stock (id, inv_id, stock, created_at) values (102, 129, 508, '2019-04-04 23:24:57');
    insert into stock (id, inv_id, stock, created_at) values (103, 226, 119, '2019-07-01 21:05:18');
    insert into stock (id, inv_id, stock, created_at) values (104, 146, 480, '2019-06-03 16:15:30');
    insert into stock (id, inv_id, stock, created_at) values (105, 169, 333, '2019-10-25 14:53:10');
    insert into stock (id, inv_id, stock, created_at) values (106, 125, 178, '2019-08-23 01:12:36');
    insert into stock (id, inv_id, stock, created_at) values (107, 107, 432, '2019-08-17 02:52:02');
    insert into stock (id, inv_id, stock, created_at) values (108, 142, 163, '2019-09-07 01:59:21');
    insert into stock (id, inv_id, stock, created_at) values (109, 261, 371, '2019-03-18 23:28:49');
    insert into stock (id, inv_id, stock, created_at) values (110, 241, 217, '2019-09-04 10:35:15');
    insert into stock (id, inv_id, stock, created_at) values (111, 169, 102, '2019-12-23 02:56:20');
    insert into stock (id, inv_id, stock, created_at) values (112, 292, 112, '2019-03-12 04:50:52');
    insert into stock (id, inv_id, stock, created_at) values (113, 266, 487, '2019-08-27 07:36:14');
    insert into stock (id, inv_id, stock, created_at) values (114, 223, 435, '2019-03-09 09:26:27');
    insert into stock (id, inv_id, stock, created_at) values (115, 163, 442, '2019-04-08 20:03:04');
    insert into stock (id, inv_id, stock, created_at) values (116, 242, 484, '2019-11-25 01:04:15');
    insert into stock (id, inv_id, stock, created_at) values (117, 265, 461, '2019-01-03 08:07:40');
    insert into stock (id, inv_id, stock, created_at) values (118, 186, 368, '2019-09-04 04:14:06');
    insert into stock (id, inv_id, stock, created_at) values (119, 229, 322, '2019-08-14 10:23:49');
    insert into stock (id, inv_id, stock, created_at) values (120, 228, 501, '2019-03-15 01:41:25');
    insert into stock (id, inv_id, stock, created_at) values (121, 295, 465, '2019-04-13 22:02:19');
    insert into stock (id, inv_id, stock, created_at) values (122, 69, 600, '2019-08-25 16:00:59');
    insert into stock (id, inv_id, stock, created_at) values (123, 267, 503, '2019-11-29 02:30:40');
    insert into stock (id, inv_id, stock, created_at) values (124, 122, 405, '2019-09-06 14:04:01');
    insert into stock (id, inv_id, stock, created_at) values (125, 218, 492, '2019-11-01 23:08:02');
    insert into stock (id, inv_id, stock, created_at) values (126, 113, 129, '2019-07-18 05:28:15');
    insert into stock (id, inv_id, stock, created_at) values (127, 89, 401, '2019-08-01 05:13:26');
    insert into stock (id, inv_id, stock, created_at) values (128, 251, 323, '2019-12-05 06:20:34');
    insert into stock (id, inv_id, stock, created_at) values (129, 68, 149, '2019-12-10 16:18:44');
    insert into stock (id, inv_id, stock, created_at) values (130, 63, 520, '2019-10-22 10:02:02');
    insert into stock (id, inv_id, stock, created_at) values (131, 62, 177, '2019-12-05 16:08:25');
    insert into stock (id, inv_id, stock, created_at) values (132, 132, 101, '2019-02-18 08:16:58');
    insert into stock (id, inv_id, stock, created_at) values (133, 249, 129, '2019-10-11 05:50:42');
    insert into stock (id, inv_id, stock, created_at) values (134, 117, 199, '2019-05-06 10:19:42');
    insert into stock (id, inv_id, stock, created_at) values (135, 38, 390, '2019-06-28 11:23:14');
    insert into stock (id, inv_id, stock, created_at) values (136, 209, 357, '2019-05-28 15:55:11');
    insert into stock (id, inv_id, stock, created_at) values (137, 2, 171, '2019-10-25 04:39:14');
    insert into stock (id, inv_id, stock, created_at) values (138, 49, 368, '2019-11-17 17:59:13');
    insert into stock (id, inv_id, stock, created_at) values (139, 295, 216, '2019-08-02 12:11:15');
    insert into stock (id, inv_id, stock, created_at) values (140, 98, 539, '2019-03-05 18:12:41');
    insert into stock (id, inv_id, stock, created_at) values (141, 80, 314, '2019-01-05 00:26:48');
    insert into stock (id, inv_id, stock, created_at) values (142, 231, 590, '2019-01-31 02:24:13');
    insert into stock (id, inv_id, stock, created_at) values (143, 279, 297, '2019-06-13 19:43:35');
    insert into stock (id, inv_id, stock, created_at) values (144, 275, 180, '2019-04-17 03:56:57');
    insert into stock (id, inv_id, stock, created_at) values (145, 88, 492, '2019-08-25 11:19:48');
    insert into stock (id, inv_id, stock, created_at) values (146, 21, 363, '2019-09-27 08:17:47');
    insert into stock (id, inv_id, stock, created_at) values (147, 263, 224, '2019-09-26 16:02:29');
    insert into stock (id, inv_id, stock, created_at) values (148, 237, 302, '2019-01-17 18:18:48');
    insert into stock (id, inv_id, stock, created_at) values (149, 237, 424, '2019-02-18 09:38:40');
    insert into stock (id, inv_id, stock, created_at) values (150, 203, 541, '2019-10-03 18:26:27');
    insert into stock (id, inv_id, stock, created_at) values (151, 135, 589, '2019-04-23 19:34:52');
    insert into stock (id, inv_id, stock, created_at) values (152, 266, 594, '2019-08-12 21:33:06');
    insert into stock (id, inv_id, stock, created_at) values (153, 107, 356, '2019-01-14 13:21:09');
    insert into stock (id, inv_id, stock, created_at) values (154, 27, 254, '2019-01-23 00:26:03');
    insert into stock (id, inv_id, stock, created_at) values (155, 140, 153, '2019-01-08 00:34:31');
    insert into stock (id, inv_id, stock, created_at) values (156, 207, 525, '2019-08-03 00:15:25');
    insert into stock (id, inv_id, stock, created_at) values (157, 162, 218, '2019-06-13 05:56:42');
    insert into stock (id, inv_id, stock, created_at) values (158, 125, 390, '2019-01-12 10:27:21');
    insert into stock (id, inv_id, stock, created_at) values (159, 272, 488, '2019-10-02 21:33:13');
    insert into stock (id, inv_id, stock, created_at) values (160, 2, 482, '2019-01-20 08:46:53');
    insert into stock (id, inv_id, stock, created_at) values (161, 148, 375, '2019-02-09 18:29:43');
    insert into stock (id, inv_id, stock, created_at) values (162, 70, 198, '2019-06-14 08:36:08');
    insert into stock (id, inv_id, stock, created_at) values (163, 265, 361, '2019-01-25 01:37:55');
    insert into stock (id, inv_id, stock, created_at) values (164, 225, 198, '2019-12-05 00:01:12');
    insert into stock (id, inv_id, stock, created_at) values (165, 166, 496, '2019-11-30 17:07:33');
    insert into stock (id, inv_id, stock, created_at) values (166, 260, 291, '2019-04-14 09:29:15');
    insert into stock (id, inv_id, stock, created_at) values (167, 219, 252, '2019-02-05 22:56:16');
    insert into stock (id, inv_id, stock, created_at) values (168, 180, 222, '2019-12-14 15:42:49');
    insert into stock (id, inv_id, stock, created_at) values (169, 256, 143, '2019-09-24 02:29:30');
    insert into stock (id, inv_id, stock, created_at) values (170, 152, 105, '2019-07-19 15:12:45');
    insert into stock (id, inv_id, stock, created_at) values (171, 195, 445, '2019-11-21 18:19:46');
    insert into stock (id, inv_id, stock, created_at) values (172, 193, 478, '2019-11-28 21:11:47');
    insert into stock (id, inv_id, stock, created_at) values (173, 212, 317, '2019-07-03 18:13:11');
    insert into stock (id, inv_id, stock, created_at) values (174, 184, 446, '2019-10-22 17:24:51');
    insert into stock (id, inv_id, stock, created_at) values (175, 263, 436, '2019-09-14 17:39:38');
    insert into stock (id, inv_id, stock, created_at) values (176, 88, 334, '2019-01-18 05:17:24');
    insert into stock (id, inv_id, stock, created_at) values (177, 131, 360, '2019-12-17 11:20:44');
    insert into stock (id, inv_id, stock, created_at) values (178, 108, 161, '2019-12-09 17:41:45');
    insert into stock (id, inv_id, stock, created_at) values (179, 143, 590, '2019-06-30 07:36:17');
    insert into stock (id, inv_id, stock, created_at) values (180, 71, 248, '2019-11-20 10:25:56');
    insert into stock (id, inv_id, stock, created_at) values (181, 94, 437, '2019-12-14 16:45:58');
    insert into stock (id, inv_id, stock, created_at) values (182, 82, 410, '2019-03-27 14:38:52');
    insert into stock (id, inv_id, stock, created_at) values (183, 207, 407, '2019-08-21 01:42:41');
    insert into stock (id, inv_id, stock, created_at) values (184, 150, 249, '2019-02-20 05:08:24');
    insert into stock (id, inv_id, stock, created_at) values (185, 242, 426, '2019-08-21 20:18:52');
    insert into stock (id, inv_id, stock, created_at) values (186, 158, 511, '2019-04-17 05:41:10');
    insert into stock (id, inv_id, stock, created_at) values (187, 11, 222, '2019-06-02 18:13:51');
    insert into stock (id, inv_id, stock, created_at) values (188, 111, 408, '2019-10-10 13:58:50');
    insert into stock (id, inv_id, stock, created_at) values (189, 92, 440, '2019-10-03 14:06:06');
    insert into stock (id, inv_id, stock, created_at) values (190, 254, 372, '2019-10-24 08:39:13');
    insert into stock (id, inv_id, stock, created_at) values (191, 128, 556, '2019-10-10 07:00:15');
    insert into stock (id, inv_id, stock, created_at) values (192, 62, 418, '2019-02-02 18:05:09');
    insert into stock (id, inv_id, stock, created_at) values (193, 12, 551, '2019-10-22 10:08:06');
    insert into stock (id, inv_id, stock, created_at) values (194, 134, 581, '2019-01-07 05:30:37');
    insert into stock (id, inv_id, stock, created_at) values (195, 106, 457, '2019-02-05 12:46:10');
    insert into stock (id, inv_id, stock, created_at) values (196, 1, 456, '2019-10-22 04:53:58');
    insert into stock (id, inv_id, stock, created_at) values (197, 158, 388, '2019-02-16 18:42:33');
    insert into stock (id, inv_id, stock, created_at) values (198, 39, 316, '2019-12-22 22:54:07');
    insert into stock (id, inv_id, stock, created_at) values (199, 244, 421, '2019-02-05 14:32:38');
    insert into stock (id, inv_id, stock, created_at) values (200, 194, 282, '2019-03-13 22:09:23');
    insert into stock (id, inv_id, stock, created_at) values (201, 298, 355, '2019-07-15 14:06:51');
    insert into stock (id, inv_id, stock, created_at) values (202, 162, 111, '2019-01-25 19:10:02');
    insert into stock (id, inv_id, stock, created_at) values (203, 80, 298, '2019-07-06 21:01:05');
    insert into stock (id, inv_id, stock, created_at) values (204, 297, 478, '2019-07-11 06:55:13');
    insert into stock (id, inv_id, stock, created_at) values (205, 269, 383, '2019-04-14 05:06:07');
    insert into stock (id, inv_id, stock, created_at) values (206, 214, 116, '2019-10-21 23:40:50');
    insert into stock (id, inv_id, stock, created_at) values (207, 120, 485, '2019-08-05 00:23:03');
    insert into stock (id, inv_id, stock, created_at) values (208, 152, 220, '2019-02-22 16:39:48');
    insert into stock (id, inv_id, stock, created_at) values (209, 228, 241, '2019-07-25 08:56:54');
    insert into stock (id, inv_id, stock, created_at) values (210, 177, 211, '2019-03-13 02:29:01');
    insert into stock (id, inv_id, stock, created_at) values (211, 278, 470, '2019-01-24 12:16:27');
    insert into stock (id, inv_id, stock, created_at) values (212, 299, 351, '2019-11-22 09:25:45');
    insert into stock (id, inv_id, stock, created_at) values (213, 45, 201, '2019-06-03 23:27:02');
    insert into stock (id, inv_id, stock, created_at) values (214, 189, 293, '2019-02-03 09:56:42');
    insert into stock (id, inv_id, stock, created_at) values (215, 280, 314, '2019-10-26 17:55:13');
    insert into stock (id, inv_id, stock, created_at) values (216, 90, 594, '2019-11-12 19:52:03');
    insert into stock (id, inv_id, stock, created_at) values (217, 78, 555, '2019-08-08 15:40:47');
    insert into stock (id, inv_id, stock, created_at) values (218, 209, 114, '2019-01-03 12:21:15');
    insert into stock (id, inv_id, stock, created_at) values (219, 69, 373, '2019-09-08 08:26:27');
    insert into stock (id, inv_id, stock, created_at) values (220, 214, 371, '2019-04-28 00:06:47');
    insert into stock (id, inv_id, stock, created_at) values (221, 230, 444, '2019-10-26 15:31:44');
    insert into stock (id, inv_id, stock, created_at) values (222, 117, 357, '2019-05-13 02:50:27');
    insert into stock (id, inv_id, stock, created_at) values (223, 30, 591, '2019-06-10 03:43:45');
    insert into stock (id, inv_id, stock, created_at) values (224, 2, 104, '2019-02-07 09:34:05');
    insert into stock (id, inv_id, stock, created_at) values (225, 237, 340, '2019-12-19 12:46:43');
    insert into stock (id, inv_id, stock, created_at) values (226, 200, 356, '2019-01-26 19:32:43');
    insert into stock (id, inv_id, stock, created_at) values (227, 168, 312, '2019-11-02 15:55:04');
    insert into stock (id, inv_id, stock, created_at) values (228, 210, 401, '2019-04-12 01:34:49');
    insert into stock (id, inv_id, stock, created_at) values (229, 200, 485, '2019-09-10 00:32:41');
    insert into stock (id, inv_id, stock, created_at) values (230, 246, 507, '2019-02-24 04:56:08');
    insert into stock (id, inv_id, stock, created_at) values (231, 6, 320, '2019-08-29 16:34:52');
    insert into stock (id, inv_id, stock, created_at) values (232, 158, 496, '2019-10-02 19:09:39');
    insert into stock (id, inv_id, stock, created_at) values (233, 4, 564, '2019-08-27 20:58:12');
    insert into stock (id, inv_id, stock, created_at) values (234, 34, 170, '2019-07-16 23:06:36');
    insert into stock (id, inv_id, stock, created_at) values (235, 294, 326, '2019-04-23 06:43:00');
    insert into stock (id, inv_id, stock, created_at) values (236, 87, 336, '2019-07-30 08:43:05');
    insert into stock (id, inv_id, stock, created_at) values (237, 165, 468, '2019-11-22 05:37:14');
    insert into stock (id, inv_id, stock, created_at) values (238, 44, 419, '2019-01-13 23:24:14');
    insert into stock (id, inv_id, stock, created_at) values (239, 171, 311, '2019-01-03 08:49:28');
    insert into stock (id, inv_id, stock, created_at) values (240, 207, 471, '2019-04-01 03:25:04');
    insert into stock (id, inv_id, stock, created_at) values (241, 211, 548, '2019-12-10 19:52:22');
    insert into stock (id, inv_id, stock, created_at) values (242, 24, 356, '2019-06-09 14:16:55');
    insert into stock (id, inv_id, stock, created_at) values (243, 84, 593, '2019-02-15 11:15:19');
    insert into stock (id, inv_id, stock, created_at) values (244, 58, 270, '2019-09-03 05:11:26');
    insert into stock (id, inv_id, stock, created_at) values (245, 298, 468, '2019-08-15 19:43:34');
    insert into stock (id, inv_id, stock, created_at) values (246, 243, 428, '2019-08-27 06:31:38');
    insert into stock (id, inv_id, stock, created_at) values (247, 5, 355, '2019-05-25 14:05:32');
    insert into stock (id, inv_id, stock, created_at) values (248, 196, 526, '2019-03-27 21:08:51');
    insert into stock (id, inv_id, stock, created_at) values (249, 282, 201, '2019-05-11 02:55:43');
    insert into stock (id, inv_id, stock, created_at) values (250, 193, 301, '2019-08-28 01:54:46');
    insert into stock (id, inv_id, stock, created_at) values (251, 281, 350, '2019-09-17 00:46:17');
    insert into stock (id, inv_id, stock, created_at) values (252, 64, 495, '2019-03-18 09:59:44');
    insert into stock (id, inv_id, stock, created_at) values (253, 169, 465, '2019-12-19 13:22:57');
    insert into stock (id, inv_id, stock, created_at) values (254, 21, 573, '2019-08-17 01:30:06');
    insert into stock (id, inv_id, stock, created_at) values (255, 158, 272, '2019-04-01 02:23:27');
    insert into stock (id, inv_id, stock, created_at) values (256, 81, 344, '2019-01-01 08:16:23');
    insert into stock (id, inv_id, stock, created_at) values (257, 186, 109, '2019-11-20 16:13:31');
    insert into stock (id, inv_id, stock, created_at) values (258, 153, 571, '2019-10-06 01:08:05');
    insert into stock (id, inv_id, stock, created_at) values (259, 152, 160, '2019-09-17 02:05:15');
    insert into stock (id, inv_id, stock, created_at) values (260, 252, 582, '2019-11-30 01:33:43');
    insert into stock (id, inv_id, stock, created_at) values (261, 168, 310, '2019-02-28 05:37:01');
    insert into stock (id, inv_id, stock, created_at) values (262, 185, 245, '2019-06-23 08:15:15');
    insert into stock (id, inv_id, stock, created_at) values (263, 174, 576, '2019-10-30 08:10:41');
    insert into stock (id, inv_id, stock, created_at) values (264, 170, 418, '2019-05-15 16:49:35');
    insert into stock (id, inv_id, stock, created_at) values (265, 259, 535, '2019-07-08 08:29:45');
    insert into stock (id, inv_id, stock, created_at) values (266, 229, 182, '2019-06-10 23:19:12');
    insert into stock (id, inv_id, stock, created_at) values (267, 300, 213, '2019-04-29 02:54:25');
    insert into stock (id, inv_id, stock, created_at) values (268, 194, 295, '2019-11-14 11:51:32');
    insert into stock (id, inv_id, stock, created_at) values (269, 63, 343, '2019-01-06 22:05:46');
    insert into stock (id, inv_id, stock, created_at) values (270, 109, 120, '2019-07-20 15:05:48');
    insert into stock (id, inv_id, stock, created_at) values (271, 259, 190, '2019-11-15 14:17:48');
    insert into stock (id, inv_id, stock, created_at) values (272, 293, 312, '2019-06-05 06:50:53');
    insert into stock (id, inv_id, stock, created_at) values (273, 168, 504, '2019-04-15 13:52:44');
    insert into stock (id, inv_id, stock, created_at) values (274, 192, 162, '2019-08-01 01:22:57');
    insert into stock (id, inv_id, stock, created_at) values (275, 284, 536, '2019-10-12 05:22:16');
    insert into stock (id, inv_id, stock, created_at) values (276, 88, 579, '2019-09-27 07:57:53');
    insert into stock (id, inv_id, stock, created_at) values (277, 259, 219, '2019-06-10 09:25:57');
    insert into stock (id, inv_id, stock, created_at) values (278, 126, 516, '2019-01-20 11:49:44');
    insert into stock (id, inv_id, stock, created_at) values (279, 290, 378, '2019-11-27 10:29:38');
    insert into stock (id, inv_id, stock, created_at) values (280, 251, 507, '2019-04-11 06:29:58');
    insert into stock (id, inv_id, stock, created_at) values (281, 259, 391, '2019-12-09 22:37:56');
    insert into stock (id, inv_id, stock, created_at) values (282, 58, 413, '2019-03-18 01:24:40');
    insert into stock (id, inv_id, stock, created_at) values (283, 116, 591, '2019-02-10 06:31:16');
    insert into stock (id, inv_id, stock, created_at) values (284, 67, 449, '2019-09-05 17:21:21');
    insert into stock (id, inv_id, stock, created_at) values (285, 205, 564, '2019-01-19 20:17:16');
    insert into stock (id, inv_id, stock, created_at) values (286, 104, 390, '2019-08-24 20:15:38');
    insert into stock (id, inv_id, stock, created_at) values (287, 229, 101, '2019-06-01 08:40:14');
    insert into stock (id, inv_id, stock, created_at) values (288, 49, 272, '2019-04-03 19:34:04');
    insert into stock (id, inv_id, stock, created_at) values (289, 215, 251, '2019-09-17 13:40:28');
    insert into stock (id, inv_id, stock, created_at) values (290, 20, 103, '2019-01-12 16:41:02');
    insert into stock (id, inv_id, stock, created_at) values (291, 221, 393, '2019-01-05 14:01:35');
    insert into stock (id, inv_id, stock, created_at) values (292, 189, 251, '2019-01-09 21:59:21');
    insert into stock (id, inv_id, stock, created_at) values (293, 217, 403, '2019-06-17 01:11:55');
    insert into stock (id, inv_id, stock, created_at) values (294, 177, 135, '2019-06-06 22:24:52');
    insert into stock (id, inv_id, stock, created_at) values (295, 214, 566, '2019-08-18 05:36:56');
    insert into stock (id, inv_id, stock, created_at) values (296, 156, 188, '2019-08-27 12:52:49');
    insert into stock (id, inv_id, stock, created_at) values (297, 94, 325, '2019-05-12 22:52:10');
    insert into stock (id, inv_id, stock, created_at) values (298, 142, 129, '2019-03-25 23:35:05');
    insert into stock (id, inv_id, stock, created_at) values (299, 133, 285, '2019-04-08 10:44:06');
    insert into stock (id, inv_id, stock, created_at) values (300, 103, 477, '2019-09-10 00:36:03'); """)
    cur.commit()


    # cur.execute("SELECT * FROM sales")
    # cur.execute("""SELECT EXTRACT (MONTHS FROM sales.created_at) AS months,
    # SUM(sales.quantity) as "Total Sales" 
    # FROM sales
    # GROUP BY 
    # months 
    # ORDER BY 
    # months""")

    cur.execute("""SELECT EXTRACT (MONTHS FROM sales.created_at) AS months,SUM(sales.quantity) as "Total Sales" FROM public.sales GROUP BY months ORDER BY  months""")
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
    