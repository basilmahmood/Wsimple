"""
 Wsimple v1.0
 Copyright (c) 2020 Chromazmoves
"""
from .api import Wsimple
from .errors import LoginError, MethodInputError
from .errors import InvalidAccessTokenError, InvalidRefreshTokenError
from .errors import WSOTPUser, WSOTPError, WSOTPLoginError