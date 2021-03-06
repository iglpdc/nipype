# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ....testing import assert_equal
from ..utils import Similarity


def test_Similarity_inputs():
    input_map = dict(ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    mask1=dict(),
    mask2=dict(),
    metric=dict(usedefault=True,
    ),
    volume1=dict(mandatory=True,
    ),
    volume2=dict(mandatory=True,
    ),
    )
    inputs = Similarity.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(inputs.traits()[key], metakey), value


def test_Similarity_outputs():
    output_map = dict(similarity=dict(),
    )
    outputs = Similarity.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
