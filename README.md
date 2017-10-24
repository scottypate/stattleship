# stattleship
 
This wrapper for the stattleship API will download the specified data and return it as a pandas dataframe.

### Installation
`pip install git+https://github.com/scottypate/stattleship.git`

### Example

```python
from stattleship.stattleship import Stattleship

stattleship = Stattleship()
stattleship.env_config(token='YOUR API TOKEN HERE')

params = {
    'season_id': 'nba-2017-2018',
    'interval_type': 'regularseason'
}

stattleship.get_data(
    data_type='players',
    sport='basketball',
    league='nba',
    param_dict=params
)
```