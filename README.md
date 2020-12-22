# Scraping Ecommerce

Scraping scripts to get data from ecommerce websites

## Install

Clone the repository

```bash
$ git clone https://github.com/PieroNarciso/ecommerce-scraping-pc.git

$ cd ecommerce-scraping-pc
```

### Pip method

```bash
$ python -m pip install -r requirements.txt

$ python main.py --help
```

### Pipenv method

```bash
$ pipenv install

$ pipenv run python main.py --help
```

### Usage

First create a directory to store all data
```bash
$ mkdir data
```

* `--query`, `-Q`: Search keyword on websites
* `--store`, `-S`: Select stores supported (`all` select all stores)

The output files are stores in `data` directory in `csv` format.
