from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect
from django.views.generic import UpdateView, CreateView, ListView, DetailView
from .models import Commission, Job, JobApplication
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Case, When, IntegerField
from django.urls import reverse_lazy
from django.forms.models import inlineformset_factory
from django.contrib import messages

class CommissionListView(ListView):
    model = Commission
    template_name = "commissions_list.html"
    context_object_name = "commissions"

    def get_queryset(self):
        return (
            Commission.objects.all()
            .annotate(
                status_order=Case(
                    When(status="Open", then=0),
                    When(status="Full", then=1),
                    When(status="Completed", then=2),
                    When(status="Discontinued", then=3),
                    output_field=IntegerField(),
                )
            )
            .order_by("status_order", "-created_on")
        )

class CommissionDetailView(DetailView):
    model = Commission
    template_name = "commissions_detail.html"
    context_object_name = "commission"
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()  # get the Commission object
        job_id = request.POST.get("job_id")
        job = get_object_or_404(Job, id=job_id, commission=self.object)

        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to apply.")
            return redirect(request.path)

        user_profile = request.user.profile

        if job.is_full():
            messages.error(request, "This job is already full.")
        elif job.applications.filter(applicant=user_profile).exists():
            messages.warning(request, "You've already applied to this job.")
        elif self.object.creator == user_profile:
            messages.error(request, "You cannot apply to your own commission.")
        else:
            JobApplication.objects.create(job=job, applicant=user_profile)
            messages.success(request, "Application submitted!")

        return redirect(request.path)

# Create the inline formset
JobFormSet = inlineformset_factory(
    Commission,
    Job,
    fields=["role", "manpower_required", "status"],
    extra=1,  # number of blank job forms shown to add a job
    can_delete=True,
)

class CommissionUpdateView(UpdateView):
    model = Commission
    fields = ["title", "description", "status"]
    template_name_suffix = "_update_form"
    
    def get_success_url(self):
        return reverse_lazy("commissions:detail_view", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["job_formset"] = JobFormSet(self.request.POST, instance=self.object)
        else:
            context["job_formset"] = JobFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        job_formset = context["job_formset"]
        if form.is_valid() and job_formset.is_valid():
            self.object = form.save()
            job_formset.instance = self.object
            job_formset.save()
            self.object.update_job_full_status()
            return redirect(self.get_success_url())
        else:
            return self.form_invalid(form)

class CommissionCreateView(LoginRequiredMixin,CreateView):
    model = Commission
    fields = ["title", "description", "status"]
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("commissions:list_view")
    def form_valid(self, form):
        form.instance.creator = self.request.user.profile
        return super().form_valid(form)

class JobView(LoginRequiredMixin,DetailView):
    model = Job
    template_name = "job_detail.html"
    context_object_name = "job"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        job = self.object
        if "accept" in request.POST:
            app_id = request.POST.get("accept")
            application = get_object_or_404(JobApplication, id=app_id)
            application.accept_application()   

        elif "reject" in request.POST:
            app_id = request.POST.get("reject")
            application = get_object_or_404(JobApplication, id=app_id)
            application.reject_application()
        
        return redirect("commissions:job_view", pk=job.pk)
    Job.objects.annotate(
    status_order=Case(
        When(status="Open", then=0),
        When(status="Full", then=1),
        output_field=IntegerField(),
        )
    ).order_by("status_order", "-manpower_required", "role")
    
        




