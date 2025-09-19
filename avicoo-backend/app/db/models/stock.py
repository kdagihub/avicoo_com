# app/db/models/stock.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.session import Base
import enum

class StockMovementType(str, enum.Enum):
    IN = "in"  # Entrée de stock
    OUT = "out"  # Sortie de stock
    ADJUSTMENT = "adjustment"  # Ajustement

class StockMovement(Base):
    __tablename__ = "stock_movements"
    
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"), nullable=True)
    movement_type = Column(Enum(StockMovementType), nullable=False)
    quantity = Column(Integer, nullable=False)  # Positif pour entrée, négatif pour sortie
    batch_date = Column(DateTime, nullable=True)
    location = Column(String(100), nullable=True)
    reason = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    created_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    
    # Relations
    product = relationship("Product", back_populates="stock_movements")
    supplier = relationship("Supplier", back_populates="stock_movements")
    creator = relationship("User")
