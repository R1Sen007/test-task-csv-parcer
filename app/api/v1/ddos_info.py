from fastapi import APIRouter, status, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.ddos import ddos_crud
from app.schemas.ddos import DdosSchema
from app.api.validators import (
    check_file_type_csv,
)


router = APIRouter()


@router.post(
        '/upload_ddos_info',
        response_model=list[DdosSchema],
        status_code=status.HTTP_201_CREATED,
        summary='Загрузка csv файла.',
        description='После загрузки, вычисляет среднее по полю `saddr`, '
                'а также сохраняет или обновляет существующие данные в бд.'
)
async def processing_ddos_info(
    file: UploadFile = File(...),
    session: AsyncSession = Depends(get_async_session)
):
    check_file_type_csv(file.filename)
    result = await ddos_crud.create_update_from_csv(file, session)
    return result
