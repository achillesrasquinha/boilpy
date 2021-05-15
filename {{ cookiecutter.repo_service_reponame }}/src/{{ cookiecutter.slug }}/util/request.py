import re

import requests

# from fake_useragent import UserAgent

from {{ cookiecutter.slug }}.db import get_connection
from {{ cookiecutter.slug }}.util.proxy     import get_random_requests_proxies
from {{ cookiecutter.slug }}.util._dict     import merge_dict
from {{ cookiecutter.slug }}.util.imports   import import_or_raise

# user_agent = UserAgent(verify_ssl = False)

# https://git.io/JsnSI
_REGEX_URL = re.compile(
    r'^(?:http|ftp)s?://' # http:// or https://
    r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
    r'localhost|' #localhost...
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
    r'(?::\d+)?' # optional port
    r'(?:/?|[/?]\S+)$', re.IGNORECASE)

def proxy_request(*args, **kwargs):
    fallback = kwargs.pop("fallback", False)

    session  = requests.Session()

    proxies  = get_random_requests_proxies()
    # session.headers.update({ "User-Agent": user_agent.random })
    session.proxies.update(proxies)

    try:
        kwargs["timeout"] = 5
        response = session.request(*args, **kwargs)
    except requests.exceptions.ConnectionError as e:
        if fallback:
            session.headers = kwargs.get("headers", {})
            session.proxies = kwargs.get("proxies", {})
            response = session.request(*args, **kwargs)
        else:
            raise e

    return response

def proxy_grequest(*args, **kwargs):
    proxies = get_random_requests_proxies()
    
    # kwargs["headers"] = merge_dict(kwargs.get("headers", {}), {
    #     "User-Agent": user_agent.random })
    kwargs["proxies"] = merge_dict(kwargs.get("proxies", {}), proxies)
    grequests         = import_or_raise("grequests")

    return grequests.request(*args, **kwargs)

def check_url(url, raise_err = True):
    if not re.match(_REGEX_URL, url):
        if raise_err:
            raise ValueError("Invalid URL: %s" % url)
        
        return False
    
    return True