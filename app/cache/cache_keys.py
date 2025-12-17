def make_search_cache_key(
        industry:str | None,
        min_size:int | None,
        max_size:int | None,
        limit:int,
        offset:int,
) -> str:
    return (
        "search:"
        f"industry={industry}|"
        f"min={min_size}|"
        f"max={max_size}|"
        f"limit={limit}|"
        f"offset={offset}"
    )