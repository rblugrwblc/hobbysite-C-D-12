from django.db import models
from user_management.models import Profile
from django.urls import reverse

class Commission(models.Model):
    class CommissionStatusOptions(models.TextChoices):
        OPEN = "Open"
        FULL = "Full"
        COMPLETED = "Completed"
        DISCONTINUED = "Discontinued"
    title = models.CharField(max_length = 255)
    description = models.TextField()
    status = models.CharField(
        max_length=15,
        default=CommissionStatusOptions.OPEN,
        choices=CommissionStatusOptions,
    )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE, 
        related_name="commissions",
    )

    class Meta:
        ordering = ["status","-created_on"]

    def __str__(self):
        return self.title    
    
    def get_absolute_url(self):
        return reverse("commission_detail", kwargs={"pk": self.pk})
    
    def update_job_full_status(self): 
        """Updates Commission Status when all jobs are filled"""
        if self.status in [
            self.CommissionStatusOptions.COMPLETED, 
            self.CommissionStatusOptions.DISCONTINUED
        ]:
            return
        if not self.jobs.filter(status=Job.JobStatusOptions.OPEN).exists():
            self.status = self.CommissionStatusOptions.FULL
            self.save()
    
class Job(models.Model):
    class JobStatusOptions(models.TextChoices):
        OPEN = "Open"
        FULL = "Full"
    commission = models.ForeignKey(
        Commission,
        on_delete=models.CASCADE,
        related_name = "jobs"
    )
    role = models.CharField(max_length=255)
    manpower_required = models.PositiveIntegerField()
    status = models.CharField(
        max_length=15,
        default=JobStatusOptions.OPEN,
        choices=JobStatusOptions,
    )
    class Meta:
        ordering = ["-status", "-manpower_required", "role"]

    def __str__(self):
        return f"{self.role} for {self.commission.title}"

    def accept_applicant(self):
        if self.status == self.JobStatusOptions.OPEN and self.manpower_required > 0:
            self.manpower_required -= 1
            if self.manpower_required == 0:
                self.set_full()
            self.save()

    def set_full(self):
        self.status = self.JobStatusOptions.FULL
        self.save()
        self.commission.fill_job()
    
    def is_full(self):
        return self.status == self.JobStatusOptions.FULL


class JobApplication(models.Model):
    class ApplicationStatusOptions(models.TextChoices):
        PENDING = "Pending"
        ACCEPTED = "Accepted"
        REJECTED = "Rejected"
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    applicant = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="applications"
    )
    status = models.CharField(
        max_length=15,
        default=ApplicationStatusOptions.PENDING,
        choices=ApplicationStatusOptions,
    )
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["status", "-applied_on"]
    
    def __str__(self):
        return f"{self.applicant.username} applied to {self.job.role}"

    def accept_application(self):
        self.status = self.ApplicationStatusOptions.ACCEPTED
        self.save()
        self.job.accept_applicant()

    def reject_application(self):
        self.status = self.ApplicationStatusOptions.REJECTED
        self.save()