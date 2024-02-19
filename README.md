# Project Name

**Arabic Text Extraction with English Numbers using Python**

## Overview

This project focuses on extracting Arabic text along with English numbers from images using Python. The main file, `main_file.py`, contains the code that utilizes various libraries such as numpy, pandas, matplotlib, opencv, and arabicocr to achieve the task. The process involves reading an image, extracting Arabic text using arabicocr, recognizing the text with high accuracy, annotating the output image with respective numbers, and generating a final CSV file containing the text and its corresponding serial numbers.

## Dependencies

Make sure you have the following libraries installed before running the code:

- numpy
- pandas
- matplotlib
- opencv
- arabicocr

You can install these dependencies using the following command:

```bash
pip install numpy pandas matplotlib opencv-python arabicocr
```

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

2. Run the main file:

```bash
python main_file.py
```

3. Provide the path to the image when prompted.

4. The program will extract Arabic text, annotate the image, and generate a CSV file.

## Example

```python
python main_file.py
```

```
Enter the path to the image: /path/to/your/image.jpg
```

The program will then process the image and display the annotated output.

## Output

The output will consist of:

1. Annotated image with Arabic text and corresponding numbers.
2. A CSV file containing the extracted text and its respective serial numbers.

## Note

- Ensure that the image file is in a supported format (e.g., JPG, PNG).
- Make sure the image contains Arabic text and English numbers for accurate extraction.

Feel free to explore the code in `main_file.py` for customization and further understanding of the implementation. If you encounter any issues or have suggestions, please create an issue in the repository.

Happy coding!
