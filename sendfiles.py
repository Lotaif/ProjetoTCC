import mysql.connector
import os

def send_files():
    db = mysql.connector.connect(
        host="70.37.66.33",
        user="mapscovid",
        passwd="mapscovid",
        database="casos_covid"
    )

    cursor = db.cursor()

    files_sql = []
    cwd = os.getcwd() + '\\ready_files\\'
    
    for file in os.listdir(cwd):
        if file.endswith("_finalcsv.csv"):
            files_sql.append(os.path.join(cwd, file).replace('\\', '/'))

    for file in files_sql:
        print("começou inserção arquivo " + file)
        load_file = "LOAD DATA LOCAL INFILE '" + file + "' INTO TABLE srag FIELDS TERMINATED BY ';' LINES TERMINATED BY '\n' IGNORE 1 ROWS;"

        cursor.execute(load_file)
        db.commit()
        print("terminou inserção arquivo " + file)

    print("começou inserção cnes")
    load_file = "LOAD DATA LOCAL INFILE '" + cwd.replace('\\', '/') + "out-2.csv' INTO TABLE cnes FIELDS TERMINATED BY ';' LINES TERMINATED BY '\n' IGNORE 1 ROWS;"
    print(load_file)
    cursor.execute(load_file)
    db.commit()
    print("terminou inserção cnes")