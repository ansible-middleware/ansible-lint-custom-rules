# Copyright (C) 2020, 2021 Satoru SATOH <satoru.satoh@gmail.com>
# SPDX-License-Identifier: MIT
#
# pylint: disable=inherit-non-class
"""Common utility functios and classes - datatypes.
"""
import pathlib
import typing


class SubCtx(typing.NamedTuple):
    """A namedtuple object to keep sub context info, conf and env.
    """
    conf: typing.Dict[str, typing.Any]
    env: typing.Dict[str, str]
    os_env: typing.Dict[str, str]


class Context(typing.NamedTuple):
    """A namedtuple object to keep context info.
    """
    workdir: pathlib.Path
    lintables: typing.List[typing.Any]  # TBD
    conf: typing.Dict[str, typing.Any]
    env: typing.Dict[str, str]
    os_env: typing.Dict[str, str]


class Result(typing.NamedTuple):
    """A namedtuple object to keep lint result and context info.
    """
    result: typing.Any
    ctx: Context

# vim:sw=4:ts=4:et:
