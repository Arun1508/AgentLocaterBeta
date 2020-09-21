from django.shortcuts import render
from django.db.models import Q
from .models import AgentLocations
from . import models
import os,csv
from django.contrib.auth.models import User
# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def bulk_create():
    filepath =os.path.join(BASE_DIR,'agents.tsv')
    with open(filepath, 'r+') as filedata:
        rows =csv.reader(filedata, delimiter="\t")
        rows = list(rows)
        rows.pop(0)
        instances =[
            models.AgentLocations(
                id = row[0],
                name = row[1],
                Address = row[2],
                city = row[3],
                zipcode = row[4],
                state = row[5]
            )
            for row in rows
        ]
        models.AgentLocations.objects.bulk_create(instances)


def home(request):

    if request.method == "POST":
        count = AgentLocations.objects.count()
        # IF DB IS EMPTY INSERT DATA FILE TSV FROM PROJECT ROOT DIR
        if count == 0:
            bulk_create()
        zipc = int(request.POST['location'])
        print(zipc)
        record_count = AgentLocations.objects.filter(zipcode = zipc).count()
        if record_count < 100:
            n = 10
            while n <= 100:
                record_count= AgentLocations.objects.filter(zipcode__gte = zipc - n ,zipcode__lte = zipc + n).count()
                if record_count >= 100:

                    print("int loop", n)
                    break
                n += 10
            data = AgentLocations.objects.filter(zipcode__gte=zipc - n, zipcode__lte=zipc + n)
        return render(request,'home.html', {'data':data})
    else:
        disZip = AgentLocations.objects.values('zipcode').order_by('zipcode').distinct()
        print(disZip)
        return render(request,'home.html', {'disZip': disZip})