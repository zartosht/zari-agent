#!/usr/bin/env python3
"""
Simple test runner script for the zari-agent project.
This can be run with: uv run test.py
"""

import subprocess
import sys
import os

def run_tests():
    """Run the test suite using pytest."""
    print("🧪 Running Zari Agent tests...")
    print("=" * 50)
    
    # Change to project directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    try:
        # Run pytest with coverage
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "tests.py",
            "--verbose",
            "--tb=short",
            "--cov=functions",
            "--cov-report=term-missing"
        ], check=True)
        
        print("\n✅ All tests completed!")
        return 0
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Tests failed with exit code {e.returncode}")
        return e.returncode
    except FileNotFoundError:
        print("❌ pytest not found. Install test dependencies with: uv add pytest pytest-cov --optional test")
        return 1

def run_calculator_tests():
    """Run the calculator-specific tests."""
    print("\n🧮 Running calculator tests...")
    print("=" * 30)
    
    try:
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "calculator/tests.py",
            "--verbose"
        ], check=False)  # Don't fail if calculator tests don't exist
        
        return result.returncode
        
    except FileNotFoundError:
        print("📁 No calculator tests found, skipping...")
        return 0

if __name__ == "__main__":
    print("🚀 Zari Agent Test Suite")
    print("=" * 50)
    
    # Run main tests
    main_result = run_tests()
    
    # Run calculator tests
    calc_result = run_calculator_tests()
    
    # Summary
    print("\n" + "=" * 50)
    if main_result == 0:
        print("✅ Main tests: PASSED")
    else:
        print("❌ Main tests: FAILED")
        
    if calc_result == 0:
        print("✅ Calculator tests: PASSED")
    else:
        print("❌ Calculator tests: FAILED")
    
    print("=" * 50)
    
    # Exit with error if any tests failed
    sys.exit(max(main_result, calc_result))
