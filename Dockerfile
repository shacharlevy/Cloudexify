# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Install any needed packages
RUN apt-get update && apt-get install -y \
    clang \
    cmake \
    git

# Clone the repository
RUN git clone https://github.com/learnedsystems/LearnedSecondaryIndex.git

# Set the working directory to the repository directory
WORKDIR /app/LearnedSecondaryIndex

# Comment out the GIT_TAG line for tlx-populate in CMakeLists.txt
RUN sed -i 's/GIT_TAG fa1ee82/#GIT_TAG fa1ee82/g' CMakeLists.txt

# Copy any necessary files (e.g., .env) - adjust paths as needed
COPY .env /app/LearnedSecondaryIndex/.env

# Execute test.sh
RUN chmod +x ./test.sh
RUN ./test.sh

# Execute run.sh
RUN chmod +x ./run.sh
RUN ./run.sh

# Optional: Create plots
# Note: Ensure Jupyter is installed and you have a compatible Python environment
# COPY paper_plots.ipynb /app/LearnedSecondaryIndex/paper_plots.ipynb
# RUN jupyter nbconvert --to notebook --execute paper_plots.ipynb

# Optional: CMake setup (if you want to include lsi in your own CMake project)
# Note: Modify your CMakeLists.txt accordingly
# include(FetchContent)
# FetchContent_Declare(
#     lsi
#     GIT_REPOSITORY "https://github.com/learnedsystems/LearnedSecondaryIndex"
#     GIT_TAG main
# )
# FetchContent_MakeAvailable(lsi)
# target_link_libraries(your_target lsi)
