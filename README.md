# ComfyUI HTTP Request Node

这是一个用于 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 的自定义节点，允许你在工作流中发起 HTTP 请求（GET, POST, PUT, DELETE）。

它非常适合需要与外部 API 交互、发送生成结果或获取远程数据的场景。

## 功能特点

- 支持多种 HTTP 方法：`GET`, `POST`, `PUT`, `DELETE`。
- 自定义 Headers：支持 JSON 格式的请求头配置。
- 自定义 Body：支持发送 JSON 数据或普通文本数据。
- 自动 JSON 解析：如果响应是 JSON 格式，会自动格式化输出。
- 超时控制：可配置请求超时时间。

## 安装方法

1.  进入你的 ComfyUI 安装目录下的 `custom_nodes` 文件夹。
2.  克隆本仓库或下载代码到该目录：
    ```bash
    cd ComfyUI/custom_nodes
    git clone https://github.com/yourusername/comfyui_http.git
    # 或者手动创建一个文件夹 comfyui_http 并将文件放入
    ```
3.  安装依赖（如果需要）：
    ComfyUI 通常自带了 `requests` 库，如果没有，请在 ComfyUI 的 Python 环境中运行：
    ```bash
    pip install requests
    ```
4.  重启 ComfyUI。

## 使用说明

在 ComfyUI 的节点列表中，找到 `Network` 分类，选择 `HTTP Request` 节点。

### 输入参数 (Inputs)

- **url**: 目标 URL 地址 (例如: `http://localhost:8000/api/v1/generate`).
- **method**: HTTP 请求方法 (GET, POST, PUT, DELETE).
- **headers**: JSON 格式的请求头字符串。
  - 默认: `{"Content-Type": "application/json"}`
  - 示例: `{"Authorization": "Bearer YOUR_TOKEN"}`
- **body**: 请求体内容。
  - 如果是 JSON 格式字符串，节点会自动将其解析并以 `application/json` 发送。
  - 如果解析失败，将作为普通字符串发送。
- **timeout**: 请求超时时间（秒），默认 10 秒。

### 输出参数 (Outputs)

- **text**: 原始响应内容（字符串）。
- **status_code**: HTTP 状态码（整数，如 200, 404, 500）。
- **json_str**: 如果响应内容是 JSON，这里返回格式化后的 JSON 字符串；否则返回空 JSON `{}`。

## 示例

### 发送 POST 请求

假设你要调用一个外部 API 来处理数据：

1.  **URL**: `https://api.example.com/v1/process`
2.  **Method**: `POST`
3.  **Headers**: `{"Content-Type": "application/json", "Authorization": "Bearer 123456"}`
4.  **Body**: `{"prompt": "a beautiful landscape", "seed": 123}`

连接节点的输出 `json_str` 到其他文本处理节点即可查看结果。

## 常见问题

- **节点没显示？**
  请检查是否正确放入了 `custom_nodes` 目录，并确保重启了 ComfyUI。查看控制台是否有报错信息。
- **请求失败？**
  请检查 URL 是否正确，以及网络是否通畅。控制台会打印简单的请求日志，例如 `[SimpleHttpRequest] GET ... - Status: 404`。
