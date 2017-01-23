from django.shortcuts import render
import json
from django.http import HttpResponse
from .models import Muppet

def index(request):
    if request.method == 'GET':
        muppets = Muppet.objects.all()
        return HttpResponse(json.dumps({
              "total": len(muppets),
              "muppets": [
                  m.json_output() for m in muppets
              ]
        }), content_type='text/json')
    elif request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))
        m = Muppet.objects.create(name=body['name'], occupation=body['occupation'])
        return HttpResponse(json.dumps(m.json_output()), content_type='text/json')

def muppet(request, id):
    muppet = Muppet.objects.get(id=id)
    if request.method == 'DELETE':
        muppet.delete()
        return HttpResponse(json.dumps({'status': 'ok'}), content_type='text/json')
    if request.method == 'PUT':
        body = json.loads(request.body.decode('utf-8'))
        for key, val in body.items():
            setattr(muppet, key, val)
            muppet.save()
    return HttpResponse(json.dumps(muppet.json_output()), content_type='text/json')