from typing import Optional, List, Tuple

class PanCakeCookie:
  def __init__(self, w: int, h: int, maxC: int, u: int, d: int):
    self.__w=w
    self.__h=h
    self.__x=0
    self.__y=0
    self.__t=0
    self.__score=0
    self.__maxC=1
    self.__curC=self.maxC
    self.__u=1
    self.__d=1    

  def getX(self) -> int:
    return self.__x

  def getY(self) -> int:
    return self.__y

  def getU(self) -> int:
    return self.__u

  def getD(self) -> int:
    return self.__d

  def getScore(self) -> int:
    return self.__score

  def getC(self) -> int:
    return self.__curC

  def reset(self) -> None:
    # TODO

  def setU(self, x: int) -> None:
    # TODO

  def setD(self, x: int) -> None:
    # TODO

  def setC(self, x: int) -> None:
    # TODO

  def setT(self, t: int) -> None:
    # TODO
