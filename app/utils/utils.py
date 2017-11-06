from django.shortcuts import render


def render_template(request, template, context=None):
    context = context or {}

    context.update({
        'template': template
    })
    return render(request, 'base_template.html', context)