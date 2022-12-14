### About

This is a bot that automates solving gleam.io giveaways that require actions with Twitter account

### Installation

Install required packages
```
pip install -r requirements.txt
```

### Usage

1. Change `REFERAL_LINK` constant in `main.py`

2. Add twitter accounts to `accounts.txt`
They will be used during fulfilling giveaway requirements
Each line represents one account - information is separated by comma:
`username,password,phone number`
Feel free to use current accounts which are defined in `accounts.txt`
2. Run main.py
```
python main.py
```
