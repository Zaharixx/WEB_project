from django.core.paginator import Paginator

def paginate(objects_list, request, per_page=10):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(objects_list, per_page)
    page = paginator.page(page_num)
    return page