class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL
        self.__old_volume: int = 0

    def power(self) -> None:
        """
        Toggles power status of TV
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Toggles mute status of TV
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__old_volume
            else:
                self.__muted = True
                self.__old_volume = self.__volume
                self.__volume = self.MIN_VOLUME

    def channel_up(self) -> None:
        """
        Increases channel, looping if at max
        """
        if self.__status:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decreases channel, looping if at min
        """
        if self.__status:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increases volume, halting at max
        """
        if self.__status:
            if self.__muted:
                self.mute()
                if self.__volume < self.MAX_VOLUME:
                    self.__volume += 1
            else:
                if self.__volume < self.MAX_VOLUME:
                    self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases volume, halting at min
        """
        if self.__status:
            if self.__muted:
                self.mute()
                if self.__volume > self.MIN_VOLUME:
                    self.__volume -= 1
            else:
                if self.__volume > self.MIN_VOLUME:
                    self.__volume -= 1

    def __str__(self) -> str:
        return f'Power = {self.__status}, Channel  = {self.__channel}, Volume = {self.__volume}'
