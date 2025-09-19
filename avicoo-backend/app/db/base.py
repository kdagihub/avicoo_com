from app.db.session import Base
from app.db.models import *  # Importe tous les modèles

# Cette ligne assure que tous les modèles sont enregistrés avec SQLAlchemy
__all__ = ["Base"]
