"""Test for baird.cli"""
# pylint: disable=redefined-outer-name


import argparse
import textwrap
import pytest

from baird.cli import Cli

ARGS = [
    "--title",
    "mock_title",
    "--login",
    "mock_login",
    "--identityfile",
    "mock_identityfile",
    "--bastion",
    "mock_bastion",
    "--bastion-login",
    "mock_bastion_login",
    "--bastion-id",
    "mock_bastion_id",
    "mockserver1",
    "mockserver2",
]


@pytest.fixture
def parser():
    """
    Return arguments
    """
    return Cli(argparse, textwrap).return_parser()


def test_cli_with_args(parser):
    """
    Will succeed when all passed arguments are stored
    """
    args = parser.parse_args(ARGS)
    assert args.title == "mock_title"
    assert args.login == "mock_login"
    assert args.identityfile == "mock_identityfile"
    assert args.bastion == "mock_bastion"
    assert args.bastion_login == "mock_bastion_login"
    assert args.bastion_id == "mock_bastion_id"
    assert args.servers == ["mockserver1", "mockserver2"]


def test_cli_without_servers():
    """
    Will fail when no servers are passed
    """
    with pytest.raises(SystemExit):
        Cli(argparse, textwrap).return_args()
