import requests
import json
import pandas as pd


class Stattleship:

    def __init__(self):

        self.header = None
        self.token = None

    def env_config(self, token):

        self.token = token

    # Setup the request parameters and error handling.
    @staticmethod
    def _request_get(url, headers, params, data_type):

        req = requests.get(
            url=url,
            headers=headers,
            params=params
        )

        if req.status_code == 200:
            df = pd.DataFrame.from_dict(json.loads(req.text)[data_type])
            return df, req.headers

        elif req.status_code != 200:
            req.raise_for_status()

    # Query the API and return the data as a pandas dataframe.
    # The param_dict object accepts the query parameters for the Stattleship API
    # such as interval_type, on, since, player_id, and team_id.
    # This method pages through the result set until all results are captured.
    def _api_query(self, page, data_type, sport, league, param_dict=None):

        self.header = {
          'Content-Type': 'application/json',
          'Authorization': self.token,
          'Accept': 'application/vnd.stattleship.com; version=1'
        }

        params = {
            'per_page': 40,
            'page': page
        }

        if param_dict is not None:

            for key in param_dict:
                if param_dict[key] is not None:
                    params[key] = param_dict[key]

        url = 'https://api.stattleship.com/{}/{}/{}'.format(
            sport, league, data_type
        )

        return self._request_get(
            url=url,
            headers=self.header,
            params=params,
            data_type=data_type
        )

    # The responses from the API are concatenated into a single pandas
    # dataframe object and then returned. 
    def get_data(self, data_type, sport, league, param_dict=None):
        i = 0

        # Run the initial query to build the dataframe base
        response = self._api_query(
            page=i,
            data_type=data_type,
            param_dict=param_dict,
            sport=sport,
            league=league
        )

        response_df = response[0]
        response_header = response[1]

        # Iterate through the pages until there are no more links
        # The try method is in case the result only has 1 page of items
        try:
            while 'rel="next"' in response_header['link']:
                i += 1
                response = self._api_query(
                    page=i,
                    data_type=data_type,
                    sport=sport,
                    league=league,
                    param_dict=param_dict
                )
                response_df = response_df.append(response[0])
                response_header = response[1]

            return response_df

        except requests.exceptions.HTTPError as err:
            raise err

        except KeyError:
            return response_df