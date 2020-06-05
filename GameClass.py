class Game(object):
    """
    Creates a Game class object to start a Bowling Game.
    """

    def __init__(self):
        self.__frame = {}

    def create_frame(self):
        """
        Create a frame to score the pins knocked in each turn of play.
        :return: A frame in python dict format:
        {1: [None, None], 2: [None, None], 3: [None, None], 4: [None, None], 5: [None, None], 6: [None, None],
               7: [None, None], 8: [None, None], 9: [None, None], 10: [None, None, None]}
        """
        for i in range(1, 10):
            self.__frame[i] = [None, None]
        self.__frame[10] = [None, None, None]

    @property
    def get_frame(self):
        return self.__frame

    def roll(self, pins):
        """
        Method to perform a roll in bowling and appending the result to the created frame.
        :param pins: Number of pins knocked on this roll.
        :return: Insert the number of pins on the appropriated frame..
        """
        for key, value in self.__frame.items():
            if key < 10:
                if value[0] is None and value[1] is None:
                    if pins == 10:
                        value[0] = 10
                        value[1] = 0
                    else:
                        value[0] = pins
                    break
                elif value[0] is not None and value[1] is None:
                    value[1] = pins
                    break
            elif key == 10:  # rules for 10th frame
                if value[0] is None:
                    value[0] = pins
                elif value[1] is None:
                    value[1] = pins
                else:
                    value[2] = pins
                break

    @property
    def score(self):
        """
        Defines the score of the game based on iterating over the frames of the Game.
        :return: An integer representing the total score of the game.
        """
        result = 0
        # Iterating over self.rolls two by two, 2 rolls per frame
        for frame_index in self.__frame.keys():
            if self.is_strike(frame_index):
                result += self.strike_score(frame_index)
            elif self.is_spare(frame_index):
                result += self.spare_score(frame_index)
            else:
                result += self.frame_score(frame_index)
        return result

    def frame_score(self, frame_index):
        """
        Defines the sum of points for a frame of rolls.
        :return: Integer representing the frame score.
        """
        if frame_index < 10:
            return (self.__frame[frame_index][0] or 0) + (self.__frame[frame_index][1] or 0)
        else:
            return (self.__frame[frame_index][0] or 0) + (self.__frame[frame_index][1] or 0) + (
                    self.__frame[frame_index][2] or 0)

    def is_spare(self, frame_index):
        """
        Defines if the frame is a spare.
        :return: True or False if a frame is a spare.
        """
        return (self.__frame[frame_index][0] or 0) + (self.__frame[frame_index][1] or 0) == 10

    def spare_score(self, frame_index):
        """
        Defines the sum of points for a spare frame of rolls.
        :return: Integer representing the spare score.
        """
        if frame_index < 10:
            return (self.__frame[frame_index][0] or 0) + (self.__frame[frame_index][1] or 0) + (
                    self.__frame[frame_index + 1][
                        0] or 0)
        else:
            return (self.__frame[frame_index][0] or 0) + (self.__frame[frame_index][1] or 0) + (
                    self.__frame[frame_index][
                        2] or 0)

    def is_strike(self, frame_index):
        return self.__frame[frame_index][0] == 10

    def strike_score(self, frame_index):
        if frame_index < 9:
            if self.is_strike(frame_index + 1) and self.is_strike(frame_index + 2):
                return 30
            elif self.is_strike(frame_index + 1) and not self.is_strike(frame_index + 2):
                return 20 + (self.__frame[frame_index + 2][0] or 0)
            else:
                return 10 + (self.__frame[frame_index + 1][0] or 0) + (self.__frame[frame_index + 1][1] or 0)
        elif frame_index == 9:
            return 10 + (self.__frame[frame_index + 1][0] or 0) + (self.__frame[frame_index + 1][1] or 0)
        else:
            return 10 + (self.__frame[frame_index][1] or 0) + (self.__frame[frame_index][2] or 0)

    def roll_many(self, rolls):
        """
        Only used on the tests.
        Method to produce a number os rolls with fixed pins knocked.
        :param rolls: list of rolls pins knocked
        :return: insert on the frames for score iteration.
        """
        for pin in rolls:
            self.roll(pin)
