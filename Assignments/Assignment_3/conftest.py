import os
import sys

# Add the backend/src directory to the Python path
backend_src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../backend/src'))
sys.path.insert(0, backend_src_path) 