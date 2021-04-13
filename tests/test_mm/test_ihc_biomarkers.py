def test_biomarkers(kb):
    text = 'CD20 - POSITIVE IN RARE SCATTERED B-CELLS'
    doc = kb.parse(text, pipeline='mm')
    assert len(doc.spans) == 1
    assert doc.spans[0].label == 'BIOMARKER_RESULT'
    assert len(doc.spans[0].entity.subspans) == 2
    assert doc.spans[0].entity.subspans[0].label == 'BIOMARKER'
    assert doc.spans[0].entity.subspans[0].text == 'CD20'
    assert doc.spans[0].entity.subspans[1].label == 'PNE_STATUS'
    assert doc.spans[0].entity.subspans[1].text == 'POSITIVE IN RARE SCATTERED B-CELLS'
