from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def apiOverview(request):
    base_url = reverse(apiOverview, request=request)
    api_urls = {
        "welcome to Munya's rest api": base_url,
        "Blog": f"{base_url}blogapi/",
        "Mailing List": f"{base_url}mail/send",
        "Todo": f"{base_url}todoapi/",
        "Projects": f"{base_url}project_api/",
    }
    return Response(api_urls)
