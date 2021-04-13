def test_abnormal_impression(kb):
    text = 'Abnormal female karyotype'
    doc = kb.parse(text, pipeline='mm')
    assert len(doc.spans) == 1
    assert doc.spans[0].label == 'IMPRESSION'
    assert doc.spans[0].text == 'Abnormal female karyotype'


def test_normal_impression(kb):
    text = 'Normal female karyotype'
    doc = kb.parse(text, pipeline='mm')
    assert 'IMPRESSION' not in [x.label for x in doc.spans]
