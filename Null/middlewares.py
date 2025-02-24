from django.utils.deprecation import MiddlewareMixin

class ExperienceSalaryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            user = request.user
            experience = user.profile.experience_years
            if experience < 2:
                user.profile.salary = 50000
            elif 2 <= experience < 5:
                user.profile.salary = 70000
            else:
                user.profile.salary = 100000
            user.profile.save()
