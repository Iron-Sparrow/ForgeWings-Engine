from pprint import pprint

class ScreenSettings:
    def __init__(self, AspectRatio={16, 9}, height=1080, width=1920, RefreshRate=60, ScreenNumber=0) -> None:
        self.AspectRatio = AspectRatio
        self.Height = height
        self.Width = width
        self.RefreshRate = RefreshRate
        self.ScreenNumber = ScreenNumber
        if len(AspectRatio) != 2:
            raise ValueError(f"There isn't the right amout of values (2) in {AspectRatio}.")
        if height*AspectRatio[0]/AspectRatio[1] != width:
            pprint(f"The AspectRatio and the Screen Resolution don't match. {AspectRatio},{width, height}")