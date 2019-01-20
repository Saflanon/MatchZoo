import matchzoo as mz
from matchzoo.auto.tuner.callbacks.callback import Callback


class LambdaCallback(Callback):
    """
    LambdaCallback. Just a shorthand for creating a callback class.

    See :class:`matchzoo.tuner.callbacks.Callback` for more details.

    Example:
        >>> import matchzoo as mz
        >>> callback = mz.tuner.callbacks.LambdaCallback(on_run_start=print)
        >>> callback.on_run_start('tuner', {'dict': 'of sample'})
        tuner {'dict': 'of sample'}

    """

    def __init__(
        self,
        on_run_start=None,
        on_build_end=None,
        on_result_end=None
    ):
        """Init."""
        self._on_run_start = on_run_start
        self._on_build_end = on_build_end
        self._on_result_end = on_result_end

    def on_run_start(self, tuner, sample: dict):
        """`on_run_start`."""
        self._on_run_start(tuner, sample)

    def on_build_end(self, tuner, model: mz.engine.BaseModel):
        """`on_build_end`."""
        self._on_build_end(tuner, model)

    def on_run_end(self, tuner, model: mz.engine.BaseModel, result: dict):
        """`on_run_end`."""
        self._on_result_end(tuner, model, result)
