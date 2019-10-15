"""Test for baird.ssh_cmd"""
# pylint: disable=redefined-outer-name


from mocks.mock_cli import Cli
from baird.ssh_cmd import SSHCmd


def test_ssh_cmd_strings():
    """
    Will succeed when expected strings are returned
    """
    args = Cli()
    ssh_cmd = SSHCmd(
        args
    )
    assert ssh_cmd.bastion_login() == f"-l {args.bastion_login}"
    assert ssh_cmd.bastion_id() == f"-i {args.bastion_id}"
    assert ssh_cmd.bastion() == f"{args.bastion} -At ssh"
    assert ssh_cmd.login() == f"-l {args.login}"
    assert ssh_cmd.identityfile() == f"-i {args.identityfile}"


def test_return_ssh_cmd():
    """
    Will succeed when expected string is returned
    """
    args = Cli()
    ssh_cmd = SSHCmd(
        args
    )
    mock_ssh_cmd = [
        'ssh',
        '-l', args.bastion_login,
        '-i', args.bastion_id,
        args.bastion, '-At ssh',
        '-l', args.login,
        '-i', args.identityfile,
    ]

    assert ssh_cmd.return_ssh_cmd() == ' '.join(mock_ssh_cmd)
