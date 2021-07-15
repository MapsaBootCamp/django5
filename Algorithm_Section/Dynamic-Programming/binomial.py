# def binomial(n, k):
#     if n == 1 or k == 0 or n == k:
#         return 1
#     else:
#         return binomial(n-1, k-1) + binomial(n-1, k)

def binomial_optimize(n, k, memoize={}):
    if n == k:
        return 1
    if n == 1 or k == 0:
        return 1
    if (n, k) in memoize:
        print(memoize)
        return memoize.get((n, k))

    else:
        result = binomial_optimize(
            n-1, k-1, memoize) + binomial_optimize(n-1, k, memoize)
        memoize[(n, k)] = result
        return result


print(binomial_optimize(12, 54))


def factotial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factotial(n-1)


def binomial_maskhareh(n, k):
    if n == 1 or k == 0 or n == k:
        return 1
    else:
        return factotial(n) / (factotial(n-k) * factotial(k))
