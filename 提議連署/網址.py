# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from 提議連署.介面 import 提議網頁
from 提議連署.介面 import QRCode
from 提議連署.介面 import ShopQRCode


urlpatterns = patterns('',
	url(r'^QRCode/(?P<data>.*)$', QRCode, name='QRCode'),
	url(r'^ShopQRCode$', ShopQRCode.as_view(), name='ShopQRCode'),
	url(r'^.*$', 提議網頁.as_view(), name='首頁'),
)
