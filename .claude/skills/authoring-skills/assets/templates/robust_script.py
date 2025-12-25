#!/usr/bin/env python3
"""
Template for robust Agent Skills scripts.
Features: Argument parsing, Error handling, JSON output option, Path resolution.
"""

import argparse
import json
import sys
import os
from pathlib import Path

# Resolve paths relative to this script's location
# This ensures assets are found regardless of where the script is called from
SCRIPT_DIR = Path(__file__).parent.resolve()
SKILL_ROOT = SCRIPT_DIR.parent
ASSETS_DIR = SKILL_ROOT / "assets"

def setup_logging(verbose: bool):
    """Simple logging to stderr so stdout remains clean for JSON/Data."""
    def log(msg):
        if verbose:
            print(f"[INFO] {msg}", file=sys.stderr)
    return log

def main():
    parser = argparse.ArgumentParser(description="Description of what this script does.")
    parser.add_argument("input_file", type=str, help="Path to input file")
    parser.add_argument("--output", type=str, default=None, help="Path to output file")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose logging")
    
    # Parse args
    args = parser.parse_args()
    log = setup_logging(args.verbose)

    try:
        # 1. Validation
        input_path = Path(args.input_file).resolve()
        if not input_path.exists():
            print(f"Error: Input file not found: {input_path}", file=sys.stderr)
            sys.exit(1)

        log(f"Processing {input_path}...")

        # 2. Execution Logic
        # ... Your logic here ...
        result = {"status": "success", "processed": str(input_path)}

        # 3. Output
        # Print structured data to stdout for the Agent to parse
        print(json.dumps(result, indent=2))
        
    except Exception as e:
        # Catch-all to prevent raw stack traces from confusing the Agent unless verbose
        error_msg = {"status": "error", "message": str(e)}
        print(json.dumps(error_msg), file=sys.stdout) # Print valid JSON even on error
        if args.verbose:
            raise
        sys.exit(1)

if __name__ == "__main__":
    main()
