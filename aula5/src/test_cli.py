from click.testing import CliRunner
from run import run

def test_call_hello():
    breakpoint()
    runner = CliRunner()
    result = runner.invoke(run.hello)
    assert result.exit_code == 0
    assert "Hello" in result.output