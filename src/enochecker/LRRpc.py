from requests import post
from os import environ
import json

BACKEND = environ["CONNHANDLER_URL"]


def rpc_call(target, action_name, runlength, logger=None, **kwargs):
    try:
        if isinstance(action_name, type):
            action_name = type.__name__()
        
        kwargs["address"] = target
        kwargs.setdefault("initial_timeout", 10)
        kwargs.setdefault("long_timeout", runlength)

        if logger is not None:
            logger.debug(kwargs)
            logger.debug(json.dumps(kwargs))
        req = post("{}/{}".format(BACKEND, action_name), data=kwargs)
        
        if logger is not None:
            logger.debug(req.text)
            logger.debug(req.json())

        result = req.json()
    except Exception:
        raise
    return result
