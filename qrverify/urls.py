# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from qrverify.views import Verify

urlpatterns = patterns('',
                       url(r'^$', Verify.as_view(), name='Verify'),
                      )
