import requests
import json


class SimpleHttpRequest:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "url": ("STRING", {
                    "default": "http://localhost:8000"
                }),
                "method": (["GET", "POST", "PUT", "DELETE"], ),
            },
            "optional": {
                "headers": ("STRING", {
                    "multiline":
                    True,
                    "default":
                    "{\"Content-Type\": \"application/json\"}"
                }),
                "body": ("STRING", {
                    "multiline": True,
                    "default": "{}"
                }),
                "timeout": ("INT", {
                    "default": 10,
                    "min": 1,
                    "max": 60
                }),
            }
        }

    RETURN_TYPES = ("STRING", "INT", "STRING")
    RETURN_NAMES = ("text", "status_code", "json_str")
    FUNCTION = "make_request"
    CATEGORY = "Network"

    def make_request(self, url, method, headers="{}", body="{}", timeout=10):
        try:
            headers_dict = json.loads(headers) if headers else {}
        except Exception as e:
            print(f"Error parsing headers: {e}")
            headers_dict = {}

        json_data = None
        data = None

        if body:
            try:
                json_data = json.loads(body)
            except:
                data = body

        try:
            # 如果 json_data 解析成功，将其作为 'json' 参数使用，这通常会自动将 Content-Type 设置为 application/json，
            # 但如果手动设置了 headers，requests 会遵循手动设置。
            # 如果使用 data，则是表单编码或原始字节。

            # 逻辑：如果我们成功解析了 JSON，则作为 json 发送。如果没有，则作为 data 发送。
            # 然而，有时用户希望将 JSON 字符串作为原始 body 发送。
            # 让我们坚持：如果 json_data 不是 None，使用 json=，否则使用 data=。

            kwargs = {
                "method": method,
                "url": url,
                "headers": headers_dict,
                "timeout": timeout
            }

            if json_data is not None:
                kwargs["json"] = json_data
            else:
                kwargs["data"] = data

            response = requests.request(**kwargs)

            text_output = response.text
            status_code = response.status_code

            print(
                f"[SimpleHttpRequest] {method} {url} - Status: {status_code}")

            # 将 JSON 作为字符串返回，以便对 ComfyUI 类型安全，或者可以是自定义类型。
            # 标准 ComfyUI 没有在没有自定义节点的情况下轻松传递的通用 JSON 类型，
            # 但将其作为字符串返回是安全的。
            try:
                json_output = json.dumps(response.json(), indent=2)
            except:
                json_output = "{}"

            return (text_output, status_code, json_output)

        except Exception as e:
            return (f"Error: {str(e)}", 0, "{}")
