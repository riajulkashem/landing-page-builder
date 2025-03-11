import json
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib import messages
from .models import Website
from .forms import WebsiteForm


def website_list(request):
    websites = Website.objects.all()
    return render(request, 'website_list.html', {'websites': websites})


def website_create(request):
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            website = form.save(commit=False)
            website.save()
            messages.success(request, 'Website created successfully!')
            return redirect('website_list')
    else:
        form = WebsiteForm()
    return render(request, 'website_form.html', {'form': form, 'action': 'Create'})


def website_preview(request, website_id):
    website = get_object_or_404(Website, id=website_id)
    return render(request, 'website_viewer.html', {'website': website})


def edit_website_content(request, website_id):
    website = get_object_or_404(Website, id=website_id)
    return render(request, 'website_editor.html', {'website': website})

@csrf_exempt
def save_website_content(request, website_id):
    website = get_object_or_404(Website, id=website_id)
    data = request.POST.get('project')
    if data:
        website.content = json.loads(data)
        website.save()
        return JsonResponse(status=200, data={'status': 'success'})
    return JsonResponse(data={'error': 'No project data provided'}, status=400)

def website_delete(request, website_id):
    website = get_object_or_404(Website, id=website_id)
    if request.method == 'POST':
        website.delete()
        messages.success(request, 'Website deleted successfully!')
        return redirect('website_list')
    return render(request, 'website_confirm_delete.html', {'website': website})