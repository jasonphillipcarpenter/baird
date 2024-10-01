"""Test for baird.cli"""
# pylint: disable=redefined-outer-name


import argparse
import textwrap
import pytest
import toml
from unittest import mock

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
    return Cli(argparse, textwrap, toml).return_parser()


@pytest.mark.parametrize("args", [["--version"]])
def test_cli_with_version(parser, args):
    """
    Test that --version outputs the correct version
    """
    with mock.patch("sys.exit") as exit_mock, mock.patch("sys.stdout", new_callable=mock.MagicMock()) as stdout_mock:
        parser.parse_args(args)
        exit_mock.assert_called_once()
        stdout_mock.write.assert_called_once_with("pytest 1.0.1\n")


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
        Cli(argparse, textwrap, toml).return_args()
