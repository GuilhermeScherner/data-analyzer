import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from pytest_mock import MockerFixture
from starlette import status

pytestmark = pytest.mark.anyio


async def test_get_analyzer(
    client: AsyncClient,
    fastapi_app: FastAPI,
    mocker: MockerFixture,
) -> None:
    """
    Test get analyzer.

    :param client: client for the app.
    :param fastapi_app: current FastAPI application.
    """
    expected_result = [{"user_id": "test", "device_id": "test", "data": "test"}]
    mocker.patch(
        "analyzer.db.repositories.file.FileRepository.get_items",
        return_value=expected_result,
    )

    url = fastapi_app.url_path_for("Analyzer: get analyzer")
    response = await client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_result


@pytest.mark.anyio
async def test_put_analyzer(
    client: AsyncClient,
    fastapi_app: FastAPI,
    mocker: MockerFixture,
) -> None:
    """
    Test put analyzer.

    :param client: client for the app.
    :param fastapi_app: current FastAPI application.
    """
    expected_result = {"user_id": "test", "device_id": "test", "data": "test"}
    mocker.patch(
        "analyzer.db.repositories.analyzer.FileRepository.put_item",
        return_value=expected_result,
    )
    url = fastapi_app.url_path_for("Analyzer: create analyzer")
    response = await client.post(url, json={"user_id": "test", "device_id": "test"})
    keys_to_extract = ["user_id"]
    result = {
        key: expected_result[key]
        for key in expected_result.keys()
        if key in keys_to_extract
    }

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == result
