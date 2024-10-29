from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime



class SecuritySetting(Base):
    __tablename__ = 'security_settings'

    setting_id = Column(Integer, primary_key=True)
    two_factor_enabled = Column(Boolean, default=False)
    last_login = Column(DateTime)

    user = relationship("User", back_populates="security_settings")


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime)
    security_settings_id = Column(Integer, ForeignKey('security_settings.setting_id'))

    security_settings = relationship("SecuritySetting", back_populates="user")
    categories = relationship("Category", back_populates="user")


class Category(Base):
    __tablename__ = 'categories'

    category_id = Column(Integer, primary_key=True)
    category_name = Column(String, nullable=False)
    created_at = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.user_id'))

    user = relationship("User", back_populates="categories")
    passwords = relationship("Password", back_populates="category")


class Password(Base):
    __tablename__ = 'passwords'

    password_id = Column(Integer, primary_key=True)
    service_name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    notes = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    category_id = Column(Integer, ForeignKey('categories.category_id'))

    category = relationship("Category", back_populates="passwords")
    password_history = relationship("PasswordHistory", back_populates="password")


class PasswordHistory(Base):
    __tablename__ = 'password_history'

    history_id = Column(Integer, primary_key=True)
    old_password = Column(String, nullable=False)
    changed_at = Column(DateTime)
    password_id = Column(Integer, ForeignKey('passwords.password_id'))

    password = relationship("Password", back_populates="password_history")

# Configuración de base de datos para pruebas (en memoria)
engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=engine)

# Crear las tablas en la base de datos de prueba
Base.metadata.create_all(engine)