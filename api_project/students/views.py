import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student

@csrf_exempt

def student_api(request):

    if request.method == "GET":
        students = list(Student.objects.values())
        return JsonResponse(students, safe=False)

    elif request.method == "POST":
        data = json.loads(request.body)

        student = Student.objects.create(
            name = data['name'],
            age = data['age'],
            department = data['department']
        )

        return JsonResponse({"id" : student.id}, status=201)

    elif request.method == 'PUT':
        data = json.loads(request.body)

        student = Student.objects.get(id = data['id'])

        student.name = data['name']
        student.age = data['age']
        student.department = data['department']

        student.save()

        return JsonResponse({"id" : student.id})

    elif request.method == 'DELETE':
        data = json.loads(request.body)

        student = Student.objects.get(id = data['id'])
        student.delete()
        return JsonResponse({"message" : "Deleted"})


# Create your views here.
