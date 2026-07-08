def precision_at_k(ranking, gold, k):
    top = ranking[:k]
    return sum(1 for d in top if gold.get(d, 0) >= 1) / k


def recall_at_k(ranking, gold, k):
    rel_gesamt = sum(1 for g in gold.values() if g >= 1)
    if not rel_gesamt:
        return 0.0
    top = ranking[:k]
    return sum(1 for d in top if gold.get(d, 0) >= 1) / rel_gesamt


def reciprocal_rank(ranking, gold):
    for i, d in enumerate(ranking, start=1):
        if gold.get(d, 0) >= 1:
            return 1.0 / i
    return 0.0


def average_precision(ranking, gold):
    rel_gesamt = sum(1 for g in gold.values() if g >= 1)
    if not rel_gesamt:
        return 0.0
    treffer = 0
    summe = 0.0
    for i, d in enumerate(ranking, start=1):
        if gold.get(d, 0) >= 1:
            treffer += 1
            summe += treffer / i
    return summe / rel_gesamt


def dcg(grades, k):
    return sum((2 ** g - 1) / math.log2(i + 2) for i, g in enumerate(grades[:k]))


def ndcg_at_k(ranking, gold, k):
    grades = [gold.get(d, 0) for d in ranking]
    ideal = sorted(gold.values(), reverse=True)
    idcg = dcg(ideal, k)
    return dcg(grades, k) / idcg if idcg else 0.0
