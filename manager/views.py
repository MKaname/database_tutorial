from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from manager.models import Person, Worker


class WorkerListView(TemplateView):
    template_name = "worker_list.html"

    def get(self, request, *args, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)

        workers = Worker.objects.filter(person__sex=Person.WOMAN)
        context['workers'] = workers
        return render(self.request, self.template_name, context)
