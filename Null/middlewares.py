from django.utils.deprecation import MiddlewareMixin

class SalaryMiddleware(MiddlewareMixin):
    def procces_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            year = int(request.POST.get('year'))
            if year < 1:
                return HttpResponseBadRequest('Не может быть меньше 1')
            elif year > 1 and year < 3:
                request.salary = 100
            elif year > 3 and year < 8:
                request.salary = 200
            elif year > 8 and year <= 15:
                request.salary = 300
            else:
                request.salary = 400
