from typing import List

from fastapi import APIRouter, Depends, UploadFile

from analyzer.api.dependencies.services import analyzer_service_dependency
from analyzer.services.analyzer import AnalyzerService
from analyzer.services.models import analyzer as analyzer_models

router = APIRouter()


@router.post(
    "/upload-file/",
    name="upload_file",
    response_model=analyzer_models.AnalyzerCreateResponse,
)
async def create_upload_file(
    file: UploadFile,
    service: AnalyzerService = Depends(analyzer_service_dependency),
) -> analyzer_models.AnalyzerCreateResponse:
    """
    Upload file.

    :param file: file.
    :param service: analyzer service.
    :return: Id of the file.
    """
    return await service.upload_file_service(file)


@router.get(
    "get-analyzer/{id}",
    name="get_analyzer",
    response_model=analyzer_models.AnalyzerGetResponse,
)
async def get_analyzer(
    id: int,
    service: AnalyzerService = Depends(analyzer_service_dependency),
) -> analyzer_models.AnalyzerGetResponse:
    """
    Get analyzer.

    :param id: id of the file.
    :param service: analyzer service.
    :return: analyzer.
    """
    return await service.get_analyzer_service(id)


@router.get(
    "get-analyzer-list/",
    name="get_analyzer_list",
    response_model=List[analyzer_models.AnalyzerGetResponse],
)
async def get_analyzer_list(
    service: AnalyzerService = Depends(analyzer_service_dependency),
) -> List[analyzer_models.AnalyzerGetResponse]:
    """
    Get analyzer list.

    :param service: analyzer service.
    :return: analyzer list.
    """
    return await service.get_analyzer_list_service()
