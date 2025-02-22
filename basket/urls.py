from django.urls import path
from .views import ParsedDataListView, ParserView

urlpatterns = [
    path('parsed_data/', ParsedDataListView.as_view(), name='parsed_data_list'),
    path('parser/', ParserView.as_view(), name='parser_form'),
]
