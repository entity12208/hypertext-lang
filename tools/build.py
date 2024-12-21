#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys
from pathlib import Path

def setup_build_dir():
    """Create and prepare build directory."""
    build_dir = Path("build")
    build_dir.mkdir(exist_ok=True)
    return build_dir

def configure_project(build_dir: Path, build_type: str):
    """Configure the CMake project."""
    cmd = [
        "cmake",
        "..",
        f"-DCMAKE_BUILD_TYPE={build_type}",
        "-DBUILD_TESTS=ON"
    ]
    
    subprocess.run(cmd, cwd=build_dir, check=True)

def build_project(build_dir: Path, jobs: int):
    """Build the project using CMake."""
    cmd = ["cmake", "--build", ".", f"-j{jobs}"]
    subprocess.run(cmd, cwd=build_dir, check=True)

def main():
    parser = argparse.ArgumentParser(description="Hypertext build tool")
    parser.add_argument("--build-type", choices=["Debug", "Release"], default="Debug")
    parser.add_argument("--jobs", "-j", type=int, default=os.cpu_count())
    args = parser.parse_args()

    try:
        build_dir = setup_build_dir()
        configure_project(build_dir, args.build_type)
        build_project(build_dir, args.jobs)
        print("Build completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
