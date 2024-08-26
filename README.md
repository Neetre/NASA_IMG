# NASA_IMG

## Description

This is a simple web application that uses the NASA API to display images from the NASA database.
The interface has 3 tabs:

- The first tab gets you a random image or more from the NASA database.
- The second tab gets you some data about the asteroids that are near the Earth.

## Requirements

python >= 3.9

To run the project, you need to have Python installed on your machine. You can download Python from the [official website](https://www.python.org/downloads/)

**Setting Up the Environment**

* Windows: `./setup_Windows.bat`
* Linux/macOS: `./setup_Linux.sh`

These scripts will install required dependencies, and build a virtual environment for you if you don't have one.

## Usage

Make sure you have added your API key in the .env file.
Inside the .env file, add the following line with your API key:

```bash
NASA_KEY=""
```

To run the project, execute the following command:

```bash
cd bin
python ./interface.py
```

The application will open in your default browser.
![NASA_IMG](../data/readme/NASA_IMG.PNG)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

[Neetre](https://github.com/Neetre)
