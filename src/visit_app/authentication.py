from rest_framework.authentication import BaseAuthentication

from visit_app.models import Employee


class PhoneAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = request.headers.get("Authorization")
        if not auth or not auth.startswith("Phone "):
            return None
        try:
            phone_number = auth.split(" ")[1]
            employee = Employee.objects.get(phone_number=phone_number)
        except (IndexError, Employee.DoesNotExist):
            return None
        return (employee, None)
