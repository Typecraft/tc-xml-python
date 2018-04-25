import six

from typecraft_python.integrations.treetagger import TreeTagger


def batch(iterable, n=1):
    length = len(iterable)
    for next_index in range(0, length, n):
        yield iterable[next_index:min(next_index + n, length)]


# Taken from https://stackoverflow.com/questions/2130016/splitting-a-list-into-n-parts-of-approximately-equal-length
def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


TAGGER_TRANSLATIONS = {
    'tree': TreeTagger
}


def get_tagger_by_name(name):
    assert isinstance(name, six.string_types)

    name_lower = name.lower()
    if 'tree' in name_lower:
        return TreeTagger

    raise ValueError("Tagger %s not found" % (name,))


