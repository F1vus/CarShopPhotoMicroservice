from sqlalchemy import Column, BigInteger, Text, Integer, ForeignKey, TIMESTAMP, LargeBinary, UniqueConstraint
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Photo(Base):
    __tablename__ = "photos"
    __table_args__ = {"schema": "photoservice"}

    id = Column(BigInteger, primary_key=True, index=True)
    car_id = Column(
        BigInteger,
        ForeignKey("public.cars.id", ondelete="CASCADE"),
        nullable=False
    )
    uploaded_by_user_id = Column(BigInteger)
    filename = Column(Text)
    content_type = Column(Text)
    format = Column(Text)
    hash = Column(Text)
    size_bytes = Column(Integer)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    variants = relationship("PhotoVariant", back_populates="photo", cascade="all, delete")


class PhotoVariant(Base):
    __tablename__ = "photo_variants"
    __table_args__ = {"schema": "photoservice"}

    id = Column(BigInteger, primary_key=True)
    photo_id = Column(BigInteger, ForeignKey("photos.id", ondelete="CASCADE"))
    width = Column(Integer, nullable=False)
    height = Column(Integer)
    data = Column(LargeBinary)
    size_bytes = Column(Integer)
    content_type = Column(Text)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    photo = relationship("Photo", back_populates="variants")

    __table_args__ = (
        UniqueConstraint("photo_id", "width"),
    )
