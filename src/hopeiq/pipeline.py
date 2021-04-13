from typing import Iterator
from entitykb import (
    Span,
    DedupeByKeyOffset,
    SpanMatch,
    interfaces
)
from ontologykb.field_name import FieldNameCombiner as FNCombiner
from ontologykb.biomarker_results import ResultCombiner as BRCombiner
from hopeiq.mm_biomarker import ResultCombiner as MMBRCombiner


class DedupeCustom(DedupeByKeyOffset):
    """ Keeps longest overlapping spans. """

    def is_unique(self, span: Span) -> bool:
        is_unique = self.seen.isdisjoint(span.offsets)
        self.seen.update(span.offsets)
        return is_unique

    @classmethod
    def sort_key(cls, span: Span):
        return (
            -span.num_tokens,  # longest wins
            span.match_type(),  # exact name > exact synonym > lower case
            span.offset,  # deterministic
            span.label,  # deterministic
        )


class ShortInexactFilterer(interfaces.IFilterer):
    def is_keep(self, span: Span):
        return (
            # keep text with length > 3
            len(span.text) > 3
            # keep text with numbers or symbols (often measurements)
            or len(set.intersection(set(span.text), set("1234567890%<>=-+~")))
            > 0
            # keep text which is not solely a lowercase synonym
            or span.match_type()
            not in {SpanMatch.LowercaseSynonym, SpanMatch.LowercaseName}
        )


class MMFilterer(interfaces.IFilterer):
    """ Strategic ordering of Filterers to minimize configuration issues. """

    def filter(self, spans: Iterator[Span]) -> Iterator[Span]:
        spans = ShortInexactFilterer(self.doc).filter(spans)
        spans = DedupeCustom(self.doc).filter(spans)
        spans = FNCombiner(self.doc).filter(spans)
        spans = MMBRCombiner(self.doc).filter(spans)
        spans = BRCombiner(self.doc).filter(spans)
        return spans
