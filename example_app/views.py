from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from example_app.models import ExampleModel
from example_app.forms import ExampleForm, ExampleFilterForm


class ExampleCreateView(CreateView):
    form_class = ExampleForm
    model = ExampleModel
    template_name = 'example_app/example_create.html'
    success_url = reverse_lazy('example_list')


class ExampleUpdateView(UpdateView):
    form_class = ExampleForm
    model = ExampleModel
    template_name = 'example_app/example_create.html'
    success_url = reverse_lazy('example_list')


class ExampleDeleteView(DeleteView):
    model = ExampleModel
    success_url = reverse_lazy('example_list')


class ExampleListView(ListView):
    model = ExampleModel
    template_name = 'example_app/example_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = getattr(self, 'form', ExampleFilterForm())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        from_date = self.request.GET.get('from_date')
        to_date = self.request.GET.get('to_date')
        if from_date or to_date:
            self.form = ExampleFilterForm({"from_date": from_date, "to_date": to_date})
            if self.form.is_valid():
                queryset = queryset.filter(
                    nepali_date__range=(self.form.cleaned_data['from_date'], self.form.cleaned_data['to_date'])
                )
        return queryset
