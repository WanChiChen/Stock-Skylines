# Stock Skylines
 An attempt to find city skylines that fit a stock's graph

## Command line version

https://github.com/WanChiChen/stock-skylines-desktop

## Live App

https://wanchichen.github.io/Stock-Skylines/

## Dependencies
Server dependencies:
```
cd backend
pip install -r requirements.txt
```

Web-app dependencies:
```
cd react-app
npm install
```

## Usage

Start server:
```
cd backend
python manage.py runserver
```
Start web-app:
```
cd react-app
npm start
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
