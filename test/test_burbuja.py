import pytest
from src.burbuja import OrdenarNumerosBurbuja

@pytest.mark.parametrize(
    "a",
    [
      [8, 3, 1, 19, 14],
      [1, 3, 8, 14, 19]
    ]
  )
def test_OrdenarNumeroBurbuja(a):
    assert OrdenarNumerosBurbuja(a) == a