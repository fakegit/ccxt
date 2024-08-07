import os
import sys

root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.append(root)

# ----------------------------------------------------------------------------

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

# ----------------------------------------------------------------------------
# -*- coding: utf-8 -*-

from ccxt.async_support.base.ws.cache import ArrayCache, ArrayCacheByTimestamp, ArrayCacheBySymbolById, ArrayCacheBySymbolBySide  # noqa: F402





def equals(a, b):
    return a == b

# ----------------------------------------------------------------------------
def test_ws_cache():
    array_cache = ArrayCache(3)
    array_cache.append({
        'symbol': 'BTC/USDT',
        'data': 1,
    })
    array_cache.append({
        'symbol': 'BTC/USDT',
        'data': 2,
    })
    array_cache.append({
        'symbol': 'BTC/USDT',
        'data': 3,
    })
    array_cache.append({
        'symbol': 'BTC/USDT',
        'data': 4,
    })
    assert(equals(array_cache, [{
    'symbol': 'BTC/USDT',
    'data': 2,
}, {
    'symbol': 'BTC/USDT',
    'data': 3,
}, {
    'symbol': 'BTC/USDT',
    'data': 4,
}]))
    array_cache.append({
        'symbol': 'BTC/USDT',
        'data': 5,
    })
    array_cache.append({
        'symbol': 'BTC/USDT',
        'data': 6,
    })
    array_cache.append({
        'symbol': 'BTC/USDT',
        'data': 7,
    })
    array_cache.append({
        'symbol': 'BTC/USDT',
        'data': 8,
    })
    assert(equals(array_cache, [{
    'symbol': 'BTC/USDT',
    'data': 6,
}, {
    'symbol': 'BTC/USDT',
    'data': 7,
}, {
    'symbol': 'BTC/USDT',
    'data': 8,
}]))
    array_cache.clear()
    array_cache.append({
        'symbol': 'BTC/USDT',
        'data': 1,
    })
    assert(equals(array_cache, [{
    'symbol': 'BTC/USDT',
    'data': 1,
}]))
    # ----------------------------------------------------------------------------
    arraycache2 = ArrayCache(1)
    arraycache2.append({
        'symbol': 'BTC/USDT',
        'data': 1,
    })
    arraycache2.append({
        'symbol': 'BTC/USDT',
        'data': 2,
    })
    assert(equals(arraycache2, [{
    'symbol': 'BTC/USDT',
    'data': 2,
}]))
    # ----------------------------------------------------------------------------
    timestamp_cache = ArrayCacheByTimestamp()
    ohlcv1 = [100, 1, 2, 3]
    ohlcv2 = [200, 5, 6, 7]
    timestamp_cache.append(ohlcv1)
    timestamp_cache.append(ohlcv2)
    assert equals(timestamp_cache, [ohlcv1, ohlcv2])
    modify2 = [200, 10, 11, 12]
    timestamp_cache.append(modify2)
    assert equals(timestamp_cache, [ohlcv1, modify2])
    # ----------------------------------------------------------------------------
    cache_symbol_id = ArrayCacheBySymbolById()
    object1 = {
        'symbol': 'BTC/USDT',
        'id': 'abcdef',
        'i': 1,
    }
    object2 = {
        'symbol': 'ETH/USDT',
        'id': 'qwerty',
        'i': 2,
    }
    object3 = {
        'symbol': 'BTC/USDT',
        'id': 'abcdef',
        'i': 3,
    }
    cache_symbol_id.append(object1)
    cache_symbol_id.append(object2)
    cache_symbol_id.append(object3)  # should update index 0
    assert equals(cache_symbol_id, [object2, object3])
    # ----------------------------------------------------------------------------
    cache_symbol_id_5 = ArrayCacheBySymbolById(5)
    for i in range(1, 11):
        cache_symbol_id_5.append({
            'symbol': 'BTC/USDT',
            'id': str(i),
            'i': i,
        })
    assert(equals(cache_symbol_id_5, [{
    'symbol': 'BTC/USDT',
    'id': '6',
    'i': 6,
}, {
    'symbol': 'BTC/USDT',
    'id': '7',
    'i': 7,
}, {
    'symbol': 'BTC/USDT',
    'id': '8',
    'i': 8,
}, {
    'symbol': 'BTC/USDT',
    'id': '9',
    'i': 9,
}, {
    'symbol': 'BTC/USDT',
    'id': '10',
    'i': 10,
}]))
    for i in range(1, 11):
        cache_symbol_id_5.append({
            'symbol': 'BTC/USDT',
            'id': str(i),
            'i': i + 10,
        })
    assert(equals(cache_symbol_id_5, [{
    'symbol': 'BTC/USDT',
    'id': '6',
    'i': 16,
}, {
    'symbol': 'BTC/USDT',
    'id': '7',
    'i': 17,
}, {
    'symbol': 'BTC/USDT',
    'id': '8',
    'i': 18,
}, {
    'symbol': 'BTC/USDT',
    'id': '9',
    'i': 19,
}, {
    'symbol': 'BTC/USDT',
    'id': '10',
    'i': 20,
}]))
    middle = {
        'symbol': 'BTC/USDT',
        'id': '8',
        'i': 28,
    }
    cache_symbol_id_5.append(middle)
    assert(equals(cache_symbol_id_5, [{
    'symbol': 'BTC/USDT',
    'id': '6',
    'i': 16,
}, {
    'symbol': 'BTC/USDT',
    'id': '7',
    'i': 17,
}, {
    'symbol': 'BTC/USDT',
    'id': '9',
    'i': 19,
}, {
    'symbol': 'BTC/USDT',
    'id': '10',
    'i': 20,
}, {
    'symbol': 'BTC/USDT',
    'id': '8',
    'i': 28,
}]))
    other_middle = {
        'symbol': 'BTC/USDT',
        'id': '7',
        'i': 27,
    }
    cache_symbol_id_5.append(other_middle)
    assert(equals(cache_symbol_id_5, [{
    'symbol': 'BTC/USDT',
    'id': '6',
    'i': 16,
}, {
    'symbol': 'BTC/USDT',
    'id': '9',
    'i': 19,
}, {
    'symbol': 'BTC/USDT',
    'id': '10',
    'i': 20,
}, {
    'symbol': 'BTC/USDT',
    'id': '8',
    'i': 28,
}, {
    'symbol': 'BTC/USDT',
    'id': '7',
    'i': 27,
}]))
    for i in range(30, 33):
        cache_symbol_id_5.append({
            'symbol': 'BTC/USDT',
            'id': str(i),
            'i': i + 10,
        })
    assert(equals(cache_symbol_id_5, [{
    'symbol': 'BTC/USDT',
    'id': '8',
    'i': 28,
}, {
    'symbol': 'BTC/USDT',
    'id': '7',
    'i': 27,
}, {
    'symbol': 'BTC/USDT',
    'id': '30',
    'i': 40,
}, {
    'symbol': 'BTC/USDT',
    'id': '31',
    'i': 41,
}, {
    'symbol': 'BTC/USDT',
    'id': '32',
    'i': 42,
}]))
    first = {
        'symbol': 'BTC/USDT',
        'id': '8',
        'i': 38,
    }
    cache_symbol_id_5.append(first)
    assert(equals(cache_symbol_id_5, [{
    'symbol': 'BTC/USDT',
    'id': '7',
    'i': 27,
}, {
    'symbol': 'BTC/USDT',
    'id': '30',
    'i': 40,
}, {
    'symbol': 'BTC/USDT',
    'id': '31',
    'i': 41,
}, {
    'symbol': 'BTC/USDT',
    'id': '32',
    'i': 42,
}, {
    'symbol': 'BTC/USDT',
    'id': '8',
    'i': 38,
}]))
    another = {
        'symbol': 'BTC/USDT',
        'id': '30',
        'i': 50,
    }
    cache_symbol_id_5.append(another)
    assert(equals(cache_symbol_id_5, [{
    'symbol': 'BTC/USDT',
    'id': '7',
    'i': 27,
}, {
    'symbol': 'BTC/USDT',
    'id': '31',
    'i': 41,
}, {
    'symbol': 'BTC/USDT',
    'id': '32',
    'i': 42,
}, {
    'symbol': 'BTC/USDT',
    'id': '8',
    'i': 38,
}, {
    'symbol': 'BTC/USDT',
    'id': '30',
    'i': 50,
}]))
    # ----------------------------------------------------------------------------
    # test ArrayCacheBySymbolById limit with symbol set
    symbol = 'BTC/USDT'
    cache_symbol_id_2 = ArrayCacheBySymbolById()
    initial_length = 5
    for i in range(0, initial_length):
        cache_symbol_id_2.append({
            'symbol': symbol,
            'id': str(i),
            'i': i,
        })
    limited = cache_symbol_id_2.get_limit(symbol, None)
    assert initial_length == limited
    # ----------------------------------------------------------------------------
    cache_symbol_id_3 = ArrayCacheBySymbolById()
    append_items_length = 3
    for i in range(0, append_items_length):
        cache_symbol_id_3.append({
            'symbol': symbol,
            'id': str(i),
            'i': i,
        })
    outside_limit = 5
    limited = cache_symbol_id_3.get_limit(symbol, outside_limit)
    assert append_items_length == limited
    outside_limit = 2  # if limit < newsUpdate that should be returned
    limited = cache_symbol_id_3.get_limit(symbol, outside_limit)
    assert outside_limit == limited
    # ----------------------------------------------------------------------------
    # test ArrayCacheBySymbolById limit with symbol undefined
    symbol = 'BTC/USDT'
    cache_symbol_id_4 = ArrayCacheBySymbolById()
    initial_length = 5
    for i in range(0, initial_length):
        cache_symbol_id_4.append({
            'symbol': symbol,
            'id': str(i),
            'i': i,
        })
    limited = cache_symbol_id_4.get_limit(None, None)
    assert initial_length == limited
    # ----------------------------------------------------------------------------
    cache_symbol_id_6 = ArrayCacheBySymbolById()
    append_items_length = 3
    for i in range(0, append_items_length):
        cache_symbol_id_6.append({
            'symbol': symbol,
            'id': str(i),
            'i': i,
        })
    outside_limit = 5
    limited = cache_symbol_id_6.get_limit(symbol, outside_limit)
    assert append_items_length == limited
    outside_limit = 2  # if limit < newsUpdate that should be returned
    limited = cache_symbol_id_6.get_limit(symbol, outside_limit)
    assert outside_limit == limited
    # ----------------------------------------------------------------------------
    # test ArrayCacheBySymbolById, same order should not increase the limit
    cache_symbol_id_7 = ArrayCacheBySymbolById()
    symbol = 'BTC/USDT'
    other_symbol = 'ETH/USDT'
    cache_symbol_id_7.append({
        'symbol': symbol,
        'id': 'singleId',
        'i': 3,
    })
    cache_symbol_id_7.append({
        'symbol': symbol,
        'id': 'singleId',
        'i': 3,
    })
    cache_symbol_id_7.append({
        'symbol': other_symbol,
        'id': 'singleId',
        'i': 3,
    })
    outside_limit = 5
    limited = cache_symbol_id_7.get_limit(symbol, outside_limit)
    limited2 = cache_symbol_id_7.get_limit(None, outside_limit)
    assert limited == 1
    assert limited2 == 2
    # ----------------------------------------------------------------------------
    # test testLimitArrayCacheByTimestamp limit
    timestamp_cache_2 = ArrayCacheByTimestamp()
    initial_length = 5
    for i in range(0, initial_length):
        timestamp_cache_2.append([i * 10, i * 10, i * 10, i * 10])
    limited = timestamp_cache_2.get_limit(None, None)
    assert initial_length == limited
    append_items_length = 3
    for i in range(0, append_items_length):
        timestamp_cache_2.append([i * 4, i * 4, i * 4, i * 4])
    outside_limit = 5
    limited = timestamp_cache_2.get_limit(None, outside_limit)
    assert append_items_length == limited
    outside_limit = 2  # if limit < newsUpdate that should be returned
    limited = timestamp_cache_2.get_limit(None, outside_limit)
    assert outside_limit == limited
    # ----------------------------------------------------------------------------
    # test ArrayCacheBySymbolById, watch all orders, same symbol and order id gets updated
    cache_symbol_id_8 = ArrayCacheBySymbolById()
    symbol = 'BTC/USDT'
    outside_limit = 5
    cache_symbol_id_8.append({
        'symbol': symbol,
        'id': 'oneId',
        'i': 3,
    })  # create first order
    cache_symbol_id_8.get_limit(None, outside_limit)  # watch all orders
    cache_symbol_id_8.append({
        'symbol': symbol,
        'id': 'oneId',
        'i': 4,
    })  # first order is closed
    cache_symbol_id_8.get_limit(None, outside_limit)  # watch all orders
    cache_symbol_id_8.append({
        'symbol': symbol,
        'id': 'twoId',
        'i': 5,
    })  # create second order
    cache_symbol_id_8.get_limit(None, outside_limit)  # watch all orders
    cache_symbol_id_8.append({
        'symbol': symbol,
        'id': 'twoId',
        'i': 6,
    })  # second order is closed
    limited = cache_symbol_id_8.get_limit(None, outside_limit)  # watch all orders
    assert limited == 1  # one new update
    # ----------------------------------------------------------------------------
    # test ArrayCacheBySymbolById, watch all orders, and watchOrders (symbol) work independently
    cache_symbol_id_9 = ArrayCacheBySymbolById()
    symbol = 'BTC/USDT'
    symbol2 = 'ETH/USDT'
    outside_limit = 5
    cache_symbol_id_9.append({
        'symbol': symbol,
        'id': 'one',
        'i': 1,
    })  # create first order
    cache_symbol_id_9.append({
        'symbol': symbol2,
        'id': 'two',
        'i': 1,
    })  # create second order
    assert cache_symbol_id_9.get_limit(None, outside_limit) == 2  # watch all orders
    assert cache_symbol_id_9.get_limit(symbol, outside_limit) == 1  # watch by symbol
    cache_symbol_id_9.append({
        'symbol': symbol,
        'id': 'one',
        'i': 2,
    })  # update first order
    cache_symbol_id_9.append({
        'symbol': symbol2,
        'id': 'two',
        'i': 2,
    })  # update second order
    assert cache_symbol_id_9.get_limit(symbol, outside_limit) == 1  # watch by symbol
    assert cache_symbol_id_9.get_limit(None, outside_limit) == 2  # watch all orders
    cache_symbol_id_9.append({
        'symbol': symbol2,
        'id': 'two',
        'i': 3,
    })  # update second order
    cache_symbol_id_9.append({
        'symbol': symbol2,
        'id': 'three',
        'i': 3,
    })  # create third order
    assert cache_symbol_id_9.get_limit(None, outside_limit) == 2  # watch all orders
    # ----------------------------------------------------------------------------
    # test ArrayCacheBySymbolBySide, watch all positions, same symbol and side id gets updated
    cache_symbol_side = ArrayCacheBySymbolBySide()
    symbol = 'BTC/USDT'
    outside_limit = 5
    cache_symbol_side.append({
        'symbol': symbol,
        'side': 'short',
        'contracts': 1,
    })  # create first position
    cache_symbol_side.append({
        'symbol': symbol,
        'side': 'short',
        'contracts': 0,
    })  # first position is closed
    assert cache_symbol_side.get_limit(symbol, outside_limit) == 1  # limit position
    cache_symbol_side.append({
        'symbol': symbol,
        'side': 'short',
        'contracts': 1,
    })  # create first position
    assert cache_symbol_side.get_limit(symbol, outside_limit) == 1  # watch all positions
    # ----------------------------------------------------------------------------
    # test ArrayCacheBySymbolBySide, watch all positions, same symbol and side id gets updated
    cache_symbol_side_2 = ArrayCacheBySymbolBySide()
    symbol = 'BTC/USDT'
    outside_limit = 5
    cache_symbol_side_2.append({
        'symbol': symbol,
        'side': 'short',
        'contracts': 1,
    })  # create first position
    assert cache_symbol_side_2.get_limit(None, outside_limit) == 1  # watch all positions
    cache_symbol_side_2.append({
        'symbol': symbol,
        'side': 'short',
        'contracts': 0,
    })  # first position is closed
    assert cache_symbol_side_2.get_limit(None, outside_limit) == 1  # watch all positions
    cache_symbol_side_2.append({
        'symbol': symbol,
        'side': 'long',
        'contracts': 3,
    })  # create second position
    assert cache_symbol_side_2.get_limit(None, outside_limit) == 1  # watch all positions
    cache_symbol_side_2.append({
        'symbol': symbol,
        'side': 'long',
        'contracts': 2,
    })  # second position is reduced
    cache_symbol_side_2.append({
        'symbol': symbol,
        'side': 'long',
        'contracts': 1,
    })  # second position is reduced
    assert cache_symbol_side_2.get_limit(None, outside_limit) == 1  # watch all orders
    # ----------------------------------------------------------------------------
    # test ArrayCacheBySymbolBySide, watchPositions, and watchPosition (symbol) work independently
    cache_symbol_side_3 = ArrayCacheBySymbolBySide()
    symbol = 'BTC/USDT'
    symbol2 = 'ETH/USDT'
    cache_symbol_side_3.append({
        'symbol': symbol,
        'side': 'short',
        'contracts': 1,
    })  # create first position
    cache_symbol_side_3.append({
        'symbol': symbol2,
        'side': 'long',
        'contracts': 1,
    })  # create second position
    assert cache_symbol_side_3.get_limit(None, outside_limit) == 2  # watch all positions
    assert cache_symbol_side_3.get_limit(symbol, outside_limit) == 1  # watch by symbol
    cache_symbol_side_3.append({
        'symbol': symbol,
        'side': 'short',
        'contracts': 2,
    })  # update first position
    cache_symbol_side_3.append({
        'symbol': symbol2,
        'side': 'long',
        'contracts': 2,
    })  # update second position
    assert cache_symbol_side_3.get_limit(symbol, outside_limit) == 1  # watch by symbol
    assert cache_symbol_side_3.get_limit(None, outside_limit) == 2  # watch all positions
    cache_symbol_side_3.append({
        'symbol': symbol2,
        'side': 'long',
        'contracts': 3,
    })  # update second position
    assert cache_symbol_side_3.get_limit(None, outside_limit) == 1  # watch all positions
    # ----------------------------------------------------------------------------
    # test ArrayCacheBySymbolBySide, watchPositions does not override
    cache_symbol_side_4 = ArrayCacheBySymbolBySide()
    symbol = 'BTC/USDT'
    symbol2 = 'ETH/USDT'
    symbol3 = 'XRP/USDT'
    cache_symbol_side_4.append({
        'symbol': symbol,
        'side': 'long',
        'contracts': 1,
    })  # create first position
    cache_symbol_side_4.append({
        'symbol': symbol2,
        'side': 'long',
        'contracts': 2,
    })  # create second position
    cache_symbol_side_4.append({
        'symbol': symbol3,
        'side': 'long',
        'contracts': 3,
    })  # create short position
    assert cache_symbol_side_4[0]['symbol'] == symbol
    assert cache_symbol_side_4[1]['symbol'] == symbol2
    cache_symbol_side_4.append({
        'symbol': symbol2,
        'side': 'long',
        'contracts': 4,
    })  # update first position
    assert cache_symbol_side_4[0]['contracts'] == 1 and cache_symbol_side_4[0]['symbol'] == symbol
    assert cache_symbol_side_4[1]['contracts'] == 3 and cache_symbol_side_4[1]['symbol'] == symbol3
    assert cache_symbol_side_4[2]['contracts'] == 4 and cache_symbol_side_4[2]['symbol'] == symbol2
    array_length = len(cache_symbol_side_4)
    assert array_length == 3
