import unittest
from app import app

class TestFlaskAPI(unittest.TestCase):
    
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_get_users(self):
        response = self.client.get("/users")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)
        self.assertIn("users", response.json)
        self.assertIsInstance(response.json["users"], list)
    
    def test_add_user(self):
        new_user = {"name": "Charlie"}
        response = self.client.post("/users", json=new_user)
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response.json, dict)
        self.assertIn("id", response.json)
        self.assertEqual(response.json["name"], new_user["name"])
    
    def test_add_user_invalid_data(self):
        response = self.client.post("/users", json={})
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response.json, dict)
        self.assertIn("error", response.json)
        self.assertEqual(response.json["error"], "Invalid request data")
    
    def test_update_user(self):
        updated_user = {"name": "Updated Alice"}
        response = self.client.put("/users/1", json=updated_user)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, dict)
        self.assertEqual(response.json["name"], updated_user["name"])
    
    def test_update_user_not_found(self):
        updated_user = {"name": "Non-existent User"}
        response = self.client.put("/users/999", json=updated_user)
        self.assertEqual(response.status_code, 404)
        self.assertIsInstance(response.json, dict)
        self.assertIn("error", response.json)
        self.assertEqual(response.json["error"], "User not found")
    
    def test_update_user_invalid_data(self):
        response = self.client.put("/users/1", json={})
        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response.json, dict)
        self.assertIn("error", response.json)
        self.assertEqual(response.json["error"], "Invalid request data")

if __name__ == "__main__":
    unittest.main()
