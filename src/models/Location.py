
class Location:
  __slots__ = ('url', 'ok')

  def __init__(self, url: str, ok: bool) -> None:
    self.url = url; self.ok = ok

  def __repr__(self) -> str:
    return f'{self.url} -> {self.ok}'