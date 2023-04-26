# SteganoPhoto

SteganoPhoto is a user-friendly desktop application built with Python and Tkinter that allows you to hide secret messages inside images using steganography. With SteganoPhoto, you can encrypt your messages, hide them inside images, and share them securely with your friends and family. The app also allows you to extract hidden messages from images, so you can decode and read them easily.

## Demo

https://user-images.githubusercontent.com/59524376/234670359-0605a5e2-d9c5-447b-9cb7-a4321599c62b.mp4

## Requirements

To run SteganoPhoto, you will need to have Python 3 installed on your system. You can download Python from the official website [here](https://www.python.org/downloads/). You will also need to install the following Python module(s):

* Pillow
* tkinter
* stegano

You can install these modules using pip, which comes with Python. Simply run the following command in your terminal:

## Installation

1. Clone this repository to your local machine using `git clone https://github.com/n4vn337/SteganoPhoto.git`
2. Navigate to the cloned repository using `cd SteganoPhoto`
3. Run the `main.py` file using `python main.py`

## Usage

1. Click the "Open Image" button and select the image you want to hide your message in.
2. Enter your message in the "Message" text field.
3. Click the "Encode" button to hide your message in the image.
4. Save the new image using the "Save As" button. This will be saved as hidden.png
5. To decode, simply open the hidden.png and click on decode to see the hidden image.
