class DisabledFormFieldsMixin:
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].disabled = True
