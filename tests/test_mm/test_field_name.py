import pytest


def test_lab_no(kb):
    text = 'Lab No: 12345'
    doc = kb.parse(text, pipeline='mm')
    assert len(doc.spans) == 1
    assert doc.spans[0].label == 'REPORT_ID'
    assert doc.spans[0].text == '12345'


def test_collected_date(kb):
    text = "Collection Date/Time: 02/07/2017"
    doc = kb.parse(text, pipeline='mm')
    assert len(doc.spans) == 1
    assert doc.spans[0].label == 'COLLECTED_DATE'
    assert doc.spans[0].text == '02/07/2017'


# supporting this requires an update to structure detection and an update to
# base ontologies
@pytest.mark.xfail()
def test_stemline(kb):
    text = "Stemline: 42,XX,dic(1;22)(p13;p11.2),der(1;3)(q10;p10),+dup(1)" \
           "(q11q21),der(2)t(2;3)(p11.2;q12),der(2;17)(p10;q10), del(6)" \
           "(q21q23),der(8)t(8;9)(p23;q13),-13,?add(14)(q32.3),t(14;16)" \
           "(q32.3;q23.2),del(15)(?q11.1q11.2), der(16)t(1;16)(q21;q22)," \
           "der(21;?22)(q10;q10)[3]"
    doc = kb.parse(text, pipeline='mm')
    assert len(doc.spans) == 1
    assert doc.spans[0].label == 'STEMLINE'
    assert doc.spans[0].text == "42,XX,dic(1;22)(p13;p11.2),der(1;3)(q10;p10)," \
                                "+dup(1)(q11q21),der(2)t(2;3)(p11.2;q12)," \
                                "der(2;17)(p10;q10), del(6)(q21q23),der(8)" \
                                "t(8;9)(p23;q13),-13,?add(14)(q32.3),t(14;16)" \
                                "(q32.3;q23.2),del(15)(?q11.1q11.2), der(16)" \
                                "t(1;16)(q21;q22),der(21;?22)(q10;q10)[3]"


