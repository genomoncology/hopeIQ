from hopeiq import SyncKB


def test_resolve_gene():
    kb = SyncKB()
    gene = kb.find_one("BRAF")
    assert gene.key == "BRAF|GENE"
