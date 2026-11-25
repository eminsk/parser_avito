"""Tests for community, Telegram channel, and proxy link constants."""

import ast
from pathlib import Path

import lang


def test_community_and_proxy_links():
    """Verify partner, SDK, and Telegram channel links stay aligned."""
    assert lang.PROXY_LINK == "https://mobileproxy.rent/?p=279117"
    assert lang.PROXY_FREE_TRIAL_LINK == "https://mobileproxy.rent/user.html?free&p=279117"
    assert lang.TELEGRAM_CHANNEL_LINK == "https://t.me/avito_sdk_pro"
    assert lang.SDK_LINK == "https://github.com/eminsk/avito-sdk"
    assert lang.ISSUES_LINK == "https://github.com/eminsk/parser_avito/issues"
    assert lang.TELEGRAM_CHANNEL_LINK in lang.PROXY_PANEL_HELP
    assert lang.PROXY_FREE_TRIAL_LINK in lang.PROXY_PANEL_HELP


def test_gui_module_valid_syntax_and_references():
    """Ensure AvitoParser.py parses cleanly and wires Telegram channel links."""
    gui_path = Path(__file__).resolve().parent.parent / "AvitoParser.py"
    source = gui_path.read_text(encoding="utf-8")
    ast.parse(source)
    assert "TELEGRAM_CHANNEL_LINK" in source
    assert "PROXY_FREE_TRIAL_LINK" in source
