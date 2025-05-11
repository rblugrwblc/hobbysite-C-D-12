from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.views.generic import UpdateView, CreateView, ListView, DetailView
from .models import Commission, Job, JobApplication
from django.contrib.auth.mixins import LoginRequiredMixin

class CommissionListView(ListView):
    model = Commission
    template_name = "commissions_list.html"
    context_object_name = "commissions"

class CommissionDetailView(DetailView):
    model = Commission
    template_name = "commissions_detail.html"
    context_object_name = "commission"

class CommissionUpdateView(UpdateView):
    model = Commission
    fields = ["title", "description", "status"]
    template_name_suffix = "_update_form"

class CommissionCreateView(CreateView):
    model = Commission
    fields = ["title", "description", "status"]
    template_name_suffix = "_create_form"

class JobView(DetailView):
    model = Job
    template_name = "job_detail.html"
    context_object_name = "job"

    def post(self, request, *args, **kwargs):
        if "accept" in request.POST:
            app_id = request.POST.get("accept")
            application = get_object_or_404(JobApplication, id=app_id)
            application.accept_job()

        elif "reject" in request.POST:
            app_id = request.POST.get("reject")
            application = get_object_or_404(JobApplication, id=app_id)
            application.reject_job()




