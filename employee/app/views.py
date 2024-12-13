from django.shortcuts import render,redirect
from .forms import EmployeeForm

def index(request):
	form = EmployeeForm()
	if request.method == 'POST':
		form = EmployeeForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('manager_list')
	context={'form':form}
	return render(request, 'manager_add.html',context)
def list(request):
	list =EmployeeForm.objects.all()
	context={'list':list}
	return render(request, 'manager_list.html',context)