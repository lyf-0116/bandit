#
# Copyright 2016 Hewlett-Packard Development Company, L.P.
#
# SPDX-License-Identifier: Apache-2.0
r"""Utils module."""

from bandit.core import blacklisting


def build_conf_dict(name, bid, cwe, qualnames, message, level="MEDIUM"):
    """Build and return a blacklist configuration dict."""
    return {
        "name": name,
        "id": bid,
        "cwe": cwe,
        "message": message,
        "qualnames": qualnames,
        "level": blacklisting.normalize_level(level),
    }
