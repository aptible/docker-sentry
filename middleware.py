from django.http import HttpResponsePermanentRedirect


class ForceSSLMiddleware(object):
    """
    Force redirect http:// urls to https://
    """
    def process_request(self, request):
        if request.is_secure():
            return None

        url = request.build_absolute_uri(request.get_full_path())
        https_url = url.replace('http://', 'https://', 1)
        return HttpResponsePermanentRedirect(https_url)
