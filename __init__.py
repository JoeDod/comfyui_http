from .http_request_node import SimpleHttpRequest, SimpleShowText

NODE_CLASS_MAPPINGS = {
    "SimpleHttpRequest": SimpleHttpRequest,
    "SimpleShowText": SimpleShowText
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SimpleHttpRequest": "HTTP Request",
    "SimpleShowText": "Show Text"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
