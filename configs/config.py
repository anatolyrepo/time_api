class Config:
    """Класс-конфиг, со всеми параметрами, которые необходимы фикстурам / тестам."""

    # Базовый хост
    base_host: str = None
    base_url: str = None

    @classmethod
    def configure(cls, **kwargs):
        for name in kwargs:
            if not hasattr(cls, name):
                raise TypeError(f'Config doesn\'t have option {name}. Is there typo?')
            setattr(cls, name, kwargs[name])

        Config.base_url = f"https://{Config.base_host}"
