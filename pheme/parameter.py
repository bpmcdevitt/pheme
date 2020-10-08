from typing import Dict, Callable
from pathlib import Path
import json
import rest_framework
from django.core.files.uploadedfile import UploadedFile
from rest_framework.decorators import api_view, parser_classes, renderer_classes
from rest_framework.request import Request
from rest_framework.response import Response
from pheme.datalink import filename_as_datalink
from pheme import settings


def load_params(from_path: str = None) -> Dict:
    if not from_path:
        from_path = settings.PARAMETER_FILE_ADDRESS
    param_file_obj = Path(from_path)
    return json.loads(param_file_obj.read_text())


def __store(params: Dict, *, from_path: str = None) -> Dict:
    if not from_path:
        from_path = settings.PARAMETER_FILE_ADDRESS
    Path(from_path).write_text(json.dumps(params))
    return params


def __put(func: Callable[[Dict], Dict]) -> Response:
    params = load_params()
    return Response(__store(func(params)))


@api_view(['PUT'])
@parser_classes([rest_framework.parsers.JSONParser])
@renderer_classes(
    [
        rest_framework.renderers.JSONRenderer,
    ]
)
def put_value(request: Request, key: str) -> Response:
    def manipulate(data: Dict) -> Dict:
        data[key] = request.data
        return data

    return __put(manipulate)


@api_view(['PUT'])
@parser_classes([rest_framework.parsers.MultiPartParser])
@renderer_classes(
    [
        rest_framework.renderers.JSONRenderer,
    ]
)
def put_file(request: Request) -> Response:
    def manipulate(data: Dict) -> Dict:
        for (key, value) in request.data.items():
            if isinstance(value, UploadedFile):
                data[key] = filename_as_datalink(value.name, value.read())
            else:
                data[key] = value
        return data

    return __put(manipulate)
