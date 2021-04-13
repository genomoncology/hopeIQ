import pytest

@pytest.mark.xfail()
def test_mm_biomarker(kb):
    text = 'Chromosome 1p/1q FISH Assay [Cytocell CDKN2C (1p32.3)/CKS1B (1q21.3) DC]'
    doc = kb.parse(text, pipeline='mm')
    assert len(doc.spans) == 1
    assert doc.spans[0].label == 'BIOMARKER_RESULT'
    assert doc.spans[0].text == 'CDKN2C (1p32.3)/CKS1B (1q21.3)'
    assert len(doc.spans[0].entity.subspans) == 1
    assert doc.spans[0].entity.subspans[0].label == 'BIOMARKER'
    assert doc.spans[0].entity.subspans[0].text == 'CDKN2C (1p32.3)/CKS1B (1q21.3)'


@pytest.mark.xfail()
def test_mm_biomarker_cell_counts(kb):
    text = 'nuc ish(CDKN2Cx2,CKS1Bx5)[19/20]'
    doc = kb.parse(text, pipeline='mm')
    assert len(doc.spans) == 2
    assert doc.spans[0].label == 'ABNORMAL_CELLS'
    assert doc.spans[0].text == '19'
    assert doc.spans[1].label == 'TOTAL_CELLS'
    assert doc.spans[1].text == '20'


@pytest.mark.xfail()
def test_mm_biomarker_cell_counts_no_abnormal(kb):
    text = 'nuc ish(MYCx2)[60]'
    doc = kb.parse(text, pipeline='mm')
    assert len(doc.spans) == 1
    assert doc.spans[0].label == 'TOTAL_CELLS'
    assert doc.spans[0].text == '60'


@pytest.mark.xfail()
def test_mm_biomarker_mutation(kb):
    text = 'nuc ish(CDKN2Cx2,CKS1Bx5)[19/20] Copy number changes of CKS1B [5 copies]'
    doc = kb.parse(text, pipeline='mm')
    assert len(doc.spans) == 3
    assert doc.spans[2].label == 'MM_BIOMARKER_MUTATION'
    assert doc.spans[2].text == 'Copy number changes of CKS1B [5 copies]'


