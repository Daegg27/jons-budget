from enum import Enum


class Month(Enum):
    JAN = 0
    FEB = 1
    MAR = 2
    APR = 3
    MAY = 4
    JUNE = 5
    JULY = 6
    AUG = 7
    SEPT = 8
    OCT = 9
    NOV = 10 
    DEC = 11

    @staticmethod
    def get_month_name(method):
        if month == Month.MAY:
            return "May"