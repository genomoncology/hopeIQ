import pytest


@pytest.mark.xfail()
def test_light_chain_restriction(kb):
    text = "KAPPA MONOTYPIC PLASMA CELL MYELOMA, INVOLVING 50% OF NORMOCELLULAR MARROW"
    doc = kb.parse(text, pipeline='mm')
    assert len(doc.spans) == 2
    assert doc.spans[0].label == 'LIGHT_CHAIN_RESTRICTION'
    assert doc.spans[0].text == 'KAPPA MONOTYPIC'
    assert doc.spans[1].label == 'AVERAGE_PLASMA_CELL_PERCENTAGE'
    assert doc.spans[1].text == '50%'
