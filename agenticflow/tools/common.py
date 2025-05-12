"""Common tools for AgenticFlow framework."""

import json
import requests
from typing import Dict, Any, List, Optional
from .base import register_tool


@register_tool(
    name="http_request",
    description="Make an HTTP request to a URL"
)
def http_request(url: str, method: str = "GET", headers: Optional[Dict[str, str]] = None, 
                data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Make an HTTP request to a URL."""
    headers = headers or {}
    
    response = requests.request(
        method=method.upper(),
        url=url,
        headers=headers,
        json=data if method.upper() in ["POST", "PUT", "PATCH"] and data else None,
        params=data if method.upper() == "GET" and data else None
    )
    
    try:
        return {
            "status_code": response.status_code,
            "content": response.json() if response.headers.get("content-type", "").startswith("application/json") else response.text,
            "headers": dict(response.headers)
        }
    except json.JSONDecodeError:
        return {
            "status_code": response.status_code,
            "content": response.text,
            "headers": dict(response.headers)
        }


@register_tool(
    name="file_read",
    description="Read content from a file"
)
def file_read(filepath: str) -> str:
    """Read content from a file."""
    with open(filepath, "r") as f:
        return f.read()


@register_tool(
    name="file_write",
    description="Write content to a file"
)
def file_write(filepath: str, content: str) -> bool:
    """Write content to a file."""
    with open(filepath, "w") as f:
        f.write(content)
    return True


@register_tool(
    name="json_parse",
    description="Parse a JSON string into a Python object"
)
def json_parse(json_str: str) -> Dict[str, Any]:
    """Parse a JSON string into a Python object."""
    return json.loads(json_str)


@register_tool(
    name="json_stringify",
    description="Convert a Python object to a JSON string"
)
def json_stringify(obj: Any, pretty: bool = False) -> str:
    """Convert a Python object to a JSON string."""
    indent = 2 if pretty else None
    return json.dumps(obj, indent=indent)
