# EpicGamesFree-Parsing

<details>
  <summary>Link to backend of free games on EGS</summary>
  https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=en&country=US&allowCountries=US
</details>
<br>

## 📚 ABOUT
This repo shows how to parse free games of Epic Games.
<br>

## ❓ EXAMPLE OF USAGE
Also have in main.py
<br><br>

**get_info**
```python
from examples import get_info

data = get_info()
for i in range(len(data)):
    print('GAME TITLE', data[i][0])
    print('GAME DESCRIPTION', data[i][1])
    print('OFFER TYPE', data[i][2])
    print('ORIGINAL PRICE', data[i][3])
    print('DISCOUNT PRICE', data[i][4])
    print('PRODUCT SLUG', data[i][5])
    print('IMG URL', data[i][6])
    print()
```

## 📖 RETURN TYPES
* get_title - str
* get_titles - tuple
* get_info - tuple[tuple[any, any, any, any, any, any, any]]

## 🤝 CONTRIBUTE
If you would like to contribute to this project, fork it and then create a pull request.
Please ensure checked code.

## ❗ NOTICE

> [!NOTE]
> It\`s unnofficial way to parse free games on EGS. But the [backend](https://store-site-backend-static-ipv4.ak.epicgames.com/freeGamesPromotions?locale=ru&country=US&allowCountries=US) is official. This code isn`t relate to Epic Games
