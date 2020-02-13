from flask import Flask, render_template
import pygal
import psycopg2

app = Flask(__name__)
# conn = psycopg2.connect("dbname='postgres' user='postgres' password='dbpass'")

@app.route('/', methods=['GET','POST'])
def home():

    conn = psycopg2.connect("dbname=d2olmc1g1ep2um user=lbklkxnrccbafn host=ec2-18-210-51-239.compute-1.amazonaws.com password=9ba141e9e03ccd7f51b9f445e0a471ae284159ab97b3997b85e6367a2417634c")
    cur = conn.cursor()
    cur.execute("DROP TABLE sales") 
    conn.commit()
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
    

    # cur.execute("SELECT * FROM sales")
    # SELECT EXTRACT (MONTHS FROM sales.created_at) AS months,
    # SUM(sales.quantity) as "Total Sales" 
    # FROM sales
    # GROUP BY 
    # months 
    # ORDER BY 
    # months""")
    records = cur.fetchall()

    # xlabels = []
    # sales = []

    # for i in records:
    #     xlabels.append(i[0])
    #     sales.append(i[1])




    line_chart = pygal.Line()
    line_chart.title = 'Sales total in each month'
    line_chart.x_labels = map(str, records)
    # line_chart.add('Sales', sales)
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
    # conn.commit()
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
    