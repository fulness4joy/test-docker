from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from time import sleep
# from urllib.parse import unquote

# def index(request):
#     polls = Poll.objects.all()
#     paginator = Paginator(polls, 2)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     return render(request, 'polls/index.html', {'page_obj': page_obj})


class PollsList(ListView):
    model = Poll
    template_name = 'polls/index.html'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        print("queryset:", queryset)
        search_query = self.request.GET.get('q', '').lower()
        if search_query:
            # search_query = unquote(search_query)
            queryset = queryset.filter(title__icontains=search_query.lower())
            print(search_query, queryset)
        return queryset

    def get(self, request):
        super().get(request)

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            queryset = self.get_queryset()
            context = {
                'page_obj': self.paginate_queryset(queryset, self.paginate_by)[2]
            }
            return render(request, 'polls/list.html', context=context)

        return render(request, self.template_name, context=self.get_context_data())

class PollDetail(DetailView):
    model = Poll
    template_name = 'polls/detail.html'
    context_object_name = 'poll'
    

class PollCreate(CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'polls/form.html'
    success_url = reverse_lazy('index')

class AjaxTestView(TemplateView):
    template_name = 'polls/ajax_test.html'


async def ajax_request(request):
    sleep(1)
    return HttpResponse("Simple Answer!")





















@csrf_exempt
def ajax_request_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        return JsonResponse({'message': 'Data received', 'title': title, 'body': body})
    return JsonResponse({'error': 'Invalid request'}, status=400)