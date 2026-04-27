#!/usr/bin/env python3
"""
License header checker for MIT License.
Checks that Python files have proper MIT license headers.
"""

import os
import sys
from pathlib import Path

# MIT License header template
MIT_LICENSE_HEADER = """MIT License

Copyright (c) 2024 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

# Files to exclude from license check
EXCLUDE_DIRS = {
    '.git',
    '.github',
    '__pycache__',
    'venv',
    'env',
    '.venv',
    'build',
    'dist',
    'egg-info',
    '.pytest_cache',
    '.mypy_cache',
}

EXCLUDE_FILES = {
    '__init__.py',
    'setup.py',
}


def should_check_file(file_path: Path) -> bool:
    """Determine if a file should be checked for license headers."""
    # Check if file is in excluded directory
    for part in file_path.parts:
        if part in EXCLUDE_DIRS:
            return False
    
    # Check if file is excluded
    if file_path.name in EXCLUDE_FILES:
        return False
    
    # Only check Python files
    return file_path.suffix == '.py'


def has_license_header(file_path: Path) -> bool:
    """Check if a file has a valid MIT license header."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for MIT License mention in first 50 lines
        lines = content.split('\n')[:50]
        header_text = '\n'.join(lines)
        
        # Check for key MIT License phrases
        return 'MIT License' in header_text or 'Permission is hereby granted' in header_text
    except Exception:
        return False


def main():
    """Main function to check license headers."""
    # Get repository root
    repo_root = Path(__file__).parent.parent
    
    # Find all Python files
    python_files = []
    for root, dirs, files in os.walk(repo_root):
        # Remove excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for file in files:
            file_path = Path(root) / file
            if should_check_file(file_path):
                python_files.append(file_path)
    
    # Check each file
    missing_license = []
    for file_path in python_files:
        if not has_license_header(file_path):
            missing_license.append(file_path)
    
    # Report results
    if missing_license:
        print(f"❌ License header check failed for {len(missing_license)} files:")
        for file_path in missing_license:
            print(f"  - {file_path.relative_to(repo_root)}")
        sys.exit(1)
    else:
        print(f"✅ License header check passed for {len(python_files)} Python files")
        sys.exit(0)


if __name__ == '__main__':
    main()