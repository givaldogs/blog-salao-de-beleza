from django.core.paginator import Paginator
from django.shortcuts import render

posts = list(range(1000))


def index(request):
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )


def page(request):
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/page.html',
        {
            # 'page_obj': page_obj,
        }
    )


def post(request):
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/post.html',
        {
            # 'page_obj': page_obj,
        }
    )


def search_view(request):
    search_query = request.GET.get('search', '')  # Obtém o termo de pesquisa da query string
    # Aqui você pode adicionar a lógica de busca, como buscar posts ou páginas com base no termo de pesquisa
    results = []  # Substitua isso por sua lógica de busca real

    return render(request, 'search_results.html', {'search_query': search_query, 'results': results})
