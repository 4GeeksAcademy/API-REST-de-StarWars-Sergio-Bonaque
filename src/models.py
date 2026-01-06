from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(200), nullable=False)  # puse 200 por si uso hash largo
    is_active: Mapped[bool] = mapped_column(Boolean(), default=True)  # por defecto activo

    # esto es para que se vea bonito en la consola 
    def __repr__(self):
        return f'<User {self.email}>'

    # metodo para convertir a json, importante no mandar la password!!!
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # "password": self.password,  <-- nunca, por seguridad!!!
            "is_active": self.is_active
        }