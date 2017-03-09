from rest_framework.views import exception_handler

CUSTOM_ERROR_CODE = 10101


def custom_exception_handler(exc, context):

    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        extra = "yes"

        # one way to get class attribute
        if hasattr(context['view'], 'extra_bit'):
            extra = context['view'].extra_bit

        # another way to get class attribute
        more = getattr(context['view'], 'more', 'less')

        response.data = {
            'result': CUSTOM_ERROR_CODE,
            'data': {
                'url': 'http://example.com',
                'extra': extra,
                'more': more
            }
        }

    return response
