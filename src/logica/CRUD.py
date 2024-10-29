from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
from src.modelo.modelo import User, Password, SecuritySetting, PasswordHistory, Category
from src.modelo.declarative_base import Base, engine, session

# Configurar la base de datos (ajusta la URL según tu base de datos)
DATABASE_URL = "sqlite:///example.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# CRUD de cada modelo
class UserCRUD:
    def __init__(self, session):
        self.session = session

    def create_user(self, username, password_hash, email, security_settings):
        user = User(
            username=username,
            password_hash=password_hash,
            email=email,
            created_at=datetime.now(),
            security_settings=security_settings
        )
        self.session.add(user)
        self.session.commit()
        return user

    def get_user(self, user_id):
        return self.session.query(User).filter(User.user_id == user_id).first()

    def update_user(self, user_id, **kwargs):
        user = self.get_user(user_id)
        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
            self.session.commit()
        return user

    def delete_user(self, user_id):
        user = self.get_user(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
        return user


class SecuritySettingCRUD:
    def __init__(self, session):
        self.session = session

    def create_security_setting(self, two_factor_enabled, last_login):
        setting = SecuritySetting(
            two_factor_enabled=two_factor_enabled,
            last_login=last_login
        )
        self.session.add(setting)
        self.session.commit()
        return setting

    def get_security_setting(self, setting_id):
        return self.session.query(SecuritySetting).filter(SecuritySetting.setting_id == setting_id).first()

    def update_security_setting(self, setting_id, **kwargs):
        setting = self.get_security_setting(setting_id)
        if setting:
            for key, value in kwargs.items():
                setattr(setting, key, value)
            self.session.commit()
        return setting

    def delete_security_setting(self, setting_id):
        setting = self.get_security_setting(setting_id)
        if setting:
            self.session.delete(setting)
            self.session.commit()
        return setting


class CategoryCRUD:
    def __init__(self, session):
        self.session = session

    def create_category(self, category_name, user_id):
        category = Category(
            category_name=category_name,
            created_at=datetime.now(),
            user_id=user_id
        )
        self.session.add(category)
        self.session.commit()
        return category

    def get_category(self, category_id):
        return self.session.query(Category).filter(Category.category_id == category_id).first()

    def update_category(self, category_id, **kwargs):
        category = self.get_category(category_id)
        if category:
            for key, value in kwargs.items():
                setattr(category, key, value)
            self.session.commit()
        return category

    def delete_category(self, category_id):
        category = self.get_category(category_id)
        if category:
            self.session.delete(category)
            self.session.commit()
        return category


class PasswordCRUD:
    def __init__(self, session):
        self.session = session

    def create_password(self, service_name, username, password, notes, category_id):
        new_password = Password(
            service_name=service_name,
            username=username,
            password=password,
            notes=notes,
            created_at=datetime.now(),
            category_id=category_id
        )
        self.session.add(new_password)
        self.session.commit()
        return new_password

    def get_password(self, password_id):
        return self.session.query(Password).filter(Password.password_id == password_id).first()

    def update_password(self, password_id, **kwargs):
        password = self.get_password(password_id)
        if password:
            for key, value in kwargs.items():
                setattr(password, key, value)
            self.session.commit()
        return password

    def delete_password(self, password_id):
        password = self.get_password(password_id)
        if password:
            self.session.delete(password)
            self.session.commit()
        return password


class PasswordHistoryCRUD:
    def __init__(self, session):
        self.session = session

    def create_password_history(self, old_password, password_id):
        history = PasswordHistory(
            old_password=old_password,
            changed_at=datetime.now(),
            password_id=password_id
        )
        self.session.add(history)
        self.session.commit()
        return history

    def get_password_history(self, history_id):
        return self.session.query(PasswordHistory).filter(PasswordHistory.history_id == history_id).first()

    def update_password_history(self, history_id, **kwargs):
        history = self.get_password_history(history_id)
        if history:
            for key, value in kwargs.items():
                setattr(history, key, value)
            self.session.commit()
        return history

    def delete_password_history(self, history_id):
        history = self.get_password_history(history_id)
        if history:
            self.session.delete(history)
            self.session.commit()
        return history
