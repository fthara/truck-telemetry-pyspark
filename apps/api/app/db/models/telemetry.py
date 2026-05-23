from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Telemetry(Base):
    __tablename__ = "telemetries"

    id: Mapped[int] = mapped_column(primary_key=True)
    truck_id = mapped_column(ForeignKey("trucks.id"))
    driver_id = mapped_column(ForeignKey("drivers.id"))
    latitude: Mapped[float]
    longitude: Mapped[float]
    speed: Mapped[float]
    temperature: Mapped[float]
    fuel_level: Mapped[float]
    timestamp: Mapped[str]

    truck: Mapped["Truck"] = relationship(back_populates="telemetries")
    driver: Mapped["Driver"] = relationship(back_populates="telemetries")