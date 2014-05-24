# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect, render
from django.template import RequestContext, loader
from django.utils.decorators import method_decorator
from django.views import generic
from qrverify.models import Shop
import urllib
from django.views.generic.base import View
import qrcode
import io

class Verify(View):
    def get(self, request, *args, **kwargs):
        uid=request.GET.get("uid", None)
        if not uid:
            template = loader.get_template('qrverify/post.html')
            content = RequestContext(request, {})
            return HttpResponse(template.render(content))
        item = Shop.objects.get(uid=uid)
        data = { "name": item.name, "address": item.address, "phone": item.address} 
        import json
        return HttpResponse(json.dumps(data), content_type='application/json')
    def post(self, request, *args, **kwargs):
        params=dict(request.POST)
        wanted = 'name={0}, address={1}, phone={2}'.format(params['name'], params['address'], params['phone'])
        print (wanted)
        item = Shop(name = params['name'], address = params['address'], phone = params['phone'])
        item.save()
        encoded_str = "http:127.0.0.1:8000/qrverify?uid={0}".format(item.pk)
        png = qrcode.make(encoded_str)

        reps = HttpResponse()
        png.save(reps , "PNG")
        reps['Content-Type'] = 'image/png'
        return reps