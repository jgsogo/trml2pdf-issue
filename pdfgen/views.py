#!/usr/bin/env python
# -*- coding: utf-8 -*-

import trml2pdf
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import render_to_string


class PDFView(View):
    template_name = 'rml/template.rml'

    def get_template_name(self):
        if self.template_name is None:
            raise ImproperlyConfigured('%s requires either a definition of '
                                       'template_name or an implementation of '
                                       'get_template_name()'
                                       % self.__class__.__name__)
        return self.template_name

    def get_context_data(self, **kwargs):
        return {'filename': 'report.pdf',
                'user': 'María'}

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context.setdefault('filename', 'report.pdf')

        rml = render_to_string(self.get_template_name(), context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = ('filename="report.pdf"')
        response.write(trml2pdf.parseString(str(rml)))
        return response

