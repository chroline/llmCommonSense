import numpy as np


def dcg_at_k(r, k=5):
    """ Calculate DCG for the top k scores only """
    r = np.asarray(r, dtype=np.float64)[:k]
    if r.size:
        return r[0] + np.sum(r[1:] / np.log2(np.arange(2, r.size + 1)))
    return 0.


def ndcg_at_k(r, k=5):
    """ Calculate NDCG for the top k scores """
    dcg_max = dcg_at_k(sorted(r, reverse=True), k)
    return dcg_at_k(r, k) / dcg_max if dcg_max > 0 else 0.
