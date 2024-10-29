import unittest
from PassKeeper.src.modelo.modelo import Session
from CRUD import UserCRUD, PasswordCRUD, CategoryCRUD, PasswordHistoryCRUD, SecuritySettingCRUD
from datetime import datetime


# Importar los modelos y los CRUD desde el código anterior
# from your_module import UserCRUD, SecuritySettingCRUD, CategoryCRUD, PasswordCRUD, PasswordHistoryCRUD
# from your_module import Base, User, SecuritySetting, Category, Password, PasswordHistory



class TestCRUDOperations(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada prueba. Configura una nueva sesión de base de datos."""
        self.session = Session()
        self.user_crud = UserCRUD(self.session)
        self.security_crud = SecuritySettingCRUD(self.session)
        self.category_crud = CategoryCRUD(self.session)
        self.password_crud = PasswordCRUD(self.session)
        self.history_crud = PasswordHistoryCRUD(self.session)

    def tearDown(self):
        """Se ejecuta después de cada prueba. Cierra la sesión y limpia la base de datos."""
        self.session.close()

    # Pruebas para UserCRUD
    def test_create_user(self):
        user = self.user_crud.create_user("test_user", "hashed_pass", "test@example.com", None)
        self.assertIsNotNone(user.user_id)
        self.assertEqual(user.username, "test_user")

    def test_get_user(self):
        user = self.user_crud.create_user("test_user2", "hashed_pass", "test2@example.com", None)
        fetched_user = self.user_crud.get_user(user.user_id)
        self.assertEqual(fetched_user.username, "test_user2")

    def test_update_user(self):
        user = self.user_crud.create_user("test_user3", "hashed_pass", "test3@example.com", None)
        updated_user = self.user_crud.update_user(user.user_id, email="new_email@example.com")
        self.assertEqual(updated_user.email, "new_email@example.com")

    def test_delete_user(self):
        user = self.user_crud.create_user("test_user4", "hashed_pass", "test4@example.com", None)
        deleted_user = self.user_crud.delete_user(user.user_id)
        self.assertIsNone(self.user_crud.get_user(user.user_id))

    # Pruebas para SecuritySettingCRUD
    def test_create_security_setting(self):
        setting = self.security_crud.create_security_setting(True, datetime.now())
        self.assertIsNotNone(setting.setting_id)
        self.assertTrue(setting.two_factor_enabled)

    def test_update_security_setting(self):
        setting = self.security_crud.create_security_setting(False, datetime.now())
        updated_setting = self.security_crud.update_security_setting(setting.setting_id, two_factor_enabled=True)
        self.assertTrue(updated_setting.two_factor_enabled)

    # Pruebas para CategoryCRUD
    def test_create_category(self):
        user = self.user_crud.create_user("user_cat", "hashed_pass", "cat@example.com", None)
        category = self.category_crud.create_category("Personal", user.user_id)
        self.assertIsNotNone(category.category_id)
        self.assertEqual(category.category_name, "Personal")

    def test_update_category(self):
        user = self.user_crud.create_user("user_cat2", "hashed_pass", "cat2@example.com", None)
        category = self.category_crud.create_category("Work", user.user_id)
        updated_category = self.category_crud.update_category(category.category_id, category_name="Updated Work")
        self.assertEqual(updated_category.category_name, "Updated Work")

    # Pruebas para PasswordCRUD
    def test_create_password(self):
        user = self.user_crud.create_user("user_pw", "hashed_pass", "pw@example.com", None)
        category = self.category_crud.create_category("Business", user.user_id)
        password = self.password_crud.create_password("Service1", "user1", "pass123", "note1", category.category_id)
        self.assertIsNotNone(password.password_id)
        self.assertEqual(password.service_name, "Service1")

    def test_update_password(self):
        user = self.user_crud.create_user("user_pw2", "hashed_pass", "pw2@example.com", None)
        category = self.category_crud.create_category("Travel", user.user_id)
        password = self.password_crud.create_password("Service2", "user2", "pass456", "note2", category.category_id)
        updated_password = self.password_crud.update_password(password.password_id, service_name="Updated Service")
        self.assertEqual(updated_password.service_name, "Updated Service")

    # Pruebas para PasswordHistoryCRUD
    def test_create_password_history(self):
        user = self.user_crud.create_user("user_hist", "hashed_pass", "hist@example.com", None)
        category = self.category_crud.create_category("Finance", user.user_id)
        password = self.password_crud.create_password("Service3", "user3", "pass789", "note3", category.category_id)
        history = self.history_crud.create_password_history("old_pass", password.password_id)
        self.assertIsNotNone(history.history_id)
        self.assertEqual(history.old_password, "old_pass")

    def test_delete_password_history(self):
        user = self.user_crud.create_user("user_hist2", "hashed_pass", "hist2@example.com", None)
        category = self.category_crud.create_category("Shopping", user.user_id)
        password = self.password_crud.create_password("Service4", "user4", "pass321", "note4", category.category_id)
        history = self.history_crud.create_password_history("old_pass2", password.password_id)
        deleted_history = self.history_crud.delete_password_history(history.history_id)
        self.assertIsNone(self.history_crud.get_password_history(history.history_id))

if __name__ == '__main__':
    unittest.main()
