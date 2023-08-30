# LearnedSecondaryIndex

## Overview 
This repo is the main codebase based on this paper _LSI: A Learned Secondary Index Structure_.

Learned Secondary Index (LSI) is a first attempt to use learned indexes for indexing unsorted data.
LSI works by building a learned index over a permutation vector,
which allows binary search to performed on the unsorted base data using random access.
We additionally augment LSI with a fingerprint vector to accelerate equality lookups. 

## Usage

Execute `./run.sh` to run benchmarks.
Note that you may need to edit the `.env` file first to contain the correct path to your compiler.
Any recent version of clang should work.

Run all cells in `paper_plots.ipynb` to recreate the plots in `results/`.

### CMake

You can include `lsi` in your own CMake based project like this:
``` lsi
include(FetchContent)
FetchContent_Declare(
    lsi
    GIT_REPOSITORY "https://github.com/learnedsystems/LearnedSecondaryIndex"
    GIT_TAG main
)
FetchContent_MakeAvailable(lsi)

target_link_libraries(your_target lsi)
```

## Structure

- `include/` contains the code newly contributed by our work
- `src/` contains tests, benchmark driver code and competitors
- `results/` contains the results referenced in the paper and the accompanying plots

  keywords = {Databases (cs.DB), Machine Learning (cs.LG), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {LSI: A Learned Secondary Index Structure},
  publisher = {arXiv},
  year = {2022}, 
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```
