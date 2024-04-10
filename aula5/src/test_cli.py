from click.testing import CliRunner
from run import run

def test_call_hello():
    breakpoint()
    runner = CliRunner()
    result = runner.invoke(run.hello)
    assert result.exit_code == 0
    assert "Hello" in result.output


def test_call_add():
    breakpoint()
    runner = CliRunner()
    result = runner.invoke(run.CARROT)
    assert result.exit_code == 0
    assert "CARROT added!" in result.output


def test_call_remove():
    breakpoint()
    runner = CliRunner()
    result = runner.invoke(run.hellopo)
    assert result.exit_code == 0
    assert "CARROT remove" in result.output