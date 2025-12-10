from fastapi import Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


from app.db.session import sessionmanager
from app.models.photos import Photo, PhotoVariant
from app.utils.image_processing import load_image_bytes, generate_variant, sha256_hash
from app.models.photos import PhotoVariant

class PhotoService:
    def __init__(self, db: AsyncSession = Depends(sessionmanager.get_db)):
        self.db: AsyncSession = db

    async def upload_photo(self, car_id: int, file_bytes: bytes, filename: str, content_type: str):
        # compute hash of original
        file_hash = sha256_hash(file_bytes)

        # PIL image
        img = load_image_bytes(file_bytes)
        fmt = img.format.lower()  # jpeg / png / webp

        photo = Photo(
            car_id=car_id,
            filename=filename,
            content_type=content_type,
            format=fmt,
            hash=file_hash,
            size_bytes=len(file_bytes),
        )

        self.db.add(photo)
        await self.db.flush()  # get photo.id

        # sizes
        for size in (64, 128, 512):
            variant = generate_variant(img, size, fmt)
            pv = PhotoVariant(
                photo_id=photo.id,
                width=variant["width"],
                height=variant["height"],
                data=variant["bytes"],
                size_bytes=variant["size_bytes"],
                content_type=variant["content_type"]
            )
            self.db.add(pv)

        await self.db.commit()
        await self.db.refresh(photo)
        return photo
    
    async def get_photo(self, photo_id: int, size: int) -> PhotoVariant:
        result = await self.db.execute(
            select(PhotoVariant).where(PhotoVariant.photo_id == photo_id, PhotoVariant.width == size)
        )
        variant = result.scalar()
        if not variant:
            raise HTTPException(404)
        return variant
