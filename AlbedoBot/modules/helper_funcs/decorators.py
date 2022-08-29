from typing import List, Optional, Union

from telegram.ext import (
    CallbackQueryHandler,
    CommandHandler,
    InlineQueryHandler,
    MessageHandler,
)
from telegram.ext.filters import BaseFilter

from AlbedoBot import LOGGER
from AlbedoBot import NEKO_PTB as d
from AlbedoBot.modules.disable import (
    DisableAbleCommandHandler,
    DisableAbleMessageHandler,
)


class NekoTelegramHandler:
    def __init__(self, d):
        self._NEKO_PTB = d

    def command(
        self,
        command: str,
        filters: Optional[BaseFilter] = None,
        admin_ok: bool = False,
        pass_args: bool = False,
        pass_chat_data: bool = False,
        run_async: bool = True,
        can_disable: bool = True,
        group: Optional[Union[int]] = 40,
    ):
        def _command(func):
            try:
                if can_disable:
                    self._NEKO_PTB.add_handler(
                        DisableAbleCommandHandler(
                            command,
                            func,
                            filters=filters,
                            run_async=run_async,
                            pass_args=pass_args,
                            admin_ok=admin_ok,
                        ),
                        group,
                    )
                else:
                    self._NEKO_PTB.add_handler(
                        CommandHandler(
                            command,
                            func,
                            filters=filters,
                            run_async=run_async,
                            pass_args=pass_args,
                        ),
                        group,
                    )
                LOGGER.debug(
                    f"[NEKOCMD] Loaded handler {command} for function {func.__name__} in group {group}"
                )
            except TypeError:
                if can_disable:
                    self._NEKO_PTB.add_handler(
                        DisableAbleCommandHandler(
                            command,
                            func,
                            filters=filters,
                            run_async=run_async,
                            pass_args=pass_args,
                            admin_ok=admin_ok,
                            pass_chat_data=pass_chat_data,
                        )
                    )
                else:
                    self._NEKO_PTB.add_handler(
                        CommandHandler(
                            command,
                            func,
                            filters=filters,
                            run_async=run_async,
                            pass_args=pass_args,
                            pass_chat_data=pass_chat_data,
                        )
                    )
                LOGGER.debug(
                    f"[NEKOCMD] Loaded handler {command} for function {func.__name__}"
                )

            return func

        return _command

    def message(
        self,
        pattern: Optional[str] = None,
        can_disable: bool = True,
        run_async: bool = True,
        group: Optional[Union[int]] = 60,
        friendly=None,
    ):
        def _message(func):
            try:
                if can_disable:
                    self._NEKO_PTB.add_handler(
                        DisableAbleMessageHandler(
                            pattern, func, friendly=friendly, run_async=run_async
                        ),
                        group,
                    )
                else:
                    self._NEKO_PTB.add_handler(
                        MessageHandler(pattern, func, run_async=run_async), group
                    )
                LOGGER.debug(
                    f"[NEKOMSG] Loaded filter pattern {pattern} for function {func.__name__} in group {group}"
                )
            except TypeError:
                if can_disable:
                    self._NEKO_PTB.add_handler(
                        DisableAbleMessageHandler(
                            pattern, func, friendly=friendly, run_async=run_async
                        )
                    )
                else:
                    self._NEKO_PTB.add_handler(
                        MessageHandler(pattern, func, run_async=run_async)
                    )
                LOGGER.debug(
                    f"[NEKOMSG] Loaded filter pattern {pattern} for function {func.__name__}"
                )

            return func

        return _message

    def callbackquery(self, pattern: str = None, run_async: bool = True):
        def _callbackquery(func):
            self._NEKO_PTB.add_handler(
                CallbackQueryHandler(
                    pattern=pattern, callback=func, run_async=run_async
                )
            )
            LOGGER.debug(
                f"[NEKOCALLBACK] Loaded callbackquery handler with pattern {pattern} for function {func.__name__}"
            )
            return func

        return _callbackquery

    def inlinequery(
        self,
        pattern: Optional[str] = None,
        run_async: bool = True,
        pass_user_data: bool = True,
        pass_chat_data: bool = True,
        chat_types: List[str] = None,
    ):
        def _inlinequery(func):
            self._NEKO_PTB.add_handler(
                InlineQueryHandler(
                    pattern=pattern,
                    callback=func,
                    run_async=run_async,
                    pass_user_data=pass_user_data,
                    pass_chat_data=pass_chat_data,
                    chat_types=chat_types,
                )
            )
            LOGGER.debug(
                f"[NEKOINLINE] Loaded inlinequery handler with pattern {pattern} for function {func.__name__} | PASSES USER DATA: {pass_user_data} | PASSES CHAT DATA: {pass_chat_data} | CHAT TYPES: {chat_types}"
            )
            return func

        return _inlinequery


nekocmd = NekoTelegramHandler(d).command
nekomsg = NekoTelegramHandler(d).message
nekocallback = NekoTelegramHandler(d).callbackquery
nekoinline = NekoTelegramHandler(d).inlinequery
