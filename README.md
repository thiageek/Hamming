# Hamming Code

This project was developed as an experiment to understand the Hamming's Algorithm in order to send a sequency of bits with its parity bits, as well as to to receive a sequency and detect if it has any error.

## Getting Started

Make sure you are running this project with Python 2.7. Then, all you need to do is import the Hamming class in your project:

```
from hamming import Hamming
```

As soon as tha Hamming class is available to be used in your project, you can create a new instance from it:

```
h = Hamming()
```

### Calculate R

When you send and receive a message using Hamming's, one thing you will always have to know is how many parity bits you will need to that amount of data. You can calculate this using the method calculateR, as shown below:

```
r = h.calculateR(data)
```

### Encode

To send a message, you will need to encode it with a certain amout of parity bits. You can use the method encode to build this message, like this:

```
message = h.encode(data)
```

### Decode

When you receive a message, you may need to check if it is correct. Also, if it is incorrect, you will need to know where is the error. This is what the method decode will do for you, using the data received as parameter and returning in binary the error position.

```
errorPosition = h.decode(data)
```

If the integer value of the binary number reveived is 0, the message was received without any error.

### Correct Message

If the message received has an error and you already know where (you will need the integer value of the error position), it is easy to correct it with the method correct.

```
correctMessage = h.correct(data, 7)
```

## License

This project is licensed under the GNU AGPL v3.0 - see the [LICENSE.md](LICENSE.md) file for details.

## Authors

* **Thiago Pinheiro** - *Initial work* - [@thiageek](https://github.com/thiageek)

## Acknowledgments

* My teacher Ivandro Ribeiro for the inspiration
* The beautiful Jaqueline Teles for the motivation