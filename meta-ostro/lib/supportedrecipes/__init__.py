try:
    from supportedrecipes import load_supported_recipes, dump_sources, check_build, Columns
except ImportError:
    # Python3
    from supportedrecipes.supportedrecipes import load_supported_recipes, dump_sources, check_build, Columns
