from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from factotum.apps.finance.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("upload-csv/", self.upload_csv, name="upload-csv"),
        ]
        return my_urls + urls

    def upload_csv(self, request):
        context = dict(
            self.admin_site.each_context(request),
        )
        return TemplateResponse(request, "admin/finance/upload-csv.html", context)


admin.site.register(Transaction, TransactionAdmin)
