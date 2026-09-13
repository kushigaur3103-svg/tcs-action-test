"""
File exporter utilities with intentional Command Injection and Path Traversal.
"""

import subprocess
from flask import request


def export_archive():
    """CWE-78: User-controlled input reaching subprocess.Popen with shell=True."""
    target_format = request.args.get("format")
    # Command string concatenation with untrusted input
    cmd = "tar -czf export.tar.gz --format=" + target_format
    proc = subprocess.Popen(cmd, shell=True)
    return proc.pid


def read_exported_report():
    """CWE-22: User-controlled path reaching unsafe open() filesystem access."""
    report_name = request.args.get("report_name")
    # Path composition with untrusted input without containment checks
    file_path = "/var/reports/" + report_name
    with open(file_path, "r") as f:
        return f.read()
