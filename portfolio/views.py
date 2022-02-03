from django.shortcuts import render
from portfolio.models import Project


def index(request):
      """
      View funtion for home page of site
      """
      projects_preview = Project.objects.all()[:3]

      context = {
            'projects_preview' : projects_preview,
      }

      return render(request, 'index.html', context)




def project_index(request):
    """
    Shows snippets of each project.
    """
    projects_ind = Project.objects.all()
    context = {
        'projects': projects_ind
    }
    return render(request, 'project_index.html', context)




def project_detail(request, pk):
    """
    Shows more information on a project.
    """
    project_det = Project.objects.get(pk=pk)
    context = {
        'project': project_det
    }
    return render(request, 'project_detail.html', context)
