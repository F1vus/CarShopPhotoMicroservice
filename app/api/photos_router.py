from fastapi import APIRouter, UploadFile, Depends,Response

from app.services.photo_service import PhotoService
from app.models.photos import PhotoVariant


router = APIRouter()

@router.post("/cars/{car_id}/photos")
async def upload_car_photo(car_id: int, file: UploadFile, service: "PhotoService" = Depends(PhotoService)):
    file_bytes = await file.read()

    photo = await service.upload_photo(
        car_id,
        file_bytes,
        filename=file.filename,
        content_type=file.content_type
    )

    return {"photo_id": photo.id}


@router.get("/photos/{photo_id}/{size}")
async def get_photo_variant(photo_id: int, size: int, service: "PhotoService" = Depends(PhotoService)):
    photo_variant: PhotoVariant = await service.get_photo(photo_id, size)
    return Response(content=photo_variant.data, media_type=photo_variant.content_type)
