from enum import Enum


class UserRole(Enum):
    GUEST = 'Guest'
    PLAYER = 'Player'
    ADMIN = 'Administrator'
    NANNY_MODERATOR = 'NannyModerator'
    REGULAR_MODERATOR = 'RegularModerator'
    SENIOR_MODERATOR = 'SeniorModerator'
