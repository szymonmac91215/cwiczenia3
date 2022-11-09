from day_z3 import Day
import re


class Term:
    def __init__(self, d, h, m, duration=90):
        self.day = d
        self.hour = h
        self.minute = m
        self.duration = duration

    def __str__(self):
        hoursDelta = self.duration // 60
        minutesDelta = self.duration % 60
        if self.minute + minutesDelta > 59:
            hoursDelta += 1
            minutesDelta -= 60
        if self.duration < 91:
            return f'{self.day} {self.hour}:{self.minute:02d}-{self.hour + hoursDelta}:{self.minute + minutesDelta:02d} [{self.duration}]'
        else:
            return f'{self.day} {self.hour}:{self.minute:02d} [{self.duration}]'

    def earlierThan(self, termin):
        if self.day.difference(termin.day) < 0:
            return False

        if self.day.difference(termin.day) > 0:
            return True

        if termin.hour < self.hour:
            return False

        if termin.hour > self.hour:
            return True

        if termin.minute <= self.minute:
            return False

        return True

    def laterThan(self, termin):
        if self.day.difference(termin.day) > 0:
            return False

        if self.day.difference(termin.day) < 0:
            return True

        if termin.hour > self.hour:
            return False

        if termin.hour < self.hour:
            return True

        if termin.minute >= self.minute:
            return False

        return True

    def equals(self, termin):
        return termin.hour == self.hour and termin.minute == self.minute and termin.duration == self.duration and self.day == termin.day

    def __lt__(self, termin):
        return self.earlierThan(termin)

    def __gt__(self, termin):
        return self.laterThan(termin)

    def __eq__(self, termin):
        return self.equals(termin)

    def __le__(self, termin):
        return self.earlierThan(termin) or self.equals(termin)

    def __ge__(self, termin):
        return self.laterThan(termin) or self.equals(termin)

    def __sub__(self, termin):
        return Term(termin.day, termin.hour, termin.minute,
                    (self.day.value - termin.day.value) * 1440 + (self.hour - termin.hour) * 60 + (
                                self.minute - termin.minute) + self.duration)
