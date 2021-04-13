from typing import Iterator, Iterable, List, Tuple
from entitykb import DocToken, Span
from entitykb.interfaces import IFilterer
from .models import (
    Biomarker,
    BiomarkerResult,
    AbnormalCells,
    TotalCells,
    MmBiomarkerMutation
)


class ResultRelevantEntity(IFilterer):
    def filter(self, spans: Iterable[Span]) -> Tuple[List[Span], List[Span]]:
        relevant_spans, irrelevant_spans = [], []
        for span in spans:
            if span.label in ['MEASUREMENT', 'MM_BIOMARKER_MUTATION']:
                relevant_spans.append(span)
            else:
                irrelevant_spans.append(span)
        return relevant_spans, irrelevant_spans


class BiomarkerRelevantEntity(IFilterer):
    def filter(self, spans: Iterable[Span]) -> Tuple[List[Span], List[Span]]:
        relevant_spans, irrelevant_spans = [], []
        for span in spans:
            if span.label == 'MM_BIOMARKER':
                relevant_spans.append(span)
            else:
                irrelevant_spans.append(span)
        return relevant_spans, irrelevant_spans


class ResultCombiner(IFilterer):
    def filter(self, spans: Iterator[Span]) -> Iterator[Span]:
        spans = list(spans)
        if self.doc.text.startswith('nuc ish'):
            relevant_spans, _ = ResultRelevantEntity().filter(
                spans
            )
            output_spans = _process_mm_biomarker_result(
                relevant_spans, self.doc.tokens
            )
        elif 'MM_BIOMARKER' in [x.label for x in spans]:
            relevant_spans, _ = BiomarkerRelevantEntity().filter(
                spans
            )
            output_spans = _process_mm_biomarker(relevant_spans)
        else:
            output_spans = spans
        return sorted(output_spans, key=lambda x: x.tokens[0].offset)


def _process_mm_biomarker_result(
        spans: List[Span], tokens: List[DocToken]
) -> List[Span]:
    result_spans = []

    measurement_spans = [x for x in spans if x.label == 'MEASUREMENT']
    if len(measurement_spans) > 1:
        abnormal_text = measurement_spans[0].text
        total_text = measurement_spans[1].text
        result_spans.append(
            Span(
                text=abnormal_text,
                entity=AbnormalCells.create(abnormal_text),
                tokens=measurement_spans[0].tokens
            )
        )
        result_spans.append(
            Span(
                text=total_text,
                entity=TotalCells.create(total_text),
                tokens=measurement_spans[1].tokens
            )
        )
    elif len(measurement_spans) == 1:
        total_text = measurement_spans[0].text
        result_spans.append(
            Span(
                text=total_text,
                entity=TotalCells.create(total_text),
                tokens=measurement_spans[0].tokens
            )
        )

    mm_mutation_type_spans = [
        x for x in spans if x.label == 'MM_BIOMARKER_MUTATION'
    ]
    if len(mm_mutation_type_spans) > 0:
        token_start = mm_mutation_type_spans[0].offset
        mm_mutation_type_tokens = tokens[token_start:]
        text = ' '.join([x.token for x in mm_mutation_type_tokens])
        result_spans.append(
            Span(
                text=text,
                entity=MmBiomarkerMutation.create(text),
                tokens=mm_mutation_type_tokens
            )
        )
    return result_spans


def _process_mm_biomarker(spans: List[Span]) -> List[Span]:
    result_spans = []
    if len(spans) > 0:
        text = '/'.join([x.text for x in spans])
        tokens = [token for span in spans for token in span.tokens]

        biomarker_span = Span(
            text=text,
            entity=Biomarker.create(text),
            tokens=tokens
        )

        biomarker_result_span = Span(
            text=text,
            entity=BiomarkerResult.create(biomarker_span),
            tokens=tokens
        )
        result_spans.append(biomarker_result_span)

    return result_spans
