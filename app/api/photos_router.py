from fastapi import APIRouter, UploadFile, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.services.photo_service import PhotoService
from app.models.photos import PhotoVariant
from fastapi import Response

router = APIRouter()

@router.post("/cars/{car_id}/photos")
async def upload_car_photo(car_id: int, file: UploadFile, db: AsyncSession = Depends(get_db)):
    file_bytes = await file.read()

    service = PhotoService(db)
    photo = await service.upload_photo(
        car_id,
        file_bytes,
        filename=file.filename,
        content_type=file.content_type
    )

    return {"photo_id": photo.id}


@router.get("/photos/{photo_id}/{size}")
async def get_photo_variant(photo_id: int, size: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(PhotoVariant).where(PhotoVariant.photo_id == photo_id, PhotoVariant.width == size)
    )
    variant = result.scalar()

    if not variant:
        raise HTTPException(404)

    return Response(content=variant.data, media_type=variant.content_type)
