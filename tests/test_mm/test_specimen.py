import pytest


@pytest.mark.xfail()
def test_specimen(kb):
    text = "BONE MARROW, SITE NOT SPECIFIED, ASPIRATE SMEAR, CLOT SECTION, TREPHINE BIOPSY AND PERIPHERAL BLOOD"
    doc = kb.parse(text, pipeline='mm')
    assert len(doc.spans) == 1
    assert doc.spans[0].label == 'SPECIMEN'
    assert doc.spans[0].text == 'BONE MARROW ASPIRATE'
    assert len(doc.spans[0].entity.subspans) == 2
    assert doc.spans[0].entity.subspans[0].label == 'SITE'
    assert doc.spans[0].entity.subspans[0].text == 'BONE MARROW'
    assert doc.spans[0].entity.subspans[1].label == 'PROCEDURE'
    assert doc.spans[0].entity.subspans[1].text == 'ASPIRATE'
