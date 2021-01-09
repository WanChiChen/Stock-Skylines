# Stock Skylines
 An attempt to find city skylines that fit a stock's graph

## Live App

https://wanchichen.github.io/Stock-Skylines/

## Usage

Start server:
```
cd backend
python manage.py runserver
```

Sample POST body:
```
{
    "ticker": "MAR",
    "period": "1d",
    "start": "2010-10-01",
    "end": "2020-12-31",
    "ratio": "0.8"
}
```
