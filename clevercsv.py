import json,requests,base64,csv

def listsections(token='token'):
    """Given a client id and client secret, list available district tokens"""
    if token == 'token':
        print 'enter a real token!'
        return

    #open a csv
    writer = open(('shared_sections_%s.csv' % (token)), 'w')
    cwriter = csv.writer(writer)
    headers = ['section_id','course_number','course_name','section_name','building_id','building_name'] #buiding id => section.school, section_name => section.name, building_name maps to school.name 
    cwriter.writerow(headers)
    #for each page of sections data, collect and move to next
    #print token
    base = 'https://api.clever.com'
    endpoint = '/v1.1/sections'
    next_page = True
    while next_page:
        r = requests.get(('%s%s' % (base,endpoint)), headers={'Authorization':('Bearer %s')%(token)})
        js = r.json()
        data = js['data']
        for section in data:
            sectiondat = section['data']
            #print (('%s/v1.1/schools/%s') % (base,sectiondat['school']))
            s = requests.get((('%s/v1.1/schools/%s') % (base,sectiondat['school'])), headers={'Authorization':('Bearer %s')%(token)})
            #print s 
            jss = s.json()
            data = jss['data']
            school_name = data['name']
            row = [sectiondat['id'],sectiondat['course_number'],sectiondat['course_name'],sectiondat['name'],sectiondat['school'],school_name]
            cwriter.writerow(row)
        newendpoint = endpoint
        for link in js['links']:
            if(link['rel'] == 'next'):
                newendpoint = link['uri']
        if endpoint == newendpoint:
            next_page = False
        endpoint = newendpoint
                
    #print data
    print('done!')

def listenrollments(token='token'):
    """Given a client id and client secret, list available district tokens"""
    if token == 'token':
        print 'enter a real token!'
        return

    #open a csv
    writer = open(('shared_enrollments_%s.csv' % (token)), 'w')
    cwriter = csv.writer(writer)
    headers = ['school_id','section_id','student_id']
    cwriter.writerow(headers)
    #for each page of sections data, collect and move to next
    #print token
    base = 'https://api.clever.com'
    endpoint = '/v1.1/sections'
    next_page = True
    while next_page:
        r = requests.get(('%s%s' % (base,endpoint)), headers={'Authorization':('Bearer %s')%(token)})
        js = r.json()
        data = js['data']
        for section in data:
            sectiondat = section['data']
            students = sectiondat['students']
            for student in students:
                row = [sectiondat['school'],sectiondat['id'],student]
                cwriter.writerow(row)
        newendpoint = endpoint
        for link in js['links']:
            if(link['rel'] == 'next'):
                newendpoint = link['uri']
        if endpoint == newendpoint:
            next_page = False
        endpoint = newendpoint
                
    #print data
    print('done!')

def liststudents(token='token'):
    """Given a client id and client secret, list available district tokens"""
    if token == 'token':
        print 'enter a real token!'
        return

    #open a csv
    writer = open(('all_students_%s.csv' % (token)), 'w')
    cwriter = csv.writer(writer)
    headers = ['id','sis_id','first_name','last_name','student_number','school','grade','dob','email','state_id']
    cwriter.writerow(headers)
    #for each page of sections data, collect and move to next
    #print token
    base = 'https://api.clever.com'
    endpoint = '/v1.1/students'
    next_page = True
    while next_page:
        r = requests.get(('%s%s' % (base,endpoint)), headers={'Authorization':('Bearer %s')%(token)})
        js = r.json()
        data = js['data']
        for student in data:
            studat = student['data']
            names = studat['name']
            row = [studat['id'],studat['sis_id'],names['first'],names['last'],studat['student_number'],studat['school'],studat['grade'],studat['dob'],studat['email'],studat['state_id']]
            cwriter.writerow(row)
        newendpoint = endpoint
        for link in js['links']:
            if(link['rel'] == 'next'):
                newendpoint = link['uri']
        if endpoint == newendpoint:
            next_page = False
        endpoint = newendpoint
                
    #print data
    print('done!')