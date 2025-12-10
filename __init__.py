from .http_request_node import SimpleHttpRequest

NODE_CLASS_MAPPINGS = {"SimpleHttpRequest": SimpleHttpRequest}

NODE_DISPLAY_NAME_MAPPINGS = {"SimpleHttpRequest": "HTTP Request"}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
