# from flask import Blueprint, Response as FlaskResponse, current_app, request
from fastapi import BackgroundTasks
from fastapi.responses import Response as FastApiResponse, StreamingResponse as FastApiStreamingResponse
import json
from libs.collections.respcode import RespCode
import typing as t
from http import HTTPStatus

class Response(FastApiResponse):
    
    def __init__(
        self, 
        respCode: RespCode, 
        status_code: t.Union[int, HTTPStatus] = HTTPStatus.OK,
        media_type: str = 'application/json',
        data = None,
        operation_type = None
        ):
        
        # if data is None and respCode != RespCode.OK:
        #     if respCode.columns not in (None, []):
        #         data = {
        #             "error": 
        #                 {
        #                     "columns": respCode.columns
        #                 },
        #             "data": data
        #         }
        
        self.resp_code = respCode
        returnData = {}
        returnData['code'] = respCode.code
        returnData['message'] = respCode.description
        returnData['data'] = data
        if operation_type is not None:
            returnData['operation_type'] = operation_type
        super().__init__(json.dumps(returnData, ensure_ascii=False), media_type=media_type, status_code=status_code)
        
class StreamResponse(FastApiStreamingResponse):
    
    def __init__(
        self, 
        respCode: RespCode, 
        content,
        status_code: int = 200,
        headers: t.Mapping[str, str] | None = None,
        media_type: str | None = None,
        background: BackgroundTasks | None = None
        ):
        self.resp_code = respCode 
        super().__init__(content, status_code=status_code, headers=headers, media_type=media_type)