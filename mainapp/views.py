from django.http import HttpResponse
from django.views.generic import TemplateView
from datetime import datetime


# class HelloWorldView(View):
#
#     def get(self, request, *args, **kwargs):
#         return HttpResponse("Hello world!")
#
# # def hello_world(request):
# #     return HttpResponse("Hello world!")
#
# def blog(request, **kwargs):
#     return HttpResponse(f'{kwargs}')

class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['contacts'] = [
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHcrhA',
                'city': 'Санкт‑Петербург',
                'phone': '+7-999-11-11111',
                'email': 'geeklab@spb.ru',
                'address': 'территория Петропавловская крепость, 3Ж',
            },
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHX3xB',
                'city': 'Казань',
                'phone': '+7-999-22-22222',
                'email': 'geeklab@kz.ru',
                'address': 'территория Кремль, 11, Казань, Республика Татарстан, Россия',
            },
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHh9kD',
                'city': 'Москва',
                'phone': '+7-999-33-33333',
                'email': 'geeklab@msk.ru',
                'address': 'Красная площадь, 7, Москва, Россия',
            },
        ]
        return context_data

class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'

class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'

class IndexView(TemplateView):
    template_name = 'mainapp/index.html'

class LoginView(TemplateView):
    template_name = 'mainapp/login.html'

class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # context_data['title'] = 'Новость раз'
        # context_data['preview'] = 'Превью к новости раз'
        # context_data['date'] = '2022-01-01'
        context_data['object_list'] = [
            {
                'title': 'Новость раз',
                'preview': 'Превью к новости раз',
                'date': datetime.now()
            },
            {
                'title': 'Новость два',
                'preview': 'Превью к новости два',
                'date': datetime.now()
            },
            {
                'title': 'Новость три',
                'preview': 'Превью к новости три',
                'date': datetime.now()
            },
            {
                'title': 'Новость четыре',
                'preview': 'Превью к новости четыре',
                'date': datetime.now()
            },
            {
                'title': 'Новость пять',
                'preview': 'Превью к новости пять',
                'date': datetime.now()
            },
            {
                'title': 'Новость шесть',
                'preview': 'Превью к новости шесть',
                'date': datetime.now()
            },

        ]


        return context_data

