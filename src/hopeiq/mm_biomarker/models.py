from __future__ import annotations
from typing import List
from entitykb import Entity, Span


class Biomarker(Entity):
    def __init__(self, **data):
        super().__init__(**data)

    @classmethod
    def create(self, text: str) -> Biomarker:
        return Biomarker(
            name=text
        )


class BiomarkerResult(Entity):
    biomarker: Entity
    subspans: List[Span] = []

    def __init__(self, **data):
        super().__init__(**data)

    @classmethod
    def create(self, biomarker_span: Span) -> BiomarkerResult:
        return BiomarkerResult(
            name=biomarker_span.text,
            biomarker=biomarker_span.entity,
            subspans=[biomarker_span]
        )


class AbnormalCells(Entity):
    def __init__(self, **data):
        super().__init__(**data)

    @classmethod
    def create(self, text: str) -> AbnormalCells:
        return AbnormalCells(
            name=text
        )


class TotalCells(Entity):
    def __init__(self, **data):
        super().__init__(**data)

    @classmethod
    def create(self, text: str) -> TotalCells:
        return TotalCells(
            name=text
        )


class MmBiomarkerMutation(Entity):
    def __init__(self, **data):
        super().__init__(**data)

    @classmethod
    def create(self, text: str) -> MmBiomarkerMutation:
        return MmBiomarkerMutation(
            name=text
        )
