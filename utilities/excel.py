import csv
from django.http import HttpResponse, JsonResponse, FileResponse        
from datetime import datetime    
def exporttoexcel(rows,filename):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="'+filename+str(datetime.now().date())+'.csv"'
    writer = csv.writer(response)
    for row in rows:
        for colmn in row:
            writer.writerow(colmn)
    return response


def importtoexcel(csv_file):
    csv_row_data = [row for row in csv.reader(csvfile.read().splitlines())]
    return csv_row_data

    
def mass_sms(phone_numbers,message,sender):
    phone_nos = ''
    for phone_number in phone_numbers:
        phone_nos += phone_number  + ','
    phone_nos = phone_nos[:-1]
    API_KEY = '99461AkdT30Wn5662bdea'
    url = 'http://api.msg91.com/api/sendhttp.php?authkey=' + API_KEY + '&mobiles=' + phone_nos + '&message=%s&sender=%s&route=4&country=91' % (message,sender)
    print url
    proxy = urllib2.ProxyHandler({})
    auth = urllib2.HTTPBasicAuthHandler()
    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    f = urllib2.urlopen(url)
    return HttpResponse('done')




'''if request.method == 'POST':
        post = request.POST
        data = {}
        if post['query'] == 'exportfee':
            students = Student.objects.filter(batch__batchId = int(post['batch']))
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
            writer = csv.writer(response)
            firstrow = ['Name', 'StudentId']
            writer.writerow(firstrow)
            for student in students:
                writer.writerow([student.studentName, student.studentId])
            return response
            '''