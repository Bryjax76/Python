from django.shortcuts import render, redirect, get_object_or_404
from service.models import Notice
from django.db.models import Q
from service.forms import SearchForm, NoticeForm
from django.contrib.auth.decorators import login_required


def list_(request):
    form = SearchForm(request.POST)
    notices = None
    if form.is_valid():
        notice_filter = Q()
        if form.cleaned_data["title"] != "":
            notice_filter &= Q(Q(title__icontains=form.cleaned_data["title"]))
        if form.cleaned_data["autor"] != "":
            notice_filter &= Q(Q(autor__icontains=form.cleaned_data["autor"]))
        if form.cleaned_data["status"]:
            notice_filter &= Q(status=form.cleaned_data["status"])
        if form.cleaned_data["category"]:
            notice_filter &= Q(category=form.cleaned_data["category"])

        notices = Notice.objects.filter(notice_filter)
    return render(request,
                  template_name="service/list.html",
                  context={"form": form,
                           "notices": notices})


def preview(request, pk):
    return render(request,
                  template_name="service/preview.html",
                  context={"notice": Notice.objects.get(id=pk)})


@login_required
def create(request):
    form = NoticeForm()
    if request.POST:
        form = NoticeForm(request.POST,
                          request.FILES)
        if form.is_valid():
            form.save()
            return redirect("service-list")
    return render(request,
                  template_name="service/create.html",
                  context={"form": form})


@login_required
def update(request, pk):
    notice = get_object_or_404(Notice,
                               pk=pk)
    form = NoticeForm(instance=notice)
    if request.POST:
        form = NoticeForm(request.POST,
                          request.FILES,
                          instance=notice)
        if form.is_valid():
            form.save()
            return redirect("service-list")
        
    
    return render(request,
                  template_name="service/update.html",
                  context={"form": form})


@login_required
def delete(request, pk):
    get_object_or_404(Notice,
                      pk=pk).delete()
    return redirect("service-list")

