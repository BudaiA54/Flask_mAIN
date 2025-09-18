#!/usr/bin/env python3
"""
Simple test script to verify application structure and imports
without requiring database connectivity.
"""

import sys
import os

# Add the app directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

def test_imports():
    """Test that all modules can be imported successfully."""
    try:
        print("Testing imports...")
        
        # Test models import
        from app.models import User, Message, db
        print("✓ Models imported successfully")
        
        # Test that User has the required methods
        assert hasattr(User, 'set_password'), "User.set_password method missing"
        assert hasattr(User, 'check_password'), "User.check_password method missing"
        assert hasattr(User, 'is_manager'), "User.is_manager property missing"
        print("✓ User model has required methods")
        
        # Test app factory
        from app import create_app
        print("✓ App factory imported successfully")
        
        # Test routes
        from app.routes import main
        print("✓ Routes imported successfully")
        
        print("\nAll imports successful!")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except AssertionError as e:
        print(f"❌ Assertion error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_password_hashing():
    """Test password hashing functionality without database."""
    try:
        print("\nTesting password hashing...")
        
        from werkzeug.security import generate_password_hash, check_password_hash
        
        test_password = "test123"
        password_hash = generate_password_hash(test_password)
        
        assert check_password_hash(password_hash, test_password), "Password verification failed"
        assert not check_password_hash(password_hash, "wrong_password"), "Wrong password accepted"
        
        print("✓ Password hashing works correctly")
        return True
        
    except Exception as e:
        print(f"❌ Password hashing test failed: {e}")
        return False

def test_user_model_logic():
    """Test User model methods without database."""
    try:
        print("\nTesting User model logic...")
        
        from app.models import User
        
        # Create a user instance (without database)
        user = User()
        user.username = "testuser"
        user.email = "test@example.com"
        user.role = "manager"
        
        # Test password setting and checking
        user.set_password("testpassword")
        assert user.check_password("testpassword"), "Password check failed"
        assert not user.check_password("wrongpassword"), "Wrong password accepted"
        
        # Test role property
        assert user.is_manager == True, "is_manager property failed for manager"
        
        user.role = "employee"
        assert user.is_manager == False, "is_manager property failed for employee"
        
        print("✓ User model logic works correctly")
        return True
        
    except Exception as e:
        print(f"❌ User model test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("Flask Employee Messaging App - Structure Test")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_password_hashing,
        test_user_model_logic
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✓ All tests passed! Application structure is correct.")
        return 0
    else:
        print("❌ Some tests failed. Please check the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())