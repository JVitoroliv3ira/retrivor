from typer.testing import CliRunner
from retrivor_cli.cli import app

runner = CliRunner()

def test_index_command():
    result = runner.invoke(app, ["index"])
    assert result.exit_code == 0
    assert "Hello, World!" in result.output