from django.shortcuts import render
from myapp.models import Student

# Create your views here.
def fakerview(request):
	s=Student.objects.all()
	d={'stud':s}
	return render(request,'htmlpage/output.html',d)

