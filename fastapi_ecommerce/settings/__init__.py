from .settings import (
    DBSettings,
    DevelopmentDBSettings,
    EnvironmentSettings,
    TestDBSettings,
)

environment_settings = EnvironmentSettings()

match environment_settings.name:
    case "development":
        db_settings = DevelopmentDBSettings()
    case "production":
        db_settings = DBSettings()
    case "test":
        db_settings = TestDBSettings()

