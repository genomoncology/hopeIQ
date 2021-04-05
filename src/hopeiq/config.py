import os

from entitykb import Config, environ

environ.DEFAULTS.ENTITYKB_ROOT = os.path.expanduser("~/.hopeiq/")

default_config = Config(
    graph="entitykb.Graph",
    modules=["ontologykb", "hopeiq"],
    normalizer="entitykb.LatinLowercaseNormalizer",
    searcher="entitykb.DefaultSearcher",
    tokenizer="ontologykb.PathTokenizer",
    pipelines={
        "default": {
            "extractor": "entitykb.DefaultExtractor",
            "resolvers": [
                "entitykb.TermResolver",
                "entitykb.contrib.date.DateResolver",
                "ontologykb.PersonResolver",
                "ontologykb.MutationGrammarResolver",
                "ontologykb.IntensityResolver",
                "ontologykb.ClockPositionResolver",
                "ontologykb.MeasurementResolver",
                "ontologykb.pathology_stage.PathologyStageResolver",
                "ontologykb.SystemIDResolver",
                "ontologykb.LymphNodesResolver",
            ],
            "filterers": ["ontologykb.CombinedFilterer"],
        }
    },
)
