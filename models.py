import MySQLdb

def get_conn():
    host='127.0.0.1'
    port=3306
    db='csuspider'
    user='spider'
    password='xyz'
    conn=MySQLdb.connect(
        host=host,
        user=user,
        passwd=password,
        db=db,
        port=port,
        charset='utf8'
    )
    return conn

def get_all_locations():
    conn=get_conn()
    cursor=conn.cursor()
    sql="select location_id,title,longitude,latitude from location"
    cursor.execute(sql)
    rows=cursor.fetchall()
    locations=[]
    for row in rows:
        dic={}
        dic['location_id']=row[0]
        dic['title']=row[1].encode('utf-8')
        dic['longitude']=row[2]
        dic['latitude']=row[3]
        locations.append(dic)
    conn.commit()
    cursor.close()
    conn.close()
    return locations

def parse_info_dict(rows):
    results=[]
    for row in rows:
        dic={}
        dic['aca_id']=row[0]
        dic['title']=row[1].encode('utf-8')
        dic['url']=row[2].encode('utf-8')
        dic['time']=row[3].encode('utf-8')
        dic['location']=row[4].encode('utf-8')
        dic['longitude']=row[5]
        dic['latitude']=row[6]
        dic['academy']=row[7].encode('utf-8')
        dic['type']=row[8].encode('utf-8')
        dic['html_content']=row[9].encode('utf-8')
        dic['date_sort']=row[10].encode('utf-8')
        results.append(dic)
    return results

def get_all_infos():
    conn=get_conn()
    cursor=conn.cursor()
    sql="""
        SELECT a.aca_id,a.title,a.url,a.time,a.location,l.longitude,l.latitude,a.academy,a.type,a.html_content,a.date_sort
        FROM academic a
        INNER JOIN location l
        ON a.location_id=l.location_id
        ORDER BY date_sort DESC"""
    cursor.execute(sql)
    rows=cursor.fetchall()
    results=parse_info_dict(rows)
    conn.commit()
    cursor.close()
    conn.close()
    return results


def search_from_string(string):
    conn=get_conn()
    cursor=conn.cursor()
    sql="""
        SELECT a.aca_id,a.title,a.url,a.time,a.location,l.longitude,l.latitude,a.academy,a.type,a.html_content,a.date_sort
        FROM academic a
        INNER JOIN location l
        ON a.location_id=l.location_id
        WHERE a.title REGEXP "%s" OR a.location REGEXP "%s" OR a.academy REGEXP "%s" OR a.html_content REGEXP "%s"
        ORDER BY date_sort DESC"""%(string,string,string,string)
    cursor.execute(sql)
    rows=cursor.fetchall()
    results=parse_info_dict(rows)
    conn.commit()
    cursor.close()
    conn.close()
    return results

def search_from_type(info_type):
    conn=get_conn()
    cursor=conn.cursor()
    sql="""
        SELECT a.aca_id,a.title,a.url,a.time,a.location,l.longitude,l.latitude,a.academy,a.type,a.html_content,a.date_sort
        FROM academic a
        INNER JOIN location l
        ON a.location_id=l.location_id
        WHERE a.type REGEXP "%s"
        ORDER BY date_sort DESC"""%(info_type)
    cursor.execute(sql)
    rows=cursor.fetchall()
    results=parse_info_dict(rows)
    conn.commit()
    cursor.close()
    conn.close()
    return results

def search_from_date(begin,end):
    conn=get_conn()
    cursor=conn.cursor()
    sql="""
        SELECT a.aca_id,a.title,a.url,a.time,a.location,l.longitude,l.latitude,a.academy,a.type,a.html_content,a.date_sort
        FROM academic a
        INNER JOIN location l
        ON a.location_id=l.location_id
        WHERE a.date_sort BETWEEN "%s" AND "%s"
        ORDER BY date_sort DESC"""%(begin,end)
    cursor.execute(sql)
    rows=cursor.fetchall()
    results=parse_info_dict(rows)
    conn.commit()
    cursor.close()
    conn.close()
    return results

def search_from_location_id(location_id):
    conn=get_conn()
    cursor=conn.cursor()
    sql="""
        SELECT a.aca_id,a.title,a.url,a.time,a.location,l.longitude,l.latitude,a.academy,a.type,a.html_content,a.date_sort
        FROM academic a
        INNER JOIN location l
        ON a.location_id=l.location_id
        WHERE a.location_id="%s"
        ORDER BY date_sort DESC"""%(location_id)
    cursor.execute(sql)
    rows=cursor.fetchall()
    results=parse_info_dict(rows)
    conn.commit()
    cursor.close()
    conn.close()
    return results


