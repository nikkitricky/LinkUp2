# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def Index(request):
    template=loader.get_template("recruit/index.html")
    result=template.render()
    return HttpResponse(result)