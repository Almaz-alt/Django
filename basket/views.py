from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import ParsedData
from .forms import ParserForm


class ParsedDataListView(ListView):
    model = ParsedData
    template_name = 'parsed_data_list.html'
    context_object_name = 'parsed_data'


class ParserView(CreateView):
    form_class = ParserForm
    template_name = 'parser_form.html'
    success_url = '/parsed_data/'

    def form_valid(self, form):
        from .parser import parsing_rezka
        parsed_data = parsing_rezka()
        media_type = form.cleaned_data['media_type']
        for item in parsed_data:
            ParsedData.objects.create(
                title=item['title'],
                link='https://rezka.ag/',
                summary='',
                media_type=media_type
            )
        return super().form_valid(form)
