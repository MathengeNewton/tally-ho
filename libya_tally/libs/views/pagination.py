from django.core.paginator import EmptyPage, PageNotAnInteger


def paginate(paginator, page):
    """Get the pages for this paginator and page.

    :param paginator: The paginator to fetch pages from
    :param page: The page to fetch.

    :returns: A list of records for this paginator and page.
    """
    try:
        return paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        return paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page.
        return paginator.page(paginator.num_pages)